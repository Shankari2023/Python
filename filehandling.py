#######File Handling

file = open("E:\\Python\\sample.txt","r")   #(r"E:\Python\sample.txt","r")
for i in file:
    print(i)
file.close()


###Write -----> if file is present, it will delete the current file and create a new one
### if file is not present, it will creates a new one
file = open("E:\\Python\\demo.txt","w")     #also we can write as (r"E:\Python\demo.txt","w")
file.write("hello\nwelcome")
file.close()

####Append -------> add content to the existing file
file = open("E:\\Python\\demo.txt","a")     #(r"E:\Python\demo.txt","a")
file.write("\nto\ntoday's\nclass")
file.close()


#####pandas
import pandas as pd
data = pd.read_csv("E:\\Python\\Book1.csv")
data


