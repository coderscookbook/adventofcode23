# import modules

# create variables
answer = 0
file_input_path = '../puzzle-inputs/puzzle1-input.txt'

# open input file
with open(file_input_path, 'r') as file:
# for each line in the file:
    count = 1
    for line in file:
    # get first digit
        print(count, line.strip())
        count = count + 1
    # get last digit 
    # concatenate the digits to create new number
    # add new number to answer

