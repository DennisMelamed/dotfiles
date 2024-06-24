
names = []
emails = []
institutions = []
while True:
    name = input("Author Full Name (q to end entering authors): ")
    if name == 'q':
        break
    names.append(name)
    email = input("Author email: ")
    emails.append(email)
    institutions = input("Author Institution, comma separated for multiple names").split(",")
conference_name = input("Conference Name: ")
conferences_abbrevs = input("Conference abbreviations (any you can think of, comma separated): ").split(",")



