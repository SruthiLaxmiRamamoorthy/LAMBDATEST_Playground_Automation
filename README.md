# This README file provides instructions on how to run the LAMBDATEST_Playground tests and dependencies required for the project.

# Dependencies:
To run the tests successfully, you will need the following dependencies installed:
Python
Pytest
PyCharm (or any Python IDE of your choice)
Selenium
Driver Jar Files 

# Installation:
**Python**: You can download and install it from the official Python website: Python Downloads
**Pytest**: You can install pytest using pip, a package management system for Python. Open your terminal or command prompt and run the following command: pip install pytest
**PyCharm**: Download and install PyCharm, an integrated development environment (IDE) for Python, from the official website: PyCharm Downloads
**Selenium**: Install Selenium using pip: pip install selenium
**Driver Jar Files**: Download the driver jar files for the specific browser(s) you intend to test (e.g., ChromeDriver for Google Chrome, GeckoDriver for Mozilla Firefox) and place them in your project directory.

# Configuration:
Once you have installed the dependencies, you need to configure your project:
1. Open the project in PyCharm or your preferred Python IDE.
2. To run the tests from the terminal/command prompt, navigate to the project directory and execute the following command: pytest -rA
This command will run all the tests and display detailed information about the results.

# Generating Test Report:
To generate a test report in HTML format, run the following command: pytest -rA --html="report.html"
Replace "report.html" with the desired name for your report file.
This command will execute the tests and generate an HTML report with detailed information about the test results.
