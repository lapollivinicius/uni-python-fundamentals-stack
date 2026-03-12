# Virtual environment

Venv is used to create a isolated environment for each project in python - to work with libs and frameworks without affecting your OS settings default,

It's easy work venv, with some commands you can work in a virtual environment 

## To start a venv use:

```terminal
python -m venv <name-venv>
```

so, now, you have to active your venv, use:

```terminal
source myworld/bin/activate
or
myworld\Scripts\activate
```

now, any command you run will be executed in the virtual environment (venv).

```terminal
(venv) myproject > _
```

## How to install libs

Working with venv, you just run pip to install libs or install requirements 

use to install dependencies:
```
pip install <name-dependencie>
```

use after dependencies installed:
```
pip freeze > requirements.txt
```

use to install according requirements.txt:
```
pip install -r requirements.txt
```

## Desactive Venv

In terminal with venv active use:
```
deactivate
```