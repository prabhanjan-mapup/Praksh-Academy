first_name = input("Enter your first name = ")
last_name = input("Enter your last name = ")
print(first_name, last_name)
text_to_write = "\n"+first_name+" "+last_name
file = open("/Users/prabhanjan/Downloads/PrakshAcademy/Praksh-Academy/Session 17_Memory_That_Survives/data.txt","a")
file.write(text_to_write)
file.close()

with open("/Users/prabhanjan/Downloads/PrakshAcademy/Praksh-Academy/Session 17_Memory_That_Survives/data.txt","a") as file:
    file.write("Adding new dummy data")
option = input("Enter 1 to see the data in the file = ")
if option == "1":
    file = open("/Users/prabhanjan/Downloads/PrakshAcademy/Praksh-Academy/Session 17_Memory_That_Survives/data.txt","r")
    data=file.read()
    file.close()
    print(data)

