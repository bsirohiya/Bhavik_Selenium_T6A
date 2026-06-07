# agent/agent_core.py
#
# PURPOSE: This is the "brain" of your agent.
# It reads what the user typed, decides which tool to call,
# calls it, then uses Gemini to give a final polished response.
#
# ROUTING APPROACH (Phase 1): Keyword-based routing.
# We look for trigger words in the user's message.
# Example: if they say "improve locator" → call improve_locator()
#          if they say "generate test cases" → call generate_testcases()
#
# WHY KEYWORD ROUTING FIRST?
# It's simple, transparent, and easy to debug.
# In Phase 2, we'll upgrade to AI-driven routing where Gemini
# itself decides which tool to call. But always learn simple first.

import google.generativeai as genai
from config.settings import GEMINI_API_KEY

# Import all three tools
from tools.locator_improver import improve_locator
from tools.testcase_generator import generate_testcases
from tools.automation_generator import automation_generator

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# ─────────────────────────────────────────────────────────
# TOOL REGISTRY
# This dictionary is our "menu" of available tools.
# Key   = tool name (used internally for logging/display)
# Value = dict with:
#   - "function": the actual Python function to call
#   - "keywords": trigger words that activate this tool
#   - "description": human-readable description
# ─────────────────────────────────────────────────────────

TOOL_REGISTRY = {
    "improve_locator": {
        "function": improve_locator,
        "keywords": [
            "improve locator", "fix locator", "better xpath",
            "better css", "locator issue", "xpath", "css selector",
            "selector", "improve selector", "weak locator",
            "fragile locator", "locator suggestion"
        ],
        "description": "Improves weak XPath/CSS selectors into stable ones"
    },
    "generate_testcases": {
        "function": generate_testcases,
        "keywords": [
            "test case", "testcase", "test cases", "generate test",
            "write test", "create test", "test scenario",
            "test plan", "test coverage", "what to test"
        ],
        "description": "Generates structured QA test cases for any feature"
    },
    "automation_generator": {
        "function": automation_generator,
        "keywords": [
            "automate", "automation", "selenium script", "write script",
            "generate script", "automation script", "playwright script",
            "robot framework", "generate automation", "create script",
            "code for", "script for"
        ],
        "description": "Generates Selenium/Playwright/Robot Framework automation scripts"
    }
}


def detect_tool(user_message: str) -> str | None:
    """
    Scans the user's message for keyword matches.
    Returns the tool name if found, or None if no match.

    How it works:
    - Converts message to lowercase (so "XPath" matches "xpath")
    - Checks if ANY keyword from ANY tool appears in the message
    - Returns the FIRST matching tool name

    Example:
    Input:  "Can you improve my xpath selector? It keeps breaking."
    Output: "improve_locator"  ← matched on "improve" and "xpath"
    """

    # Lowercase for case-insensitive matching
    message_lower = user_message.lower()

    # Loop through every tool in our registry
    for tool_name, tool_info in TOOL_REGISTRY.items():
        # Check every keyword for this tool
        for keyword in tool_info["keywords"]:
            # If this keyword appears anywhere in the message
            if keyword in message_lower:
                print(f"\n [agent] Keyword '{keyword}' matched → Tool: '{tool_name}'")
                return tool_name  # Return immediately on first match

    # No keyword matched — return None (will use plain Gemini)
    return None


def extract_main_input(user_message: str) -> tuple[str, str]:
    """
    Tries to extract the main input and optional framework from user's message.

    Returns a tuple: (main_input, framework)

    Example inputs:
    "Improve this locator: //div[@class='btn'][3]"
    → returns ("//div[@class='btn'][3]", "")

    "Generate test cases for login feature"
    → returns ("login feature", "")

    "Write a selenium script for login flow"
    → returns ("login flow", "selenium")
    """

    # Detect framework mentions for automation_generator
    framework = "selenium"  # default
    if "playwright" in user_message.lower():
        framework = "playwright"
    elif "robot framework" in user_message.lower() or "robot" in user_message.lower():
        framework = "robot_framework"
    elif "selenium" in user_message.lower():
        framework = "selenium"

    # Common patterns where user provides input after a colon
    # Example: "Improve this locator: //div[@id='btn']"
    if ":" in user_message:
        # Split on first colon, take everything after it
        parts = user_message.split(":", 1)
        main_input = parts[1].strip()
    else:
        # Use the whole message as input if no colon found
        main_input = user_message.strip()

    return main_input, framework


def run_tool(tool_name: str, user_message: str) -> str:
    """
    Calls the appropriate tool function with the user's input.

    Parameters:
    - tool_name: which tool to run (from TOOL_REGISTRY keys)
    - user_message: the full original user message

    Returns:
    - Tool's output as a string
    """

    # Get the tool's function from the registry
    tool_function = TOOL_REGISTRY[tool_name]["function"]

    # Extract the main input from the user's message
    main_input, framework = extract_main_input(user_message)

    print(f"  [agent] Running tool: {tool_name}")
    print(f" [agent] Input extracted: {main_input[:80]}...")  # Show first 80 chars

    # Call the right tool with the right parameters
    # Each tool has slightly different parameters, so we handle each
    if tool_name == "improve_locator":
        result = tool_function(locator=main_input)

    elif tool_name == "generate_testcases":
        result = tool_function(feature_description=main_input)

    elif tool_name == "automation_generator":
        print(f" [agent] Framework detected: {framework}")
        result = tool_function(
            scenario_description=main_input,
            framework=framework
        )

    else:
        result = f"Tool '{tool_name}' is registered but has no handler yet."

    return result


def chat_without_tools(user_message: str) -> str:
    """
    Fallback: when no tool matches, use plain Gemini as QA assistant.
    This ensures the agent is ALWAYS helpful, even for general questions.
    """

    model = genai.GenerativeModel("gemini-2.5-flash")

    # System context makes Gemini respond as a QA expert
    system_context = """You are an expert QA automation engineer and AI assistant.
You specialize in: Selenium, XPath, CSS selectors, test case design,
automation frameworks, and web testing best practices.
Answer questions clearly, with examples when helpful."""

    full_prompt = f"{system_context}\n\nUser question: {user_message}"

    response = model.generate_content(full_prompt)
    return response.text


def process_message(user_message: str) -> str:
    """
    MAIN ENTRY POINT for the agent.
    This is what main.py calls for every user message.

    Flow:
    1. Detect if a tool should be called
    2. If yes → run the tool → return tool output
    3. If no  → use plain Gemini as QA assistant

    Parameters:
    - user_message: exactly what the user typed

    Returns:
    - Final response string to show the user
    """

    print(f"\n{'=' * 60}")
    print(f" [User] {user_message}")
    print(f"{'=' * 60}")

    # Step 1: Try to detect which tool to use
    tool_name = detect_tool(user_message)

    if tool_name:
        # Step 2: Tool detected — run it
        print(f" [agent] Tool selected: {tool_name}")
        tool_output = run_tool(tool_name, user_message)

        # Add a header so user knows which tool responded
        tool_description = TOOL_REGISTRY[tool_name]["description"]
        final_response = f" **{tool_description}**\n\n{tool_output}"

        return final_response

    else:
        # Step 3: No tool matched — use Gemini directly
        print(" [agent] No tool matched — using Gemini directly")
        return chat_without_tools(user_message)