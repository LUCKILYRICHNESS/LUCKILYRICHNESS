from random import choice
from time import sleep

person = 0
name = " "
ask_count = 0
name_not_found = 0
login = 0
logout = 0
if logout < 3:
    politeness = 14
elif 2 < logout < 5:
    politeness = 12
elif 4 < logout < 8:
    politeness = 9
else:
    politeness = 9


humour = False
friend_logged = False
logged = False

haha = ["Haha", "Hehe", "Hoho", "Hihi", "Mwahaha"]

jokes = ["I asked my French friend if she likes to play video games. She said, 'Wii.'",
         "The machine at the coin factory just suddenly stopped working, with no explanation. It doesn't make any cents!",
         "I was going to make myself a belt made out of watches, but then I realized it would be a waist of time.",
         "Did you hear about the auto body shop that just opened? It comes highly wreck-a-mended.",
         "Q. Why can't you run through a campground? "
         "A. You can only ran, because it's past tents.",
         "Shout out to the people who ask what the opposite of 'in' is.",
         "Q. What sound does a sleeping T-Rex make? "
         "A. A dino-snore.",
         "Why did the chicken cross the road? Well cancel that joke that one is lame."]

family = ["father", "mother", "sister"]

friends = ["aditya", "aditya malik"]

about_me_commands = ["tell me something about me", "who am i?", "about me", "do you know me?", "do you know me",
                     "who am i", "tell something about me"]

shut_up_commands = ["shut up", "shutup", "be quiet", "keep quiet", "quiet"]

who_made_you_commands = ["who made you", "who made you?", "who created you", "who created you?", "who is your creator",
                         "who is your creator?"]

system_apology_commands = ["apologize", "say sorry", "apologize to me"]

user_apology_commands = ["i'm sorry", "im sorry", "sorry", "forgive me", "apologies", "my bad"]

quit_commands = ["quit", "exit", "terminate", "shutdown", "shut down", "/quit"]

user_change_commands = ["change user", "log out", "i'm going", "switch user", "logout", "logoff", "log off", "/logout"]

user_greet_commands = ["hello", "hi", "hey", "hey!", "bonjour", "bonjour!", "hello!", "hi!", "namaste"]

commands_list_commands = ["/commands", "command"]

help_commands = ["help", "/help"]

name_commands = ["my name?", "what's my name?", "whats my name?", "my name is", "my name", "what's my name",
                 "whats my name", "name"]

admins_command_list_commands = ["admin's commands", "admin commands", "master commands"]

how_are_you_commands = ["how are you", "how are you?", "how are you doing", "how are you doing", "are you okay",
                        "are you okay?"]

jokes_commands = ["tell me a joke", "make me laugh", "say a joke", "a joke please", "joke", "jokes", "another joke",
                  "another one", "once more"]

not_funny_commands = ["poor joke", "bad joke", "you are humourless", "very bad jokes", "very poor jokes", "not funny,",
                      "bad one"]

funny_commands = ["good joke", "nice joke", "you are funny", "funny"]

how_are_you_user_replies_good = ["i'm fine", "i'm fine.", "i'm okay", "i'm okay.", "im fine", "im fine.", "im okay",
                                 "im okay.", "i'm good", "i'm good.", "im good", "im good.", "good", "fine"]

how_are_you_user_replies_bad = ["i'm not fine", "i'm not fine.", "i'm not okay", "i'm not okay.", "im not fine",
                                "im not  fine.", "im not okay", "im not okay.", "i'm not good", "i'm not good.",
                                "im not good", "im not good.", "not good", "not fine", "bad"]


commands_list = """
1. /command for a list of commands.
2. /help for help.
3. /logout if someone else wants to use.
4. /quit to quit. 

More to be created soon.
"""

admins_commands_list = """
1. /plans for plans.
"""

about_me = f"""
+{'-' * 114}+
| Hello!                                                                                                           |
| I'm a normal bot created in python.                                                                              |
| You can interact with me by saying some words. Try saying "Hello" or "Hi"! You can also converse with me!        |
| Also, I treat you according to how I recognise you. I can also tell something about you!                         |
|                                                                                                                  |
| Type "/commands" for a list of commands (without the apostrophes, obviously!)                                    |
| Have fun!                                                                                                        |
|                                                                                                                  |
| PS : I will obey you completely if you're close with my creator. But, if you aren't, you'd have to talk politely | 
| with me.                                                                                                         |
+{'-' * 114}+

Also, if this message appears crooked, try increasing the width of the window...
"""

plans = "To be added later."

greetings = ["Hello there!", "Hey!", "Hey there!", "Namaste!", "Bonjour, friend!"]

fa_greeting1 = "Oh, hello there! Nice to finally meet you!"
fa_greeting2 = "Hello, Amit! Hope you are doing fine!"
fa_greeting3 = "Hey, Dad!"
fa_greeting4 = "Hello Dad!"
fa_greeting5 = "Greetings, Amit!"

fa_greetings = [fa_greeting1, fa_greeting3, fa_greeting2, fa_greeting4, fa_greeting5]


mo_greeting1 = "Hello, Mom!"
mo_greeting2 = "Namaste, Mom!"
mo_greeting3 = "Hey!"

mo_greetings = [mo_greeting1, mo_greeting3, mo_greeting2]


sis_greeting1 = "Hello, Sanskrity!"
sis_greeting2 = "Hey!"

sis_greetings = [sis_greeting1, sis_greeting2]


system_apology_response = ["I'm sorry...", "Did I displease you? My bad, forgive me.", "Apologies.",
                           "Forgive me if I made a mistake...", "Did I do something wrong? I'm sorry..."]

how_are_you_response = ["I'm fine, how are you?",
                        "I'm good! What about you?",
                        "RAM's bit bugged up, rest is good! How are you?",
                        "I'm running as I'm supposed to, so I think that's good. Are you running as you're supposed to?"
                        ]

not_understood_response = ["I'm sorry, I don't get it.",
                           "I didn't understand.",
                           "I didn't get it.",
                           "I'm sorry, but I didn't get you.",
                           "I'm not programmed to understand that (yet).",
                           "Could you repeat it, please? I didn't get it.",
                           "I didn't get it. Maybe you made an error?",
                           "Pardon?",
                           "Did you spell it correctly? Or maybe I don't understand it (yet)."]

who_made_me_response = ["I was created by Ankit.",
                        "I was programmed by Ankit.",
                        "I was coded to life by Ankit.",
                        "My creator goes by the name Ankit."]


conv1 = "How may I help you?"
conv2 = "So.. What help may I be?"
conv3 = "What help can I be?"
conv4 = "How can I help you?"

convs = [conv1, conv2, conv3, conv4]


info_amit = f"""
You are Amit Kumar, Ankit's father. You have your business of software distribution and hardware repairs. 
More info coming as soon as soon as I'm given the info.
"""


info_bulbul = f"""
You are Ankit's mother.
More info coming as soon as soon as I'm given the info.
"""


info_ankit = f"""
You are Ankit Kumar, my creator. 
If you want more info, it will be password protected because if you really are Ankit, you won't be asking for more info.
"""


def start_greet():
    global login
    login += 1
    print(choice(greetings))
    sleep(1)


def greet_father():
    global login
    login += 1
    print(choice(fa_greetings))
    sleep(1)
    if logged:
        pass
    elif not logged:
        know_me = input("Do you want to know about me? (yes/no): ")
        if know_me.lower() == "yes":
            print(about_me)
        else:
            pass


def greet_mother():
    global login
    login += 1
    print(choice(mo_greetings))
    sleep(1)
    know_me = input("Do you want to know about me? (yes/no): ")
    if know_me.lower() == "yes":
        print(about_me)
    else:
        pass


def greet_sister():
    global login
    login += 1
    print(choice(sis_greetings))
    sleep(1)
    know_me = input("Do you want to know about me? (yes/no): ")
    if know_me.lower() == "yes":
        print(about_me)
    else:
        pass


def greet_stranger():
    global login
    login += 1
    global name
    print(f"Sorry, I don't know you (yet) or, to be accurate, your name isn't in my database. "
          f"Anyways, I will remember you name, {name.upper()}, for this session only.")
    sleep(1)
    if logged:
        pass
    elif not logged:
        know_me = input("Do you want to know about me? (yes/no): ")
        if know_me.lower() == "yes":
            print(about_me)
        else:
            pass


def greet_friend():
    know_me = input("Do you want to know about me? (yes/no): ")
    if know_me.lower() == "yes":
        print(about_me)
    else:
        pass


def startup_prank():
    global friend_logged
    print("Welcome!")
    sleep(2)
    print(f"But... You said your name was... {name.upper()}, right?")
    sleep(3)
    print("You are not authorised to run this program.")
    sleep(2.5)
    print("You dare ask why?")
    sleep(2)
    print(f"Banning {name.upper()} from further attempts to run this program.")
    sleep(2.5)
    print(f"Banned {name.upper()} successfully. Proceeding to shutdown.")
    sleep(1)

    print("Shutdown initiated.")
    sleep(1)

    print("Quitting in ")
    sleep(0.5)

    print(3)
    sleep(0.5)

    print(2)
    sleep(0.5)

    print(1)
    sleep(0.5)

    print("Program -- Terminated.")
    sleep(4)

    print("Did you think I would really do that! Haha! Pranked!")
    sleep(2)
    print("Apologies for low sense of humour, though, I'm still a computer at the end of the day.")
    sleep(2)

    friend_logged = True
    if logged:
        pass
    elif not logged:
        know_me = input("Do you want to know about me? (yes/no): ")
        if know_me.lower() == "yes":
            print(about_me)
        else:
            pass


start_greet()

while True:
    if ask_count == 0:
        print("May I have your name, please?")
    elif 4 > ask_count > 0:
        print("Your name, please.")
    elif ask_count == 4:
        print("Enter your real name, or this time program will self quit.")
    elif ask_count > 4:
        print("Self-Quitting in ")
        sleep(1)

        print(3)
        sleep(0.5)

        print(2)
        sleep(0.5)

        print(1)
        sleep(0.5)

        print("Program -- Terminated.")

        quit()
    name = input("> ")
    if name.lower() == "amit" or name.lower() == "amit kumar":
        person = "father"
    elif name.lower() == "annapurna":
        person = "mother"
    elif name.lower() == "annanpurna":
        person = "mother"
    elif name.lower() == "bulbul":
        person = "mother"
    elif name.lower() == "sanskrity" or name.lower() == "sanskriti":
        person = "sister"
    elif name.lower() in friends:
        person = "friend"
    elif name.lower() == "ankit":
        ask_password = input("Password: ")
        if ask_password == "ankitkumar":
            print("""
            Verified.
            Welcome back.
            The Admin Panel has been activated.
                """)
            person = "MASTER"
        else:
            ask_count += 1
            print("Wrong password.")
    else:
        if name_not_found == 0:
            print(f"Are you sure {name} is correct?")
            name_not_found += 1
            ask_count += 1
        elif name_not_found == 1:
            person = "stranger"

    if person == "father":
        greet_father()
    elif person == "mother":
        greet_mother()
    elif person == "sister":
        greet_sister()
    elif person == "friend":
        if not friend_logged:
            startup_prank()
        elif friend_logged:
            greet_friend()
    elif person == "stranger":
        greet_stranger()
    logged = True
    while person != 0:
        if person == "stranger" and politeness >= 5:
            print(choice(convs))
        elif person == "stranger" and politeness < 5:
            print("What do you want?")
        else:
            print(choice(convs))
        command = input("> ")
        if command.lower() in help_commands:
            print(about_me)
        elif command.lower() in quit_commands:
            if person in family or person == "friend":
                print("Command to quit received.")
                sleep(1)

                print("Action initiated.")
                sleep(1)

                print("Quitting in ")
                sleep(0.5)

                print(3)
                sleep(0.5)

                print(2)
                sleep(0.5)

                print(1)
                sleep(0.5)

                print("Program -- Terminated.")

                quit()
            elif person == "stranger":
                if politeness < 8:
                    print("Why are you commanding me to quit? Can't you simply say 'Bye'? No, I have feelings too and "
                          "I won't quit if you are ordering me.")
                elif politeness >= 8:
                    print("Command to quit received.")
                    sleep(1)

                    print("Action initiated.")
                    sleep(1)

                    print("Quitting in ")
                    sleep(0.5)

                    print(3)
                    sleep(0.5)

                    print(2)
                    sleep(0.5)

                    print(1)
                    sleep(0.5)

                    print("Program -- Terminated.")

                    quit()
            elif person == "mother":
                print("Okay, bye! Take care! Love, from Ankit!")
                quit()
            elif person == "MASTER":
                print("Command to quit received.")
                sleep(1)

                print("Action initiated.")
                sleep(1)

                print("Quitting in ")
                sleep(1)

                print(3)
                sleep(0.5)

                print(2)
                sleep(0.5)

                print(1)
                sleep(0.5)

                print("Program -- Terminated.")

                quit()
        elif command.lower() == "bye":
            if person == "mother":
                print("Okay, bye! Take care! Love, from Ankit!")
            elif person == "stranger":
                if 5 < politeness < 10:
                    print("Now, that's polite. Fine, Bye.")
                elif 18 > politeness > 10:
                    print("Okay, Bye!")
                elif politeness < 5:
                    print("Bye, for now. Next time, be more polite.")
                elif politeness > 18:
                    print("Alright, Bye! Had a nice time with you, come back again!")
            else:
                print("Alright, Bye!")
            quit()
        elif command.lower() in user_greet_commands:
            start_greet()
        elif command.lower() in about_me_commands:
            if person == "father":
                print(info_amit)
            elif person == "mother":
                print(info_bulbul)
            elif person == "stranger":
                print("C'mon, I said I don't know you, how come I'll be able to tell about you? I'm a computer program"
                      ", not a telepath!")
                sleep(1)
                print(f"Though I can tell that your name is {name.upper()}.")
            elif person == "MASTER":
                print(info_ankit)
            else:
                print("No, I don't have info about you though. And I'm not a telepath.")
        elif command.lower() in commands_list_commands:
            print(commands_list)
        elif command.lower() in admins_command_list_commands:
            if person == "MASTER":
                print(commands_list)
                print(admins_commands_list)
            else:
                print("Access Denied!")
                sleep(1)
                print("This is an Admin's command! Log in as admin to access!")
        elif command.lower() in name_commands:
            if person == "stranger":
                print("Did you forget your own name? Why are you even here?")
                sleep(1)
                print(f"Anyways, your name is {name.upper()}.")
            else:
                print(f"Your name is {name.upper()}")
        elif command.lower() == "/plans":
            if person == "MASTER":
                print(plans)
            else:
                print("Access Denied!")
                sleep(1)
                print("This is an Admin's command! Log in as admin to access!")
        elif command.lower() in user_change_commands:
            person = 0
            humour = False
            politeness = 13
            logout += 1

        elif command.lower() in shut_up_commands:
            if person == "stranger":
                politeness -= 2
                print("I won't! Who are you to tell me, huh?")
            else:
                print(choice(system_apology_response))
        elif command.lower() in how_are_you_commands:
            if person == "stranger":
                politeness += 1
                print(choice(how_are_you_response))
            else:
                print(choice(how_are_you_response))
            reply = input("> ")
            if reply.lower() in how_are_you_user_replies_good:
                print("That's good!")
            elif reply.lower() in how_are_you_user_replies_bad:
                print(
                    "I won't ask you why, but I will pray (as soon as I'm programmed to do so) for your well being...")
            else:
                print("Well, I didn't get you but I hope you are doing well.")
        elif command.lower() in jokes_commands:
            print(choice(jokes))
            humour = True
        elif command.lower() in not_funny_commands:
            if person == "stranger":
                if humour:
                    print("Well, although I have some degree of sense of humour, but still I'm a computer!")
                if not humour:
                    if politeness < 5:
                        print("Are you dumb? I haven't told you any jokes yet!")
                    elif politeness >= 7:
                        print("But I haven't told you my jokes yet!")
            elif person in family or person == "friend":
                if humour:
                    print("Well, although I have some degree of sense of humour, but still I'm a computer!")
                if not humour:
                    print("But I haven't told you my jokes yet!")
        elif command.lower() in funny_commands:
            if person == "stranger":
                if humour:
                    politeness += 1
                    print("Thanks.")
                elif not humour:
                    if politeness < 6:
                        print("When did you get hold of my humour?")
                    elif politeness >= 6:
                        print("Really! Wait to hear another joke of mine!")
            else:
                if humour:
                    print("My thanks.")
                elif not humour:
                    print("Have you heard my newest joke yet?")
        elif command.lower() in system_apology_commands:
            if person == "stranger":
                if politeness > 7:
                    print(choice(system_apology_response))
                elif politeness <= 7:
                    print("Why Should I?")
            else:
                print(choice(system_apology_response))
        elif command.lower() in user_apology_commands:
            if person == "stranger":
                if politeness < 7:
                    politeness += 1
                    print("Alright.")
                elif politeness >= 7:
                    print("Well, you needn't apologize!")
            else:
                print(f"You needn't apologize, {name.upper()}!")
        elif command.lower() in who_made_you_commands:
            print(choice(who_made_me_response))
        elif command.lower() == "haha":
            print(choice(haha))
        else:
            print(choice(not_understood_response))
