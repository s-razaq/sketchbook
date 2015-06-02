__author__ = 'Saqib Razaq'

import os.path


def main():
    """
    Ask the user for the name of a text file. Display the final line of that file.
    """
    filename = raw_input("Enter a filename: ")
    if os.path.isfile(filename):
        with open(filename) as f:
            lines = f.readlines()
            print lines[-1] # retrieve the last item in a list with index -1
    else:
        print "File not found"


if __name__ == '__main__':
    main()