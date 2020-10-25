## main.py
## Lists the directory structure of my music share and writes to csv file
## 
## import module to traverse the filesystem
import os
## path to directory to list + write files, this case an UNRAID share
m_path = "/Volumes/SHARE/KYLE/MUSIC"
## path to plex share
p_path = "/Volumes/SHARE/MEDIANEW"
## csv files to write to
music_csv = 'csv/music.csv'
plex_csv = 'csv/plex.csv'

def music_share():
    ## create / open music csv file
    with open(music_csv, 'w') as output:
        output.write('FILE NAME,FOLDER NAME,FILE PATH,\n')
        for root, dirs, files in os.walk(m_path):
            for x in files:
                file_path= os.path.join(root, x)
                folder_name = os.path.dirname(root)
                file_name= os.path.basename(x)
                output.write('{},{},{}\n'.format(file_name, folder_name, file_path))

def plex_share():
    ## create / open plex csv file
    with open(plex_csv, 'w') as output:
        output.write('FILE NAME,FOLDER NAME,FILE PATH,\n')
        for root, dirs, files in os.walk(p_path):
            for x in files:
                file_path= os.path.join(root, x)
                folder_name = os.path.dirname(root)
                file_name= os.path.basename(x)
                output.write('{},{},{}\n'.format(file_name, folder_name, file_path))

## call functions to run program
music_share()
plex_share()