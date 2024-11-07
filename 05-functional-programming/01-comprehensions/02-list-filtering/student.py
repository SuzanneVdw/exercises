def movies_from_year(movies, year):

    return [Movie.title for Movie in movies if Movie.year == year]

def movies_with_actor(movies, actor):

    return [Movie.title for Movie in movies if actor in Movie.actors]

def divisors(n):

    return [number for number in range(1,n+1) if n%number == 0]