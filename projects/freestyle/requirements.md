# "Freestyle" Project Planning and Requirements Document

> Prerequisite: ["Freestyle" Project Description](/projects/freestyle.md)

## Instructions

Prepare a written document (in PDF format) which describes the results of your project planning, analysis, and design efforts.

The document should include an analysis of the problem, comparison of potential solutions, and a description of the functional objectives of your proposed solution. It should convey a thorough understanding of the problem, and a detailed plan to guide future development / implementation efforts.

If the document were to be shared with clients or potential investors, it should reinforce their confidence in your capabilities and planning efforts. If the document were to be shared with a third-party development team, it should convey enough information to instruct the development team what to build.

The document should incorporate embedded illustrations and diagrams as necessary. These may be low-fidelity hand-drawn images, but prefer to deliver higher-fidelity versions produced via a [digital diagramming tool](/notes/diagramming.md).

A reasonable length for this document, including embedded images, is between three and eight pages, with a maximum of around 15 pages.

If you get stuck, try thinking about responses for each of the sections outlined below:

  + Problem Statement
    + User Needs
    + Current State Processes
    + Potential Solutions
  + Proposed Solution
    + Future State Processes
    + System Objectives
    + Information Requirements
    + Functionality Requirements
    + Interface Requirements
    + Technology Requirements

### Problem Statement

What problem would you like to solve, or what opportunity will you address? Why is it a problem? What is the impact of the problem? Provide an executive summary.

#### User Needs

Who are the individuals affected by the problem? How are they impacted? How could their experience be improved? What are their needs? Please include language like: "[WHO] needs [WHAT] so that [WHY]".

#### Current State Processes

Describe the current state of the problematic process, and identify any pain points as applicable.

Include a diagram of the process (i.e. "Current State Process Diagram").

#### Potential Solutions

Brainstorm a few potential solutions to the problem you've identified. Keep in mind, these solutions could be technical or non-technical in nature, and may or may not all involve application software. How can each of these potential solutions help the affected users? After identifying and describing a few potential solutions, compare the merits of each. If the best solution might not translate well into the objectives of this Python programming project, consider identifying a different problem which might lend itself more easily to being solved by a technology solution.

### Proposed Solution

Which solution are you proposing to implement, and why? Provide an executive summary.

#### Future State Processes

Describe the future state of the process to be implemented by your proposed solution, and identify any areas of simplification and automation.

Include a diagram of the process (i.e. "Future State Process Diagram").

#### System Objectives

What are the goals or objectives of your proposed system? Please briefly describe the system's desired functionality at the highest possible level (e.g. "The system should send me an email every morning to share information about the day's weather forecast...").

#### Functionality Requirements

After describing the functionality at a high level, also decompose this functionality into smaller logical sub-components, and describe each in more detail. Prefer to use a hierarchical outline with a section for each of the sub-components.

Describe functionality in terms of desired user experience, as well as underlying system responsibilities. When describing system responsibilities, think in terms of information inputs and outputs (see "Information Requirements" section). When describing functionality in terms of user experience, feel free to include interface mockups and illustrations (see "Interface Requirements" section).

#### Information Requirements

Describe the system's information requirements, in terms of information inputs and outputs. What information inputs does the system require in order to achieve its desired functionality? Where do these inputs come from? What is the data format of these inputs? What information outputs does the system produce in the process of achieving its desired functionality? What will be the data format of these outputs?

Include a Data Flow Diagram to help illustrate these information requirements.

#### Interface Requirements

Describe the mechanisms in which your users will interact with the system.

Include visual representations in the form of mockups, wireframes, flow-charts, storyboards, etc.

#### Technology Requirements

Which APIs, if any, does your system require in order to produce its desired functionality? What functionality do these APIs provide? Why are they necessary or helpful?

Which third-party Python packages, if any, does your system require in order to produce its desired functionality? What functionality do these packages provide? Why are they necessary or helpful?

Will your software be deployed to a remote server (i.e. web app or scheduled service)? Will your system need to integrate with other hardware like scanners and sensors? Describe these hardware integrations.

<hr>


## Submission Instructions

Upload your PDF document [to Canvas](https://georgetown.instructure.com/courses/75384/assignments/203920).

Later, when you create a repository for the ["Freestyle" Project Implementation](/projects/freestyle/implementation.md), you're encouraged to also include this document in that repository in a subdirectory called "planning" or "design", and refer back to it as a guide for your development activities.

## Evaluation

Implementations will be evaluated based on the criteria below:

Category | Weight
--- | ---
Problem Statement | 25%
Potential Solutions | 15%
Proposed Solution | 40%
Thoroughness and clarity of analysis | 20%

This rubric is tentative, and may be subject to adjustments during the grading process.
