class Member:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

class Post:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def __str__(self):
        return self.title
