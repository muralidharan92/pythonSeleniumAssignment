# Trello Automation Assignment using Selenium & Python

## Command for execute script with Report
    behave -f allure_behave.formatter:AllureFormatter -o ./reports/ features/ --no-capture

## Command for execute script without Report
    behave features/ --no-capture

## To Generate HTML Report
    allure serve ./reports

## Project used Libs
    selenium
    behave
    requests
    PyYAML
    allure-behave

## Browser
    Chrome

## Additional Feature
    Added Screenshot for failed steps
    Added Screenshot for every scenario complete
    Used REST API to encrypt & decrypt data
