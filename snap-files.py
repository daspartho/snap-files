import os
import random
import shutil
import time

universe= input('enter path: ')
members =  os.listdir(universe)
random.shuffle(members)
n = len(members)//2

for i in members[:n]:
    try:
        os.remove(f'{universe}/{i}')
    except IsADirectoryError:
        shutil.rmtree(f'{universe}/{i}')

    print(f'snapped {i} from existence')
    time.sleep(1) # slight delay looks good

print(f'{n} file(s) disintegerated')
print('Boom! Half of the population is gone!')



