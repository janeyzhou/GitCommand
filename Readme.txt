Test the UI and API functions for Fashe website.

Test frameworke: Pytest + Allure + Jenkins pipeline

Plugins: pytest, selenium, pytest-allure, requests, deepdiff

Framework structure:
1. Utils - define the common used functions for API test and UI test project
2. Config - define the test environment for API test and UI test project
3. PageObject and PageFactory to implement UI test
	basePage: rewrite some frequently used function in webdriver
	pages: define locator and element actions
	widgets: define the common sections on several pages, e.g footer, header, cart
	business flow: define each page and widget's work flow/ verification/ data tranform


