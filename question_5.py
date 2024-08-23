import random

# read random line from file

def choose_random_line(file_name):
    lines = open(file_name).read().splitlines() # split lines will give you the amount of lines in the file.
    # lines is now a list i think. As a list it holdes each line in a different index
    return random.choice(lines)
    
        

       

        

        


print(choose_random_line('geek_combined.txt'))