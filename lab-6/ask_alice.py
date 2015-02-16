__author__ = 'eric'

fileName = "alice.txt"

# open the file for reading
inFile = open (fileName,"r")

# initialize the list of words to empty
words=[]
# initialize line and character counts to 0

# for each line in file (including newline)
for eachLine in inFile:
    # echo line out (no newline since already in line)

    print (eachLine,end='')

     # remove punctuation: .,-"'?!;:
    #   (best to replace each with blank, one call at a time)

    modline = eachLine.replace('.',' ')

    # make all letters lower-case

    # split modline into individual words

    # concatenate individual words to list of words

    # end of for

# sort the words

# print out each word, one per line

# print out total number of words

inFile.close()