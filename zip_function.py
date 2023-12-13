usernames = [
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen", "Ivy", "Jack",
    "Kelly", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tina",
    "Ursula", "Victor", "Wendy", "Xander", "Yara", "Zane", "Sophia", "Henry", "Emily", "Daniel",
    "Ava", "James", "Sophie", "Lucas", "Ella", "Benjamin", "Luna", "Oliver", "Stella", "William",
    "Nova", "Ethan", "Chloe", "Alexander", "Mila", "Michael", "Aria", "Emma", "Logan", "Harper",
    "Jacob", "Avery", "Aiden", "Scarlett", "Elijah", "Zoe", "Matthew", "Evelyn", "Lucas", "Layla",
    "Mason", "Madison", "Sebastian", "Grace", "Carter", "Riley", "Jayden", "Penelope", "Wyatt", "Aurora",
    "Luke", "Sofia", "Jayce", "Bella", "Dylan", "Hannah", "Gabriel", "Aaliyah", "Nathan", "Nora",
    "Isaac", "Victoria", "Owen", "Skylar", "Levi", "Eleanor", "Aaron", "Claire", "Connor", "Lily",
    "Julian", "Amelia", "Christopher", "Ellie", "Josiah", "Abigail", "Lincoln", "Ariana", "Hudson", "Maya",
    "Nicholas", "Addison", "Thomas", "Elizabeth", "Samuel", "Leah", "John", "Audrey", "Madison", "Sebastian", "Grace", "Carter", "Riley", "Jayden", "Penelope", "Wyatt", "Aurora",
    "Luke", "Sofia", "Jayce", "Bella", "Dylan", "Hannah", "Gabriel", "Aaliyah", "Nathan", "Nora",
    "Isaac", "Victoria", "Owen", "Skylar", "Levi", "Eleanor", "Aaron", "Claire", "Connor", "Lily",
    "Julian", "Amelia", "Christopher", "Ellie", "Josiah", "Abigail", "Lincoln", "Ariana", "Hudson", "Maya",
    "Nicholas", "Addison", "Thomas", "Elizabeth", "Samuel", "Leah", "John", "Audrey"
]

# Creating corresponding passwords for each name (just for illustration purposes)
# Please note: These passwords are NOT secure and are just placeholders
passwords = [
    "password1", "pass1234", "abc123", "securePW", "qwerty", "letmein", "p@ssw0rd", "hello123", "testpass",
    "password123", "iloveyou", "welcome", "admin", "changeme", "12345678", "password", "qwerty123", "access",
    "pass", "abc1234", "password!", "123456", "login", "pass123", "admin123", "welcome1", "secret", "root",
    "letmein1", "123456789", "12345", "letmein123", "pass123!", "welcome123", "qwerty123!", "admin123!", "password!",
    "pass12345", "password1!", "1234567890", "password12", "1234567", "test123", "qwerty1", "password123!", "123456789a",
    "password1234", "123456789!", "qwerty1234", "passw0rd", "password12345", "password12345!", "1234567890a", "qwertyuiop",
    "password1234!", "qazwsx", "123123", "qwertyui", "adminadmin", "111111", "password1@3", "1234567a", "iloveyou123",
    "zxcvbnm", "1234567890!", "1234", "zaq1zaq1", "password123456", "123", "pass123456", "passw0rd123", "p@ssw0rd1",
    "123qwe", "123456789qwe", "password1234567", "qwe123", "123qwe!", "password12345678", "password@123", "q1w2e3",
    "qweasd", "asdfgh", "1qaz2wsx", "pass1234!", "qweasdzxc", "qwerty12345", "password@1", "1q2w3e4r",
    "admin@123", "1qazxsw2", "1q2w3e", "zxcvbn", "11111111", "zaqwsx", "1234qwer", "abcd1234", "pass@123",
    "123qweasd", "pass1234@",
]

emails = [
    f"{name.lower()}@example.com" for name in usernames
]
users = zip(usernames, passwords, emails)
for i in users:
    print(i)