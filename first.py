
from tkinter import W



my_path1 = "C:/Users/serge/projects/MoreAdvancedPython/test1.txt"
my_path2 = "C:/Users/serge/projects/MoreAdvancedPython/test2.txt"

with open(my_path1, "r") as my_file1:
    content = my_file1.read()
    
with open(my_path2, "a+") as my_file2:
     my_file2.write(content)
     my_file2.seek(0)
     my_file2.write(content)
     my_file2.seek(0)
     my_file2.write(content)

    



