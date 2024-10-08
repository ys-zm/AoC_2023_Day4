import sys

# returns a list
def get_numbers(line):
    return [n for n in line.split() if n]

def check_cards(file):
    points = 0
    for card in file:
        # skip empty lines
        if not card.strip():
            continue 
        # remove the title and strip white spaces
        trim_line = card[card.find(":") + 1:len(card)].strip()

        split_line = trim_line.split('|')
        if len(split_line) != 2:
            continue 
        winning_numbers = get_numbers(split_line[0])
        own_numbers = get_numbers(split_line[1])
        n_matches = len(set(winning_numbers) & set(own_numbers))
        if n_matches:
            points += 2 ** (n_matches - 1) # 2^0 = 1, so we use n_matches - 1
    return points
        
def main(input_file):
    try:
        with open(input_file, 'r') as file:
            print("Points:" , check_cards(file))
    except Exception as e:
        print(f"Error: {e}")

# calling main function
if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python script.py <input_file>")
