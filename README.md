# Installation

1. Run dotenv_create.py to setup and .env file with configurations

    `python dotenv_create.py`

2. Create and activate a virtual environment with your preferred method (detailed below)

# Run the bot

- After completing the installation process, you can run the bot just using:

    `python main.py`

- If you used pipenv, use this command instead

    `pipenv run python main.py`

- Make sure to activate the virtual environment if needed (see below)

# Setting up the virtual environment

## Using venv module

1. Create the virtual environment

    `python -m venv VENV_NAME`

    This will create a folder named VENV_NAME in your current directory

    The name VENV_NAME is just for this example, please choose a more descriptive name for the folder instead.

2. Activate the virtual environment

    Activating the virtual environment depends on the OS you're running:

    - Windows: `.\VENV_NAME\Scripts\activate`
    - Linux: `source VENV_NAME/bin/activate`
    
3. Install the requirements

    `pip install -r requirements.txt`

## Using pipenv

(Make sure you have pipenv installed in your system)

Using pipenv you only need one command to set it up:

`pipenv install -r requirements.txt`

You don't need to activate the virtual environment when using pipenv. If you need you run anything with the virtual environment, do it using `pipenv run` or `pipenv shell`

## Install globally (not recommended)

You can install the requirements globally, it's more comfortable and easy, but not recommended at all. Please consider using other methods instead.

Run this command:

`pip install -r requirements.txt`

