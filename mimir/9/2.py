'''
Write a function named is_float(s) that takes one argument that is a string.  It returns True if string s represents a floating point value and returns False otherwise.  You are required to use try-except.  The basic concept is to "try" to convert string s to a float and if it succeeds, return True, but if it fails (that is, an exception is raised), return False.  Note that float() raises a  ValueError exception.
'''
def is_float(value: str):
    try:
        float(value)
        return True
    except:
        return False
# is_float function definition goes here

# Example usage
print(is_float('3.45'))
print(is_float('abc'))

