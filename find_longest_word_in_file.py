
def longest_word(file):
    with open(file, 'r') as infile:
        words = infile.read().split() # splitting every word when a space happens
    
    max_len = len(max(words, key = len))

    return [word for word in words if len(word) == max_len]


print(longest_word("geek.txt"))
        