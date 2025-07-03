from tkinter import ttk
import tkinter as tk
import track_library as lib
from font_manager import get_h1_font
import tkinter.scrolledtext as tkst
from track_library import increment_play_count, get_name, get_artist, get_rating
import json
import os


def insert_text(text_area, content):
    text_area.insert(tk.END, content)
    text_area.insert(tk.END, '\n')

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)



class CreateTrackList:
    def __init__(self, window):
        self.window = window
        self.window.geometry("720x400")
        self.window.configure(bg="#f4f4f4")
        self.window.title("Track Manager")
        self.window.resizable(False, False)
        self.id_lib = []
        self.file_path = "playlist.json"

        self.create_widgets()   #call function to create GUI

    def create_widgets(self):
        title_lbl = tk.Label(self.window, text="🎵 Create Playlist", font=get_h1_font(), bg="#f4f4f4")
        title_lbl.grid(row=0, column=0, pady=(10, 5), padx=(40,0))

        self.list_txt = tkst.ScrolledText(self.window, width=46, height=10, wrap="none", font=("Segoe UI", 10))
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="w", padx=30, pady=(5, 10))


        add_track_frame = ttk.Frame(master=self.window)
        add_track_frame.grid(row=2, column=0, columnspan=2, sticky="w", pady=20, padx=30)

        input_lbl = tk.Label(add_track_frame, text="Enter track number:", font=("Segoe UI", 10), bg="#f4f4f4")
        input_lbl.pack(side="left", padx=(0,20))

        self.track_txt = tk.Entry(add_track_frame, width=12, font=("Segoe UI", 10))
        self.track_txt.pack(side="left", padx=(0,20))
        self.track_txt.focus()

        self.add_track_btn = tk.Button(add_track_frame, text="Add Track", command=self.add_track_clicked, font=("Segoe UI", 10), bg="#008080", fg="white")
        self.add_track_btn.pack(side="left")

        self.save_btn = tk.Button(self.window, text="Save playlist", command=self.save_clicked, font=("Segoe UI", 10), bg="#008080", fg="white")
        self.save_btn.grid(row=0, column=2, padx=(20,0), pady=(40,0))

        self.view_playlist_btn = tk.Button(self.window, text="View playlist", command=self.load_clicked, font=("Segoe UI", 10), bg="#008080", fg="white")
        self.view_playlist_btn.grid(row=0, column=3, padx=(40,0), pady=(40,0))

        self.play_btn = tk.Button(self.window, text="Play playlist", command=self.play_click, font=("Segoe UI", 10), bg="#008080", fg="white")
        self.play_btn.grid(row=1, column=2, padx=(20,0))

        self.reset_btn = tk.Button(self.window, text="Reset playlist", command=self.reset_clicked, font=("Segoe UI", 10), bg="#008080", fg="white")
        self.reset_btn.grid(row=1, column=3, padx=(20,0))

        self.status_lbl = tk.Label(self.window, text="status", font=("Segoe UI", 10), bg="#f4f4f4")  # create label to inform status
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="we", padx=10, pady=10)



    def add_track_clicked(self):
        key = self.track_txt.get()
        if not key:
            self.status_lbl.configure(text="Input is empty!", fg="red")
            return

        if key in self.id_lib:
            self.status_lbl.configure(text=f"Track {key} already in playlist!", fg="orange")
            return

        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            self.id_lib.append(key)
            track_details = f"{name} by {artist} - rating: {rating}"
            self.status_lbl.configure(text=f"Track {key} added", fg="green")
            insert_text(self.list_txt, track_details)
        else:
            self.status_lbl.configure(text=f"Track {key} not found!", fg="red")

        self.track_txt.delete(0, tk.END)

    def save_clicked(self):
        with open(self.file_path, "w") as file:
            json.dump(self.id_lib, file, indent=4)
            self.status_lbl.configure(text="Playlist saved", fg="green")


    def load_clicked(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            load_track = []
            for trackId in data:
                load_track.append(f"{get_name(trackId)} by {get_artist(trackId)} - rating: {get_rating(trackId)}")
                self.id_lib.append(trackId)
            set_text(self.list_txt, '\n'.join(load_track) + '\n')
            self.status_lbl.configure(text="Playlist loaded successfully!", fg="green")


    def play_click(self):
        if self.id_lib:
            for key in self.id_lib:
                increment_play_count(key)
            self.status_lbl.configure(text="Play successfully!")
            print(f"{lib.get_name(key)} now has {lib.get_play_count(key)} plays")

        else:
            self.status_lbl.configure(text="Please add a track first!", fg="red")

    def reset_clicked(self):
        self.list_txt.delete(1.0, tk.END)
        self.status_lbl.configure(text="Reset successfully!", fg="green")
        self.id_lib.clear()


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    CreateTrackList(window)     # open the CreateTrackList GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc