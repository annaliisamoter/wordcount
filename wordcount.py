# put your code here.
def word_count(file):

    """ keeps count of unique words in a text file """

    word_counts = {}

    f = open(file)
    for line in f:
        line = line.strip()
        line = line.split(" ")
        for word in line:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    for key, value in word_counts.items():
        print key, value


word_count('test.txt')
