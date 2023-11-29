def main():
    user = input()
    user_input = convert(user)
    print(user_input)

def convert(user):
    user = user.replace(":)","🙂")
    user = user.replace(":(","🙁")
    return user

main()
