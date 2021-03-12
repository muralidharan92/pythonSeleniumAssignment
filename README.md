### Execute Command
    behave -f allure_behave.formatter:AllureFormatter -o ./reports/ features/ --no-capture

## To Generate Report
    allure serve ./reports