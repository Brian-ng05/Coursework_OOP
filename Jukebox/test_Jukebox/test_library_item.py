from library_item import LibraryItem

def test_info():
    item = LibraryItem("Ex's Hate Me", "B Ray", 4)
    expected = "Ex's Hate Me - B Ray ****"
    assert item.info() == expected

def test_starts():
    item = LibraryItem("Stayin' Alive", "Bee Gees", 5)
    assert item.stars() == "*****"

def test_default_constructor():
    item = LibraryItem("Stayin' Alive", "Bee Gees")
    assert item.play_count == 0
    assert item.rating == 0
