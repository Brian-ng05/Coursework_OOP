import tkinter as tk
from view_tracks import TrackViewer
from update_tracks import UpdateRating
from create_track_list import CreateTrackList


def view_tracks_clicked():
    status_lbl.configure(text="View Tracks button was clicked!", fg="green")
    TrackViewer(tk.Toplevel(window))

def update_rating_clicked():
    status_lbl.configure(text="Update Rating button was clicked!", fg="green")
    UpdateRating(tk.Toplevel(window))

def create_track_clicked():
    status_lbl.configure(text="Create track button was clicked!", fg="green")
    CreateTrackList(tk.Toplevel(window))

window = tk.Tk()
window.geometry("400x150")
window.title("JukeBox")
window.configure(bg="#f4f4f4")
window.resizable(False, False)

# fonts.configure()

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below", font=("Helvetica", 12), bg="#f4f4f4")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=(15,10))

view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked, bg="#008080", fg="white")
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

create_track_list_btn = tk.Button(window, text="Create Track List", command=create_track_clicked, bg="#008080", fg="white")
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_tracks_btn = tk.Button(window, text="Update Tracks", command=update_rating_clicked, bg="#008080", fg="white")
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, text="Status", font=("Helvetica", 10), bg="#f4f4f4")
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
