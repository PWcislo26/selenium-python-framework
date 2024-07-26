# Test Automation Project

This is my first python test automation project based on Selenium. Tests are based on https://www.saucedemo.com/ web page.
Current collection of tests contains:
- user login (correct / incorrect login and password / lockedout user )
- user logout
- adding product to cart
- full checkout process

## Project Structure 
Short description of main directories and their content
- [pages](pages) - set of class based objects that represent each page, containing methods used in tests.
- [tests](tests) - set of tests for page functionalities.
- [reports](reports) - an example pytest report in .html that is generated for each run of tests.

## Project features
- framework follows page object pattern
- tests can be triggered directly via github actions, report is generated as an artifact and can be downaloded to your pc

## Getting started
To run the project download or clone this repository. You need to install all required packages using pip.
Run below command in your terminal:

```
pip install -r requirements.txt
```

## Run tests

You can run test in various ways. Here are some examples:
This will run all the tests without generating a report
```
pytest
```

This one will generate a report for all tests. Here report is put inside ./reports directory

```
pytest --html=reports/report.html --self-contained-html
```
![image](https://github.com/user-attachments/assets/ae4a7904-be4c-4bec-a38d-4f127bfd11e4)

You can also run chosen test based on pytest marks for example

```
pytest -m login
```
