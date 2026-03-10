# =========== virtual environment ============= #

# similar to node_modules in js
# it's an environment to run and test py
# it allow manage project and dependencies

# to create use
'''
python -m venv <project-name>
'''
# project
# |― Include
# |― Lib
# |― Scripts
# |― .gitignore
# |― pyvenv.cfg

# now, to use the venv you need active this environment

'''
project\Scripts\activate

your terminal:
(venv) C:\project 
'''

# to desactive the venv use 
'''
(myfirstproject) C:\project  "deactivate"
'''

# it's works - now you can install packages
'''
pip install django
'''

# to delete venv use
'''
rmdir /s /q myfirstproject
'''

# important create a requirements.txt to list the dependencies
# after install the dependencies
'''
pip freeze > requirements.txt
'''

# to install the dependencies use
'''
pip install -r requirements.txt
'''


