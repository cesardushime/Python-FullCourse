# filter() = creates a collection of elements from an iterable for which a function returns
# filter(function, iterable)

friends = [
    ("Alice", 25), ("Bob", 30), ("Charlie", 16), ("David", 28), ("Emma", 14),
    ("Frank", 27), ("Grace", 18), ("Henry", 29), ("Ivy", 22), ("Jack", 33),
    ("Katie", 12), ("Liam", 32), ("Mia", 29), ("Noah", 17), ("Olivia", 30),
    ("Parker", 19), ("Quinn", 28), ("Ryan", 26), ("Sophia", 34), ("Tyler", 15),
    ("Uma", 21), ("Victor", 16), ("Wendy", 20), ("Xander", 13), ("Yara", 31),
    ("Zach", 23), ("Amelia", 18), ("Benjamin", 25), ("Chloe", 16), ("Daniel", 27),
    ("Ella", 14), ("Finn", 32), ("Gemma", 29), ("Harrison", 17), ("Isabella", 30),
    ("Jacob", 19), ("Kayla", 28), ("Landon", 26), ("Mila", 34), ("Nathan", 15),
    ("Oliver", 21), ("Peyton", 16), ("Quincy", 20), ("Riley", 13), ("Samantha", 31),
    ("Theo", 23), ("Ursula", 18), ("Vincent", 25), ("Willa", 16), ("Xavier", 27),
    ("Yasmine", 14), ("Zane", 32), ("Ava", 29), ("Blake", 17), ("Caleb", 30),
    ("Daisy", 19), ("Ethan", 28), ("Freya", 26), ("George", 34), ("Hannah", 15),
    ("Isla", 21), ("Jackson", 16), ("Kylie", 20), ("Lucas", 13), ("Molly", 31),
    ("Nolan", 23), ("Olivia", 18), ("Preston", 25), ("Quinn", 16), ("Ruby", 27),
    ("Seth", 14), ("Talia", 32), ("Ulysses", 29), ("Violet", 17), ("Wyatt", 30),
    ("Xena", 19), ("Yuri", 28), ("Zara", 26), ("Adam", 34), ("Bella", 15),
    ("Carter", 21), ("Diana", 16), ("Eli", 20), ("Fiona", 13), ("Gavin", 31),
    ("Hazel", 23), ("Ian", 18), ("Jade", 25), ("Kian", 16), ("Luna", 27),
("Katie", 12), ("Liam", 32), ("Mia", 29), ("Noah", 17), ("Olivia", 30),
    ("Parker", 19), ("Quinn", 28), ("Ryan", 26), ("Sophia", 34), ("Tyler", 15),
    ("Uma", 21), ("Victor", 16), ("Wendy", 20), ("Xander", 13), ("Yara", 31),
    ("Zach", 23), ("Amelia", 18), ("Benjamin", 25), ("Chloe", 16), ("Daniel", 27),
    ("Ella", 14), ("Finn", 32), ("Gemma", 29), ("Harrison", 17), ("Isabella", 30),
    ("Jacob", 19), ("Kayla", 28), ("Landon", 26), ("Mila", 34), ("Nathan", 15),
    ("Oliver", 21), ("Peyton", 16), ("Quincy", 20), ("Riley", 13), ("Samantha", 31),
    ("Theo", 23), ("Ursula", 18), ("Vincent", 25), ("Willa", 16), ("Xavier", 27),
    ("Yasmine", 14), ("Zane", 32), ("Ava", 29), ("Blake", 17), ("Caleb", 30),
    ("Daisy", 19), ("Ethan", 28), ("Freya", 26), ("George", 34), ("Hannah", 15),
    ("Isla", 21), ("Jackson", 16), ("Kylie", 20), ("Lucas", 13), ("Molly", 31),
    ("Nolan", 23), ("Olivia", 18), ("Preston", 25), ("Quinn", 16), ("Ruby", 27),
    ("Seth", 14), ("Talia", 32), ("Ulysses", 29), ("Violet", 17), ("Wyatt", 30),
    ("Xena", 19), ("Yuri", 28), ("Zara", 26), ("Adam", 34), ("Bella", 15),
    ("Carter", 21), ("Diana", 16), ("Eli", 20), ("Fiona", 13), ("Gavin", 31),
    ("Hazel", 23), ("Ian", 18), ("Jade", 25), ("Kian", 16), ("Luna", 27),
("Katie", 12), ("Liam", 32), ("Mia", 29), ("Noah", 17), ("Olivia", 30),
    ("Parker", 19), ("Quinn", 28), ("Ryan", 26), ("Sophia", 34), ("Tyler", 15),
    ("Uma", 21), ("Victor", 16), ("Wendy", 20), ("Xander", 13), ("Yara", 31),
    ("Zach", 23), ("Amelia", 18), ("Benjamin", 25), ("Chloe", 16), ("Daniel", 27),
    ("Ella", 14), ("Finn", 32), ("Gemma", 29), ("Harrison", 17), ("Isabella", 30),
    ("Jacob", 19), ("Kayla", 28), ("Landon", 26), ("Mila", 34), ("Nathan", 15),
    ("Oliver", 21), ("Peyton", 16), ("Quincy", 20), ("Riley", 13), ("Samantha", 31),
    ("Theo", 23), ("Ursula", 18), ("Vincent", 25), ("Willa", 16), ("Xavier", 27),
    ("Yasmine", 14), ("Zane", 32), ("Ava", 29), ("Blake", 17), ("Caleb", 30),
    ("Daisy", 19), ("Ethan", 28), ("Freya", 26), ("George", 34), ("Hannah", 15),
    ("Isla", 21), ("Jackson", 16), ("Kylie", 20), ("Lucas", 13), ("Molly", 31),
    ("Nolan", 23), ("Olivia", 18), ("Preston", 25), ("Quinn", 16), ("Ruby", 27),
    ("Seth", 14), ("Talia", 32), ("Ulysses", 29), ("Violet", 17), ("Wyatt", 30),
    ("Xena", 19), ("Yuri", 28), ("Zara", 26), ("Adam", 34), ("Bella", 15),
    ("Carter", 21), ("Diana", 16), ("Eli", 20), ("Fiona", 13), ("Gavin", 31),
    ("Hazel", 23), ("Ian", 18), ("Jade", 25), ("Kian", 16), ("Luna", 27),
("Katie", 12), ("Liam", 32), ("Mia", 29), ("Noah", 17), ("Olivia", 30),
    ("Parker", 19), ("Quinn", 28), ("Ryan", 26), ("Sophia", 34), ("Tyler", 15),
    ("Uma", 21), ("Victor", 16), ("Wendy", 20), ("Xander", 13), ("Yara", 31),
    ("Zach", 23), ("Amelia", 18), ("Benjamin", 25), ("Chloe", 16), ("Daniel", 27),
    ("Ella", 14), ("Finn", 32), ("Gemma", 29), ("Harrison", 17), ("Isabella", 30),
    ("Jacob", 19), ("Kayla", 28), ("Landon", 26), ("Mila", 34), ("Nathan", 15),
    ("Oliver", 21), ("Peyton", 16), ("Quincy", 20), ("Riley", 13), ("Samantha", 31),
    ("Theo", 23), ("Ursula", 18), ("Vincent", 25), ("Willa", 16), ("Xavier", 27),
    ("Yasmine", 14), ("Zane", 32), ("Ava", 29), ("Blake", 17), ("Caleb", 30),
    ("Daisy", 19), ("Ethan", 28), ("Freya", 26), ("George", 34), ("Hannah", 15),
    ("Isla", 21), ("Jackson", 16), ("Kylie", 20), ("Lucas", 13), ("Molly", 31),
    ("Nolan", 23), ("Olivia", 18), ("Preston", 25), ("Quinn", 16), ("Ruby", 27),
    ("Seth", 14), ("Talia", 32), ("Ulysses", 29), ("Violet", 17), ("Wyatt", 30),
    ("Xena", 19), ("Yuri", 28), ("Zara", 26), ("Adam", 34), ("Bella", 15),
    ("Carter", 21), ("Diana", 16), ("Eli", 20), ("Fiona", 13), ("Gavin", 31),
    ("Hazel", 23), ("Ian", 18), ("Jade", 25), ("Kian", 16), ("Luna", 27)


    # Each tuple format: ("name", age)
]

age = lambda data:data[1]>=18
drinking_buddies = list(filter(age, friends))
drinking_buddies_sorted = sorted(drinking_buddies, key=lambda x:x[1])

for i in drinking_buddies_sorted:
    print(i)