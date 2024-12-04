#!/usr/bin/python3

import re

#Matches a number of up to 3 digits (not 0)
NUM_MATCH_STR = "[1-9][0-9]{0,2}"
#Matches mults of the form "mul(xxx,yyy)" where xxx or yyy is a number of the above form
MULT_MATCH_STR = f"mul\({NUM_MATCH_STR},{NUM_MATCH_STR}\)"

DO_MATCH_STR = "do\(\)"
DONT_MATCH_STR = "don't\(\)"

UNION_MATCH_STR = f"({DO_MATCH_STR})|({DONT_MATCH_STR})|({MULT_MATCH_STR})"

INPUT = "./input"


def do_mult(multstr):
    pattern = re.compile(NUM_MATCH_STR)
    x, y = re.findall(pattern, multstr)
    return int(x) * int(y)


def main():
    union_pattern = re.compile(UNION_MATCH_STR)
    mult_pattern = re.compile(MULT_MATCH_STR)
    do_pattern = re.compile(DO_MATCH_STR)
    dont_pattern = re.compile(DONT_MATCH_STR)

    total = 0
    enabled = True

    with open(INPUT, "r") as f:

        for line in f:
            commands = re.findall(union_pattern, line)
            
            for command in commands:
                #Because there's an or in the regex it returns a 3-tuple
                #so pull out the non-null value
                for val in command:
                    if bool(val):
                        command = val

                if enabled and re.match(mult_pattern, command):
                    total += do_mult(command)
                elif re.match(dont_pattern, command):
                    enabled = False
                elif re.match(do_pattern, command):
                    enabled = True

    print(total)




if __name__ == "__main__":
    main()