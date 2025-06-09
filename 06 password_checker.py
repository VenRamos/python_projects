def password_check():
    psswrd = None
    password = "Hello_world"
    tries = 0

    while psswrd != password:
        psswrd = input("Enter Password: ")
        tries = tries + 1
        if psswrd == password:
            return "Password correct!"
        if tries == 1:
            print("Try again.")
            print("2 attempts left")
        elif tries == 2:
            print("Try again.")
            print("1 attempt left")
        elif tries == 3:
            print("Password limit reached.")
            break


trial = password_check()
