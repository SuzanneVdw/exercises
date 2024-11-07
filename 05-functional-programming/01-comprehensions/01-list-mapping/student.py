import re

def titles(movies):

    return [Movie.title for Movie in movies]

def titles_and_years(movies):

    return [(Movie.title,Movie.year) for Movie in movies]

def titles_and_actor_counts(movies):

    return [(Movie.title,len(Movie.actors)) for Movie in movies]

def reverse_words(sentence):

    words = re.findall(r"\b[a-zA-Z]+\b",sentence)  

    return " ".join([word[::-1] for word in words])