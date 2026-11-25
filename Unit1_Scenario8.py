class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    def get_category(self):
        if self.rating >= 8.0:
            return "Hit"
        elif self.rating >= 5.0:
            return "Average"
        else:
            return "Flop"

    def __str__(self):
        return (
            f"Movie: {self.movie_name} | Rating: {self.rating} | "
            f"Ticket Price: ₹{self.ticket_price} | Category: {self.get_category()}"
        )


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        for movie in self.movies:
            print(movie)


if __name__ == "__main__":
    cinema = Cinema()
    cinema.add_movie(Movie("Movie A", 8.5, 250))
    cinema.add_movie(Movie("Movie B", 6.5, 200))
    cinema.add_movie(Movie("Movie C", 4.0, 150))
    cinema.display_movies()

#OUTPUT
#Movie: Movie A | Rating: 8.5 | Ticket Price: ₹250 | Category: Hit
#Movie: Movie B | Rating: 6.5 | Ticket Price: ₹200 | Category: Average
#Movie: Movie C | Rating: 4.0 | Ticket Price: ₹150 | Category: Flop