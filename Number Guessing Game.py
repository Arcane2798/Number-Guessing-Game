import random

print("\n-------------------Welcome to Number Guessing Game!-------------------\n")
print("I've chosen a random number between 1 to 100. You have 7 attempts to guess it.\n")


target = random.randint(1, 100)

attempt = 7

condition = False

for i in range(1, 8, 1):
    print(f"Attempt {i}")
    answer = int(input("Enter your guess: "))

    if answer == target:
        condition = True
        break

    elif answer < target:
        print("Too Low. Try higher\n")
        
    else:
        print("Too High. Try lower\n")
        
if condition == True:
    print("\nYou Won! You've guessed the right number.\n")
else: 
      print(f"You're out of attempt. The answer is {target}.")

