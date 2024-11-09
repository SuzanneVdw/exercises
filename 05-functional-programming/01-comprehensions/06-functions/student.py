def movie_count(movies, director):

    return len([Movie for Movie in movies if Movie.director == director])

def longest_movie_runtime_with_actor(movies, actor):

    return max([Movie.runtime for Movie in movies if actor in Movie.actors])

def has_director_made_genre(movies, director, genre):

    return any([genre in movie.genres and movie.director == director for movie in movies])

def is_prime(n):

    return all([n%x != 0 for x in range(2, n)]) and n > 1

def is_increasing(ns):

    return all([ns[x-1] <= ns[x] for x in range(1,len(ns))])

def count_matching(xs, ys):

    zipped_counts = zip(xs,ys)
    return []