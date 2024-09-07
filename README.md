**Configure Project**
- Clone URL and write in cmd in any location of your system
**git clone** git@github.com:Ghayur99/E2E-testing-of-web-app-with-selenium-python-pytest.git
- To execute the following command on the terminal: git checkout develop
- Switch your branch:
- i.e.: git checkout feature/employee-crud-t4slips
# Configure Python Project
- Open pycharm, open project from **File** menu
- Set the configuration from **Debug Configuration**
- "pip install virtualenv"dir
- Create venv > "virtualenv venv"
- To activate venv > go to Script folder > "activate"
- Install packages into venv "pip install -r requirements.txt"
  - install the latest chrome driver from that url(window user download window version, Linux u
    ser download linux version):
    https://chromedriver.chromium.org/downloads
      - Set the driver path in following: settings/development.py file.
      - Set the login credentials in settings -> development.py file.
- To generate the report of all test cases execute the following commands on the terminal:
            "pip install pytest-html"
            "pytest --html=report.html"
- To execute the test implementation from all the files
  in the folder & sub-folders execute the following command on the terminal:
        "pytest --verbose --capture=no"
  - This command is used, if you run the specific test case
- Pytest -k testName or methodName -v -s
