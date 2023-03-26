from shutil import *
from tkinter import messagebox
from os import *
from tkinter import *
from time import *
import win32con,ctypes

#FIND WALLPAPER FUNCTION
def getWallpaper():
    ubuf = ctypes.create_unicode_buffer(512)
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_GETDESKWALLPAPER,len(ubuf),ubuf,0)
    return ubuf.value

#FIND USER
User=''
Folder_Users=listdir('C:\\Users')
for i in Folder_Users:
    if i not in ['Administrator', 'All Users', 'Default', 'Default User', 'desktop.ini', 'Public']:
        User=i

#CHANGE BACKGROUND
BG_Default=getWallpaper()
BG_Change='C:\\Users\\{}\\Downloads\\SETUP\\Image\\virus.jpg'.format(User)
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\{}\\Downloads\\SETUP\\Image\\virus.jpg".format(User) , 0)
system('C:/Users/{}/Downloads/SETUP/Tools/refresh.bat'.format(User))
sleep(3)
#MESSAGEBOX
messagebox.showwarning(title='WARNING!',message='THE VIRUS HAS ENTERED YOUR PC!!!')

#SCREEN
window=Tk()
window.title('MONEY MONEY')
window.config(background='red')
window.iconbitmap('C:/Users/{}/Downloads/SETUP/Image/favicon.ico'.format(User))

#ENABLE CLOSE BUTTON
def enable_close_button():
    window.destroy()
#DISABLE CLOSE BUTTON
def disable_close_button():
    pass
window.protocol('WM_DELETE_WINDOW',disable_close_button)
window.update()

#CENTER SCREEN
window_width=1000
window_height=600

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x_axis=(screen_width/2)-(window_width/2)
y_axis=(screen_height/2)-(window_height/2)

window.geometry('{}x{}+{}+{}'.format(window_width,window_height,int(x_axis),int(y_axis)))

#BEFORE SCREENGUI
l1=Label(window,
         text='YOUR FILE IN DESKTOP WILL DELETE IN...',
         font=('Arial',25,'bold'),
         fg='Black',
         bg='red')
l1.pack()

window.after(1000)

for j in range(10,-1,-1):
    l1.config(text='YOUR FILE IN DESKTOP WILL DELETE IN...{}'.format(j))
    window.after(1000)
    window.update()

for run in range(10):
    system('C:\\Users\\{}\\Downloads\\SETUP\\Tools\\Summon.bat'.format(User))

#HIDE FILE
system('C:/Users/{}/Downloads/SETUP/Tools/Hide_file.bat'.format(User))

window.after(3000)
l1.config(text='YOUR FILE IN DESKTOP HAS BEEN DELETED')
window.update()
window.after(4000)
l1.config(text='ALL FILE WILL DELETE IN...')
window.update()

#SHOW FILE
for f in range(5,-1,-1):
    l1.config(text='ALL FILE WILL DELETE IN...{}'.format(f))
    window.update()
    window.after(1000)

for run in range(20):
    system('C:\\Users\\{}\\Downloads\\SETUP\\Tools\\Summon.bat'.format(User))
#SHOW FILE
system('C:/Users/{}/Downloads/SETUP/Tools/Show_file.bat'.format(User))

#AFTER SCREENGUI
ctypes.windll.user32.SystemParametersInfoW(20, 0, BG_Default , 0)
window.config(background='white')
window.state('zoomed')
window.update()
Image_happy_birthday=PhotoImage(file='C:\\Users\\{}\\Downloads\\SETUP\\Image\\happy_birthday.png'.format(User))
def happy_birthday_screen():
    l1.config(text='HAPPY BIRTHDAY!!!',
              font=('Arial',50,'bold'),
              fg='red',
              bg='white',
              image=Image_happy_birthday,
              compound='bottom')
    window.update()

window.protocol('WM_DELETE_WINDOW',enable_close_button)
happy_birthday_screen()
window.mainloop()

#OPEN FILE MP3
startfile('C:\\Users\\{}\\Downloads\\SETUP\\Video\\Happy_birthday.mp3'.format(User))