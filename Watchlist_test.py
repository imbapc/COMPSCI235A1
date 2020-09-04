import pytest

from User import Watchlist, User

from Movie import Movie


@pytest.fixture
def watchlist():
    return Watchlist()


def test_size_empty(watchlist):
    size = watchlist.size()

    assert size == 0


def test_first_movie_empty(watchlist):
    first_movie = watchlist.first_movie_in_watchlist()

    assert first_movie is None


def test_add_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    first_movie = watchlist.first_movie_in_watchlist()
    size = watchlist.size()

    assert first_movie == Movie("Moana", 2016)
    assert size == 3


def test_add_same_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    watchlist.add_movie(Movie("Moana", 2016))
    size = watchlist.size()

    assert size == 3


def test_remove_unknown_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    watchlist.remove_movie(Movie("Moana", 2008))
    size = watchlist.size()

    assert size == 3


def test_remove_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    watchlist.remove_movie(Movie("Moana", 2016))
    size = watchlist.size()

    assert size == 2


def test_find_index(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    out_of_bound = watchlist.select_movie_to_watch(4)
    inbound = watchlist.select_movie_to_watch(0)

    assert inbound == Movie("Moana", 2016)
    assert out_of_bound is None


def test_iteration(watchlist):
    result = []
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    for movie in watchlist:
        result.append(movie)

    assert result == [Movie("Moana", 2016), Movie("Ice Age", 2002), Movie("Guardians of the Galaxy", 2012)]


def test_sharing_and_stop_sharing(watchlist):
    watchlist.share_watchlist()
    bool1 = watchlist.privacy
    watchlist.stop_sharing()
    bool2 = watchlist.privacy

    assert bool1 == False
    assert bool2 == True


def test_set_owner(watchlist):
    watchlist.owner = User('Martin', 'pw12345')
    user = watchlist.owner

    assert user == User('Martin', 'pw12345')


def test_assign_name(watchlist):
    watchlist.name = "123"
    string = watchlist.name
    watchlist.name = "456"
    string2 = watchlist.name

    assert string == "123"
    assert string2 == "456"