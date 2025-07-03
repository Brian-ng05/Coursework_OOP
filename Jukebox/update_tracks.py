import tkinter as tk
from tkinter import ttk
from track_library import library
from track_library import set_rating, get_name, get_play_count, get_artist
from font_manager import get_h1_font

class UpdateRating:
    def __init__(self, window):
        self.window = window    #Store the main window reference as an instance variable for later use
        self.window.title("Update Rating")  #Set name title
        self.window.geometry("600x400")     #Set size for window
        self.window.resizable(False, False)     #Don't allow to resize
        self.window.configure(bg="#f4f4f4")     #Set background color

        self.library = library  #get all data from library

        self.create_widgets()   #call function to create GUI

    def create_widgets(self):
        title_lbl = tk.Label(self.window, text="🎵 Update Track Rating", font=get_h1_font(), bg="#f4f4f4")
        title_lbl.pack(pady=(20, 5))

        self.tree = ttk.Treeview(self.window, columns=("order", "title", "artist"), show="headings", height=6, selectmode="none")  # Create a Treeview widget to display a list of tracks with 3 columns: Track Number, Title, and Artist
        self.tree.heading("title", text="Title")            #Define column header for track title
        self.tree.heading("artist", text="Artist")          #Define column header for artist name
        self.tree.heading("order", text="Track Number")     #Define column header for track number (key)
        #Set the width for each column
        self.tree.column("title", width=220)
        self.tree.column("artist", width=150)
        self.tree.column("order", width=90)

        self.tree.pack(pady=15)     #Add vertical padding around the widget

        self.populate_tree()    #Call method to insert data into the table

        input_frame = ttk.Frame(master= self.window)    #create a frame to put all the input buttons in
        input_frame.pack(pady=10)   #Add vertical padding around the input_frame

        ttk.Label(input_frame, text="Enter Track Number:").grid(row=0, column=0, padx=5, pady=5, sticky="we")   #Create and locate a label
        self.track_num_var = tk.StringVar()     #create a string variable to store user input
        self.track_num_input = ttk.Entry(input_frame, textvariable=self.track_num_var, width=12)    #Create an input field for track number (binds to self.track_num_var)
        self.track_num_input.grid(row=0, column=1, padx=10, pady=5, sticky="e")     #locate the track_num_input
        self.track_num_input.focus()    # Place the cursor in the input box

        ttk.Label(input_frame, text="Select Rating:").grid(row=1, column=0, padx=5, pady=5, sticky="we")    #Create and locate a label in input_frame

        rating_frame = ttk.Frame(input_frame)   #create a frame to put all the radio buttons in
        rating_frame.grid(row=1, column=1, padx=5, pady=5, sticky="e")      #locate the rating_frame

        self.rating_var = tk.IntVar()   #create an integer variable to store user selection
        for i in range(1, 6):
            ttk.Radiobutton(rating_frame, text=str(i), variable=self.rating_var, value=i).pack(side="left", padx=3)     #use a loop to create 5 radio buttons in a row

        self.update_btn = tk.Button(self.window, text="Update Rating", bg="#008080", fg="white", command=self.update_rating)    #create Update Rating button
        self.update_btn.pack(pady=5)

        self.status_lbl = tk.Label(self.window, text="", fg="green", bg="#f4f4f4")      #create label to inform status
        self.status_lbl.pack(pady=5)

    def populate_tree(self):    #Insert each track into the Treeview with its ID, name, and artist
        for key in self.library:
            self.tree.insert('', 'end', values=(key, get_name(key), get_artist(key)))

    def update_rating(self):    #update rating function
        selected = self.track_num_var.get()     #get user input value

        if not selected:    #check if it is empty
            self.status_lbl.config(text="Please enter a track first.", fg="red")
            return

        if selected not in self.library:    #check if it not exist in library
            self.status_lbl.config(text="Invalid track number.", fg="red")
            return

        new_rating = self.rating_var.get()      #get data
        if new_rating == 0:     #check if user don't select
            self.status_lbl.config(text="Please select a rating.", fg="red")
            return

        set_rating(selected, new_rating)    #set new rating value
        self.status_lbl.config(text=f"Updated rating for '{get_name(selected)}' to {new_rating} ⭐! Play count: {get_play_count(selected)}", fg="green")     #print new rating status and play count

        self.track_num_var.set("")  # clear track number entry
        self.rating_var.set(0)      # clear rating selection


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    UpdateRating(window)    # open the UpdateRating GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
