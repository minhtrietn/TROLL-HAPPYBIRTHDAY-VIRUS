from shutil import *
from tkinter import messagebox
from os import *
from tkinter import *
from time import *

#FIND USER
User=''
Folder_Users=listdir('C:\\Users')
for i in Folder_Users:
    if i not in ['Administrator', 'All Users', 'Default', 'Default User', 'desktop.ini', 'Public']:
        User=i
User_File=listdir('C:\\Users\\{}'.format(User))
Desktop_Folder='C:\\Users\\{}\\Desktop'.format(User)

#DELETE BACKUP DESKTOP
system('rmdir "C:\\Users\\{}\\Downloads\\SETUP\\Backup_Desktop\\Desktop_Save" /s /q'.format(User))

#COPY DESKTOP
system('del "C:\\Users\\{}\\Downloads\\SETUP\\Backup_Desktop\\Desktop_Save\\bin.txt" /s /f /q'.format(User))
copytree(Desktop_Folder,'C:\\Users\\{}\\Downloads\\SETUP\\Backup_Desktop\\Desktop_Save'.format(User))

#CHANGE BACKGROUND
copy2('C:\\Users\\{}\\Downloads\\SETUP\\Image\\CachedImage_1366_768_POS4.jpg'.format(User),'C:\\Users\\{}\\Downloads\\SETUP'.format(User))
replace('C:\\Users\\{}\\Downloads\\SETUP\\CachedImage_1366_768_POS4.jpg'.format(User),'C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles\\CachedImage_1366_768_POS4.jpg'.format(User))
system('C:/Users/{}/Downloads/SETUP/refresh.bat'.format(User))
sleep(5)

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

sleep(1)

for j in range(10,-1,-1):
    l1.config(text='YOUR FILE IN DESKTOP WILL DELETE IN...{}'.format(j))
    window.update()
    sleep(1)

#DELETE FILE
FILE_DESKTOP=listdir('C:\\Users\\{}\\Desktop'.format(User))
for k in FILE_DESKTOP:
    system('del "C:\\Users\\{}\\Desktop\\{}" /s /f /q'.format(User,k))

sleep(2)
l1.config(text='YOUR FILE IN DESKTOP HAS BEEN DELETED')
window.update()
sleep(5)
l1.config(text='ALL FILE WILL DELETE IN...')
window.update()

#RESTORE FILE
for f in range(5,-1,-1):
    l1.config(text='ALL FILE WILL DELETE IN...{}'.format(f))
    window.update()
    sleep(1)

#AFTER SCREEN
window.config(background='white')
Image_happy_birthday=PhotoImage(file='C:\\Users\\{}\\Downloads\\SETUP\\Image\\happy_birthday.png'.format(User))
l1.config(text='HAPPY BIRTHDAY!!!',
          font=('Arial',50,'bold'),
          fg='red',
          bg='white',
          image=Image_happy_birthday,
          compound='bottom')
window.state('zoomed')

#RESTORE
for l in FILE_DESKTOP:
    system('move "C:\\Users\\{}\\Downloads\\SETUP\\Backup_Desktop\\Desktop_Save\\{}" "C:\\Users\\{}\\Desktop"'.format(User,l,User))
system('del "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles\\CachedImage_1366_768_POS4.jpg" /s /f /q'.format(User))
system('echo.>C:\\Users\\{}\\Downloads\\SETUP\\Backup_Desktop\\Desktop_Save\\bin.txt'.format(User))
system('C:/Users/{}/Downloads/SETUP/refresh.bat'.format(User))
window.protocol('WM_DELETE_WINDOW',enable_close_button)
window.mainloop()

#OPEN FILE MP3
startfile('C:\\Users\\{}\\Downloads\\SETUP\\Video\\Happy_birthday.mp3'.format(User))