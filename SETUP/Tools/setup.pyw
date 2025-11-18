from os import *
from time import *
from tkinter import *
from tkinter import messagebox

import ctypes
import win32con


# FIND WALLPAPER FUNCTION
def getWallpaper():
    ubuf = ctypes.create_unicode_buffer(512)
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_GETDESKWALLPAPER, len(ubuf), ubuf, 0)
    return ubuf.value


# FIND PATH DOWNLOADS
Path_SETUP = getcwd()
Path_SETUP_CMD = Path_SETUP
s = '\ '
List_Path_SETUP = Path_SETUP.split('{}'.format(s[0]))
Path_SETUP = ''
for run in range(len(List_Path_SETUP)):
    if run == len(List_Path_SETUP) - 1:
        Path_SETUP += List_Path_SETUP[run]
    else:
        Path_SETUP = Path_SETUP + List_Path_SETUP[run] + '\\'

# CHANGE BACKGROUND
BG_Default = getWallpaper()
BG_Change = '{}\\Image\\virus.jpg'.format(Path_SETUP)
ctypes.windll.user32.SystemParametersInfoW(20, 0, "{}\\Image\\virus.jpg".format(Path_SETUP), 0)
system('{}/Tools/refresh.bat'.format(Path_SETUP_CMD))
sleep(3)
# MESSAGEBOX
messagebox.showwarning(title='WARNING!', message='THE VIRUS HAS ENTERED YOUR PC!!!')

# SCREEN
window = Tk()
window.title('MONEY MONEY')
window.config(background='red')
window.iconbitmap('{}\\Image\\favicon.ico'.format(Path_SETUP))


# ENABLE CLOSE BUTTON
def enable_close_button():
    window.destroy()


# DISABLE CLOSE BUTTON
def disable_close_button():
    pass


window.protocol('WM_DELETE_WINDOW', disable_close_button)
window.update()

# CENTER SCREEN
window_width = 1000
window_height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_axis = (screen_width / 2) - (window_width / 2)
y_axis = (screen_height / 2) - (window_height / 2)

window.geometry('{}x{}+{}+{}'.format(window_width, window_height, int(x_axis), int(y_axis)))

# BEFORE SCREENGUI
l1 = Label(window,
           text='YOUR FILE IN DESKTOP WILL DELETE IN...',
           font=('Arial', 25, 'bold'),
           fg='Black',
           bg='red')
l1.pack()

window.after(1000)

for j in range(10, -1, -1):
    l1.config(text='YOUR FILE IN DESKTOP WILL DELETE IN...{}'.format(j))
    window.after(1000)
    window.update()

for run in range(10):
    system('{}/Tools/Summon.bat'.format(Path_SETUP_CMD))

# HIDE FILE
system('{}/Tools/Hide_file.bat'.format(Path_SETUP_CMD))

window.after(3000)
l1.config(text='YOUR FILE IN DESKTOP HAS BEEN DELETED')
window.update()
window.after(4000)
l1.config(text='ALL FILE WILL DELETE IN...')
window.update()

# SHOW FILE
for f in range(5, -1, -1):
    l1.config(text='ALL FILE WILL DELETE IN...{}'.format(f))
    window.update()
    window.after(1000)

for run in range(20):
    system('{}/Tools/Summon.bat'.format(Path_SETUP_CMD))
# SHOW FILE
system('{}/Tools/Show_file.bat'.format(Path_SETUP_CMD))

# AFTER SCREENGUI
ctypes.windll.user32.SystemParametersInfoW(20, 0, BG_Default, 0)
window.config(background='white')
window.state('zoomed')
window.update()
Image_happy_birthday = PhotoImage(file='{}\\Image\\happy_birthday.png'.format(Path_SETUP))


def happy_birthday_screen():
    l1.config(text='HAPPY BIRTHDAY!!!',
              font=('Arial', 50, 'bold'),
              fg='red',
              bg='white',
              image=Image_happy_birthday,
              compound='bottom')
    window.update()


window.protocol('WM_DELETE_WINDOW', enable_close_button)
happy_birthday_screen()
window.mainloop()

# OPEN FILE MP3
startfile('{}\\Video\\Happy_birthday.mp3'.format(Path_SETUP))
