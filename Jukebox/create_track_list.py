from tkinter import ttk
import tkinter as tk
import track_library as lib
from font_manager import get_h1_font
import tkinter.scrolledtext as tkst
from track_library import increment_play_count, get_name, get_artist, get_rating, library
import json


def insert_text(text_area, content):    #Append content to the end of a text widget, followed by a newline
    text_area.insert(tk.END, content)   #Insert new content at the end of the text
    text_area.insert(tk.END, '\n')      #Insert a newline character at the end

def set_text(text_area, content):       #Clear and set content for a text widget
    text_area.delete("1.0", tk.END)     #Clear all content in the text area
    text_area.insert(1.0, content)      #Insert new content at the beginning (line 1, char 0)



class CreateTrackList:
    def __init__(self, window):
        self.window = window                    #Assign a window object
        self.window.geometry("720x400")         # Set window size
        self.window.configure(bg="#f4f4f4")     #Set background color
        self.window.title("Track Manager")      #Set window title
        self.window.resizable(False, False)     #Disable resizing
        self.id_lib = []                        #Store track IDs added to playlist
        self.file_path = "playlist.json"        #File to save/load playlist from

        self.create_widgets()   #call function to create GUI

    def create_widgets(self):
        title_lbl = tk.Label(self.window, text="🎵 Create Playlist", font=get_h1_font(), bg="#f4f4f4")       #Create and locate main label
        title_lbl.grid(row=0, column=0, pady=(10, 5), padx=(40,0))

        self.list_txt = tkst.ScrolledText(self.window, width=46, height=10, wrap="none", font=("Segoe UI", 10))     #Create and locate text area to display playlist tracks
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="w", padx=30, pady=(5, 10))


        add_track_frame = ttk.Frame(master=self.window)     #Create and locate a frame for track input and Add button
        add_track_frame.grid(row=2, column=0, columnspan=2, sticky="w", pady=20, padx=30)

        input_lbl = tk.Label(add_track_frame, text="Enter track number:", font=("Segoe UI", 10), bg="#f4f4f4")      #Create and locate label and entry for track number input
        input_lbl.pack(side="left", padx=(0,20))

        self.track_txt = tk.Entry(add_track_frame, width=12, font=("Segoe UI", 10))     #Create Entry to get user input
        self.track_txt.pack(side="left", padx=(0,20))
        self.track_txt.focus()      #Auto focus when window opens

        self.add_track_btn = tk.Button(add_track_frame, text="Add Track", command=self.add_track_clicked, font=("Segoe UI", 10), bg="#008080", fg="white")       #Create and locate a button to add track to playlist (binds to add_track_clicked)
        self.add_track_btn.pack(side="left")

        self.save_btn = tk.Button(self.window, text="Save playlist", command=self.save_clicked, font=("Segoe UI", 10), bg="#008080", fg="white")    #Create and locate a button to save current playlist to JSON file (binds to save_clicked)
        self.save_btn.grid(row=0, column=2, padx=(20,0), pady=(40,0))

        self.view_playlist_btn = tk.Button(self.window, text="View playlist", command=self.load_clicked, font=("Segoe UI", 10), bg="#008080", fg="white")   #Create and locate a button to load playlist from file (binds to load_clicked)
        self.view_playlist_btn.grid(row=0, column=3, padx=(40,0), pady=(40,0))

        self.play_btn = tk.Button(self.window, text="Play playlist", command=self.play_click, font=("Segoe UI", 10), bg="#008080", fg="white")      #Create and locate a button to simulate "playing" the playlist (binds to play_click)
        self.play_btn.grid(row=1, column=2, padx=(20,0))

        self.reset_btn = tk.Button(self.window, text="Reset playlist", command=self.reset_clicked, font=("Segoe UI", 10), bg="#008080", fg="white")      #Create and locate a button to reset the playlist (binds to reset_clicked)
        self.reset_btn.grid(row=1, column=3, padx=(20,0))

        self.status_lbl = tk.Label(self.window, text="status", font=("Segoe UI", 10), bg="#f4f4f4")  #Create and locate a label to follow status
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="we", padx=10, pady=10)



    def add_track_clicked(self):    #A function to add a track
        key = self.track_txt.get()      #Get track number from input field
        if not key:     #Check if input is empty
            self.status_lbl.configure(text="Input is empty!", fg="red")     #inform the status
            return      #Exit the loop if needed

        if key in self.id_lib:      #Check if input is already in id_lid
            self.status_lbl.configure(text=f"Track {key} already in playlist!", fg="orange")
            return
        else:
            if key in library:       #Check if the entered track ID exists in the music library
                self.id_lib.append(key)  #Add track ID to id_lib
                track_details = f"{get_name(key)} by {get_artist(key)} - rating: {get_rating(key)}"     #Get track's detail
                self.status_lbl.configure(text=f"Track {key} added", fg="green")    #inform status
                insert_text(self.list_txt, track_details)  #Display the content in list_txt
            else:
                self.status_lbl.configure(text=f"Track {key} not found!", fg="red")     #Inform if track not found

        self.track_txt.delete(0, tk.END)    # Clear input field after attempt

    def save_clicked(self):     #Function to save the current playlist to a JSON file.
        if self.id_lib:     #Check if id_lib is not empty
            with open(self.file_path, "w") as file:     #Open with file_path and write to JSON file
                json.dump(self.id_lib, file, indent=4)      #Save track IDs as JSON list
                self.status_lbl.configure(text="Playlist saved", fg="green")       #Inform the status if saved
        else:
            self.status_lbl.configure(text="Please add a track fist!", fg="red")    #Inform the status if list_txt is empty


    def load_clicked(self):     #Function to display playlist from JSON file to the list_txt
        self.id_lib.clear()     #Clear current playlist
        with open(self.file_path, 'r') as file:
            data = json.load(file)      #Read track ID list from file
            load_track = []         #Create a list to store track in JSON file
            for trackId in data:
                load_track.append(f"{get_name(trackId)} by {get_artist(trackId)} - rating: {get_rating(trackId)}")      #Add track information to load_track
                self.id_lib.append(trackId)     #Add track ID to id_lib
            set_text(self.list_txt, '\n'.join(load_track) + '\n')       #Display the content in list_txt
            self.status_lbl.configure(text="Playlist loaded successfully!", fg="green")     #Inform the status


    def play_click(self):
        if self.id_lib:     #Check if it is empty
            for key in self.id_lib:
                increment_play_count(key)       #Call function to increase play count
            self.status_lbl.configure(text="Play successfully!")    #Inform status

        else:
            self.status_lbl.configure(text="Please add a track first!", fg="red")       #Inform status

    def reset_clicked(self):    #Function to clear all data in list_txt
        self.list_txt.delete(1.0, tk.END)       #Delete data
        self.status_lbl.configure(text="Reset successfully!", fg="green")   #Inform status
        self.id_lib.clear()     #Delete track IDs in id_lib


if __name__ == "__main__":      # only runs when this file is run as a standalone
    window = tk.Tk()            # create a TK object
    CreateTrackList(window)     # open the CreateTrackList GUI
    window.mainloop()           # run the window main loop, reacting to button presses, etc