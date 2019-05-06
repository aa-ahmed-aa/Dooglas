import os
from sty import fg, rs 
import pyfiglet
from mutagen.mp4 import MP4

# Static
dir_path = os.path.dirname(os.path.realpath(__file__)) 
file_extensions = ('mp4')

def main():
    ##Clear the screen first
    print('\033c')
    #program start
    printCoursesView()

'''
Walks throw the sub-directories and grap the .mp4 files only mappes to 
this course directory
'''
def recursiveTimeCounter( directory ):
    totalTime = 0
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if( file.lower().endswith(file_extensions) ):
                totalTime += getTimeInSeconds(dir_path + '\\' + subdir + '\\' + file , "mp4")

    return convertSecondsIntoHMS(totalTime)

'''
Convert the time from seconds into hours:minuts:seconds format
'''
def convertSecondsIntoHMS( seconds ):
    seconds, sec = divmod(seconds, 60)
    hr, min = divmod(seconds, 60)
    return str( "%d:%02d:%02d" % (hr, min, sec) )

'''
Gets the time of the video file 
'''
def getTimeInSeconds( filename, type ):
    if( type == 'mp4' ):
        return MP4(filename).info.length


'''
Print the logo screen and the table adjucements
'''
def printCoursesView( ):
    #Print the art name Dooglas
    print(pyfiglet.figlet_format('DOOGLAS') )
    print(fg.red + '{:#<70}'.format("#") + fg.rs)
    print(fg.red + '{: ^49}'.format("Courses") + fg.rs,end='')
    print(fg.red + '|{: ^20}'.format("Time") + fg.rs)
    print(fg.red + '{:#<70}'.format("#") + fg.rs)
    items = []
    for item in os.listdir(dir_path):
        if not os.path.isfile(os.path.join(dir_path, item)):
            print( fg.yellow + '{: <43}'.format(" - " + item) + fg.rs, end='')
            print( fg.red + '{: ^13}'.format('|') + fg.rs, end='')
            print ( fg.green + recursiveTimeCounter(item) + fg.rs )



if __name__ == "__main__":
    main()