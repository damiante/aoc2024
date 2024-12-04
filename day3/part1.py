#!/usr/bin/python3

import re

#Matches a number of up to 3 digits (not 0)
NUM_MATCH_STR = "[1-9][0-9]{0,2}"
#Matches mults of the form "mul(xxx,yyy)" where xxx or yyy is a number of the above form
MULT_MATCH_STR = f"mul\({NUM_MATCH_STR},{NUM_MATCH_STR}\)"

INPUT = "./input"


def do_mult(multstr):
    pattern = re.compile(NUM_MATCH_STR)
    x, y = re.findall(pattern, multstr)
    return int(x) * int(y)


def main():
    pattern = re.compile(MULT_MATCH_STR)

    total = 0

    with open(INPUT, "r") as f:
        for line in f:
            mults = re.findall(pattern, line)
            for mult in mults:
                total += do_mult(mult)

    print(total)




if __name__ == "__main__":
    main()