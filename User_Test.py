import pytest
from User import User, Watchlist
from Movie import Movie


@pytest.fixture
def user():
    return User('Martin', 'pw12345')


def test_add_watchlist(user):
    user.create_watchlist()
    watchlist = user.watchlist[0]

    assert watchlist == Watchlist()


def test_add_same_name_list(user):
    watchlist = user.create_watchlist("1")
    watchlist = user.create_watchlist("1")
    length = len(user.watchlist)

    assert length == 1


def test_add_movie_to_watchlist(user):
    user.create_watchlist("1")
    user.add_movie_to_watchlist(Movie("Moana", 2016), user.watchlist[0])
    movie = user.watchlist[0].first_movie_in_watchlist()

    assert movie == Movie("Moana", 2016)


def test_share_and_save_watchlist(user):
    user1 = User('Ian', 'pw67890')
    user1.create_watchlist('2')
    user.add_movie_to_watchlist(Movie("Ice Age", 2002), user1.watchlist[0])
    compare_list = user1.watchlist[0]
    compare_list.share_watchlist()
    user.save_watchlist(compare_list)
    result = (user.watchlist[0] == compare_list)

    assert result == True


def test_non_private_watchlist(user):
    user1 = User('Ian', 'pw67890')
    user1.create_watchlist('2')
    user.add_movie_to_watchlist(Movie("Ice Age", 2002), user1.watchlist[0])
    compare_list = user1.watchlist[0]
    user.save_watchlist(compare_list)
    result = len(user.watchlist)

    assert result == 0


