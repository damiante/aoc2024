#!/usr/bin/python3

INPUT = "./input"

def is_safe(nums):
    sign = "-" if nums[0] > nums[1] else "+"
    # print(sign, nums)

    for i in range(len(nums)):
        try:
            change = nums[i] - nums[i+1]
            # print(change)
        except IndexError:
            return True
        
        if not (1 <= abs(change) <= 3):
            return False
        elif sign == "-" and nums[i] < nums[i+1]:
            return False
        elif sign == "+" and nums[i] > nums[i+1]:
            return False
    




def main():
    with open(INPUT, "r") as f:
        count = 0
        for line in f:
            line = [int(x) for x in line.split()]
            if is_safe(line):
                print(f"{line} is Safe!")
                count += 1

    print(count)


if __name__ == "__main__":
    main()
