import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
import track_library as lib


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class TrackViewer():
    def __init__(self, window):
        self.window = window
        self.window.geometry("720x400")
        self.window.configure(bg="#f4f4f4")
        self.window.title("View Tracks")
        self.window.resizable(False, False)


        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none", font=("Segoe UI", 10))
        self.list_txt.grid(row=0, column=0, columnspan=3, sticky="W", padx=20, pady=(30, 10))

        self.track_txt = tk.Text(window, width=40, height=8, wrap="none", font=("Segoe UI", 10))
        self.track_txt.grid(row=0, column=3, sticky="NW", padx=20, pady=(30, 10))


        self.list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked, bg="#008080", fg="white")
        self.list_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Track Number", bg="#f4f4f4")
        enter_lbl.grid(row=1, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=1, column=2, padx=10, pady=10)

        self.check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked, bg="#008080", fg="white")
        self.check_track_btn.grid(row=1, column=3, padx=10, pady=10)


        search_frame = ttk.Frame(master=self.window)
        search_frame.grid(row=2, column=0, columnspan=2, sticky="we", padx=(50,0), pady=10)

        self.search_txt = tk.Entry(search_frame, width=24, font=("Segoe UI", 10))
        self.search_txt.pack(side="left")
        self.search_txt.focus()

        self.search_btn = tk.Button(search_frame, text="Search", command=self.search_track ,font=("Segoe UI", 10), bg="#008080", fg="white")
        self.search_btn.pack(side="left")

        groups_sorting = ["", "rating ↑", "rating ↓", "a-z", "z-a"]
        sort_frame = ttk.Frame(window)
        sort_frame.grid(row=2, column=2, columnspan=2, sticky="we", padx=(50,0), pady=10)

        self.combo_sort = ttk.Combobox(sort_frame)
        self.combo_sort["values"] = groups_sorting
        self.combo_sort.current(0)
        self.combo_sort.pack(side="left")

        self.check_combobox = tk.Button(sort_frame, text="Sort", command=self.combobox_clicked, bg="#008080", fg="white")
        self.check_combobox.pack(side="left")


        self.status_lbl = tk.Label(window, text="", font=("Segoe UI", 10), bg="#f4f4f4")
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="we", padx=10, pady=10)


    def view_tracks_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if not key:
            self.status_lbl.configure(text="Input is empty!", fg="red")
            return
        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
        else:
            set_text(self.track_txt, f"Track {key} not found")

        self.input_txt.delete(0, tk.END)
        self.status_lbl.configure(text="View Track button was clicked!", fg="green")

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")

    def search_track(self):
        search_input = self.search_txt.get().strip().lower()

        if search_input == "":
            set_text(self.track_txt, "No matching track found")
            self.status_lbl.configure(text="Input is empty!", fg="red")
        else:
            filtered_tracks = [track for track in lib.library.values()
                               if search_input in track.name.lower() or search_input in track.artist.lower()]

            if filtered_tracks:
                lines = [f"{track.name} by {track.artist} (Rating: {track.rating})" for track in filtered_tracks]
                set_text(self.track_txt, '\n'.join(lines))
                self.status_lbl.configure(text=f"Found {len(filtered_tracks)} track(s)", fg="green")
                self.search_txt.delete(0, tk.END)
            else:
                set_text(self.track_txt, "No matching track found")
                self.status_lbl.configure(text="No matching track found", fg="red")



    def combobox_clicked(self):
        group = self.combo_sort.get()
        if group == "":
            self.status_lbl.configure(text="Please select a sorting method first!", fg="red")
        elif group == "rating ↑":
            self.ascending_sort()
            self.status_lbl.configure(text="Option sorting by rating ascending was clicked!", fg="green")
            self.combo_sort.current(0)
        elif group == "rating ↓":
            self.descending_sort()
            self.status_lbl.configure(text="Option sorting by rating descending was clicked!", fg="green")
            self.combo_sort.current(0)
        elif group == "a-z":
            self.alphabet_sort()
            self.status_lbl.configure(text="Option sorting by name A to Z was clicked!", fg="green")
            self.combo_sort.current(0)
        elif group == "z-a":
            self.alphabet_reserve()
            self.status_lbl.configure(text="Option sorting by name Z to A was clicked!", fg="green")
            self.combo_sort.current(0)

    def ascending_sort(self):
        sorted_tracks = sorted(lib.library.values(), key=lambda x: x.rating, reverse=True)
        self.display_sorted(sorted_tracks)
    def descending_sort(self):
        sorted_tracks = sorted(lib.library.values(), key=lambda x: x.rating, reverse=False)
        self.display_sorted(sorted_tracks)
    def alphabet_sort(self):
        sorted_tracks = sorted(lib.library.values(), key=lambda x: x.name.lower(), reverse=False)
        self.display_sorted(sorted_tracks)
    def alphabet_reserve(self):
        sorted_tracks = sorted(lib.library.values(), key=lambda x: x.name.lower(), reverse=True)
        self.display_sorted(sorted_tracks)

    def display_sorted(self, sorted_tracks):
        lines = []
        for track in sorted_tracks:
            lines.append(f"{track.name} by {track.artist} (Rating: {track.rating})")
        set_text(self.track_txt, '\n'.join(lines))


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
