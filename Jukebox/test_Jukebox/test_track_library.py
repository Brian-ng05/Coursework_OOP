from track_library import get_play_count, get_artist, get_rating, get_name, set_rating, increment_play_count

def test_get_name():
    assert get_name("01") == "Another Brick in the Wall"
def test_get_name_invalid():
    assert get_name("12") is None

def test_get_artist():
    assert get_artist("01") == "Pink Floyd"
def test_get_artist_invalid():
    assert get_artist("12") is None

def test_get_rating():
    assert get_rating("03") == 2
def test_get_rating_invalid():
    assert get_rating("12") == -1

def test_set_rating_valid():
    set_rating("04", 5)
    assert get_rating("04") == 5
def test_set_rating_invalid():
    assert set_rating("12", 4) is None

def test_increment_play_count():
    increment_play_count("01")
    assert get_play_count("01") == 1
def test_get_play_count_invalid():
    assert get_play_count("12") == -1