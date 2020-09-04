import time
from Movie import Director, Genre, Actor, Movie

class Review:
    def __init__(self, movie, review: str, rating: int):
        if rating in range(1, 11) and isinstance(rating, int):
            self._rating = rating
        else:
            self._rating = None
        self._review = review
        self._movie = movie
        self._timestamp = time.time()

    @property
    def movie(self):
        return self._movie

    @property
    def review_text(self):
        return self._review

    @property
    def rating(self):
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp

    def __repr__(self):
        pass

    def __eq__(self, other):
        return self._movie == other._movie and self._review == other._review and \
               self._rating == other._rating