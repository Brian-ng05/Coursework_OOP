# 🎵 Track Manager (Tkinter GUI Application)

This Python mini project simulates a simple music library and playlist manager with a graphical user interface (GUI) built using **Tkinter**. It was developed as part of a coursework assignment with the main objective of practicing **Object-Oriented Programming (OOP)** principles and demonstrating how OOP can be applied to build modular, reusable, and maintainable software systems. The design highlights concepts such as classes, objects, encapsulation, abstraction, and modular separation of concerns.  


## 🎯 Learning Objectives

This project was created as part of an OOP-focused coursework with the following learning outcomes:

- Apply **Object-Oriented Programming (OOP)** concepts such as class design, object instantiation, encapsulation, and modular decomposition.  
- Model real-world entities (tracks, playlists) as classes with relevant attributes and behaviors.  
- Implement separation of concerns through multiple modules and GUI classes, ensuring clean design and reusability.  
- Combine **data structures** (`dict` for music library, `list` for playlists) with OOP to manage track storage and playlist creation.  
- Use **algorithms** for searching and sorting tracks, integrated within GUI-based workflows.  
- Design and implement a **Tkinter GUI**, learning how to connect OOP classes to event-driven programming.  
- Apply **file handling (JSON)** to persist playlists between program runs.  
- Strengthen problem-solving and software design skills by building an application that mirrors practical use cases.  


## ✨ Features

- **Track Library Management**: Tracks are stored as `LibraryItem` objects with encapsulated attributes and methods for rating and play count. Users can browse and view all available tracks in a scrollable list.  
- **Search and Filter**: Search for tracks by name or artist, or filter by specific artist. Sorting options include rating (ascending/descending) and alphabetical (A–Z, Z–A). These features are implemented within the `TrackViewer` class, showcasing modular OOP design.  
- **Update Ratings**: Through the `UpdateRating` class, users can select a track and update its rating from 1 to 5 stars. The updated value is stored in the track object, reflecting encapsulation and direct object manipulation.  
- **Playlist Management**: Using the `CreateTrackList` class, users can create playlists by selecting tracks, save them to a JSON file, load them later, or reset them. Each action demonstrates how objects and file I/O can work together in an OOP context.  
- **Play Count Tracking**: Every time a playlist is played, the application increments the `play_count` attribute of each track object. This functionality demonstrates how OOP allows state to be stored and updated inside objects.  
- **Tkinter GUI**: The system leverages Tkinter widgets (buttons, labels, text areas, comboboxes, and treeviews) wrapped inside dedicated classes. This highlights event-driven OOP design where methods are bound to GUI events.  



## Installation

#### Requirements
- Python **3.10+** installed  
- Tkinter (included by default in most Python distributions)  

#### Steps 1: Clone the repository
```bash
git clone https://github.com/Brian-ng05/Coursework_OOP.git
cd Coursework_OOP
```
#### Steps 2: Compile the source files
```bash
Since this project is written in Python, no explicit compilation step is needed. 
Ensure all .py files are in the same directory (with supporting modules available).
```
#### Steps 3: Run the program
``` bash
python track_player.py
```
## Authors

- [@Nguyen Quoc Bao](https://github.com/Brian-ng05)

