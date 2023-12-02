import tempfile
import shutil
import atexit
import os
from functools import partial

def cleanup(temp_folder):
    shutil.rmtree(temp_folder, ignore_errors=True)
    print('cleanup')

def path(file_name):
    return os.path.join(temp, file_name)

temp = tempfile.mkdtemp()
print(temp)
atexit.register(partial(cleanup,temp))