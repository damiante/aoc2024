#!/usr/bin/python3


INPUT = "./input"

def parse_input(file):
    list1, list2 = [], []
    for line in file:
        line = line.split()
        list1.append(int(line[0]))
        list2.append(int(line[-1]))
    
    print(list1, list2)
    return (list1, list2)


def main():
    with open(INPUT, "r") as f:
        list1, list2 = parse_input(f)
    
    list1, list2 = sorted(list1), sorted(list2)

    # print(list1, list2)

    result = [abs(list1[x] - list2[x]) for x in range(len(list1))]

    # print(result)
    print(sum(result))



if __name__ == "__main__":
    main()