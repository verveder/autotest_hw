## Pytest + Playwright UI-autotest (homework in QA Bootcamp).

Has two variants: 
- simple one-module test _(test_simple.py)_ written on the go
  
- test in _src_ folder _(src\tests\test_oop_style.py)_,
trying to be OOP- and POM-like;
written after thorough reading of pytest and playwright docs
with referring to existing autotests

## Tools used
- pytest 7.4.0
- playwright 1.37.0
- pytest-playwright 0.4.2

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
Both tests are running on Chrome in headed mode.
Web-site in use: https://cloud.ru/ru

! Run each test separately.

- To run simple test:
  ```
  $ pytest test_simple.py

  ```
- To run OOP-like test:
  ```
  $ pytest src\tests\test_oop_style.py
  ```

  
