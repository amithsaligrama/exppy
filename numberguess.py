from random import *
guesses = 1
interval_min = int(raw_input("\nWhat is the minimum integer that you want in your interval? "))
interval_max = int(raw_input("What is the maximum integer that you want in your interval? "))
while interval_mind or interval_max:
  print "\nThe minimum cannot be greater than the maximum.\n"
  interval_min = int(raw_input("\nWhat is the minimum integer that you want in your interval? "))
  interval_max = int(raw_input("What is the maximum integer that you want in your interval? "))
while interval_min > interval_max:
  print "\nThe minimum cannot be greater than the maximum.\n"
  interval_min = int(raw_input("\nWhat is the minimum integer that you want in your interval? "))
  interval_max = int(raw_input("What is the maximum integer that you want in your interval? "))
while interval_min == interval_max:
  print "\nThe minimum cannot be equal to the maximum.\n"
  interval_min = int(raw_input("\nWhat is the minimum integer that you want in your interval? "))
  interval_max = int(raw_input("What is the maximum integer that you want in your interval? "))
score = 0
number = int(randrange(interval_min, interval_max))
user_number = int(raw_input("\nTry to guess my integer which is between " + str(interval_min) + " and " + str(interval_max) + " inclusive: "))
while number != user_number:
	if user_number < interval_min or user_number > interval_max:
		print "\nPlease enter a number in the range\n"
	elif user_number < number:
		print "\nHigher\n"
	elif user_number > number:
		print "\nLower\n"
	guesses += 1
	score = int(round(float((interval_max - interval_min + 1) * 10)/guesses))
	user_number = int(raw_input("Try again. "))
print "\n" + str(number) + " is correct!"
print "You took " + str(guesses) + " guess(es)."
print "Your score is " + str(score) + " out of a possible " + str(10 * (interval_max - interval_min + 1)) + ".\n"
