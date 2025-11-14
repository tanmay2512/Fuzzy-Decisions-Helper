import random
import colorama

#setting the default output color to cyan
colorama.init(autoreset=False)
cgreen = colorama.Fore.GREEN
cred = colorama.Fore.RED
ccyan = colorama.Fore.CYAN
cblue = colorama.Fore.BLUE

def random_from_book():
    f = open("book_of_answers_style" , 'r')
    list_of_content = []
    content = f.read()
    result = random.randint(0,260)
    for i in content.split("\n"):
         list_of_content.append(i)
    for i in list_of_content:
         if result == list_of_content.index(i):
              print(f"Your answer from the book is: {cblue}{i}{ccyan}")

def Gen_ran_T_F():
     result = random.randint(0,1)
     if result == 0:
          return False
     if result == 1:
          return True

while True:
     input(ccyan + "enter your question: ")
     choice = int(input(f"1.Best of 1 \n2.Best of 3 \n3.Book of answers \n{cred}4.Exit program\n{cgreen}Enter your choice:"))
     if choice == 1:
          print(f"{Gen_ran_T_F()}")
     if choice == 2:
          result_1 = Gen_ran_T_F()
          result_2 = Gen_ran_T_F()
          result_3 = Gen_ran_T_F()
          print(f"All results are {cgreen}{result_1}, {result_2}, {result_3}{ccyan}")
          if (result_1 and result_2) or (result_2 and result_3):
               print(f"Final result is {cgreen}True{ccyan}")
          else:
               print(f"Final result is {cred}False{ccyan}")
     if choice == 3:
          random_from_book()
     if choice == 4:
          break