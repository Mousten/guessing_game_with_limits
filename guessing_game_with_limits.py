import random 

# create a function that passes the range limit
def user_guess(x):
    # create a random secret number passing the range limits
    guess = random.randint(1, x)
    # you can only have 5 attempts, we create variables to keep track
    count = 0
    guess_limit = 5
    # introduce a while loop to not only check if we're right, but also if our guess is too high or too low
    while count < guess_limit:
        count += 1
        num = int(input(f'Please enter a number between 1 and {x}: '))
        if num != guess and num < guess:
            print(f'Oops! {num} is incorrect, please try again.')
            print(f'{num} is too low.')
        elif num > guess:
            print(f'Oops! {num} is incorrect, please try again.')
            print(f'{num} is too high.')
        else:
            print(f'Yaay! {num} is the correct number!!')
            break


user_guess(1000)



