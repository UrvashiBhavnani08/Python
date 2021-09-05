from datetime import datetime
print("What do you want me to do?")
user=input("Please enter what you want to do?")
if user == "game":
    print("Here is truth and Dare.")
    game=input("Which one you want to choose...Truth or Dare?")
    if game == "Truth" or "truth":
        q1=input("What is your name?")
        if q1 == "Urvashi" or "urvashi" or "uru":
            print("Well done you are telling the truth.")
        else:
            print("Noooo...Your are telling false..who are you???")
        print("Okk...Coming to the next question...")
        q2=input("What is your favourite food?")
        if q2 == "Don't know" or "don't know":
            print("Ohh..I got you...You are a programmer or coder..Am I right??")
        print("I know you are getting bore....")
    else:
        print("You have choosen dare...and you have to do whatever I will say...")
        ans=input("What is the exact time you know with seconds I want to know because I'm very busy....")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if ans == current_time:
            print("Yess you are right...")
        else:
            print("Your answer is incorrect...")
    g2=input("Which one you will choose??..Truth or Dare..Tell me..")
    if g2=="Truth" or "truth":
        print("Great choice...")
        que1=input("What is your secret..Tell me I won't tell anyone...")
        print("Fine I don't know that you are telling truth or not...fine let's move ahead...")
        que2=input("What is your favourite hobby..??")
        if que2 == "Drawing" or "drawing" or "painting" or "Painting" or "to paint":
            print("Yess you are telling the truth..I'm sure you are enjoying it...")
    elif g2=="Dare" or "dare":
        print("You have dare you have to do whatever I will say...")
        print("Just play a song and get relax..I want to hear a song....listen nice one..")
        print("Let's move ahead....")
    else:
        print("Enter a valid choice...")

print("Bye for now..")
