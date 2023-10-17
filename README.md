## Pytest + Playwright UI-autotest (homework in QA Bootcamp).

Simple UI-tests for QA Bootcamp-23 written to understand the basics of playwright.

__test_apigw_pages.py__ in main branch just opens and checks 
some pages and sections related to API Gateway (product developed by Cloud.ru).

Web-site in use: https://cloud.ru/ru

## Tools used
- pytest 7.4.0
- playwright 1.38.0
- pytest-playwright 0.4.3

## Project setup
1. Clone the project's repository 
```
$ git clone https://github.com/verveder/autotest_hw.git
```
2. Open the project's directory
```
$ cd autotest_hw
```
4. Install required dependencies (if necessary)
```
$ pip install -r requirements.txt 
```

## Running test
__test_apigw_pages.py__ runs on Chrome in headless mode 
(to change that, edit tests/conftest.py so that _chromium_page_ fixture has _headless=False_).

4 tests in total: 3 normal and one designed to fail
(the last one not marked by @pytest.mark.xfail just to see it how it fails, and not to have it skipped)

To run tests: 
  ```
  $ pytest src/tests/test_apigw_pages.py
  ``` 
