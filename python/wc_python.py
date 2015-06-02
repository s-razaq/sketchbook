__author__ = 'Saqib Razaq'


'''
Simple implementation of Unix wc (word count) utility in Python
'''


def main():
    filename = raw_input("Please enter filename: ")
    with open(filename) as f:
        lines = f.readlines()
        number_of_lines = len(lines)
        number_of_characters = 0
        number_of_words = 0
        unique_words = set()
        for line in lines:
            number_of_characters += len(line)
            number_of_words +=len(line.split())
            unique_words |= set(line.split()) # add lists member to set using join operator
        print number_of_characters
        print number_of_words
        print number_of_lines
        print len(unique_words)


if __name__ == '__main__':
    main()