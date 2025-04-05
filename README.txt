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
│   ├── constant_data.py        -> Shared constants
│   ├── api_test_data.py        -> API-specific test inputs
│   ├── ui_test_data.json       -> UI test datasets
│   └── load_test_data.py        -> Optional structured test data helper
│
├── pages/                      -> Page Object Model (UI)
│   ├── base_page.py
│   ├── home_page.py
│   ├── esim_selection_page.py
│   └── package_details_popup.py
│
├── reports/                    -> Generated HTML reports
│
├── test-logs/                  -> Log files per test session
│
├── tests/
│   ├── api/
│   │   ├── test_order_flow.py  -> Submitting order tests
│   │   ├── test_esim_fetch.py  -> Fetching and verifying eSIM data│   │
│   │
│   └── ui/
│       ├── test_search_destination.py -> UI destination search test
│
├── utils/                      -> Helper and utility scripts
│   ├── logger.py
│   ├── get_token.py
│   ├── payload_factory.py
│   ├── env_loader.py
│   └── __init__.py
│
├── .env                        -> Local secrets (never committed)
├── .env.example                -> Sample env file to copy from
├── .gitignore                  -> Ignore rules for Git
├── conftest.py                 -> Shared fixtures
├── requirements.txt            -> All required dependencies
└── README.txt                  -> This file


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
