name = (input("What is the answer to life, the universe, and everything?"))
match name:
    case '42':
        print ("yes")
    case "fourty_two":
        print ("yes")
    case _:
        print ("Heck no brochaco")
