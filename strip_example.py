file = open('geek.txt', 'w')

text = "        this is the write command\n"

stripped_text = text.lstrip() #rstrip to remove spaces from the right side.
file.write(stripped_text)

file.close()


