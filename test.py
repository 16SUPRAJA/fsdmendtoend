import os

path="notebooks/research.ipynb"

#  print(os.path.split(path))

dir,file = os.path.split(path)

os.makedirs(dir,exist_ok=True)   # if parameter already present it wont give any error

with open(path,'w') as f:
    pass