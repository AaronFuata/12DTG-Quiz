#Imports Libraries
import csv
import time
import random
import os
highscore = 0
#Functions - Random#
def randomise(seq):
    shuffled = list(seq)
    random.shuffle(shuffled)
    return iter(shuffled)
    
#Function for previous scores
def scores():
  if os.path.isfile("scores.csv"):
    with open('scores.csv', mode='r') as SCORES:
      csv_reader = csv.reader(SCORES, delimiter=',')
      for row in csv_reader:
        print("Name " + f'{row[0]}' + ", Score " + f'{row[1]}' + '.')
        #Delays Time#
        time.sleep(0.1)

#Def Test Function#
#Opens & Starts the quiz#
def test():
  with open('Quiz.csv', mode='r') as QUIZCSV:
    start = time.perf_counter()
    global highscore
    csv_reader = csv.reader(QUIZCSV, delimiter=',')
    correct = 0
    questions = 0
#Asks the quiz question#
#Also uses if/else/while statements to determine whether the answer is right or wrong which then displays a certain message to the user(e.g. "Correct, good job"#
    for row in randomise(csv_reader):
      answered = 0
      if f'{row[0]}' == "Maori":
        print("Quiz Start:")
      else:
        print("What is the english word for " + f'{row[0]}' + "?")
        while answered != 1:
          answer = input("A - " + f'{row[1]}' + ", B - " + f'{row[2]}' + ", C - " + f'{row[3]}' + ", D - " + f'{row[4]}' + ": ")
          if answer == "A" or answer == "B" or answer == "C" or answer == "D":
            #If the user gets the answer correct, the if statement will display "Correct, great job."#
            if answer == f'{row[5]}':
              print("Correct, great job.")
              correct = correct + 1
              questions = questions + 1
              print("Your current score is " + str(correct) + " out of " + str(questions) + ".")
              answered = 1
            else:
              #If the user gets the answer incorrect, the else statement will display "Incorrect, the answer was." the answer#
              print("Incorrect, the answer was " + f'{row[5]}' + ".")
              questions = questions + 1
              print("Your current score is " + str(correct) + " out of " + str(questions) + ".")
              answered = 1
          else:
            #If the user inputs something which is not valid(e.g unknown characters)then the program will print "Please enter a valid option"#
            print("Please enter a valid option.")
    end = time.perf_counter()
    score = int(((400-(end-start))*correct*10))


#Uses if/while statements. If the user passes then it will print the following strings plus the score the user obtained#
    if correct/questions >= 0.5 :
      print("You have passed the quiz, great job!")
      print("Your timed score was " + str(score) + ".")
      
#Uses if/while statements to display your highscore and prints the following strings#
      if score > highscore:
        print("That beats your previous highscore of " + str(highscore) + ".")
        highscore = score
        save = 0
        question = "Would you like to save your score: (Y/N) " 
        while save != 'N':
          save = str(input(question))
          if save == "Y":
            name = str(input("Please enter your name: "))
            with open('scores.csv', mode='a') as SCORES:
              csv_write = csv.writer(SCORES, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              csv_write.writerow([str(name), str(score)])
            save = "N"
          elif save == "N":
            break
          else:
            question = "Please enter a valid option."
      else:
        print("Your current highscore is " + str(highscore) + ".")
        #Uses if/while statements to determine if you got a good enough score to pass the quiz#
    else:
      print("Quiz FAILED! Please go over definitions and try again later.")
 

#Menu for the user#
#Displays the question(in string)which then gives the user the 3 options#
def menu():
  option = 256
  question = "Please select an option below:" 
  while option != 0:
    print(question)
    question = "Please select an option below:"
    option = input("0 - quit, 1 - test, 2 - view scores: ")
    if option == "1":
      test()
    elif option == "3":
      scores()
    elif option == "0":
      break
    else:
      question = "Please enter a valid option."
menu()