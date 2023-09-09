# collect five username and password into a list of dictionary
# example
profile = []
num = 0
while num<=5:
    username = input("username: ")
    profile.append({username}) 
    print(username)
    num += 1

print(profile)