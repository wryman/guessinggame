#  File: GuessingGame.py

#  Description:

#  Student Name:  William Ryman

#  Student UT EID: wrr368

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created: 5/2/14

#  Date Last Modified: 5/2/14
def main():

	print('Guessing Game','\n',"Think of a number between 1 and 100 inclusive.",'\n',"And I will guess what it is in 7 tries or less.",'\n')
	decide=str(input("Are you ready? (y/n):"))
	lo=1
	hi=100
	mid=(lo+hi)//2
	guessestaken=0
	#defines variables hi,mid,lo used for binary search
		#main loop to change values of variables based on user input 
	if decide=='y':
		while guessestaken<=6:
			guessestaken+=1
			print('Guess',guessestaken,':','\n',"The number you thought was",mid)
			response=input("Enter 1 if my guess was high, -1 if low, and 0 if correct:")
			if response==0:
				print("Thank you for playing the Guessing Game.")
			elif response==1:
				hi=mid//2
				print('hi',hi, 'mid',mid,'lo',lo)
			elif response==-1:
				lo=mid//2
			print('hi',hi, 'mid',mid,'lo',lo)
		if guessestaken>=8:
			print('Either you guessed a number out of range or you had an incorrect entry.')

	elif decide=='n':
		print('Bye')
# prints bye if inital answer is 'n' or reprompts entry

main()