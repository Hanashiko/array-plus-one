import sys
from typing import List

def plusOne(digits: List[int]) -> List[int]:
    max_index = len(digits) - 1
    if digits[max_index] == 9:
        i = max_index
        while(i >= -1):
            if digits[i] == 9:
                print(f"{digits = }")
                
                digits.pop()
                digits.append(1)
                digits.append(0)
            i -= 1
    else:        
        digits[max_index] = digits[max_index] + 1
    return digits

def plusOne(digits: List[int]) -> List[int]:
    string_number: str = str(int("".join([str(i) for i in digits])) + 1)
    return [int(string_number[i]) for i in range(len(string_number))]

def main() -> None:
    print(plusOne([1,2,3]))
    print(plusOne([4,3,2,1]))
    print(plusOne([4,3,2,9]))
    print(plusOne([9]))
    print(plusOne([9,9]))
    print(plusOne([1,2,9,9,9,9]))

if __name__ == "__main__":
    main()