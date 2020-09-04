import time
from Review import Review
from Movie import Movie


class User:
    def __init__(self, name: str, password: str):
        if not isinstance(name, str) or not isinstance(password, str):
            self._username = ""
            self._password = ""
        else:
            self._username = name.strip().lower()
            self._password = password
        self._watched_movies = []
        self._review = []
        self._time_spent_watching_movies_minutes = 0
        self._watchlist = []

    def __repr__(self):
        return f'<User {self._username}>'

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        else:
            return self._username == other._username

    def __lt__(self, other):
        if not isinstance(other, User):
            return False
        else:
            return self._username < other._username

    def __hash__(self):
        return hash(self._username + self._password)

    def watch_movie(self, movie):
        if isinstance(movie, Movie):
            self._watched_movies.append(movie)
            self._time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if isinstance(review, Review) and review not in self._review:
            self._review.append(review)

    def create_watchlist(self, name=""):
        for watchlist in self._watchlist:
            if name == watchlist.name:
                return "Watchlist already exists"
        self._watchlist.append(Watchlist(name))
        Watchlist.owner = self

    def add_movie_to_watchlist(self, movie, watchlist):
        if isinstance(movie, Movie) and isinstance(watchlist, Watchlist) and watchlist.owner == self:
            watchlist.add_movie(movie)

    def save_watchlist(self, watchlist):
        if isinstance(watchlist, Watchlist) and not watchlist.privacy:
            self._watchlist.append(watchlist)

    @property
    def user_name(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def watched_movies(self):
        return self._watched_movies

    @property
    def reviews(self):
        return self._review

    @property
    def time_spent_watching_movies_minutes(self):
        if self._time_spent_watching_movies_minutes == 0:
            return None
        else:
            return self._time_spent_watching_movies_minutes

    @property
    def watchlist(self):
        return self._watchlist


class Watchlist:
    def __init__(self, name=""):
        self._watchlist = []
        self._name = name
        self._privacy = True
        self._owner = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, user):
        if isinstance(user, User) and self._owner is None:
            self._owner = user
            print(self.owner)


    @property
    def privacy(self):
        return self._privacy

    def add_movie(self, movie: Movie):
        if movie not in self._watchlist:
            self._watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self._watchlist:
            self._watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if index in range(0, self.size()):
            return self._watchlist[index]
        else:
            return None

    def size(self):
        return len(self._watchlist)

    def first_movie_in_watchlist(self):
        if self.size() == 0:
            return None
        else:
            return self._watchlist[0]

    def share_watchlist(self):
        self._privacy = False

    def stop_sharing(self):
        self._privacy = True

    def __repr__(self):
        return f'<Watchlist {self._name}: {self._watchlist}>'

    def __eq__(self, other):
        if not isinstance(other, Watchlist):
            return False
        else:
            return self._name == other._name

    def __lt__(self, other):
        if not isinstance(other, Watchlist):
            return False
        else:
            return self._name < other._name

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index == self.size():
            raise StopIteration
        else:
            self._index += 1
            return self._watchlist[self._index - 1]
