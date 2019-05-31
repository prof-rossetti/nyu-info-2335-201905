# The `pytest` Package

Reference:

  + https://github.com/pytest-dev/pytest/
  + https://docs.pytest.org/en/latest/
  + https://docs.pytest.org/en/latest/getting-started.html#our-first-test-run
  + https://docs.pytest.org/en/latest/goodpractices.html
  + https://docs.pytest.org/en/latest/usage.html#dropping-to-pdb-python-debugger-on-failures
  + http://python-guide-pt-br.readthedocs.io/en/latest/writing/tests/#py-test

## Installation

If you are using Pip to manage software packages, install `pytest`, as necessary:

```sh
pip install pytest
```

Otherwise, if you are using Pipenv, you will want to first navigate inside your repository's root directory before installing `pytest`:

```sh
cd path/to/my-repo/
pipenv install pytest --dev # optionally use the --dev flag to denote this package will be used in development only
```

## Usage

The `pytest` package is generally used as a command-line utility for running pre-defined files of "test" code.

### Challenge 1: Testing Python Scripts

To setup this first example, create a new directory on your Desktop called "testing-123" and navigate there from your command line, then create files called "my_script.py" and "my_test.py" and place inside the following contents, respectively:

```python
# testing-123/my_script.py

def enlarge(i):
    return i * 100
```

```python
# testing-123/my_test.py

from my_script import enlarge # load the `enlarge()` function to avoid NameError: name 'enlarge' is not defined

def test_enlarge(): # note the function name is prefixed with "test_"
    result = enlarge(3) # directly invoke the function we want to test
    assert result == 300 # describe expectations for desired behavior
```

Once you have setup the example files, create and activate a new Python 3.7 virtual environment, then from within the virtual environment: install the `pytest` package and use it to run the tests:

```sh
cd testing-123/

# configure virtual environment (first time only)
conda create -n testing-123-env python=3.7
conda activate testing-123-env

# install pytest package (first time only)
pip install pytest

# run the tests:
pytest #> 1 passed in 0.01 seconds
```

Nice!

> NOTE: this will generate some files in a new directory called `__pycache__/`. These files should be ignored from version control, using a .gitignore file!

### Challenge 2: Testing Python Applications

When testing larger applications, conventions suggest we should move the application and test files into their own separate directories called "app" and "test", respectively.

Let's set up this example. First, move your application file into an "app" directory:

```python
# testing-123/app/my_script.py

def enlarge(i):
    return i * 100
```

Then, move your test file into a "test" directory, and slightly modify its `import` statement to reflect the application's new location:

```python
# testing-123/test/my_script_test.py

from app.my_script import enlarge # <-- NOTE this modification (app.my_script)

def test_enlarge():
    result = enlarge(3)
    assert result == 300
```

Once your repository structure looks like this, if you were to try to run tests again, you'd run into an error `ModuleNotFoundError: No module named 'app'`. We need to indicate that scripts inside the "app" directory should be able to be loaded / imported by files in other directories.

In some cases this can be achieved by adding a special file called `__init__.py` to the "app" directory. But for testing purposes, the professor recommends you take the approach of adding a special file called `conftest.py` to the repository's root directory. Even if the contents of that file are blank, it helps the `pytest` package locate the proper files.

Once you have finished setting up this example, including the `conftest.py` file, run the tests again:

```py
pytest #> 1 passed in 0.01 seconds
```

### Further Exploration

Modify the "my_script.py" such that when it is invoked it will use the `enlarge` function to process user inputs:

```python
def enlarge(i):
    return i * 100

original_number = int(input("Please select a number to be enlarged (e.g. 400): "))
print("You chose: ", original_number)
bigger_number = enlarge(original_number)
print("Enlarged number is: ", bigger_number)
```

And invoke it as a script:

```sh
python app/my_script.py
# OR:
# python -m app.my_script
```

Great! At this time, you should be able to invoke the script successfully, but when you try to re-run tests, you will see an error:

```sh
pytest #> OSError: reading from stdin while output is captured
```

When the test file imports the code from the script, it will execute all code in the script's global scope, including the new code which asks for a user input. But it doesn't make sense for our automated test to ask a user for inputs, as there is no user involved in the process. So we need a way to isolate the script's definition from its invocation. We can use a special convention (`if __name__ == "__main__"`) to check whether the file is being invoked from the command-line, or is being loaded from / imported by another file. This allows us to distinguish between what should happen in each case, and prevents certain functionality from being executed when the script is imported as a module. For more details, see also [Custom Modules in Python](/notes/python/modules/README.md).

Let's make that final change now:

```python
def enlarge(i):
    return i * 100

if __name__ == "__main__": # "if this script is run from the command-line, then ..."
    original_number = int(input("Please select a number to be enlarged (e.g. 400): "))
    print("You chose: ", original_number)
    bigger_number = enlarge(original_number)
    print("Enlarged number is: ", bigger_number)
```

After making this small change, you should be able to successfully invoke the script from the command-line, as well as import its functionality into tests:

```sh
python app/my_script.py
# OR:
# python -m app.my_script
```

```sh
pytest #> 1 passed in 0.01 seconds
```

Nice job! You're testing like a pro!
