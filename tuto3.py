#! /usr/bin/env python

# String operates? Wtf does that even mean?

def browseString(s):
    ''' (str) -> None

    >>> browseString('chi')
    c
    h
    i
    '''
    for c in s:
        print c



def cutString(s, delim):
    ''' (str, char) -> list of str

    Cut s according to the delimiter delim and return a list of the resulting
    strings

    >>> cutString("this_is_a_test", "_")
    ['this', 'is', 'a', 'test']
    '''
    # This is kinda stupid
    return s.split(delim)



def stringToWords(s):
    ''' (str) -> list of str

    Cut the string s into words

    >>> stringToWords("this is a test")
    ['this', 'is', 'a', 'test']
    '''
    # Yeah maybe too easy is a real thing
    return cutString(s, " ")



def indexString(s):
    ''' (str) -> dict

    Returns a dictionary where keys are words in s and values are number of
    occurences of each word in s.

    >>> indexString("This is not fun. Not fun at all.")
    
    '''
    d = {}
    for word in stringToWords(s):
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d







if __name__ == '__main__':
    import doctest
    res = doctest.testmod()
    print res


