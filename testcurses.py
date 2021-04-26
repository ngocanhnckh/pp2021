data = [['nameservers','panel'], ['nameservers','panel']]

with open("output.txt", "w") as txt_file:
    for line in data:
        txt_file.write(" ".join(line) + "\n") # works with any number of elements in a line