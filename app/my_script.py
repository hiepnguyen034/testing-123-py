def enlarge(i):
    return i * 100000

if __name__ == "__main__": # "if this script is run from the command-line, then ..."
    original_number = int(input("Please select a number to be enlarged (e.g. 400): "))
    print("You chose: ", original_number)
    bigger_number = enlarge(original_number)
    print("Enlarged number is: ", bigger_number)