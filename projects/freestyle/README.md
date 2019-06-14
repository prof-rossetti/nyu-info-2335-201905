# Self-Directed (a.k.a. "Freestyle") Project

The "Freestyle" Project provides students with the flexibility to follow their own interests by planning and implementing their own application software.

Students may work on these projects independently, or with one or two other group members. Each group should contain between one and three members, and these group member compositions should be designated during the Proposal phase.

## Deliverables

Follow the links below for more information about each deliverable, including submission instructions and evaluation criteria.

### [Proposal](proposal.md)

During the ideation phase, students will brainstorm their application's scope and objectives and submit this information to the professor for approval and further guidance.

During the proposal phase, students will also officially designate whether they would like to work independently, be paired with a random partner, or be paired with a partner of choice. For mutual partner selections, each student should designate the other as their partner. If pairing, students should strive to significantly increase their project's scope / difficulty level, and each student is expected to make significant contributions to the application's source code.

### [Demo](demo.md)

After coding the application, students will demonstrate selected functionality for the rest of the class. Students will submit a presentation document, including screenshots and screencasts as desired.

### [Documentation](documentation.md)

After their proposals are approved, students will further define and document their application's requirements and planned functionality. Students will submit a requirements document to include user stories, diagrams, and interface mockups as necessary.

### [Implementation](implementation.md)

After defining requirements, students will write Python code to implement some or all of the application's desired functionality. Students will also write Python code to automatically "test" or control the quality of their applications. Students will submit a Git repository containing their application's source code and tests.


<hr>

## Guidelines

Each project's requirements will be unique, but students should strive to generally adhere to the spirit of the guidelines below.

### Scope

The scope of the application's functionality should be around the same as previous projects.

> DIFFICULTY BONUS: The scope should be two to three times greater than previous projects.

### User Interface

The application's interface should be intuitive to use and simple to understand. It should provide clear instructions as necessary.

> DIFFICULTY BONUS: The user should be able to use the application through an interface other than, or in addition to, the command-line. These alternative interfaces include, but are not limited to:
>
>  + A Native Graphical User Interface (GUI), implemented with a package like [`tkinter`](/notes/python/packages/tkinter.md)
>  + A Web-based Graphical User Interface (GUI), implemented with a package like [`flask`](/notes/python/packages/flask.md)
>  + A Speech-based Interface, implemented with a package like [`speech_recognition`](/notes/python/packages/speech_recognition.md)

### Data Processing

The application should process (read and/or write) data in at least one of the following machine-readable formats:
CSV, JSON, HTML, XML, SQL, PDF.

> DIFFICULTY BONUS: The application should store data in a local file, a relational database, or a Google Sheets spreadsheet document (see [`gspread`](/notes/python/packages/gspread.md) package).

### Network Integration

The application should process data from the Internet by requesting data from, posting data to, or otherwise interfacing with one or more third-party web services (APIs).

> DIFFICULTY BONUS: The application should be accessible to users over the Internet (i.e. a production web application).

### Hardware Integration

The application should be able to be run from a Mac or Windows computer.

> DIFFICULTY BONUS: The application should be deployed to a remote server (i.e. production web application or scheduled notification service).


> DIFFICULTY BONUS: The application should incorporate other physical devices such as sensors and scanners.
