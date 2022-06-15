from pytube import *
from tkinter import *
from pytube import *
import tkinter as tk
from tkinter import ttk, filedialog
import threading
app = Tk()
app.title('Торговля')
app.geometry('400x250')
app.resizable(False, False)
app.configure(bg='#ffc3a0')
def createWidgets():
    global entryurl
    global entrypath
    labeltitle = Label(app, text='YOUTUBE DOWNLOADER', font='24')
    labelname = Label(app, text='Введите ссылку на видео')
    labelpath = Label(app, text='Путь загрузки')
    entryurl = Entry(app)
    entrypath = Entry(app, textvariable=download_path)
    btndest = Button(app, text='Путь', command=browse)
    btnexe = Button(app, text='Выполнить', command=execut)
    labelpath.place(x=100, y=125)
    entrypath.place(x=100, y=150)
    labeltitle.place(x=100, y=10)
    labelname.place(x=100, y=50)
    entryurl.place(x=100, y=75)
    btndest.place(x=235, y=147)
    btnexe.place(x=150, y=180)
def execut():
    url = entryurl.get()
    yt = YouTube(url)
    print(f'Download video {yt.title!r}: {url}')
    streams = yt.streams \
        .filter(progressive=True, file_extension='mp4', resolution='720p') \
        .order_by('resolution')
    video = streams[-1]
    print('Stream url:', video.url)
    video.download(output_path='C:\Games', filename='yt_video.mp4')
def browse():
    download_dir = filedialog.askdirectory(initialdir="Your Dir")
    download_path.set(download_dir)
video_link = StringVar()
download_path = StringVar()
createWidgets()
app.mainloop()