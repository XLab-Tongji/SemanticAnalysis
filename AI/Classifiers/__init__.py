import os
import sys

path = os.path.dirname(os.path.abspath(__file__))

exclusions = ["__init__.py", "classifier.py"]
for py in [f[:-3] for f in os.listdir(path) if f.endswith('.py') and f not in exclusions]:
    module = __import__('.'.join([__name__, py]), fromlist=[py])
    classes = [getattr(module, x) for x in dir(module) if isinstance(getattr(module, x), type)]
    for cls in classes:
        setattr(sys.modules[__name__], cls.__name__, cls)
