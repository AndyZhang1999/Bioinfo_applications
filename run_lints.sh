#!/bin/bash

# pylint 2.4.4
# astroid 2.3.3
# Python 3.6.0 (default, Jan 16 2020, 13:24:17)
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# cleslin@cleslinMacBook16[BINF6200]# flake8 --version
# 3.7.9 (mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1) CPython 3.6.0 on Darwin

set -e
# Search Results
# set -e stops the execution of a script if a command or pipeline has an error -
# which is the opposite of the default shell behaviour, which is to ignore errors in scripts

if [ $# -eq 0 ]
  then
    echo "No directory supplied, eg: bash $0 assignment2"
    exit
fi

ENFORCED_FILES="
$1
"

# Disable R0914: Too many local variables
# Disable E0401: Flask CORS ext
# Disable F401: unused imports. Only really applies to __init__.py files, since all other unused imports
# would have been caught by pylint.
# Disable C0121: Comparison to True should be just 'expr'
# assigment 3 on...
# Disable R0801: Similar lines in 2 files
MAX_LINE_LEN="--max-line-length=120"

echo "Running pylint..."
pylint  --disable=R0914,E0401,F401,C0121,R0801 $MAX_LINE_LEN --msg-template='{abspath}:{line:3d}: {obj}: {msg_id}:{msg}' \
$ENFORCED_FILES
# assignment 3 on...
# Disable: E712 comparison to True should be 'if cond is True:' or 'if cond:'
# Diaable:  W504 line break after binary operator
echo -e "\n\nRunning flake8..."
flake8  --max-complexity 12 --benchmark $MAX_LINE_LEN --ignore=R0914,E712,W504 $ENFORCED_FILES

echo -e "\n\n*****Nice work! All lints passed successfully.****"