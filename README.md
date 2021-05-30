# Playground for Ux site

[ TODO: update]

## Backends

### Requirments

* Python3

### Get Started

Run inside top ux-site directory

```terminal
$ python3 -m venv .venv
$ source .venv/bin/activate # on Linux
> .venv/Scripts/Activate.ps1 # on Windows
# Note
#
# On Microsoft Windows, it may be required to enable the Activate.ps1 script 
# by setting the execution policy for the user. 
# You can do this by issuing the following PowerShell command:
# 
# PS C:> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


(.venv) pip install -r backend/requirements.txt
```

For running flask application

```terminal
(.venv) python backend/app.py
```

Add debug option in visual code:

Sample configuration in `.vscode/launch.json`

```json
{
    "name": "Python: Flask",
    "type": "python",
    "request": "launch",
    "module": "flask",
    "env": {
        "FLASK_APP": "backend/app:app",
        "FLASK_ENV": "development"
    },
    "args": [
        "run",
        "--no-debugger"
    ],
    "jinja": true
},
```
