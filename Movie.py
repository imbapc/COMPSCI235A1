import re


class Director:
    def __init__(self, director: str):
        if not re.search("^[a-zA-Z]+", str(director)):
            self._director = 'None'
        else:
            self._director = director

    @property
    def director_full_name(self) -> str:
        return self._director

    @director_full_name.setter
    def director_full_name(self, director: str):
        self._director = director

    def __repr__(self):
        return f'<Director {self._director}>'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Director):
            return False
        return self._director == other._director

    def __lt__(self, other) -> bool:
        if not isinstance(other, Director):
            return False
        return self._director < other._director

    def __hash__(self):
        return hash(self._director)


class Genre:
    def __init__(self, genre: str):
        if genre == "":
            self._genre = "None"
        else:
            self._genre = genre

    @property
    def genre_name(self):
        return self._genre

    @genre_name.setter
    def genre_name(self, genre):
        self._genre = genre

    def __repr__(self):
        return f'<Genre {self._genre}>'

    def __eq__(self, other):
        return self._genre == other.genre_name

    def __lt__(self, other):
        return self._genre < other.genre_name

    def __hash__(self):
        return hash(self._genre)


class Actor:
    def __init__(self, name: str):
        if str(name) == "":
            self._actor_name = "None"
        else:
            self._actor_name = name
        self._act_movie = []
        self._colleague = []

    @property
    def actor_full_name(self):
        return self._actor_name

    def __repr__(self) -> str:
        return f'<Actor {self._actor_name}>'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Actor):
            return False
        return self._actor_name == other._actor_name

    def __lt__(self, other) -> bool:
        if not isinstance(other, Actor):
            return False
        return self._actor_name < other._actor_name

    def __hash__(self):
        return hash(self._actor_name)

    def add_actor_colleague(self, colleague):
        self._colleague.append(colleague)

    def check_if_this_actor_worked_with(self, colleague) -> bool:
        return colleague in self._colleague


class Movie:
    def __init__(self, name, year):
        if name == "" or not isinstance(name, str):
            self._name = "None"
        elif year < 1900 or not isinstance(year, int):
            self._year = None
        else:
            self._name = name.strip()
            self._year = year
        self._director = None
        self._actors = []
        self._genres = []
        self._runtime_minutes = None
        self._description = ""

    def __repr__(self):
        return f'<Movie {self._name}, {self._year}>'

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        else:
            return self._name == other._name and self._year == other._year

    def __lt__(self, other):
        if not isinstance(other, Movie):
            return False
        elif self._name == other._name:
            return self._year < other._year
        else:
            return self._name < other._name

    def __hash__(self):
        return hash(self._name + str(self._year))

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, director: Director):
        if self._director == None and isinstance(director, Director):
            self._director = director

    @property
    def actors(self):
        return self._actors

    def add_actor(self, actor):
        if actor not in self._actors and str(actor) != "<Actor None>" and isinstance(actor, Actor):
            self._actors.append(actor)

    def remove_actor(self, actor):
        if actor in self._actors and str(actor) != "<Actor None>" and isinstance(actor, Actor) and not len(self._actors) == 0:
            self._actors.remove(actor)

    @property
    def genres(self):
        return self._genres

    def add_genre(self, genre):
        if genre not in self._genres and str(genre) != "<Genre None>" and isinstance(genre, Genre):
            self._genres.append(genre)

    def remove_genre(self, genre):
        if genre in self._genres and str(genre) != "<Genre None>" and isinstance(genre, Genre) and not len(self._genres) == 0:
            self._genres.remove(genre)

    @property
    def runtime_minutes(self):
        return self._runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, time):
        if (time < 0 or time == 0) and isinstance(time, int):
            raise ValueError("Runtime is invalid")
        else:
            self._runtime_minutes = time

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, des):
        if isinstance(des, str):
            self._description = des.strip()

    @property
    def title(self):
        return self._name

    @title.setter
    def title(self, name):
        if isinstance(name, str):
            self._name = name.strip()
