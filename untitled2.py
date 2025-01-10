

def extract_calibration_value(line):
    digits = [char for char in line if char.isdigit()]
    if not digits:
        return 0
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit + last_digit)

def main():
    file_path = input("Enter the path to the document file: ")
    try:
        with open(file_path, "r") as file:
            input_lines = file.readlines()
    except FileNotFoundError:
        print("File not found. Exiting.")
        return

    total_sum = 0

    for line in input_lines:
        value = extract_calibration_value(line.strip())
        print(f"Line: {line.strip()} -> Calibration Value: {value}")
        total_sum += value

    print("\nThe sum of all calibration values is:", total_sum)

if __name__ == "__main__":
    main()