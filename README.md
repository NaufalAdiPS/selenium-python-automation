# selenium-python-automation

Practice automation testing scripts built with **Python**, **Selenium WebDriver**, and **pytest**. This repo is a personal QA/automation practice space — new test scripts will be added over time as I build out more automation skills.

Current tests cover:
- Login flow testing (cookie consent handling, explicit waits, form submission, success message assertion)

## Setup

#### 1. Clone this repository

```
git clone https://github.com/<your-username>/selenium-python-automation.git
```

#### 2. Navigate to the project directory

```
cd selenium-python-automation
```

#### 3. Create a virtual environment

- On Windows:

```
py -m venv venv
venv\Scripts\activate
```

- On Linux/Mac:

```
python3 -m venv venv
source venv/bin/activate
```

#### 4. Install dependencies

```
pip install -r requirements.txt
```

> for help, see: https://packaging.python.org/en/latest/tutorials/installing-packages

## Running tests

- Run all tests:

```
pytest
```

- Run a specific test:

```
pytest tests/test_login.py
```

## Project structure

```
selenium-python-automation/
├── README.md
├── requirements.txt
├── .gitignore
├── tests/
│   └── test_login.py
```
