def words_in_file(fileName):
    with open(fileName, 'r') as file:
        word_count = 0
        words =  file.read().split()
        for word in words:
            word_count += 1
        print(f"Word frequency is: {word_count}")
        

words_in_file("geek.txt")


