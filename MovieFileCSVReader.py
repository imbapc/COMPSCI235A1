import csv
from Movie import Director, Genre, Actor, Movie


class MovieFileCSVReader:
    def __init__(self, filename: str):
        if isinstance(filename, str):
            self._filename = filename
        else:
            self._filename = ""
        self._dataset_of_movies = []
        self._dataset_of_actors = []
        self._dataset_of_directors = []
        self._dataset_of_genres = []

    def read_csv_file(self):
        with open(self._filename, mode='r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            index = 2
            for row in reader:
                title = row["Title"]
                release_year = int(row["Year"])
                movie1 = Movie(title, release_year)
                self._dataset_of_movies.append(movie1)
                director_name = row["Director"]
                director = Director(director_name)
                if director not in self._dataset_of_directors:
                    self._dataset_of_directors.append(director)
                actor_name_list = row["Actors"].split(",")
                index1 = 1
                for name in actor_name_list:
                    actor = Actor(name.strip())
                    if actor not in self._dataset_of_actors:
                        self._dataset_of_actors.append(actor)
                    elif actor.actor_full_name == "None":
                        print(name)
                        print(index, actor, index1)
                    index1 += 1
                genre_list = row["Genre"].split(",")
                for type in genre_list:
                    genre = Genre(type.strip())
                    if genre not in self._dataset_of_genres:
                        self._dataset_of_genres.append(genre)
                index += 1

    @property
    def dataset_of_movies(self):
        return self._dataset_of_movies

    @property
    def dataset_of_directors(self):
        return self._dataset_of_directors

    @property
    def dataset_of_actors(self):
        return self._dataset_of_actors

    @property
    def dataset_of_genres(self):
        return self._dataset_of_genres
