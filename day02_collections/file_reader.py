try:
    with open("basics/day02_collections/ips.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            print(line)

except FileNotFoundError:
    print("File not found")
