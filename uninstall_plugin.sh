#!/bin/bash
#
# YaPyCon YASARA plugin un-installer (Linux version)
#
# Athanasios Anastasiou, Dec 2021

echo "Removing YaPyCon from YASARA."
echo
echo

# Check if YASARA_HOME has been defined
if [ -z "${YASARA_HOME}" ]; then
    # Variable has not been defined
    # Inform and exit
    echo "The installer requires that the variable YASARA_HOME is set, prior to installing the plugin."
    echo "You can set that variable by:"
    echo "    > export YASARA_HOME=/some/path/to/yasara"
    echo
    exit 1
fi

# YASARA_HOME is defined, check that it points to a YASARA folder (a very basic check is performed here).
if [ ! -d "${YASARA_HOME}"/bab ] && [ ! -d "${YASARA_HOME}"/cif ] && [ ! -d "${YASARA_HOME}"/plg ] && [ ! -f "${YASARA_HOME}"/yasara]; then
    # The variable is set but the yasara directory does not look like a valid installation directory
    # Inform and exit
    echo "The YASARA_HOME environment variable points to ${YASARA_HOME}, which does not appear to"
    echo "be a valid YASARA installation. Please check the variable (or your installation) and try"
    echo "again."
    echo
    exit 1
fi

# Check that the file exists
if [ ! -f "${YASARA_HOME}"/plg/yapycon.py ]; then
    echo "${YASARA_HOME}/plg/yapycon.py does not exist."
    echo "No further action was taken."
    echo     
    exit 1
fi

# The file exists, proceed to delete it
rm ${YASARA_HOME}/plg/yapycon.py
rm ${YASARA_HOME}/plg/yasara_kernel.py
# Inform and exit
echo "The YaPyCon plugin and its dependencies were succesfully removed from YASARA."
echo
