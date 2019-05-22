# Anaconda

Anaconda provides a command-line utility called `conda` for installing and managing different versions of the Python programming language and third-party packages.

> Anaconda is a package manager, an environment manager, a Python/R data science distribution, and a collection of over 1,500+ open source packages. Anaconda is free and easy to install, and it offers free community support. - [Anaconda website](https://docs.anaconda.com/anaconda/)

Resources:

  + https://conda.io/docs/_downloads/conda-cheatsheet.pdf
  + https://conda.io/docs/user-guide/getting-started.html
  + https://conda.io/docs/user-guide/tasks/manage-conda.html
  + https://conda.io/docs/user-guide/tasks/manage-environments.html
  + https://conda.io/docs/user-guide/tasks/manage-pkgs.html#id2
  + https://conda.io/docs/user-guide/tasks/view-command-line-help.html

## Detection

To check to see if Anaconda is already installed:

```sh
conda --version
#> conda 4.5.12

# Mac Terminal:
which conda
#> /anaconda3/bin/conda

# Windows Anaconda Prompt:
where conda
#> C:\Users\YOUR_USERNAME\Anaconda3\Library\bin\conda.bat
#> C:\Users\YOUR_USERNAME\Anaconda3\Scripts\conda.exe
```

On a Mac, you can invoke these commands directly in the Terminal.

![](/img/notes/anaconda/mac-terminal.png)

### Detection on Windows

However, on Windows, you can alternatively search for the "Anaconda Prompt" application to know whether or not you have it installed.

![](/img/notes/anaconda/windows-detecting-anaconda-prompt.png)

After the Anaconda Prompt is installed, you can invoke these commands from within it.

![](/img/notes/anaconda/windows-anaconda-prompt.png)

## Installation

If not yet installed, [download Anaconda Version 3.7](https://www.anaconda.com/download) for either Mac or Windows. NOTE: This might take a while, so prefer to do it over a strong WiFi connection. And feel free to ignore any email capture forms which may pop up afterwards.

![](/img/notes/anaconda/downloading-anaconda-windows.png)

After the download has finished, run the installer program and accept all the default options. The installation will take a few minutes to complete. After a while it may ask you whether or not you'd like to also install a text editor called "VS Code". Since VS Code is the preferred text editor for this course, you can feel free to keep this option checked, and the installer will ensure it is installed.

![](/img/notes/anaconda/anaconda-install-vs-code.png)

> DISCLAIMER: the professor had already installed VS Code before installing Anaconda, so if installing VS Code via Anaconda presents any issues, please report them immediately. Alternatively, you can always install VS Code separately.

> NOTE: After installing Anaconda on a Mac, you will need to restart your terminal for the changes to take effect.

After the installation is complete, try repeating the detection commands again, as described in the section above.

Once you are able to successfully detect your installation of Anaconda, you are ready to proceed!

## Usage

### The `conda` Utility

When activating Anaconda virtual environments and issuing project-specific `conda` commands, we generally want to do so within that project's directory. So let's take a moment to create a new project directory now, then navigate there from the command line:

```sh
cd path/to/my-first-project/ # where path/to/my-first-project/ is the actual path of your desired project directory
```

All subsequent commands assume you are running them from within the project's root directory.

#### Managing Virtual Environments

View a list of existing virtual environments:

```sh
conda env list
```

Create a new virtual environment, and name it something like "my-first-env":

```sh
conda create -n my-first-env

# FYI: you can specify a Python version for your new environment with...
# conda create -n my-first-env python=3.7

# FYI: you can delete any environment with...
# conda env remove -n my-first-env
```

Enter into, or "activate", the virtual environment:

```sh
conda activate my-first-env

# FYI: to deactivate...
# conda deactivate
```

Once activating the environment, you should be able to detect and use its installations of Python and Pip:

```sh
which python #> /anaconda3/envs/my-first-env/bin/python
python --version #> Python 3.6.7 :: Anaconda, Inc.

which pip #> /anaconda3/envs/my-first-env/bin/pip
pip --version #> pip 18.1 from /anaconda3/envs/my-first-env/lib/python3.6/site-packages/pip (python 3.6)
```

![](/img/notes/anaconda/managing-envs.png)


For more information, see notes on [the `python` utility](python.md) and [the `pip` utility](pip.md).
