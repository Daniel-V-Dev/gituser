# gituser
A simple command tool for managing git users.

## Requirements
- Git
- Terminal

## Installation
You can download the executable file [here]() and add the program's `PATH` into your own system.

Or you can clone this project and install them manually by:

```bash
git clone https://github.com/Daniel-V-Dev/gituser
```

Then create a venv in the cloned directory and activate it. Check the [documentation here](https://docs.python.org/3/library/venv.html).

Afterwards, install the requirements and `pyinstaller`:
```bash
pip install -r requirements.txt pyinstaller
```

**NOTE**: You can use other bundler if you want.

For pyinstaller, run:
```bash
pyinstaller --onefile -n gituser main.py
```

Once you are done, you can find the executable file inside `dist/gituser/` and add the program's `PATH` to your system.

Check if it's properly installed:
```bash
gituser --help
```
