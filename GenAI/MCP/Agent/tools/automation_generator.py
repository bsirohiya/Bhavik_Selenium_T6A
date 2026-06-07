# tools/automation_generator.py
#
# PURPOSE: Generates ready-to-run Selenium Python automation scripts
# based on a plain English description of what to automate.
#
# WHY: Writing Selenium scripts takes time. This tool generates
# a starting script that engineers can review and refine.
#
# NOTE ON YOUR QUESTION — Does this work for Playwright/Robot Framework?
# Short answer: different tools = different code syntax.
# This file generates Selenium code. For Playwright or Robot Framework,
# the TOOL FUNCTION changes but the AGENT ARCHITECTURE stays exactly the same.
# We will add a "framework" parameter so users can choose.
# I will explain this fully after the Selenium version works.

import google.generativeai as genai
from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def automation_generator(
        scenario_description: str,
        framework: str = "selenium"
) -> str:
    """
    Generates automation scripts based on a description.

    Parameters:
    - scenario_description: plain English description of what to automate
      Example: "Login to example.com with valid credentials and verify dashboard loads"
    - framework: which automation tool to generate code for
      Options: "selenium", "playwright", "robot_framework"
      Default: "selenium"

    Returns:
    - A complete, runnable automation script as a string
    """

    model = genai.GenerativeModel("gemini-2.5-flash")

    # ─────────────────────────────────────────────
    # FRAMEWORK-SPECIFIC INSTRUCTIONS
    # This is how we handle different frameworks —
    # we change the instructions to Gemini, not the architecture.
    # The agent layer never changes. Only this prompt changes.
    # ─────────────────────────────────────────────

    framework_instructions = {
        "selenium": """
Use Python with Selenium WebDriver.
Imports needed: from selenium import webdriver, from selenium.webdriver.common.by import By,
from selenium.webdriver.support.ui import WebDriverWait, from selenium.webdriver.support import expected_conditions as EC
Use Chrome WebDriver with options.
Use explicit waits (WebDriverWait) — never time.sleep().
Use By.ID, By.CSS_SELECTOR, or By.XPATH for locators.
Add try/except/finally block so browser always closes.
Add clear comments explaining each step.
""",
        "playwright": """
Use Python with Playwright (sync_playwright).
Imports needed: from playwright.sync_api import sync_playwright
Use page.wait_for_selector() instead of explicit waits.
Use page.locator() for finding elements.
Add with statement for browser context management.
Add clear comments explaining each step.
""",
        "robot_framework": """
Generate a Robot Framework .robot file (not Python).
Use SeleniumLibrary keywords.
Include: *** Settings ***, *** Variables ***, *** Test Cases ***, *** Keywords *** sections.
Use proper Robot Framework indentation (4 spaces).
Add comments with # symbol.
"""
    }

    # Get instructions for chosen framework, default to selenium if unknown
    fw_instructions = framework_instructions.get(
        framework.lower(),
        framework_instructions["selenium"]
    )

    prompt = f"""
You are a senior QA automation engineer.

Generate a complete, production-ready automation script for this scenario:
SCENARIO: {scenario_description}
FRAMEWORK: {framework.upper()}

FRAMEWORK-SPECIFIC REQUIREMENTS:
{fw_instructions}

GENERAL REQUIREMENTS:
1. Add a comment at the top explaining what the script does
2. Include proper setup and teardown
3. Make locators as stable as possible (prefer ID, data-testid, aria-label)
4. Add meaningful assertion/verification steps
5. Handle potential failures gracefully
6. The script should be immediately runnable with minimal changes

Generate ONLY the code. Add inline comments for learning purposes.
"""

    response = model.generate_content(prompt)
    return response.text