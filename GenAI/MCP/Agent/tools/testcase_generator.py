# tools/testcase_generator.py
#
# PURPOSE: Takes a feature description and generates
# structured QA test cases automatically.
#
# WHY: Writing test cases manually is slow. This tool
# creates them in seconds following proper QA format.

import google.generativeai as genai
from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def generate_testcases(feature_description: str, test_type: str = "functional") -> str:
    """
    Generates test cases for a given feature.

    Parameters:
    - feature_description: what feature to test
      Example: "Login page with email and password fields"
    - test_type: what kind of tests to generate
      Options: "functional", "negative", "boundary", "smoke", "regression"

    Returns:
    - Structured test cases as a formatted string
    """

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are a senior QA engineer creating test cases for a software project.

FEATURE TO TEST: {feature_description}
TEST TYPE REQUESTED: {test_type}

Generate professional test cases using this exact format for EACH test case:

---
TEST CASE ID: TC_001
TEST CASE TITLE: [Short descriptive title]
PRIORITY: High / Medium / Low
PRECONDITIONS: [What must be true before this test runs]
TEST STEPS:
  1. [Step 1]
  2. [Step 2]
  3. [Continue...]
EXPECTED RESULT: [What should happen if the feature works correctly]
TEST DATA: [Any specific data needed, e.g., email: test@example.com]
---

Generate at least 5 test cases.
Cover: happy path, edge cases, negative scenarios.
Be specific — avoid vague steps like "click the button" — say WHICH button.
"""

    response = model.generate_content(prompt)
    return response.text