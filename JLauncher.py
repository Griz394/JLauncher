from tkinter import Button, PhotoImage, Label, Entry, Tk, Checkbutton, Canvas
from tkinter.messagebox import showinfo , showerror , showwarning , askyesno
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
import os

def start():
    score=0

    nickname = nicknamefield.get()
    if nickname == '':
        showerror(title='Ошибка запуска', message='Введите свой ник в игре!')
        score +=1

    ram= ramlist.get()
    if ram != '128 мб' and ram != '256 мб' and ram !='512 мб' and ram !='1024 мб' and ram !='2048 мб':
        showerror(title='Ошибка исполнения', message='На Вашем компьютере не хватает оперативной памяти для выделения игре. Выберите меньшее значение выделяемой ОЗУ')
        score += 1

    graphic=graphiclist.get()
    if graphic == 'Сказочная' or graphic == 'Детально':
        showerror(title='Ошибка исполнения', message='Ваша видеокарта не подходит для отображения данной графики, выберите более низкие настройки')
        score +=1

    version=versionlist.get()
    if version == '1.21' or version == '1.20' or version == '1.19' or version == '1.18' or version == '1.17':
        showerror(title='Ошибка запуска', message='Ваш компьютер не соответствует минимальным требованиям для выбранной версии. Рекомендуемая версия - 1.16')
        score +=1

    if score == 0:
        showerror(title='Ошибка запуска', message='На Вашем компьютере не установлена требуемая версия Java!')
        showinfo(title='Оповещение загрузки', message='Загрузка актуальной версии Java началась, это займёт несколько секунд')
        ask=askyesno(title='Ошибка загрузки', message='JLauncher не смог установить требуемую версию Java. Вы хотите запустить Minecraft на имеющейся версии Java?')
        if ask == 1:
            os.system('game_properties.exe')


def helpdef():
    showerror(title='Ошибка исполнения', message='Отсутствует подключение к сети. Пожалуйста, выберите доступную сеть и повторите попытку')


def skin():
     showwarning(title='Мы не пираты!',message='Мы не стали создавать пиратскую систему скинов, чтобы у Вас была мотивация купить лицензию для полноценного пользования Minecraft. В игре у Вас будет отображаться стандартный скин')


os.system('loader.exe')
window = Tk()
window.title('JLauncher')
window.resizable(height=0, width=0)

image = Image.open("data/minecraftfon.png")
photo = ImageTk.PhotoImage(image)
fon = Label(window, image=photo)
fon.pack()

startbtnimg = PhotoImage(file='data/startbtn.png')
startbtnimg = startbtnimg.subsample(2, 2)
startbtn = Button(window, image=startbtnimg, command=start)
startbtn.place(x=740, y=600)

versionlist = Combobox(window, values=('1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '1.12', '1.13', '1.14', '1.15','1.16', '1.17', '1.18', '1.19', '1.20', '1.21'))
versionlist.current(11)
versionlist.place(x=400, y=650)
versiontxt = Label(window, text='Выбор версии', font=('Arial', 16), bg='yellow')
versiontxt.place(x=400, y=620)

nicknamefield = Entry(window)
nicknamefield.place(x=220, y=650)
nicknametxt = Label(text='Ник в игре', bg='yellow', font=('Arial', 16))
nicknametxt.place(x=230, y=620)

helpbtnimg = PhotoImage(file='data/helpbtn.png')
helpbtnimg = helpbtnimg.subsample(2, 2)
helpbtn = Button(window, image=helpbtnimg, command=helpdef)
helpbtn.place(x=750, y=500)

skinbtnimg = PhotoImage(file='data/skinbtn.png')
skinbtnimg = skinbtnimg.subsample(2, 2)
skinbtn = Button(window, image=skinbtnimg, command=skin)
skinbtn.place(x=765, y=400)

ramlist = Combobox(window, values=('128 мб', '256 мб', '512 мб', '1024 мб', '2048 мб', '4096 мб', '8192 мб', '16 гб', '32 гб', '64 гб'))
ramlist.current(0)
ramlist.place(x=230, y=200)
ramtxt = Label(window, text='Объём ОЗУ', bg='yellow', font=('Arial', 16))
ramtxt.place(x=240, y=170)

fpslist = Combobox(window, values=('15 fps', '30 fps', '60 fps', '120 fps', '240 fps', 'максимум'))
fpslist.current(1)
fpslist.place(x=230, y=150)
fpstxt = Label(window, text='Ограничение FPS', bg='yellow', font=('Arial', 16))
fpstxt.place(x=215, y=120)

graphiclist = Combobox(window, values=('Сказочная', 'Детально', 'Быстро', 'Очень быстро'))
graphiclist.current(2)
graphiclist.place(x=230, y=100)
graphictxt = Label(window, text='Графика', bg='yellow', font=('Arial', 16))
graphictxt.place(x=255, y=70)

lang = Combobox(window, values=('Русский', 'English (InDev)'))
lang.current(0)
lang.place(x=830, y=75)

langtxt = Label(window, text='Язык лаунчера', bg='yellow', font=('Arial', 16))
langtxt.place(x=825, y=45)

texpodderzhka = Checkbutton(window, text='Отправлять нам сведения об ошибках', bg='yellow', font=('Arial', 12))
texpodderzhka.place(x=820, y=150)

client = Checkbutton(window, text='Запустить лицензионный клиент', bg='yellow', font=('Arial', 12))
client.place(x=820, y=180)

showinfo(title='Спасибо!', message='Спасибо за то, что выбрали JLauncher! Приятной игры!')

window.mainloop()
