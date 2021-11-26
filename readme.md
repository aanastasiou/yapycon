# YaPyCon

A Python Console plugin for Yet Another Scientific Artificial Reality Application (YASARA)

**MS Windows Version**.

# Installation

## To install YASARA View:

1. Go to [yasara.org](http://www.yasara.org/viewdl.htm) and "apply" to download YASARA View.
2. An archive is made available to download. The archive's format depends on the selected platform.
   * For the windows version a `DeployYasara.exe` is provided that is approximately 1GB in size.
3. The executable is a self-extracting archive that will create a `yasara/` directory in the Current 
   Working Directory.

## To install (mini) Conda:

1. Go to [conda.io](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html) download and install 
   your favourite Conda.
2. Start an "Anaconda PowerShell Prompt" and make sure that it at least starts within a `(base)` virtual environment.


## To install the plugin

1. Copy `src/yapycon.py` to your `<YASARA_HOME_FOLDER>/plg/` directory 
2. Apply `requirements.txt` to your virtual environment.
3. Activate the virtual environment
4. Launch `<YASARA_HOME_FOLDER>/YASARA.exe` from within an "Anaconda PowerShell Prompt" with the 
   Python Virtual Environment already activated.

* If YASARA has picked up the Python interpreter from your system, the option "Python Console" will appear 
  within the top level "Window" menu, right after the "Update frequency" option.


# Using the plugin

1. Start "Anaconda PowerShell Prompt" and make sure that the right virtual environment is activated
2. Use this same *"terminal prompt"* to launch `<YASARA_HOME_FOLDER>/YASARA.exe`.
3. Select Window --> Python Console
4. A typical Python console is started

At this point, you have both a Python Console to connect to YASARA as well as a Jupyter notebook kernel that 
can connect to YASARA directly.


