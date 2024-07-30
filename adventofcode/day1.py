def extract_calibration_value(line):
    first_digit = None
    last_digit = None
    
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char
    
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