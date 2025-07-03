import tkinter as tk
from view_tracks import TrackViewer
from update_tracks import UpdateRating
from create_track_list import CreateTrackList


def view_tracks_clicked():      #Callback function triggered when the "View Tracks" button is clicked
    status_lbl.configure(text="View Tracks button was clicked!", fg="green")    #Updates the status label
    TrackViewer(tk.Toplevel(window))    #Create a new child window for viewing tracks

def update_rating_clicked():    #Callback function for the "Update Tracks" button
    status_lbl.configure(text="Update Rating button was clicked!", fg="green")
    UpdateRating(tk.Toplevel(window))   #Open update rating window

def create_track_clicked():     #Callback for the "Create Track List" button
    status_lbl.configure(text="Create track button was clicked!", fg="green")
    CreateTrackList(tk.Toplevel(window))    #Open create track list window

window = tk.Tk()    #Create the main window
window.geometry("400x150")      #Set window size
window.title("JukeBox")     #Set the title of the window
window.configure(bg="#f4f4f4")      #Set background color
window.resizable(False, False)      #Disable resizing

# fonts.configure()     #Apply global font configuration if available

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below", font=("Helvetica", 12), bg="#f4f4f4")   #Create and locate a label
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=(15,10))

view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked, bg="#008080", fg="white")      #Create and locate "View Tracks" button (binds to view_tracks_clicked)
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

create_track_list_btn = tk.Button(window, text="Create Track List", command=create_track_clicked, bg="#008080", fg="white")     #Create and locate "Create Track List" button (binds to create_track_clicked)
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_tracks_btn = tk.Button(window, text="Update Tracks", command=update_rating_clicked, bg="#008080", fg="white")    #Create and locate "Update Tracks" button (binds to update_rating_clicked)
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, text="Status", font=("Helvetica", 10), bg="#f4f4f4")  #Create a label to display the status
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()    #Keeps the window open and responsive
