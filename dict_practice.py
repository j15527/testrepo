course = {
    'name': "Python for everybody",
    'students': 100_000,
    'length': 8.5,
    'leassons': ['Strings', 'Lists', 'Dictonaries', 'if_statments']
}

users = {
    'john': "love123",
    'mike': 'mycat99'
}

group = ('Mike', 'John','Dan')


username = input("type ur username: ")
pw = users.get(username)
password = input("enter ur password: ")

if users.get(username) == password:
    print("Yes")
else:
    print("no")
