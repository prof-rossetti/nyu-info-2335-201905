# "Freestyle" Project Implementation

> Prerequisite: ["Freestyle" Project Description](/projects/freestyle.md)

## Instructions

After producing a written [Planning and Requirements Document](/projects/freestyle/requirements.md), it's time to write application software in the Python programming language to implement your proposed solution.

In addition to addressing your system's written functionality requirements, the implementation should adhere to the requirements below.

### Documentation Requirements

Your project repository should contain a "README.md" file. The README file should provide instructions to help someone else install, setup, run, and test your program. This includes instructions for installing package dependencies, for example using Pip. It also includes instructions for setting environment variables as necessary.

As you document for your application, strive to make it as easy as possible for someone else (or even your future self) to install it, use it, and understand what it is about.

### Licensing Requirements

[Choose a software license](/notes/licensing.md), and include a corresponding file called "LICENSE" or "LICENSE.md" in the root directory of your repository.

### Security Requirements

If your program requires sensitive information like secret passwords, API keys, or other credentials, those secret values should absolutely not be included in the source code or its revision history.

Use environment variables in conjunction with a ".env" file and a ".gitignore" file to read sensitive information from the software's operating environment while excluding them from the source code.

### Quality Requirements

#### Code Simplification

Scan your application's codebase for duplication of terms, and refactor to remove that duplication.

Also, your codebase should be reasonably organized and well documented with comments, to help others (and your future self) understand the code.

#### Automated Tests

Implement automated tests using the `pytest` package.

As you think about ways to test your application, consider asking yourself questions like the following:

  + As I was developing this application, what manual steps did I take to ensure it was functioning properly? Can I automate those manual processes?
  + Is it possible for the application to receive user inputs that are unexpected or invalid? How should the application handle various invalid inputs?
  + How should the application's component functions perform given various inputs, whether valid or invalid?
  + Are there any functions or sections of the code which aren't easy to read or understand? Is there a way to use examples to communicate what is supposed to happen?
  + If the application processes data from the Internet: Is there a way to test the application's functionality without making any additional network requests?
  + If the application processes data from a CSV file or database: Is there a way to test the application's functionality without affecting the development environment datastore?

#### Continuous Integration

Configure your GitHub repository to integrate with a continuous integration (CI) platform like [Travis CI](/notes/travis-ci.md), such that automated tests are run on a CI server whenever new code is pushed to the remote GitHub repository.

### Dev Process Requirements

Develop your updates [on a branch](/notes/git.md#branch-operations), push that branch to GitHub in order to create a Pull Request, where you can further review your proposed changes and allow automated tests to run and pass on the CI server before finally "merging" the code into the master branch.







## Submission Instructions

To submit:

  1. Push your local project repository to GitHub, so you can visit your remote project repository at a URL like `https://github.com/YOUR_USERNAME/YOUR_REPO`.
  2. Fork the ["upstream" course repository](https://github.com/prof-rossetti/georgetown-opim-243-201901) (or refresh your existing fork).
  3. Update your forked course repository's ["Freestyle" Submissions CSV file](/projects/freestyle/submissions.csv).
to include your GitHub username and your project repository's URL.
  4. Submit a Pull Request for your forked course repository's changes to be accepted into the "upstream" course repository.

## Evaluation

Implementations will be evaluated based on the criteria below:

Category | Requirement | Weight
--- | --- | ---
Satisfies Proposed Requirements | Addresses a problem discussed in the previously-delivered requirements document, in a manner generally consistent with the plan discussed in that document | 10%
Uniqueness and Individuality | Exhibits creativity, and a unique set of functionality | 10%
User Experience | Provides a simple, pleasant, and intuitive experience for the user, free of idiosyncrasies | 10%
Documentation | Contains a comprehensive README file | 10%
Licensing | Contains an appropriate LICENSE file | 5%
Security | Excludes sensitive information and credentials | 10%
Quality | Simplified to remove or minimize code duplication | 10%
Quality | Contains relevant automated tests | 10%
Quality | Deployed to a continuous integration (CI) server | 5%
Dev Process | Submitted via Git repository which reflects an incremental revision history, branch operations, a Pull Request workflow, and contributions from all team members | 20%

This rubric is tentative, and may be subject to slight adjustments during the grading process.
