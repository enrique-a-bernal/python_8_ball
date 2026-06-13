import random

print('Welcome to the Magic 8 Ball')

play_again = "yes"

while play_again.lower() == "yes":
  question = input('What is your question?')

  num = random.randint(1,9)

  if num == 1:
    print('Yes - definitely.')
  elif num == 2:
    print('It is decidely so.')
  elif num == 3:
    print('Without a doubt.')
  elif num == 4:
    print('Reply hazy, try again.')
  elif num == 5:
    print('Ask again later.')
  elif num == 6:
    print('Better not tell you now.')
  elif num == 7:
    print('My sources say no.')
  elif num == 8:
    print('Outlook not so good.')
  else: 
    print('Very doubtful.')
    
  play_again = input('Would you like to try the Magic 8 Ball again? (yes/no)')

print('Thanks for playing!')
