''' Exercise #5. Computational Thinking and Programming.'''
#########################################
# Question 1 - do not delete this comment
#########################################
def is_char_in_str(s1, c1):
    return c1 in s1
#########################################
# Question 2 - do not delete this comment
#########################################
def is_in_range(lst2, a, b):
    for i in lst2:
        if not (i>a and i<b):
            return False
    return True
#########################################
# Question 3 - do not delete this comment
#########################################
def upper_list_strings(lst3):
    return [word.upper() for word in lst3]
#########################################
# Question 4 - do not delete this comment
#########################################
def log10_list(lst4):
    import math
    return [math.log10(i) for i in lst4]
#########################################
# Question 5 - do not delete this comment
#########################################
def is_palindrom(s5):
    x=0
    while x < len(s5)/2:
        if s5[x] == s5[-x-1]:
            x+=1
        else:
            return False
    return True


