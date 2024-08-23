def combine_files(file1, file2):
    with open('geek_combined.txt', 'a') as file:
        with open(file1, 'r') as file_1:
            for i in file_1:
                file.write(i)
        with open(file2, 'r') as file_2:
            for i in file_2:
                file.write(i)
            


combine_files('geek.txt', 'geek_1.txt')