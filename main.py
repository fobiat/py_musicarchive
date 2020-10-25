## main.py
## Lists the directory structure of my music share and writes to csv file
## 
## import module to traverse the filesystem
import os
## path to directory to list + write files, this case an UNRAID share
path = "/Users/kyle/Dropbox/My Mac (Kyles-MacBook-Pro.local)/Desktop"
## csv file to write to
music_csv = 'music.csv'
## create / open a csv file 

with open(music_csv, 'w') as output:
    output.write('FILE NAME,FOLDER NAME,FILE PATH,\n')
    for root, dirs, files in os.walk(path):
        for x in files:
            file_path= os.path.join(root, x)
            folder_name = os.path.dirname(root)
            file_name= os.path.basename(x)
            output.write('{},{},{}\n'.format(file_name, folder_name, file_path))