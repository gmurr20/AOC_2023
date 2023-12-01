from typing import Optional


def extract_calibration_value_part_1(input_line: str) -> int:
    left_digit = None
    right_digit = None
    for i in range(len(input_line)):
        left_char = input_line[i]
        right_char = input_line[len(input_line) - 1 - i]
        if left_digit is None and left_char.isdigit():
            left_digit = left_char
        if right_digit is None and right_char.isdigit():
            right_digit = right_char
        if left_digit and right_digit:
            break
    return int(f"{left_digit}{right_digit}")


DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def extract_digit(idx: int, input_line: str) -> Optional[str]:
    curr_char = input_line[idx]
    if curr_char.isdigit():
        return curr_char
    for digit_str, val in DIGITS.items():
        right_idx = idx + len(digit_str)
        if right_idx <= len(input_line) and input_line[idx:right_idx] == digit_str:
            return str(val)
        left_idx = idx + 1 - len(digit_str)
        if left_idx >= 0 and input_line[left_idx : idx + 1] == digit_str:
            return str(val)
    return None


def extract_calibration_value_part_2(input_line: str) -> int:
    left_digit = None
    right_digit = None
    for i in range(len(input_line)):
        left_idx = i
        right_idx = len(input_line) - 1 - i
        if left_digit is None:
            left_digit = extract_digit(left_idx, input_line)
        if right_digit is None:
            right_digit = extract_digit(right_idx, input_line)
        if left_digit and right_digit:
            break
    return int(f"{left_digit}{right_digit}")


def main():
    input_file = open("input.txt", "r")
    total_sum_1 = 0
    total_sum_2 = 0
    for line in input_file:
        total_sum_1 += extract_calibration_value_part_1(line)
        total_sum_2 += extract_calibration_value_part_2(line)

    print(f"Sum of calibration values: {total_sum_1}")
    print(f"Sum of calibration values spelled out: {total_sum_2}")


if __name__ == "__main__":
    main()
