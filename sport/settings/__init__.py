import os

RUN_MODE = os.getenv('RUN_MODE')

if RUN_MODE == 'local':
    from .local import *
elif RUN_MODE == 'production':
    from .production import *
else:
    pass

