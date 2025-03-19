import re


def solution(my_string):
    numbers = re.findall(r"\d+", my_string)
    return sum(map(int, numbers))


# Example usage:
print(solution("aAb1B2cC34oO123p"))  # Output: 37
