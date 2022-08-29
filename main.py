import json
from tkinter import *
from urllib import request # из библиотеки ткинтер импортировали все функции

import requests # импортировали библиотек реквестс

root = Tk() # создали окно программы, использовав библиотеку тк интер

def get_weather():
    city = cityField.get() # получаем название города из поля для города
    key = 'a1dd46759c2bda97d33e5b9dd11307b8'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    print(json.dumps(weather,indent = 4)) 
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}' 



root["bg"] = "green"  # выставили цвет фона окна
root.title('Погодное приложение') # написали название нашего окна
root.geometry('300x250') # задали размер окна
root.resizable(width=False, height=False) # запретили менять размер окна

frame_top = Frame(root, bg='#ffb700', bd=5) # создаем фрэйм(область для размещения других объектов), задали то, что наш фрэйм распологается в окне рут, задали цвет бг и бд - это ширина границы
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25) # для фрэйм топа используем функцию плейс для размещения его на окне рут
 
frame_bottom = Frame(root, bg='#ffb700', bd=5) # создали второй фрэйм, для вывода температуры
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1) # для фрэйм боттом использовали функцию плейс для резмещения его на окне рут

cityField = Entry(frame_top, bg='white', font=30) # на фрэймтопе создаем поле для ввода названия города
cityField.pack() # функция для размещения поля на фрэймтопе

btn = Button(frame_top, text='Посмотреть погоду', command=get_weather) # разместили кнопку на фрэймтопе, добавили на неё текст "посмотреть погоду", добавили команду - функцию, которая срабатывает при нажатии кнопки
btn.pack() # размещение кнопки на фрэймтопе

info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
info.pack()

root.mainloop()













