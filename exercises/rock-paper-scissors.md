# "Rock, Paper, Scissors" Exercise

> Prerequisites:
>   + [Software Products and Services](/units/unit-1.md)
>   + [User Interfaces and Experiences (UI/UX)](/units/unit-2.md)
>   + [Python Language Overview](/units/unit-3.md)

## Learning Objectives

  + Gain familiarity with the Python programming language, with a focus on variables conditional logic.
  + Practice processing and validating user inputs.
  + Practice using a text editor to edit and save Python scripts.
  + Practice version control using GitHub Desktop.
  + Observe the relationship between application logic and automated tests, and start to get a feel for what logic to test and why.

## Instructions

Iteratively develop a Python application which will allow a user to play a game of Rock-Paper-Scissors against an AI (computer) opponent. The game should adhere to the "Basic Requirements" below.

As you progress, you are encouraged to incorporate version control practices into your development process by using GitHub Desktop to intermittently "commit", or save different versions of, your code along the way.

Before attempting to implement the requirements, take some time to set up your exercise repository.

## Setup

Use GitHub Desktop or your command-line application (Terminal on Mac, or Git Bash on Windows), to create a new local repository on your Desktop called "rock-paper-scissors-exercise", and navigate there from the command-line.

```sh
git init ~/Desktop/rock-paper-scissors-exercise # (or create the repo manually via GitHub Desktop)
cd ~/Desktop/rock-paper-scissors-exercise
```

Use your text editor or the command-line to create new files in that repo:

```sh
```

Create and activate a new Anaconda virtual environment:

```sh
conda create -n game-env python=3.7 # (first time only)
conda activate game-env
```

From within the virtual environment, install the `pytest` package (can feel free to do this later, only if you are tackling the "Automated Testing" further exploration challenge):

```sh
pip install pytest
```

Alright, now you

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
