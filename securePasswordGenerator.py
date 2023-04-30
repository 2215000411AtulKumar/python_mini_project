import string as s # to take the collections of letters and digits
import random
# taking uppercase,lowercase letters ,digits and symbols in form of single list
data = list(s.ascii_uppercase)+list(s.digits) + ['!','@','#','$','%','&','*','?']+list(s.ascii_lowercase)

s = 'welcome to in secure password generator '.title() # to make each first char of word capital
print('='*45,end='') # to print 45 equal signs before welcome msg
print(s,end='') # after printing last equal sign printing msg
print('='*45)  # to print 45 equal signs after welcome msg
print()  # to print blank lines

# formatting the recommendation
print(' '*40,end='')
msg = 'Note---> Recommended length of password bits is:12'
print('='*len(msg))
print(' '*40,end='')
print(msg)
print(' '*40,end='')
print('='*len(msg))

# logic section
while True:
    l = int(input('Enter the length of a password:'))
    if l<8:
        print('Password length must be at least 8 bits... ')
    elif l>=8:
        random_chars = [random.choice(data) for i in range(l)]
        secure_password = ''.join(random_chars) # to join the each char of list
        print('='*40)
        print(f'Your secure password is: {secure_password}')
        print('='*40)
    c = input('Want to generate more passwords[y/n]:')
    if c == 'n' or c == 'N':
        break



