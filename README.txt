Airalo Test Automation Framework
================================
**This test suite has been created specifically for testing with the Euro currency.**

This is a combined UI and API test automation framework built using:
- Playwright (for UI)
- Pytest
- Python
- Requests (for API)
- dotenv (for secrets management)

It follows the Page Object Model (POM) for UI tests, and uses maintainable test utilities for API testing. Includes logging, test data separation, and HTML reporting.

--------------------------------------
SETUP INSTRUCTIONS
--------------------------------------

1. Download the Project

   Clone the repository from GitHub:

   https://github.com/nipuna1989/Airalo_Test_Project.git

2. Go Inside the Project Folder

   example - cd C:\Airalo_Test_Project

3. Create a Virtual Environment

   python -m venv venv

   On Windows:
       venv\Scripts\activate

   On Mac/Linux:
       source venv/bin/activate

4. Install Required Packages

   pip install -r requirements.txt

5. Install Playwright Browsers (for UI tests only)

   playwright install

6. Set up Environment Variables

    How to Use It:

   - Copy the example file:
     On Mac/Linux:
       cp .env.example .env

     On Windows (Command Prompt):
       copy .env.example .env

  - Fill in your actual credentials in `.env`:
     CLIENT_ID=your_real_client_id_here
     CLIENT_SECRET=your_real_secret_here


--------------------------------------
RUNNING TESTS
--------------------------------------

To run all tests (UI + API):
   pytest -s

To run only UI tests:
   pytest tests/ui/ -s

To run only API tests:
   pytest tests/api/ -s

To run a specific test:
   pytest tests/api/test_get_esim_list.py::test_verify_esims -s

To generate an HTML report:
   pytest -s --html=reports/report.html --self-contained-html

Test logs are saved in:        test-logs/
HTML reports are generated in: reports/

--------------------------------------
PROJECT STRUCTURE
--------------------------------------

Airalo_Test_Project/
│
├── data/
│   ├── __init__.py
│   ├── constant_data.py          # Shared constants
│   ├── api_test_data.py          # API-specific test inputs
│   ├── ui_test_data.json         # UI test datasets
│   ├── load_test_data.py         # Optional structured test data helper
│   └── schema/
│       ├── __init__.py
│       ├── get_esim_list_schema_json
│       └── submit_order_schema.json
│
├── pages/                        # Page Object Model (UI)
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── esim_selection_page.py
│   └── package_details_popup.py
│
├── reports/                      -> Generated HTML reports
│
├── test-logs/                    -> Log files per test session
│
├── tests/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── test_order_flow.py    -> Submitting order tests
│   │   ├── test_esim_fetch.py    -> Fetching and verifying eSIM data
│   │
│   └── ui/
│       ├── __init__.py
│       ├── test_search_destination.py -> UI destination search test
│
├── utils/                        -> Helper and utility scripts
│   ├── __init__.py
│   ├── logger.py
│   ├── api_utils.py
│   ├── load_env_variables.py
│   └── __init__.py
│
├── .env                          -> Local secrets
├── .env.example                  -> Sample env file to copy from
├── .gitignore                    -> Ignore rules for Git
├── conftest.py                   -> Shared fixtures
├── requirements.txt              -> All required dependencies
└── README.txt                    -> This file


-------------------------------------
TEST CASES AND APPROACH
-------------------------------------

Test Case: test_search_destination
Overview:
This test case verifies the functionality of searching for a destination and selecting an eSIM package on the Airalo website.
It uses Playwright for UI automation and Pytest for test management.

Approach:
Test Data:
- The test is parameterized using @pytest.mark.parametrize with three values:
  - destination: The destination to search (e.g., 'Japan').
  - expected_details: Expected details of the selected eSIM package.
  - package_index: Index of the package to select.

Test Steps:

1. **Setup**: The test uses the `@pytest.mark.parametrize` decorator to run the test with different sets of data.
2. **Initialize Page Objects**: The test initializes the page objects for the home page, eSIM selection page, and package details popup.
3. **Navigate to Homepage**: The test navigates to the Airalo homepage.
4. **Search for Destination**: The test searches for the specified destination using the home page object.
5. **Select eSIM Package**: The test selects the eSIM package using the specified index.
6. **Verify Package Details**: The test verifies the package details using the package details popup object.
7. **Assertions**: The test asserts that the package details match the expected details.
8. **Teardown**: The test closes the browser after execution.
--------------------------------------

Test Case: test_submit_order
Overview:
This test case validates the order creation process for a specific eSIM package.
It sends a POST request to create an order, validates the response, and verifies the correct package and SIM quantity are returned.

Approach:
Test Data:
- The test uses predefined constants like `PACKAGE_ID`, `ORDER_QUANTITY`, and `ORDER_TYPE` to create a valid order payload.
- The test uses a valid authentication header for the API request.

Test Steps:
1. **Generate Payload:** The test starts by generating the payload for creating an order.
2. **Send POST Request:** A POST request is made to the `ORDER_URL` with the generated payload and authentication headers.
3. **Verify Status Code:** The test asserts that the response status code is 200 (successful).
4. **Validate Response Schema:** The response JSON is validated against the expected schema.
5. **Verify Data Fields:** The test checks if the response data contains the correct package ID, quantity, type, and description.
6. **Verify SIM Quantity:** It ensures that the number of SIMs in the response matches the expected quantity.
7. **Log Success:** Upon successful order creation, a success message is logged.

--------------------------------------

Test Case: test_submit_order_with_invalid_token
Overview:
This test case verifies the behavior of the API when an invalid token is used for authentication.
It ensures that the API returns a 401 Unauthorized status code.

Approach:
Test Data:
- The test uses an invalid authentication header (`INVALID_AUTH_HEADER`).

Test Steps:
1. **Generate Payload:** The test generates a payload for creating an order.
2. **Send POST Request with Invalid Token:** A POST request is sent using the invalid token.
3. **Verify Status Code:** The test asserts that the response status code is 401 (Unauthorized).
4. **Validate Error Message:** It checks that the error response contains the correct `meta` and `message` fields, ensuring the correct error message is returned.

--------------------------------------

Test Case: test_submit_order_invalid_package_id
Overview:
This test case checks the behavior of the order creation API when an invalid package ID is provided.
The test expects a 422 Unprocessable Entity status code along with an appropriate error message.

Approach:
Test Data:
- The test uses an invalid `package_id` in the order payload.
- The test uses a valid authentication header for the API request.

Test Steps:
1. **Generate Payload:** The test generates an order payload with an invalid `package_id`.
2. **Send POST Request:** A POST request is sent with the invalid payload.
3. **Verify Status Code:** The test asserts that the response status code is 422 (Invalid parameters).
4. **Validate Error Response:** It validates the error response structure, ensuring that the correct error code and reason are returned.

--------------------------------------

Test Case: test_submit_order_exceed_quantity
Overview:
This test case verifies the behavior of the order creation API when the order quantity exceeds the allowed limit.
The test expects a 422 Unprocessable Entity status code and a specific error message about the quantity limit.

Approach:
Test Data:
- The test uses an exceeding quantity in the payload.
- The test uses a valid authentication header for the API request.

Test Steps:
1. **Generate Payload:** The test generates an order payload with an exceeding quantity.
2. **Send POST Request:** A POST request is sent with the payload containing the exceeding quantity.
3. **Verify Status Code:** The test asserts that the response status code is 422 (Invalid parameters).
4. **Validate Error Response:** It ensures the error message about the quantity limit is returned in the response.
5. **Log Error:** The test logs the validation result for tracking.

--------------------------------------
Test Case: test_verify_esims
Overview:
This test case verifies the eSIMs associated with a given package ID.
It fetches the eSIMs from the API and checks that the number of eSIMs with the specified package ID meets the expected quantity.

Approach:
Test Data:
- The test uses predefined constants like `PACKAGE_ID` and `ORDER_QUANTITY` to fetch and validate the eSIMs.
- The test uses a valid authentication header for the API request.

Test Steps:
1. **Send GET Request:** The test sends a GET request to fetch the eSIMs associated with the correct package ID.
2. **Verify Status Code:** The test asserts that the response status code is 200 (successful).
3. **Validate Response Schema:** It validates the response JSON against the expected schema.
4. **Filter eSIMs by Package ID:** The test extracts eSIMs from the response and filters them by the `package_id`.
5. **Verify eSIM Quantity:** The test ensures that the number of matching eSIMs is at least the expected quantity.
6. **Log Success:** Upon successful verification, a success message is logged.

--------------------------------------

Test Case: test_verify_sim_with_invalid_token
Overview:
This test case checks the behavior of the API when an invalid authentication token is used.
The test ensures the API returns a 401 Unauthorized status code and the correct error message.

Approach:
Test Data:
- The test uses an invalid authentication header (`INVALID_AUTH_HEADER`).

Test Steps:
1. **Send GET Request with Invalid Token:** A GET request is sent with an invalid authentication token.
2. **Verify Status Code:** The test asserts that the response status code is 401 (Unauthorized).
3. **Validate Error Message:** It checks that the error response contains the correct `meta` and `message` fields, ensuring the correct error message is returned.
4. **Log Success:** The test logs the successful validation of the error response.

--------------------------------------

Test Case: test_verify_sim_with_invalid_limit_parameter
Overview:
This test case checks the behavior of the API when an invalid `limit` parameter is passed in the query. The test ensures the API returns a 422 Unprocessable Entity status code with the appropriate error message.

Approach:
Test Data:
- The test uses invalid query parameters with a non-integer `limit` value.
- The test uses a valid authentication header for the API request.

Test Steps:
1. **Send GET Request with Invalid `limit` Parameter:** A GET request is sent with an invalid `limit` parameter.
2. **Verify Status Code:** The test asserts that the response status code is 422 (Unprocessable Entity).
3. **Validate Error Message:** It validates that the response contains the correct error message for the `limit` parameter.
4. **Log Success:** The test logs the successful validation of the error response.


--------------------------------------
NOTES
--------------------------------------

- Python version required: 3.11 or higher
- All secrets and keys are handled via .env and loaded with python-dotenv
- Logs are written to disk per session using the custom logger in /utils
- HTML reports are generated using pytest-html

--------------------------------------
CONTACT
--------------------------------------

Maintainer: Nipuna Jayawardana
Email: jayjay0109@gmail.com
