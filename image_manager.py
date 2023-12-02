import tempfile
import shutil
import atexit
import os
from functools import partial

num=0
file_name='tree'
format='png'

def remove_temp(temp_folder):
    shutil.rmtree(temp_folder, ignore_errors=True)
    print('temp folder removed.')

def path():
    return os.path.join(temp, f'{file_name}{num}.{format}')

def new_path():
    global num
    num+=1
    return os.path.join(temp, f'{file_name}{num}')

image_list = lambda:os.listdir(temp)

temp = tempfile.mkdtemp()
print('temp folder:',temp)
atexit.register(partial(remove_temp,temp))
