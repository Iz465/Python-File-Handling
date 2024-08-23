def file_read(fname, nlines):
    with open(fname) as f:
       number = 0
       for line_num in range(nlines):
            if number < nlines:
                line = f.readline()
                number += 0   
            print(line, end = '')

file_read('geek.txt', 3) # Will read the first three lines of the file.
