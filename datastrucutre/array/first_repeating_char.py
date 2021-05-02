# Find the first character in a string without using extra space
# With extra space its simple. Just check for the element in a hash map
# If present, then it is the recurrent char

# Without extra space idea -

def first_recurrence(s):
    checker = 0 
    pos = 0
    for i in s:
        val = ord(i) - ord('a')
        if (checker & (1 << val) > 0):
            return i
        checker = checker | (1 << val)
        pos += 1
    return -1
