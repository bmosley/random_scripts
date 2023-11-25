with open("./pet.txt", "r") as f:
    for line in f.readlines():
        line = line.strip().replace("0", " ").replace("1", "#")
        print(line)

