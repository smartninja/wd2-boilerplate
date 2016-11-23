# Tests

## Installation

To run tests you need to have these Python libraries installed via PIP:

    pip install nose
    pip install NoseGAE
    pip install WebTest


## Writing tests

See `main_page_tests.py` file for an exampleof how to write a test.

**Important:** Always include word "test" in your test files. Function names should start with "test_".

## How to run tests

Run tests via command line (terminal).

**Run all tests:**

    nosetests -v --with-gae

If it doesn't recognize GAE path, you have to set it up. See `--gae-lib-root` under `nosetests --help`.

**Run only tests in one file:**

    nosetests -v --with-gae main_page_tests

**Run only one test in a file:**

    nosetests -v --with-gae main_page_tests:MainPageTests.test_main_page_handler

## Useful resources

- [Unit testing GAE apps in Python](http://ahoj.io/unit-testing-gae-apps-in-python)
- [NoseGAE docs](http://farmdev.com/projects/nosegae/)
- [Nose docs](https://nose.readthedocs.org/en/latest/)
- [GAE handler testing](https://cloud.google.com/appengine/docs/python/tools/handlertesting)
- [GAE local unit testing](https://cloud.google.com/appengine/docs/python/tools/localunittesting)