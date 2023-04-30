import random  # to generate random number and sequences
import string   # to take numeric and alpha_numeric characters


# to take capital letters and digits in form of list with help of string module
alpha_numeric = list(string.ascii_uppercase)+list(string.digits)

# taking only digits
numeric = list(string.digits)

s = 'welcome to in otp generator '.title() # to make each first char of word capital

# to format the welcome msg
print('='*45,end='')
print(s,end='')
print('='*45)
print()  # to print a blank line
print(' '*30,end='')
print('1:Numeric[0-9]')
print(' '*30,end='')
print('2:AlphaNumeric[0-9,A-Z]')

# logic section
while True:
    choice = int(input('Enter your choice[1 or 2]:'))
    if choice == 1:
        dig = int(input('Enter the number of digits[4 or 6 or 8...] to generate otp:'))
        random_numbers = [random.choice(numeric) for i in range(dig)] # create list of random numbers of given range
        otp = ''.join(random_numbers)
        print('='*50)
        print(f'Your Otp of {dig} digits are :{otp}')
        print('='*50)
    elif choice == 2:
        dig = int(input(' Enter the number of alphaNumeric characters[4 or 6 or 8...] to generate otp:'))
        random_numbers = [random.choice(alpha_numeric) for i in range(dig)]  # create list of random numbers of given range
        otp = ''.join(random_numbers) # to join the each char of list
        print('='*50)
        print(f'Your Otp of {dig} digits are :{otp}')
        print('='*50)
    else:
        print('Please ! Enter valid choice...')
        continue  # for entering the right choice again
    ch = input('Want to generate more otp[y/n]:')

    if ch == 'n' or ch =='N':
        break # to exit the infinite loop
