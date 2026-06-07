# tools/locator_improver.py
#
# PURPOSE: This tool takes a bad/fragile XPath or CSS selector
# and uses Gemini to suggest a better, more stable version.
#
# WHY: In QA automation, locators break when UI changes.
# Good locators use IDs, data-testid, aria attributes — not
# fragile things like "the 3rd div inside the 2nd table".

import google.generativeai as genai
from config.settings import GEMINI_API_KEY

# Configure Gemini with our API key
genai.configure(api_key=GEMINI_API_KEY)


def improve_locator(locator: str, html_context: str = "") -> str:
    """
    Takes a weak locator and returns improved suggestions.

    Parameters:
    - locator: the XPath or CSS selector to improve
      Example: "//div[@class='btn btn-primary'][3]"
    - html_context: optional HTML snippet for better analysis
      Example: "<button id='submit' class='btn'>Submit</button>"

    Returns:
    - A string with Gemini's improvement suggestions
    """

    # Build the model — flash is fast and cheap
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Build a detailed prompt so Gemini gives QA-specific advice
    # We tell Gemini exactly what role to play and what to output
    prompt = f"""
You are a senior QA automation engineer with expertise in Selenium and web testing.

A developer has given you this locator to review:
LOCATOR: {locator}

{"HTML CONTEXT: " + html_context if html_context else "No HTML context provided."}

Your job:
1. Analyze why this locator might be fragile or unstable
2. Suggest 3 improved alternatives in order of preference
3. For each alternative, explain WHY it is better
4. Show the improved locator as both XPath AND CSS selector if possible
5. Rate the original locator: POOR / ACCEPTABLE / GOOD

Format your response clearly with headers.
Focus on: ID selectors, data-testid, aria-label, name attributes.
Avoid: positional selectors, complex class chains, absolute XPaths.
"""

    # Send to Gemini and get response
    # .text extracts just the string from the response object
    response = model.generate_content(prompt)
    return response.text