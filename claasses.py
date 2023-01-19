import datetime
# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def __str__(self):
#         return f'Brand: {self.brand}, Model: {self.model}, Price: {self.price}'

# laptop1 = Laptop("MSI", "Leopard", 1300)
# laptop2 = Laptop("ASUS", "zenbook", 990)
# laptop3 = Laptop("Lenovo", 'thinkpad', 499)
# print(laptop1)
# print(laptop2)
# print(laptop3)

# class SoccerPlayer:
#     goals=0
#     assists=0

#     def __init__(self, name, surname, club):
#         self.name = name
#         self.surname = surname
#         self.club = club
#         SoccerPlayer.goals = 0
#         SoccerPlayer.assists = 0

#     def score(self, goals=1):
#         self.goals += goals
    
#     def make_assist(self, assists=1):
#         self.assists += assists
    
#     def statistics(self):
#         print(f"Surname: {self.surname}, Name: {self.name}, Goals: {self.goals}, Assists {self.assists}")

# player1 = SoccerPlayer('Leo', "Messi", "PSG")
# player1.score(700)
# player1.make_assist(500)
# player1.statistics()

class Person:
    def __init__(self, first_name, last_name, personal_id):
        self.first_name = first_name
        self.last_name = last_name
        self.personal_id = personal_id
    
    def full_name(self):
        return self.first_name + self.last_name
    def gender(self):
        if self.personal_id[0] == "3" or self.personal_id[0] == "5":
            return 'man'
        elif self.personal_id[0] == "4" or self.personal_id[0] == "6":
            return 'woman'
        else:
            return "wrong first personal id number"
    
    def birthday(self):
        year = self.personal_id[1:3]
        month = self.personal_id[3:5]
        day = self.personal_id[5:7]
        day_of_birth = f"{day}-{month}-{year}"
        return day_of_birth
    
    def is_adult(self):
        if self.personal_id[0] == '3' or self.personal_id[0] == "4":
            year = f'19{self.personal_id[1:3]}'
        if self.personal_id[0] == '5' or self.personal_id[0] == "6":
            year = f'20{self.personal_id[1:3]}'    
        data = datetime.datetime.now()
        age = int(data.year) - int(year)
        if age >= 18:
            return True
        else:
            return False
    
katja = Person("Jekaterina", "Shashkina", "60605112215")

print(katja.gender())
print(katja.birthday())
print(katja.is_adult())

class Student:
    def __init__(self,  first_name, last_name, group, age):
        self.name = first_name + " " + last_name
        self.group = group
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.group}, {self.age}"

student1 = Student("Ivan", "Ivanov", "JKITP21", 21)
student2 = Student("Petr", "Sokolov", "JKTPV22", 16)
student3 = Student("Anastassia","Petrova", "JKITP21", 22)
student4 = Student("Marina", "Jermakova", "JKITP21", 33)
student5 = Student("Inna", "Smirnova", "OKPOK22", 16)
student6 = Student("Irina", "Marinina", "OKPOK22", 18)
student7 = Student("Anna","Shishova", "JKTPV22", 16)
student8 = Student("Arina","Samohina", "JKTPV22", 19)
student9 = Student("Olga","Koroljova", "JKTPV22", 18)
student10 = Student("Martin","Bro", "JKITP21", 17)
students = [student1, student2, student3,student4, student5, student6, student7, student8, student9, student10]
print(students[0].group)
count = 0
for i in students:
    if i.age < 20:
        print(i)
group_list = []   
for i in students:
    group_list.append(i.group)

unique_group_list = set(group_list)
for i in range(len(unique_group_list)):
    for j in students:
        if unique_group_list[i] == j.group
print(unique_group_list)

# print(young_list)