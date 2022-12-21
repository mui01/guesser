import random
import time
def main():

  max = input('Enter max: ')
  num = random.randint(1, int(max))
  tries = input('''Enter number of tries: ''')
  for i in range(1,int(tries) + 1):
    guess = input('Enter guess: ')
    if int(guess) == num:
      print('Good')
      break
    else:
      print('Wrong')
  print('It was:', num)
  time.sleep(3)
  main()


main()
