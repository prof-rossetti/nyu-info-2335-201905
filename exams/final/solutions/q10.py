
#
# QUESTION 10
#
# Given a Python script located at filepath ​"my-repo/app/services/my_service.py"
# ... and an image file located at filepath ​"my-repo/img/empire-state-building.png", ​
# ... write Python code​ which if written inside the script will reference the image's filepath
# ... in a reliable and operating-system agnostic way.
# ... Store the image's filepath in a variable called ​img_filepath​.
# ... HINT: you might need to leverage the capabilities of a module.
#

# SOLUTION:

import os

img_filepath = os.path.join(os.path.dirname(__file__), "..", "..", "img", "empire-state-building.png")
