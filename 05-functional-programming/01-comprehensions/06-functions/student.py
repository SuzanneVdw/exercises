import re

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

    return len([x for x in list(zip(xs,ys)) if x[0] == x[1]])

def weighted_sum(ns, weights):

    return sum([x[0]*x[1] for x in list(zip(ns,weights))])

def alternating_caps(string):

    string_split_enum = enumerate(list(string))
    alternating_list = [char[1].upper() if char[0]%2 == 0 else char[1].lower() for char in string_split_enum]
    return "".join(alternating_list)

def find_repeated_words(sentence):

    words_list = (re.findall(r"(\b[a-zA-Z]+\b)",sentence))
    return {words_list[index].lower() for index in range(1,len(words_list)) if words_list[index-1].lower() == words_list[index].lower()}