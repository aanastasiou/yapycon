# YaPyCon

YaPyCon embeds a Python console in YASARA, *"...a molecular-graphics, -modeling and -simulation
program for Windows, Linux, MacOS and Android"* thereby:

1. Enabling rapid prototyping of YASARA scripts
2. Offering common "shell" functionality such as:
   * Code auto-completion
   * Inline code documentation
   * Tighter integration with ``matplotlib``

3. Improving and expanding certain aspects of YASARA's Python functionality.

![image](https://raw.githubusercontent.com/aanastasiou/yapycon/main/doc/source/resources/figures/fig_main_yapycon.png)

# Quickstart

## Installation

1. Download the [latest release of YaPyCon](https://github.com/aanastasiou/yapycon/releases/latest/download/yapycon.zip)
   and decompress it to a directory on your computer.
2. Ensure that your Python virtual environment includes YaPyCon's requirements (see `requirements.txt`)
3. Ensure that the environment variable `YASARA_HOME` points to the top level directory where YASARA is installed 
   on your computer.
4. Run the `install_plugin` script from the *decompressed* YaPyCon release archive.
5. Drop to a terminal, activate the Python environment and launch YASARA.

If everything has gone well, you will see a *"Python Console"* option added under the *"Window"* menu option:

![image](https://raw.githubusercontent.com/aanastasiou/yapycon/main/doc/source/resources/figures/fig_showing_option_focused.png)

## Uninstallation

To remove YaPyCon run the `uninstall_plugin` script from the *decompressed* YaPyCon release archive.

# Documentation

The complete documentation of YaPyCon is included in the release archive (`yapycon.zip`), under the directory `doc/` 
and [is also available online at readthedocs](https://yapycon.readthedocs.io/en/latest/).