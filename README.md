# Assignment_5
Task1:
Dictionary Definition: marks_dictionary = {'Mohan': 90, 'Rohan': 20, 'Alice': 39, 'Shane': 47, 'Abdul': 67}This line creates a dictionary named marks_dictionary where the keys are student names (e.g., 'Mohan', 'Rohan') and the values are their respective marks (e.g., 90, 20).
User Input: a = input("Enter the student's name: ") The program asks the user to enter a student's name and stores that input in the variable a. Checking if the Student's Name Exists:
if a in marks_dictionary: This line checks if the name entered by the user (stored in variable a) exists as a key in the marks_dictionary.
If the Name Exists (Found in Dictionary): print(a + "'s marks:", marks_dictionary.get(a)) If the student’s name is found in the dictionary, it prints the student's name along with their corresponding marks.
The marks_dictionary.get(a) retrieves the value (marks) associated with the key a (the student's name).
If the Name Does Not Exist: else: print("Student not found.") If the student’s name is not found in the dictionary, the program prints "Student not found." to inform the user.


Task2:
Creating the List: numbers = list(range(1, 11)) creates a list of numbers from 1 to 10 using the range() function.
Extracting the First Five Elements:extracted = numbers[:5] uses list slicing to get the first five elements from the list numbers.
Reversing the Extracted List: reversed_extracted = extracted[::-1] reverses the extracted list using slicing. The [::-1] slice step reverses the list.
Printing the Lists: The program then prints both the extracted list (the first five elements) and the reversed_extracted list (the reversed version of the first five elements).
