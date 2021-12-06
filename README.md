# MetaVerseChecker
 Basic social media checker and scorer!

# Installation

Make sure you have Python 3.x installed. (https://www.python.org/downloads/)

Make sure you have the latest Google Chrome browser installed. (https://www.google.com/intl/en_au/chrome/)

## For best practice, use a Python Virtual environment:
```
$ python -m venv .venv
```

###### NOTE: to ensure you are using the Python Virtual Environment ensure you have "(venv)" before the command line (normally in green text), otherwise use command:
```
$ .\.venv\Scripts\activate
```

## Install the required plugins:
```
$ pip install -r requirements.txt
```

## You can now run the script:
```
$ python ./main.py
```

Any questions please contact the author.

# Debugging

Python sometimes requires windows users to set Execution policies for Python Virtual environments. If you recieve the error below;

```
.\.venv\Scripts\activate : File C:\Users\user\scriptname\.venv\Scripts\Activate.ps1 cannot be loaded because running 
scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\.venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

## Open Windows Powershell in Admin mode and use:
```
$ Set-ExecutionPolicy RemoteSigned
```

## When finished use:
```
$ Set-ExecutionPolicy Restricted
```