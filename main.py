from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os

mixer.init()

root = Tk()
root.geometry('700x220')
root.title('Music Player')
root.resizable(0, 0)

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    if songs_list.curselection():
        song = songs_list.get(ACTIVE)
        song_name.set(song)
        mixer.music.load(song)
        mixer.music.play()
        status.set("Song PLAYING")
    else:
        status.set("No song selected.")

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")

def load(listbox):
    directory = filedialog.askdirectory(title='Open a songs directory')
    if directory:
        os.chdir(directory)
        tracks = [track for track in os.listdir() if track.endswith(('.mp3', '.wav'))]
        listbox.delete(0, END)
        for track in tracks:
            listbox.insert(END, track)

def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")

def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")

# Color Scheme
bg_color = "#2c2f33"  # Dark gray
accent_color = "#7289da"  # Blue
text_color = "#ffffff"  # White
button_bg = "#4caf50"  # Green
button_fg = "#ffffff"  # White
listbox_bg = "#23272a"  # Darker gray
highlight_color = "#ff9800"  # Orange 

song_frame = LabelFrame(root, text='Current Song', bg=bg_color, fg=text_color, width=400, height=80)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', bg=bg_color, fg=text_color, width=400, height=120)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Playlist', bg=bg_color, fg=text_color)
listbox_frame.place(x=400, y=0, height=200, width=300)

current_song = StringVar(root, value='<Not selected>')
song_status = StringVar(root, value='<Not Available>')

playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground=highlight_color, bg=listbox_bg, fg=text_color)
scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=Y)
playlist.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=playlist.yview)
playlist.pack(fill=BOTH, padx=5, pady=5)

Label(song_frame, text='CURRENTLY PLAYING:', bg=bg_color, fg=text_color, font=('Times', 10, 'bold')).place(x=5, y=20)
song_lbl = Label(song_frame, textvariable=current_song, bg=accent_color, fg=text_color, font=("Times", 12), width=25)
song_lbl.place(x=150, y=20)

pause_btn = Button(button_frame, text='Pause', bg=button_bg, fg=button_fg, font=("Georgia", 13), width=7,
                   command=lambda: pause_song(song_status))
pause_btn.place(x=15, y=10)

stop_btn = Button(button_frame, text='Stop', bg=button_bg, fg=button_fg, font=("Georgia", 13), width=7,
                  command=lambda: stop_song(song_status))
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, text='Play', bg=button_bg, fg=button_fg, font=("Georgia", 13), width=7,
                  command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, text='Resume', bg=button_bg, fg=button_fg, font=("Georgia", 13), width=7,
                    command=lambda: resume_song(song_status))
resume_btn.place(x=285, y=10)

load_btn = Button(button_frame, text='Load Directory', bg=button_bg, fg=button_fg, font=("Georgia", 13), width=35,
                  command=lambda: load(playlist))
load_btn.place(x=10, y=55)

Label(root, textvariable=song_status, bg=bg_color, fg=text_color, font=('Times', 9), justify=LEFT).pack(side=BOTTOM, fill=X)

root.mainloop()
