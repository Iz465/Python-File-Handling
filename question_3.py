def list_to_file(list1, file_name):
    with open(file_name, 'a') as file:
            list_len = len(list1)
            for i in range(list_len):
                file.write(list1[i])
                  
          

        


list1 = ["hello", 'how', "cold", 'is', 'it']

list_to_file(list1, "geek.txt")

