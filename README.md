Python2-to-Python3-Upgrade-Installs
---

When upgrading from Python2 to Python3, this is useful to install all of the python2 packages in python3

To use this script, you must install the dependency `pandas` using `pip install pandas`.
If you forgot, the script tries to do this for you.

But, you **must** run (with Python2) `pip freeze > pip2_freeze.list` in the current working directory to use this script.
  -- this must be done with Python2 **BEFORE** install Python3

Usage:

Python2: `pip freeze > pip2_freeze.list`

**Install Python3**

Python3 `python Python2-to-Python3-Upgrade-Installs.py /path/to/pip2_freeze.list`

Done!
