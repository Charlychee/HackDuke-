class User:
    def __init__(self, email, pwd, name, dob, diagnosis, purpose, contacts, profile):
        self.email = email
        self.pwd = pwd
        self.name = name
        self.dob = dob
        self.diagnosis = diagnosis
        self.purpose = purpose
        self.contacts = contacts
        self.profile = profile

    @property
    def __repr__(self):
        return "User('{}','{}','{}','{}','{}','{}','{}','{}')".format(self.email, self.pwd, self.name, self.dob, self.diagnosis, self.purpose, self.contacts,self.profile)

class Posts:
    def __init__(self, author, type, path, comments):
        self.author = author
        self.type = type
        self.path = path
        self.comments = comments
