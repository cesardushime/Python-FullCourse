# sort() method = used with lisfts
# sort() function = used with iterables

students = ["Squidward", "Sandy", "Patrick", "Cesar", "Spongebob", "Mr. Kraabs"]

#students.sort()

sorted_students = sorted(students, reverse=True) # sorting in a reversed order

for i in sorted_students:
    print(i)