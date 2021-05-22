# Playground for Ux site

[ TODO: update]

## Backends

### Requirments

* Python3

### Get Started

Run inside top ux-site directory

```terminal
python3 -m venv .venv
source .venv/bin/activate # on Linux
# TODO add coomand for windows
(.venv) pip install -r backend/requirments.txt
```

For running flask application

```terminal
(.venv) python backend/app.py
```

Add debub option in visual code:

Sample condifuration in `.vscode/launch.json`

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
