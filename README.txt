Airalo Test Automation Framework
================================

This is a combined UI and API test automation framework built using:
- Playwright (for UI)
- Pytest
- Python
- Requests (for API)
- dotenv (for secrets management)

It follows the Page Object Model (POM) for UI tests, and uses modular, maintainable test utilities for API testing. Includes logging, test data separation, and HTML reporting.

--------------------------------------
SETUP INSTRUCTIONS
--------------------------------------

1. Create Virtual Environment:

   python -m venv venv

   On Windows:    venv\Scripts\activate
   On Mac/Linux:  source venv/bin/activate

2. Install Required Packages:

   pip install -r requirements.txt

3. Install Playwright Browsers (for UI tests only):

   playwright install

4. Set up Environment Variables:

   Copy `.env.example` to `.env` and fill in your credentials:

   cp .env.example .env

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
   pytest tests/api/test_esim_flow.py::test_create_order -s

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
│   ├── test_data.json          -> UI test datasets
│   └── test_data.py            -> Optional structured test data helper
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
ENVIRONMENT VARIABLES (.env)
--------------------------------------

This project uses a `.env` file to manage sensitive credentials like API keys.
**Do not commit this file.**

A sample file is included as `.env.example`.

How to Use It:

1. Copy the example file:
   cp .env.example .env

2. Fill in your actual credentials in `.env`:

   CLIENT_ID=your_real_client_id_here
   CLIENT_SECRET=your_real_secret_here

3. `.env` is already added to `.gitignore`, so it will be excluded from version control.


--------------------------------------
NOTES
--------------------------------------

- Python version required: 3.11 or higher
- Internet connection is required for live tests
- All secrets and keys are handled via .env and loaded with python-dotenv
- Logs are written to disk per session using the custom logger in /utils

--------------------------------------
CONTACT
--------------------------------------

Maintainer: Nipuna Jayawardana
Email: jayjay0109@gmail.com
