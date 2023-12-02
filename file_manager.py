import tempfile
import shutil
import atexit
import os
from functools import partial

last_idx=-1
file_name='tree'
format='png'

def rmdir(temp_folder):
    shutil.rmtree(temp_folder, ignore_errors=True)
    print('temp folder removed.')

def clear():
    global temp
    global last_idx
    rmdir(temp)
    temp = tempfile.mkdtemp()
    last_idx=-1
    
def path(idx, withFormat=True):
    if withFormat:
        return os.path.join(temp, f'{file_name}{idx}.{format}')
    else:
        return os.path.join(temp, f'{file_name}{idx}')

def last_path():
    return path(last_idx)

def new_path():
    global last_idx
    last_idx+=1
    return path(last_idx, False)

temp = tempfile.mkdtemp()
print('temp folder:', temp)
atexit.register(partial(rmdir, temp))
