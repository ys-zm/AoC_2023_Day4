import argparse
import sys

def get_numbers(line):
    # split at ' ' to separate numbers, returns a list of strings
    split_numbers = line.split()
    # initialize numbers list
    numbers = []
    for n in split_numbers:
        try:
            numbers.append(int(n)) # returns an exception if conversion fails
        except ValueError:
            print(f"Warning: Unable to convert '{n}' to integer.")
    return numbers


def calc_matches(n1, n2):
    matches = 0
    # matches = sum(1 for item in list1 if item in list2)
    for item in n1:
        if item in n2:
            matches += 1
    return matches

def check_cards(file):
    points = 0
    for card in file:
        # remove the title and strip white spaces
        trim_line = card[card.find(":") + 1:len(card)].strip()

        # split remainder at '|' char
        split_line = trim_line.split('|')
       
       # store numbers into a list of ints
        winning_numbers = get_numbers(split_line[0])
        own_numbers = get_numbers(split_line[1])
        matches = calc_matches(winning_numbers, own_numbers);
        if matches:
            points = points + 2 ** (matches - 1) # 2^0 = 1, so we use len(matches) - 1
    print("points: ", points)


        
def main(input_file):
    try:
        with open(input_file, 'r') as file:
            check_cards(file)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# calling main function
if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python script.py <input_file>")
