from library_item import LibraryItem

library = {}    #Create a dictionary to store data

#Initialize the music library
library["01"] = LibraryItem("Another Brick in the Wall", "Pink Floyd", 4)
library["02"] = LibraryItem("Stayin' Alive", "Bee Gees", 5)
library["03"] = LibraryItem("Highway to Hell ", "AC/DC", 2)
library["04"] = LibraryItem("Shape of You", "Ed Sheeran", 4)
library["05"] = LibraryItem("Someone Like You", "Adele", 3)
library["06"] = LibraryItem("Vung Ky Uc", "Chilies", 3)
library["07"] = LibraryItem("Die With A Smile", "Lady Gaga/Bruno Mars", 5)
library["08"] = LibraryItem("Tro Ve", "Wxrdie",4)
library["09"] = LibraryItem("Ex's Hate Me","B Ray", 4)
library["10"] = LibraryItem("Phep Mau", "MayDays", 4)
library["11"] = LibraryItem("Ex's Hate Me 2","B Ray", 4)



def list_all():     #Returns a string containing all the track information
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):      #Return name of song
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):    #Return artist of song
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None


def get_rating(key):    #Return rating of song
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):    #Set rating of song
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):    #Return play count
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):      #Plus 1 for play
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return
