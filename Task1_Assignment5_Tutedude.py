marks_dictionary={'Mohan':90,'Rohan':20,'Alice':39,'Shane':47,'Abdul':67}
a= input("Enter the student's name: ")
if a in marks_dictionary:
    print(a+"'s marks:", marks_dictionary.get(a))
else:
    print("Student not found.")
