def directors(movies):

    return {Movie.director for Movie in movies}

def common_elements(xs, ys):

    return {value for value in xs if value in ys}