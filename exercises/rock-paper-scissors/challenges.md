# "Rock, Paper, Scissors" Exercise - Further Exploration

## Challenges

If you were able to implement the [basic requirements](README.md) with relative ease, or if you are interested in a challenge, consider expanding the scope to include one or more of the challenges below.

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
