# __init__.py

print("__init__.py")

print('__init__: importing spam...')
from . import spam
print('__init__: importing eggs...')
from . import eggs

with open('spam.py', 'w') as f:
    f.write('')

with open('eggs.py', 'w') as f:
    f.write('')

