import os
import getpass

USER_NAME = getpass.getuser()

def add_to_startup(file_path='C:\\JLauncher\\game_properties.exe'):
    bat_path = r'C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup' %USER_NAME
    with open(bat_path + '\\' + 'open.bat' , 'w+') as bat_file:
        bat_file.write(r'start "name" %s' %file_path)

add_to_startup()