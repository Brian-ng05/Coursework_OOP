import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
import track_library as lib
from track_library import get_artist, get_rating, get_name, library, get_play_count


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)     # Clear all content in the text area
    text_area.insert(1.0, content)      # Insert new content at the beginning (line 1, char 0)


class TrackViewer():
    def __init__(self, window):     #Constructor for the TrackViewer GUI class
        self.window = window        #Store reference to the parent window
        self.window.geometry("720x400")         #Set size for the window
        self.window.configure(bg="#f4f4f4")     #Set background color
        self.window.title("View Tracks")        #Set window title
        self.window.resizable(False, False)     #Disable resizing


        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none", font=("Segoe UI", 10))      #Create and locate text box with scrollbar to show all tracks
        self.list_txt.grid(row=0, column=0, columnspan=3, sticky="W", padx=20, pady=(30, 10))

        self.track_txt = tk.Text(window, width=40, height=8, wrap="none", font=("Segoe UI", 10))        #Another text box to show details of selected or searched track
        self.track_txt.grid(row=0, column=3, sticky="NW", padx=20, pady=(30, 10))


        self.list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked, bg="#008080", fg="white")        #Button to list all available tracks
        self.list_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Track Number", bg="#f4f4f4")       #Label for the track number entry
        enter_lbl.grid(row=1, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)      #Create and locate entry field to input track number
        self.input_txt.grid(row=1, column=2, padx=10, pady=10)

        self.check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked, bg="#008080", fg="white")     #Button to show details of the track with entered ID
        self.check_track_btn.grid(row=1, column=3, padx=10, pady=10)


        search_frame = ttk.Frame(master=self.window)        #Create a sub-frame to hold the search entry and button
        search_frame.grid(row=2, column=0, columnspan=2, sticky="we", padx=(50,0), pady=10)

        self.search_txt = tk.Entry(search_frame, width=24, font=("Segoe UI", 10))       #Create and locate entry field to get user input
        self.search_txt.pack(side="left")
        self.search_txt.focus()      #Set focus to the search input

        self.search_btn = tk.Button(search_frame, text="Search", command=self.search_track ,font=("Segoe UI", 10), bg="#008080", fg="white")    #Button to trigger search
        self.search_btn.pack(side="left")

        groups_sorting = ["", "rating ↑", "rating ↓", "a-z", "z-a"]     #List of sort options

        sort_frame = ttk.Frame(window)      #Create and locate frame for both sorting and filtering controls
        sort_frame.grid(row=2, column=2, columnspan=2, sticky="we", padx=(50,0), pady=10)

        self.combo_sort = ttk.Combobox(sort_frame, width=10)        #Create a combobox
        self.combo_sort["values"] = groups_sorting                  #Set the option in groups_sorting
        self.combo_sort.current(0)              #Set default selection (empty)
        self.combo_sort.pack(side="left")       #Place the sorting combobox

        self.check_combobox = tk.Button(sort_frame, text="Sort", command=self.sort_combobox_clicked, bg="#008080", fg="white")      #Button to apply selected sort option
        self.check_combobox.pack(side="left", padx=(0,30))

        groups_filter = [""]        #Initialize artist filter list with an empty option
        for key in lib.library:
            if get_artist(key) not in groups_filter:    #Avoid duplicates
                groups_filter.append(get_artist(key))   #Add artist

        self.combo_filter = ttk.Combobox(sort_frame)        #Create a combobox
        self.combo_filter["values"] = groups_filter         #Set the option in groups_filter
        self.combo_filter.current(0)                        #Set default selection (empty)
        self.combo_filter.pack(side="left")                 #Place the sorting combobox

        self.check_combo_filter = tk.Button(sort_frame, text="Filter", command=self.filtered_combobox_clicked, bg="#008080", fg="white")        #Create and locate a button binds to filtered_combobox_clicked
        self.check_combo_filter.pack(side="left")


        self.status_lbl = tk.Label(window, text="", font=("Segoe UI", 10), bg="#f4f4f4")        #Create a label to follow status
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="we", padx=10, pady=10)      #Locate the label


    def view_tracks_clicked(self):          #Called when "View Track" button is clicked
        key = self.input_txt.get()          #Get track ID from input field
        if not key:     #Check if it is empty
            self.status_lbl.configure(text="Input is empty!", fg="red")
            return      #Exit loop
        else:
            if key in library:      #Check if it is empty
                track_details = f"{get_name(key)}\n{get_artist(key)}\nrating: {get_rating(key)}\nplays: {get_play_count(key)}"      #Get track's detail
                set_text(self.track_txt, track_details)     #Display track information in track_txt
            else:
                set_text(self.track_txt, f"Track {key} not found")      #inform if key is not found

        self.input_txt.delete(0, tk.END)        #Clear input_txt (from first letter to end)
        self.status_lbl.configure(text="View Track button was clicked!", fg="green")    #Display status

    def list_tracks_clicked(self):              #Called when "List All Tracks" button is clicked
        track_list = lib.list_all()             #Get string containing all track info
        set_text(self.list_txt, track_list)     #Display in left ScrolledText
        self.status_lbl.configure(text="List Tracks button was clicked!", fg="green")       #Update status

    def search_track(self):     #Called when "Search" button is clicked
        search_input = self.search_txt.get().strip().lower()        #Get input and normalize it

        if search_input == "":      #If input is empty
            set_text(self.track_txt, "No matching track found")     #Display content in right text box
            self.status_lbl.configure(text="Input is empty!", fg="red")     #Update status
        else:
            filtered_tracks = [track for track in lib.library.values()
                               if search_input in track.name.lower() or search_input in track.artist.lower()]       # Filter tracks that match input (in name or artist)

            if filtered_tracks:     # Found matches
                lines = [f"{track.name} by {track.artist} (Rating: {track.rating})" for track in filtered_tracks]
                set_text(self.track_txt, '\n'.join(lines))      #Show results
                self.status_lbl.configure(text=f"Found {len(filtered_tracks)} track(s)", fg="green")
                self.search_txt.delete(0, tk.END)       #Clear search entry
            else:
                set_text(self.track_txt, "No matching track found")
                self.status_lbl.configure(text="No matching track found", fg="red")


    def sort_combobox_clicked(self):        #Called when "Sort" button is clicked
        group = self.combo_sort.get()       #Get selected sort option
        if group == "":
            self.status_lbl.configure(text="Please select a sorting method first!", fg="red")
        elif group == "rating ↑":
            self.descending_sort()      #Sort by rating (highest to lowest)
            self.status_lbl.configure(text="Option sorting by rating ascending was clicked!", fg="green")
            self.combo_sort.current(0)  #Reset combobox selection
        elif group == "rating ↓":
            self.ascending_sort()       #Sort by rating (lowest to highest)
            self.status_lbl.configure(text="Option sorting by rating descending was clicked!", fg="green")
            self.combo_sort.current(0)
        elif group == "a-z":
            self.alphabet_sort()        #Sort by name A–Z
            self.status_lbl.configure(text="Option sorting by name A to Z was clicked!", fg="green")
            self.combo_sort.current(0)
        elif group == "z-a":
            self.alphabet_reserve()     #Sort by name Z–A
            self.status_lbl.configure(text="Option sorting by name Z to A was clicked!", fg="green")
            self.combo_sort.current(0)

    def ascending_sort(self):
        sorted_tracks = sorted(lib.library.values(), key=lambda x: x.rating)    #Use lambda to extract 'rating' attribute as sorting key
        self.display_sorted(sorted_tracks)      #Display the sorted list
    def descending_sort(self):
        sorted_tracks = sorted(lib.library.values(), key=lambda x: x.rating, reverse=True)       #'reverse=True' reverses the order of the sorted list
        self.display_sorted(sorted_tracks)
    def alphabet_sort(self):
        sorted_tracks = sorted(lib.library.values(), key=lambda x: x.name.lower())      #Convert to lowercase to ensure case-insensitive sorting
        self.display_sorted(sorted_tracks)
    def alphabet_reserve(self):
        sorted_tracks = sorted(lib.library.values(), key=lambda x: x.name.lower(), reverse=True)
        self.display_sorted(sorted_tracks)

    def filtered_combobox_clicked(self):        #Called when "Filter" button is clicked
        group = self.combo_filter.get()         #Get selected artist name
        if group == "":
            self.status_lbl.configure(text="Please select a filter first!", fg="red")
        else:
            self.artist_filter(group)       # Filter by selected artist
            self.status_lbl.configure(text=f"Option filter by {group} was clicked!", fg="green")
            self.combo_filter.current(0)     #Reset combobox selection

    def artist_filter(self, filter_get_txt):    #Called to filter tracks by artist name
        filtered_list = [track for track in lib.library.values() if filter_get_txt == track.artist]     #Get track information
        self.display_sorted(filtered_list)      #Show matching tracks
        self.status_lbl.configure(text=f"Found {len(filtered_list)} track(s) by {filter_get_txt}", fg="green")


    def display_sorted(self, sorted_tracks):    #Display tracks in right-side text box
        lines = []      #Initialize an empty list to store formatted track strings
        for track in sorted_tracks:
            lines.append(f"{track.name} by {track.artist} (Rating: {track.rating})")    #Format each track as a string and add it to the list
        set_text(self.track_txt, '\n'.join(lines))      # Show all results


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
