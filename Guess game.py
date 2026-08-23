import random
# 1 ते 100 मधला random number घेतो
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
	#user कडून guess घेतो
	a = int(input(" Guess The Number : "))
	guesses += 1
	if(a>n):
		#number मोठा असेल तर Lower Number Please!
		print(" Lower Number Please! ")
	elif(a<n):
		#number लहान असेल तर Higher Number Please!
		print(" Higher Number Please! ")
#बरोबर guess झाल्यावर total attempts दाखवतो		
print(f" You have gussed the number {n} correctly {guesses} attempts")

'''
This program is a Number Guessing Game in Python.
First, the computer generates a random number between 1 and 100 using random.randint().
Then the user enters a guess.
If the guessed number is greater than the actual number, it prints Lower Number Please.
If the guessed number is smaller, it prints Higher Number Please.
The loop continues until the user guesses the correct number.
Finally, the program prints the correct number and total number of attempts.
'''