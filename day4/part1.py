#!/usr/bin/python3

INPUT = "./test"


def count_matches(s):
    count = 0
    for i in range(len(s)):
        word = s[i:i+4]
        if word == "XMAS" or word == "SAMX":
            count += 1

    return count



def main():

    file_contents = []
    with open(INPUT, "r") as f:
        for line in f:
            file_contents.append(line.strip())

    count = 0
    num_lines = len(file_contents)

    #Assuming the file is square

    #horizontals
    for line in file_contents:
        count += count_matches(line)

    #verticals
    for i in range(num_lines):
        s = "".join([file_contents[x][i] for x in range(num_lines)])
        count += count_matches(s)

    #descending diagonals
    for i in range(2*num_lines):
        s = ""
        if i < num_lines:
            for j in range(i+1):
                s += file_contents[j][num_lines+j-i-1]
        elif i == num_lines:
            continue
        else:
            for j in range(2*num_lines-i):
                s += file_contents[num_lines-i+j][j]
        print(s)
        count += count_matches(s)


    #ascending diagonals
    for i in range(2*num_lines):
        s = ""
        if i < num_lines:
            for j in range(i+1):
                s += file_contents[i-j][j]
        elif i == num_lines:
            continue
        else:
            for j in range(2*num_lines-i):
                s += file_contents[num_lines-1-j][(num_lines-1)-(2*num_lines-i)+j+1]
        print(s)
        count += count_matches(s)

    print(count)

if __name__ == "__main__":
    main()