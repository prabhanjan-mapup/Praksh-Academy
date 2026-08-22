class Person:
    def __init__(self, name, age,mob_no):
        self.name = name
        self.age = age
        self.__mob_no = mob_no#private variable

    def get_mobno(self):
        print(self.__mob_no)

    def update_mobno(self,mob_no):
        self.__mob_no = mob_no

    def __secrets(self):
        print("this is my top secret and it should not be accessible")
    
    def reveal_secrets(self):
        self.__secrets()

person_1 = Person("Aanya", "Goyal","7620983941")
print(person_1.name)
print(person_1.age)
print("Below number is printed by a function)")
person_1.get_mobno()
# print(person_1.__mob_no)
person_1.update_mobno('1234567899')
person_1.get_mobno()
password = input("Enter the password to access secret data = ")
if password == 'abcd123':
    person_1.reveal_secrets()
else: 
    print("You have entered wrong creds")