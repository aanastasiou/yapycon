# YaPyCon

``YaPyCon`` embeds a Python console in YASARA, *"...a molecular-graphics, -modeling and -simulation
program for Windows, Linux, MacOS and Android"* thereby:

1. Enabling rapid prototyping of YASARA scripts
2. Offering common "shell" functionality such as:
   * Code auto-completion
   * Inline code documentation
   * Tighter integration with ``matplotlib``

3. Improving and expanding certain aspects of YASARA's Python functionality.

![image](https://github.com/aanastasiou/yapycon/raw/main/doc/source/resources/figures/fig_main_yapycon.png?raw=true)

# Quickstart

## Installation

1. Copy ``yapycon/yapycon.py`` and ``yapycon/yasara_kernel.py`` to ``<YASARA_HOME_DIRECTORY>/plg/``
   
   * This step does make YASARA aware of the plugin but for YaPyCon to work properly, it needs to operate within
     a virtual environment that provides it with the necessary pre-requsites. This is achieved in the next steps.
     
2. Create a virtual environment and install ``requirements.txt``

3. Drop to a terminal, activate the environment and launch YASARA.

If everything has gone well, you will see a *"Python Console"* option added under the *"Window"* menu option:

![image](https://github.com/aanastasiou/yapycon/raw/main/doc/source/resources/figures/fig_showing_option.png?raw=true)

# Documentation

For more details head over to [readthedocs for the complete YaPyCon manual]().