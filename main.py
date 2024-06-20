def calculate_area_of_rectangle(length, width):
    """
    Calculate and print the area of a rectangle

    Parameters
    ----------
    length (int): The length of the rectangle. Must be a positive integer
    width (int): The width of the rectaingle. Must be a positive integer

    Returns
    --------
    int: The area of the rectangle

    Examples:
    --------
    >>> calculate_area_of_rectangle(2,3)
    6
    >>> calculate_area_of_rectangle(-15.5,2.6)
    Invalid
    >>> calculate_area_of_rectangle(0, 0)
    0
    >>> calculate_area_of_rectangle(8,7)
    56
    >>> calculate_area_of_rectangle(15,10)
    150
    """
    return length * width

# Ask user to enter length and width
length = int(input('Enter the length: '))
width = int(input('Enter the width: '))

# Call the function
area = calculate_area_of_rectangle(length, width)
print(f'The area of the rectangle is: {area}')

# If this script is executed,
# run the doctests to validate the examples in the docstring
if __name__ == "__main__":
    import doctest
    doctest.testmod()