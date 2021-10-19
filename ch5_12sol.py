from random import randint

score = 0

for i in range(5):
  compguess = randint(1, 10)
  userguess = eval(input('Enter guess between 1 and 10: '))
  while userguess < 0 or userguess > 10:
    userguess = eval(input('Invalid! Enter guess between 1 and 10: '))
    continue
  if userguess == compguess:
    score += 10
    print(f'You guessed right! Your score is {score}.')
  else:
    score -= 1
    print(f'Wrong. Computer guessed {compguess}. You guessed {userguess}.')
print(f'\nAfter 5 rounds, your total score is {score}.')
