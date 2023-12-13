students = [("Squidward", "F", 60),
            ("Sandy", "A", "33"),
            ("Patrick", "D", "36"),
            ("Mr. Krabs", "C", "78")]

grade = lambda grades:grades[1] # columnn two
students.sort(key=grade)
 
for i in students:
    print(i)