# "Rock, Paper, Scissors" Exercise

> Prerequisites:
>   + [Software Products and Services](/units/unit-1.md)
>   + [User Interfaces and Experiences (UI/UX)](/units/unit-2.md)
>   + [Python Language Overview](/units/unit-3.md)

## Learning Objectives

  + Gain familiarity with the Python programming language, with a focus on variables, functions, and conditional logic.
  + Practice processing and validating user inputs in Python.
  + Practice using a text editor to edit and save files of Python code.
  + Learn how to incorporate version control practices into your development process.
  + Observe the relationship between application logic and automated tests, and start to get a feel for what logic to test and why.

## Instructions

Iteratively develop a Python application which will allow a human user to play a game of Rock-Paper-Scissors against an AI (computer) opponent. The game's functionality should adhere to the "Basic Requirements" below.

Before attempting to implement the requirements, take some time to set up your project repository according to the "Setup" instructions below. After doing so, you'll have a remote repo on GitHub.com and a local copy on your computer within which to develop.

as you reach key development milestones, use the command-line or GitHub Desktop software to intermittently "commit", or save new versions of, your code. And remember to push / sync / upload your work back up to your remote project repository on GitHub.com at least once before you're done.

## Setup

### Repo Setup

Use the GitHub.com online interface to create a new remote project repository called something like "rock-paper-scissors-exercise". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like `https://github.com/YOUR_USERNAME/rock-paper-scissors-exercise`.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/rock-paper-scissors-exercise
```

Use your text editor or the command-line to create a file in that repo called "game.py", and then place the following contents inside:

```py
# game.py

print("Rock, Paper, Scissors, Shoot!")
```

Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file.

### Environment Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n game-env python=3.7 # (first time only)
conda activate game-env
```

From within the virtual environment, install the `pytest` package:

```sh
# NOTE: we won't need pytest until/unless addressing the optional "Automated Testing" challenge,
# so you can feel free to skip this now and return later...

pip install pytest
```

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python game.py
```

If you see the "Rock, Paper, Scissors, Shoot!" message, you're ready to move on to project development. This would be a great time to make any desired modifications to your project's "README.md" file, and then make your first commit, with a message like "Setup the repo".































## Basic Requirements

The gameplay logic should meet the basic requirements set forth below. It should first process user inputs, then simulate a computer selection, and then determine the winner and display the results back to the user.

### Processing User Inputs

The application should prompt the user to input or otherwise select an option (i.e. "rock", "paper", or "scissors") via a command-line interface (CLI).

### Simulating Computer Selection

The application should select one of the options (i.e. "rock", "paper", or "scissors") at random, and assign that as the computer player's choice.

### Determining the Winner

The application should compare the user's selection to the computer player's selection, and determine which is the winner.

### Displaying Results

After determining the winner, the application should display the results to the user. These information outputs should include:

  + A friendly welcome message (e.g. "Hi, welcome to my rock-paper-scissors game!")
  + The user's selection (e.g. "User selection: 'rock'")
  + The computer's selection (e.g. "Computer selection: 'paper'")
  + The winner's name (e.g. "The computer won.")
  + A friendly farewell message (e.g. "Thanks for playing, please play again!")

See example output below:

```
-------------------
Launching the game...
-------------------
Please choose either 'rock', 'paper', or 'scissors': rock
-------------------
You chose: rock
The computer chose: paper
-------------------
Oh, the computer won. It's ok.
Thanks for playing. Please play again!
```

<hr>

## Further Exploration

If you were able to implement the basic requirements with relative ease, or if you are interested in a challenge, consider expanding the scope to include one or more of the challenges below.

### Validating User Inputs

The application should either not allow the user to input an invalid selection (perhaps as a result of following the "Graphical User Interface" challenge below), or it should validate those inputs.

To validate the inputs, compare the user's selection against the list of valid options to determine whether the user has selected a valid option. And if the selection is invalid, the program should fail gracefully by displaying a friendly message to the user, and stopping further program execution. The program should not try to further process an invalid input, as it may lead to runtime errors.

### UI / UX Improvements

Besides allowing and needing to handle invalid inputs, are there any issues with the basic command-line interface (CLI)? For example, does it elicit biased responses from the user due to the user's desire to type the easiest option (i.e. "rock")? Should the user enter numbers (e.g. "1", "2", or "3") or single-letters (e.g. "R", "P", "S") instead of entire words?

Besides these and other possible improvements to the command-line interface (CLI), provide the best user experience possible?

How could you modify the user interface to improve the user experience? Should there be images involved? Some other kind of selection mechanism like a dropdown, list-box, or large press-able buttons?


 For example, would you like to implement the user interface as a native GUI using the PySimpleGUI package, or as a browser / web application using the Flask package? See the professor's example Rock-Paper-Scissors applications for guidance and examples of how to do this.


### Automated Tests

So by now you've probably been running the app manually to determin whether or not it is behaving as desired. But due to the randomness of the computer's generated selection, you might have to run many iterations of the game before you are able to _______ it determines the winner under all possible scenarios.

Are you able to abstract any of the gameplay logic, like the determination of the winning selection, into a custom function? Doing so will allow you to test that function's logic in isolation.

Create another file in your repo called "game_test.py" and place inside the following contents:

```py
# game_test.py

from game import determine_winner

def test_determination_of_the_winner():
    assert determine_winner("rock", "rock") == None # represents a tie
    assert determine_winner("rock", "paper") == "paper"
    assert determine_winner("rock", "scissors") == "rock"

    assert determine_winner("paper", "rock") == "paper"
    assert determine_winner("paper", "paper") == None # represents a tie
    assert determine_winner("paper", "scissors") == "scissors"

    assert determine_winner("scissors", "rock") == "rock"
    assert determine_winner("scissors", "paper") == "scissors"
    assert determine_winner("scissors", "scissors") == None # represents a tie
```

Then use the `pytest` package to run the test:

```sh
pytest game_test.py
```
