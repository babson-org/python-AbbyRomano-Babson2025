#flatten nested list
def flatten_list(data):
    if data == []:
        return []
    
    first = data[0]
    rest = data[1:]

    if isinstance(first, list):
        return flatten_list(first) + flatten_list(rest)
    else:
        return [first] + flatten_list(rest)

print(flatten_list([1, [2, [3, 4], 5], 6]))  # Should return [1, 2, 3, 4, 5, 6]

#convert integer to binary 
#n%2 gives last binary digit

def to_binary(n):
    if n < 2:
        return str(n)
    else:
        return to_binary(n//2) + str(n % 2)

print(to_binary(10))  # Should print 1010

#palindrom checker
def is_palindrome(s):
    #convert all letters to lowercase and assign to variable s
    s = s.lower()
    #if length of string is 0 or 1, return True because either '' or single letter so has to be palindrom
    if len(s) <= 1:
        return True
    #check if first and last letters are the same, if not return False, cannot be a palindrome
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])

print(is_palindrome("Racecar"))  # Should print True
