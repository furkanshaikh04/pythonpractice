print("""Welcome to KBC
      INSTRUCTIONS:
      1)You will start the game with first question 
      where you have 1000 prize for the question.
      2)Continuing the questions at each question amount will be increase
      3)You will have 60 seconds to answer the questions
      4)You two lifelines Audience poll and phone a friend""")
A=(input("Please type start to begin the game:\n"))
if A.lower()=='start':
    print("""Given below is the Prize money according to no. of queations attempted
             13	₹25,00,000/-
             12	₹12,50,000/-
             11	₹6,40,000/-
             10	₹3,20,000/-
             9	₹1,60,000/-
             8	₹80,000/-
             7	₹40,000/-
             6	₹20,000/-
             5	₹10,000/-
             4	₹5,000/-
             3	₹3,000/-
             2	₹2,000/-
             1	₹1,000/-
        Lifelines remaining:1)Audience poll 2)Phone a friend
          Type "continue" to proceed
          """)
else:
    print("Invalid input. Please type 'start' to begin the game")
B=input()
if B.lower()=='continue':
    c=print("""Current Railway Minister of India is:

A.Mamta Banarjee  B.Ram Vilash C.Ashwini Vaishnaw D.Piyush Goyal""")

import threading
import time

def timer_function(stop_event):
    start_time = time.time()
    while not stop_event.is_set():
        elapsed_time = time.time() - start_time
        print(f"Time remaining: {int(elapsed_time)} seconds")
        if elapsed_time >= 60:
            print("Time's up!.Thankyou for joining us on KBC")
            stop_event.set()
            break
        time.sleep(1)
    
def main_game():
    stop_event = threading.Event()
    timer_thread = threading.Thread(target=timer_function, args=(stop_event,))
    timer_thread.start()

    input("Press Enter to stop the timer: ")
    stop_event.set()
    timer_thread.join()

if __name__ == "__main__":
    main_game()


C=(input("Your answer:\n"))
if (C=='C'):
    print("""Correct answer you have won ₹1,000/-
          To move to the next question type ok
          And if you want to QUIT type QUIT\n""")
elif(C=='ok'):
    print("""Which god is also known as ‘Gauri Nandan’?
            A.Agni B.Indra C.Hanuman D.Ganesha""")
elif(C=='QUIT'):
    print("Your Game ends here.Thankyou for joining us on KBC")
else:
    print("Wrong answer,Your game ends here")