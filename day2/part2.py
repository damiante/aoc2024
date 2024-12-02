#!/usr/bin/python3

INPUT = "./input"


def safe_pair(num1, num2, gradient):
    if not (1 <= abs(num1 - num2) <= 3):
        return False
    if gradient == "+":
        return num1 < num2
    elif gradient == "-":
        return num1 > num2

def is_safe(nums, safety):
    #determine gradient
    asc = 0
    desc = 0
    for i in range(len(nums)):
        try:
            if nums[i] < nums[i+1]:
                asc += 1 
            elif nums[i] > nums[i+1]:
                desc += 1
        except IndexError:
            break
    sign = "-" if desc > asc else "+"

    #check each pair for conformity
    for i in range(len(nums)):
      
        try:
            result = safe_pair(nums[i], nums[i+1], sign)  
        except IndexError:
            return True
        
        #if a pair doesn't work, try with each number from the pair removed
        if not result:
            if safety and (is_safe(nums[:i] + nums[i+1:], False) or is_safe(nums[:i+1] + nums[i+2:], False)):
                return True
            else:
                return False
                

    
    




def main():
    with open(INPUT, "r") as f:
        count = 0
        for line in f:
            line = [int(x) for x in line.split()]
            if is_safe(line, True):
                # print(f"{line} is Safe!")
                count += 1


    print(count)


if __name__ == "__main__":
    main()
