def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    TODO: comment the parameter and the return value.
    """


    # TODO initialize a new data structure
    genre_dict = {}
    genre_list = []


    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres_split = genres.split(",")


            # TODO add the name and genres data to the data structure


            if name not in genre_dict:
                genre_dict[name] = genres_split

            for genre_name in sorted(genres_split):
                if genre_name not in genre_list:
                    genre_list.append(genre_name)

        genres_alphabetically = sorted(genre_list)
        genres_joined = ", ".join(genres_alphabetically)


        file.close()
        return genres_joined, genre_dict

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    series_genres = {}
    series_list = []
    genres_joined = ""

    genres_joined, series_genres = read_file(filename)
    # paluuarvot = funktio(kutsujaparametri)

    # TODO print the genres
    print(f"Available genres are: {genres_joined}")

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        # TODO print the series belonging to a genre.
        else:
            for series_x in series_genres:
                name, genres = series_x.rstrip().split(",")

                if genres not in series_genres:
                    series_genres[genres] = name

                for series_name in series_genres:
                    if series_name not in series_list:
                        series_list.append(series_name)

                        print(series_name)




if __name__ == "__main__":
    main()