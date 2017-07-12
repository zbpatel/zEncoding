# Written by Zac Patel on 7/12/17

# only supports ascii at the moment, but could be expanded later to support
# other encoding types
def readFile(filepath):
    # the r indicates that we want read only mode
    file_str = open(filepath, mode="r", encoding="utf-8").read()
    # initializing our frequency array
    radix = 128 # using 128 because we only want ascii characters
    frequency = [0 for i in range(radix)]

    # counter for how many characters we missed
    num_errs = 0

    # using a long for loop rather than a list comprehension / map of ord() to
    # avoid needing two copies of the file in memory
    for i in range(len(file_str)):
        ascii_val = ord(file_str[i])
        if ascii_val > radix:
            num_errs += 1
        else:
            frequency[ascii_val] += 1

    #print("finished parsing with " + str(num_errs) + " errors")

    # returning the file string and frequency chart
    return file_str, frequency

def testParser():
    file_str, freq = readFile("docs\mobydick.txt")

    #print("Read: " + str(len(file_str)) + " chars from mobydick.txt")

    freq_str = ""
    for i in range(128):
        if freq[i] > 0:
            freq_str = freq_str + "\'" + chr(i) + "\': " + str(freq[i]) + ", "
    print(freq_str)

testParser()
