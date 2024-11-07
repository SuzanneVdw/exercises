def title_to_director(movies):

    return {Movie.title: Movie.director for Movie in movies}

def director_to_titles(movies):

    def list_titles(director,movies):

        return [Movie.title for Movie in movies if Movie.director == director]

    return {Movie.director: list_titles(Movie.director,movies) for Movie in movies}