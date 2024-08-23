
file_path = "geek.txt"

line_list = []

with open (file_path, 'r') as file:
    for line in file:
        line_list.append(line)

print(line_list)