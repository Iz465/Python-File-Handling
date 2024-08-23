
def calculate_lines(file_name):
    with open(file_name, 'r') as file:
        line_amount = 0
        for line in file:
            line_amount += 1
        return line_amount

print(calculate_lines('geek.txt'))
