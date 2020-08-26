from os import listdir
from os.path import isfile, isdir, join


mypath = "./static/gif-10"

files = listdir(mypath)

with open("filenames.txt", "w") as fout:

    for f in files:
        fout.write(f[:-4] + '\n')

print("done")