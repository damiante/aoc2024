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


def make_count_dict(l):
    count_dict = dict()

    for val in l:
        if not val in count_dict:
            count_dict[val] = 1
        else:
            count_dict[val] += 1

    return count_dict

def calculate_similarity(l, d):
    result = []
    for val in l:
        result.append((val * d[val] if val in d else 0))
    
    return result

def main():
    with open(INPUT, "r") as f:
        list1, list2 = parse_input(f)
    

    count_dict = make_count_dict(list2)

    similarity_list = calculate_similarity(list1, count_dict)

    print(sum(similarity_list))



if __name__ == "__main__":
    main()