# Creating a student list with names and IDs
students = ["Elizabeth (ID : 20)", "Kwanele (ID : 27)", "Sipho (ID : 15)", "Cayden (ID : 24)"]
print(students)

# Inserting 5 students to the beginning of the list
students.insert(0, "Claire (ID : 06)")
students.insert(0, "Mitchelle (ID : 56)")
students.insert(0, "Phil (ID : 12)")
students.insert(0, "Cameroon (ID : 567)")
students.insert(0, "Lilly (ID : 2225)")
print(students)

# Adding John to the last index of the list
students.append("John (ID : 67)")
print(students)


# Checking if Elizabeth is an element of the students list

if "Elizabeth (ID : 20)" in students:
    index_Elizabeth = students.index("Elizabeth (ID : 20)")
    index_Elizabeth != -1 and index_Elizabeth < len(students) - 1
    del students[index_Elizabeth + 1]  

else:
    print("Elizabeth not found in the list.")

print(students)

    


