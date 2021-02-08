# Magic 8-ball - msjupiter96
import random
import time



# function to create a random int between 1-9
def get_randomnum():
    randomnum = random.randint(1,9)
    return randomnum

# function search for an answer after the user inputs question
def search_for_answer(question):
    waitperiod = [1, 2]
    time.sleep(5)
    print("Searching for an answer.")
    time.sleep(1)
    print("Please be patient")

    for seconds in waitperiod:
        print("..........")
        time.sleep(0.5)

# function that uses the randomly generated number to give back a statement/fortune
def get_answer(result):
    if result == 1:
        print("As I see it, yes. ")
    elif result == 2:
        print("Ask again later. ")
    elif result == 3:
        print("It is certain. ")
    elif result == 4:
        print("Very doubtful. ")
    elif result == 5:
        print("Concentrate and ask again. ")
    elif result == 6:
        print("Most likely. ")
    elif result == 7:
        print("My sources say no. ")
    elif result == 8:
        print("Yes. ")
    elif result == 9:
        print("Better not tell you now. ")
    
    
def main(program_status):

    while program_status == 1:
        question = input("Ask the Magic 8 ball a question: ")
        search_for_answer(question)

        result = get_randomnum()

        get_answer(result)

        user_choice = input("Would you like to go again? yes or no: ")
        if (user_choice == "yes") or (user_choice == "Yes") or (user_choice == "YES"):
            program_status = 1
        elif (user_choice == "no") or (user_choice == "No") or (user_choice == "NO"):
            program_status = 0
            print("Goodbye")
            time.sleep(1.5)
            exit()
        else:
            print("Invalid input. Shutting down..")
            exit()

# Running the program
program_status = 1
main(program_status)
    
