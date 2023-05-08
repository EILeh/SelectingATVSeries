"""
Selecting a TV-series

The program reads the TV series they know from a file, where the format of every
row is name;genres and genres are separated using commas. At the start of the
program, all the genres found from the file in an alphabetic order. The program
waits for the user's input with the prompt "> ". The user enters one of the
genres entered at the beginning, and the program prints the user all the series
marked to the genre in question. The program's execution ends with the command
exit. The series are printed in alphabetic order, so that each series is on its
own row. If the given genre does not include any series, nothing is printed.

Writer of the program: EILeh

"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.
    :param filename: The name of the file that contains the information.
    :return: genres_joined, genre_dict
    """

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

            # If the name is not in dictionary genre_dict, a new key-value
            # pair is added.
            if name not in genre_dict:
                genre_dict[name] = genres_split

            # Goes through the variable genres_split.
            for genre_name in sorted(genres_split):
                # If the genre_name is not is the list genre_list,
                # a new genre name is added to the list.
                if genre_name not in genre_list:
                    genre_list.append(genre_name)

        # Sorts the list genre_list.
        genres_alphabetically = sorted(genre_list)

        # Joins all the genres together where they are separated from comma.
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

    # return values = function_call(parameters)
    genres_joined, series_genres = read_file(filename)

    print(f"Available genres are: {genres_joined}")

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        else:
            # Goes through the dictionary series_genres.
            for series in sorted(series_genres):
                # Goes through the dictionary series_genres at the index series.
                for genres in sorted(series_genres[series]):
                    # If input genre is the same as genres, prints all the
                    # series that belong to the category.
                    if genre == genres:
                        print(series)


if __name__ == "__main__":
    main()