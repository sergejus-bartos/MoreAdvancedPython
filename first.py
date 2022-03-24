import pandas
import os

my_path = "C:/Users/serge/projects/MoreAdvancedPython/"
my_file = "data.csv"
the_file = my_path + my_file

if os.path.exists(the_file):
    data = pandas.read_csv(the_file)
    print(data.mean()["st1"])
else:
    print("no file")
    
print(data)



