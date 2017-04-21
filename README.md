# Exercise 8: Collaborative Work & Deployment to PaaS

CSCM602023 - Advanced Programming (Pemrograman Lanjut) @ Faculty of
Computer Science Universitas Indonesia, Even Semester 2016/2017

[![build status](https://gitlab.com/CSUI-AdvProg-2017/lab-exercises/badges/week_8/build.svg)](https://gitlab.com/CSUI-AdvProg-2017/lab-exercises/commits/week_8)

* * *

This tutorial will introduce students to the software product that will
worked on during class project period. Students can team up with 2 - 3
friends to finish this tutorial. *Please note that this team is intended
for this tutorial, not for the upcoming class project.*

## Table of Contents

1. [Preparation](#preparation)
2. [First Part: Collaborative Work](#first-part-collaborative-work)
3. [Second Part: Deploy to PaaS (Heroku)](#second-part-deploy-to-pass)
4. [Mandatory Checklist](#mandatory-checklist)
5. [Additional Checklist](#additional-checklist)
6. [Guide: How the Bot Works](#guide-how-the-bot-works)
7. [Guide: How to Run Tests/Linter](#guide-how-to-run-tests-linters)

## Preparation

1. Fork the template repository to your GitLab account and clone the
forked repository to your local machine.

    If you are working on your partner's repository, clone your 
    partner's repository instead of cloning the template repository.
    Do not forget to ask for Developer role so that you can make
    commits and push them to your partner's repository.
2. Navigate to the project directory where you cloned the repository
in your local machine.
3. Create a new virtual environment using built-in `venv` module. In
the command prompt/shell, execute: `python -m venv env`

    If you are using IDE (e.g. PyCharm), do not forget to set PyCharm
    to use the recently created virtual environment.
4. Activate the virtual environment. The commands are different depend
on the OS. On Windows, execute: `env\Scripts\activate.bat`; On Unix-based
OS, execute: `source env/bin/activate`
5. Install the required dependencies. Execute:
`pip install -r requirements.txt`

    Dependencies are all listed in `requirements.txt`. To re-generate
    this file (after installing new packages), simply run:
    `pip freeze > requirements.txt`; For Unix-based OS users, if there
    are problems installing the dependencies, install `python3-dev` or
    `python3-devel` system package first.
6. Create `.env` file under the project root directory. It contains the
configuration variables for the application. Sample `.env` file can be
found in `env.example`. If you have a problem in generating `.env` in
Windows, you can use Git Bash and run this command on the project
directory: `cp .env.example .env`
7. Run the application: `python manage.py runserver`. The command
prompt/shell should display a message similar to `* Running on
http://127.0.0.1:5000/ (Press CTRL+C to quit)`

    Reminder: Always ensure that the virtual environment has been
    activated before running the application!
8. Terminate the application by pressing CTRL-C (or equivalent key
combinations on Mac-based laptops)

## First Part: Collaborative Work 

See [MANDATORY.md](MANDATORY.md).

## Second Part: Deploy to PaaS

See [ADDITIONAL.md](ADDITIONAL.md).

## Mandatory Checklist

- [X] (For repository owner) Create a fork from the template repository
- [X] (For collaborators) Has Developer role in partner's repository
    - Tips: To make your demo session more convenient, bring your
    partners (i.e. repository owner and collaborators) during demo session
    with TA
- [X] Write unit tests for all zodiacs and shios
- [X] Implement all zodiacs and shios
- [X] Can run unit tests although there is at least one failing unit tests
- [X] Can run linter although there are at least one complaints generated
by the linter
- [X] All branches are merged into `master` branch

## Additional Checklist

- [ ] All unit tests except `test_get_index` pass succesfully
- [ ] Linter does not produce any complaints when run on `master`
branch
- [ ] Deploy the bot on Heroku 
- [ ] The bot can respond to valid input when given zodiac & shio
commands
- [ ] The bot can respond to invalid input when given zodiac & shio
commands

## Guide: How the Bot Works

There are two ways for the bot to get updates from Telegram: long
polling and webhook. In this project, we are using webhook.
By using `setWebhook` method provided by Telegram API, we can associate
a bot with a webhook URL so that whenever there is an update (e.g. a
new message, a new member joining a group, etc.), Telegram will send
the update data to the webhook URL in a JSON format. The general steps
are as follows:

1. An update occurs in a chat or group of which the bot is a member.
2. Telegram sends the update to the bot's webhook URL as HTTP POST
request containing JSON data.
3. Server makes a request to Telegram via its Bot API to initiate bot's
response, while responding with 200 status to the HTTP POST request
made by Telegram.

More detailed information can be found [here](https://core.telegram.org/bots/api#getting-updates).

## Guide: How to Run Tests/Linter
 
1. Make sure you already installed [pytest][pytest] and [flake8][flake8]. Both are listed in `requirements.txt` so if you followed the instructions to setup your machine above then they should already be installed.
2. Put an `.env` file under your `tests` directory. This file could be identical to the one in project root directory or you may also set some environment variables for testing to your liking.
3. You can run the tests and linters with `python manage.py test` and `python manage.py lint` respectively.
4. To run both linters and tests in one command, you can use `python manage.py check`. This is useful to check your code before making a merge request.
5. For more info on what you can do with `manage.py`, run `python manage.py --help`.

[pytest]: http://pytest.org/latest/
[flake8]: https://pypi.python.org/pypi/flake8
