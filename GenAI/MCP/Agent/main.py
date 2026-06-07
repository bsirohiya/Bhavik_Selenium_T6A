# main.py
#
# PURPOSE: This is the file you RUN in PyCharm.
# It starts an interactive loop where you type messages
# and the agent responds.
#
# Think of this as the "front door" of your application.
# It handles the UI (command line interface) and calls
# the agent for every message.

from agent.agent_core import process_message, TOOL_REGISTRY


def print_welcome():
    """Prints a welcome banner when the program starts."""
    print("\n" + "=" * 60)
    print(" QA AI AGENT — Phase 1")
    print("=" * 60)
    print("I can help you with:")

    # Dynamically list all available tools from the registry
    for tool_name, tool_info in TOOL_REGISTRY.items():
        print(f"  {tool_info['description']}")

    print("\nHow to use:")
    print("  • 'improve locator: //div[@class=\"btn\"][3]'")
    print("  • 'generate test cases for login page'")
    print("  • 'write a selenium script for checkout flow'")
    print("  • 'write a playwright script for search feature'")
    print("  • Or just ask any QA question!")
    print("\nType 'quit' or 'exit' to stop.")
    print("=" * 60 + "\n")


def print_tools_help():
    """Shows available tools when user types 'help'."""
    print("\n AVAILABLE TOOLS:")
    print("-" * 40)
    for tool_name, tool_info in TOOL_REGISTRY.items():
        print(f"\n🔧 {tool_name.upper()}")
        print(f"   {tool_info['description']}")
        print(f"   Trigger words: {', '.join(tool_info['keywords'][:4])}...")
    print("-" * 40 + "\n")


def main():
    """
    Main loop — keeps running until user types 'quit'.

    Loop structure:
    1. Wait for user input
    2. Check for special commands (quit, help)
    3. Send to agent for processing
    4. Print the response
    5. Repeat
    """

    print_welcome()

    while True:
        try:
            # Get user input
            # The '> ' prefix shows it's waiting for input
            user_input = input("You > ").strip()

            # Skip empty input (user just pressed Enter)
            if not user_input:
                continue

            # Check for exit commands
            if user_input.lower() in ["quit", "exit", "q", "bye"]:
                print("\nGoodbye! Happy testing!")
                break

            # Check for help command
            if user_input.lower() in ["help", "tools", "?"]:
                print_tools_help()
                continue

            # Process through the agent
            response = process_message(user_input)

            # Print the agent's response
            print(f"\n Agent:\n{response}\n")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n Interrupted. Goodbye!")
            break

        except Exception as e:
            # Catch any unexpected errors so the program doesn't crash
            print(f"\n Error occurred: {str(e)}")
            print("Please try again or rephrase your question.\n")


# This is the standard Python way to say:
# "Only run main() if this file is run directly,
#  not if it's imported by another file"
if __name__ == "__main__":
    main()