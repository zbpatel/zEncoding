def readFile(filepath):
    # the r indicates that we want read only mode
    raw_file = open(filepath, "r")
    file_str = raw_file.read()
