'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # wl contains the length of our word; 
    # use this for adjusting workspace
    wl = len(word)
    # if wl is less than 2 (the length of 'th') result will be 0
    if wl < 2:
        return 0
    # otherwise, check the first two index positions to match against th
    # if true return 1, and then run recursion on the string again, 
    # starting at the next index in the string
    if word[:2] == 'th':
        return 1 + count_th(word[1:])
    # if its not true, we just run recursion from the same point, and dont return extra value
    else:
        return count_th(word[1:])
