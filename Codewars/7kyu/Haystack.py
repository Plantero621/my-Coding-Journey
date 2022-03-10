haystack =['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']

def find_needle(haystack):
    return "found the needle at position {}".format(haystack.index("needle"))

print(find_needle(haystack))