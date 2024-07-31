# Mapping of spelled-out digits to their numeric equivalents
digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def extract_calibration_value(line):
    first_digit = None
    last_digit = None
    words = line.split()
    
    for word in words:
        if word.isdigit():
            if first_digit is None:
                first_digit = word
            last_digit = word
        elif word in digit_map:
            if first_digit is None:
                first_digit = digit_map[word]
            last_digit = digit_map[word]
    
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    return 0

def sum_calibration_values(filename):
    total_sum = 0
    with open("day1input.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                total_sum += extract_calibration_value(line)
    return total_sum

# Replace 'calibration_document.txt' with the actual filename
filename = 'calibration_document.txt'
result = sum_calibration_values(filename)
print(f"The sum of all calibration values is: {result}")