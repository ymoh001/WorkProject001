# function that computes the average of a list of numbers
def average(numbers):
    return sum(numbers) / len(numbers)

#implement the function using a splitted list from the input of user
def main():
    numbers = [float(i) for i in input("Enter numbers separated by spaces: ").split()]
    print("The average is:", average(numbers))

# call the main function
if __name__ == "__main__":
    main()