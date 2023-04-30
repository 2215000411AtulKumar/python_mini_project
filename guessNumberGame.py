import random  # to generate the random numbers
import time as t # to make the timer
l = list(range(5,-1,-1))
print('Initiating... ',end='')
for i in l:
     print(i,end='')
     t.sleep(0.5) # to make the delay of 0.5 seconds in countDown
     print('\b'*int(len(str(i))),end='')
print('\b'*len('initiating....')) # to clear the screen on completing the timing
print() # to print blank line
print('*'*60)  # to print 60 stars
info = '''note: your points will act as oxygen for you.
          game have 5 chances to guess two digit  number on first right guess you will get 20 points otherwise
          on every wrong guess you will destroy your 4 points[4L oxygen] and on 0 points[0L oxygen] you will die...'''.title()
print(info)
print('*'*60)
name = input('Enter Your Good Name: ')

# to formatting the welcome message for  user
msg = '*' * 45 + 'Welcome ' + name.title() + ' In Number Guess Game' + '*' * 45
print(msg)
while True:
     cnumb = random.randint(10,99) # to generate 2 digits random number each time
     score,turns = 20,5
     print(f'Hint: Number is starting with {str(cnumb)[0]}')
     while turns>0:
          print() # to print blank line
          gnumb = int(input(name.title() + ', Guess Your Number: '))
          if gnumb == cnumb:
               print(f'You win! You scored {score} points...')
               break
          else:
               score -= 4 # on wrong guess destroy 4 points
               print()
               print(f'Wrong Guess! {score}L oxygen remaining...')
               if score == 0:
                    print('You Died...')

          turns -= 1
     print()
     choice = input('Want To Play More<y/n>:')
     if choice =='n' or choice == 'N':
          break  # to come out from infinite loop









