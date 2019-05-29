answer = raw_input ("Are you an Environmentalist? (yes/no) ")

if answer.lower().strip() == "yes":

    answer = raw_input ("You have a wild house party. Bottles and rubbish everywhere! Would you still recycle? yes or no?").lower().strip()
    if answer == "yes":
        answer = raw_input ("You're commited. So would you bother your friends to do the same?")

        if answer == "yes":
            print ("Pefect! Looks like you're one of us!")
        else:
            print ("Ow come on, I'm sure they are not that drunk!")

    else:
        answer = raw_input ("ah come on, it doesn't take that long. What if your parents were there to help you?")

        if answer == "yes":
            print ("I knew it! Lazzzy")
        else:
            print ("No hope for you...")

elif answer.lower().strip() == "no":
    print ("Ah you're no fun!")
