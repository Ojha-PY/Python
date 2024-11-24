with open('test3.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Prints each line without leading/trailing whitespace