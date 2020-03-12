filename = input("Put filename here: ")

try:
    with open(filename) as f:
        usernames = f.readlines()
        cnt = 0 
        for name in usernames:
            print("Line {}: {}".format(cnt, name.strip()))
            name = f.readline()
            cnt += 1
        line_check = int(input("Which line were you? "))
        if line_check < cnt:
            print("Hello " + usernames[line_check].strip())
        else:
            if input("Were you not on the list? (y/n) ") == 'n':
                current_user = input("Sorry!\nCould you give us a name to write down? ")
                f = open(filename, "a")
                f.writelines('\n')
                f.writelines(current_user)
                f.close()
                print(f"we're saved your username {current_user}")
    f.close()
except FileNotFoundError:
    with open(filename, 'w') as f:
        current_user = input("can't find file {}, give us a username to start the file: ".format(filename))
        f.writelines(current_user)
        print(f"We'll remember your username, {current_user} for your return!")
