for i in range(0,1):
    print ("Hi There!")
    
my_name = "Jerame Kim"

# combine the name with the typical hello world message:
print("Hello World!, from " + my_name)

"""
 program that computes total rent payments given
  a) INITIAL_RENT
  b) NUM_YEARS
  c) AVG_YEARLY_RENT_BUMP  (average increase each year)
"""

import locale   # this line and the next support localized currency symbols
# updated 5/22/18 18:41 pvdL
# was locale.setlocale( locale.LC_ALL, '' )
locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )

# intended constants for the program
INITIAL_RENT = 2000.
NUM_YEARS = 5
AVG_YEARLY_RENT_BUMP = 1.02   # 2% per year

rent = INITIAL_RENT  # our initial rent
total = 0.           # keeps track of how much we paid "so far"

# loop for five years
for year in range(1, NUM_YEARS) :
   cost_this_year = rent * 12
   total += cost_this_year
   # now increase the rent in prep for the next year
   rent *= AVG_YEARLY_RENT_BUMP

# prepare total in currency format
total_in_currency_format = locale.currency( total, grouping = True )

#output the result to user
print("\nYou will have paid", \
   total_in_currency_format,  \
   "after " + str(NUM_YEARS) \
   + " years\n")


"""
program that does some *crazy* stuff. the first few lines in
triple quotes are python 'docstring' comments which summarize
the entire program (i am not using this docstring in this program
to describe it -- we'll do that later in the course).
"""

# this line and others starting with # are individaul comments 
# inside the code

# get the user's name and echo it back
users_answer = input("What's your name? ")
print("Okay,", users_answer, ", I'm going to do some math.")

# show the length of the name, and some computations using that length
length_of_name = len(users_answer)     
result = length_of_name
print("The length of your name is", result)
result = length_of_name / 2
print("HALF the length is", result)
result = length_of_name ** 2
print("Your name SQUARED is", result)

# sign off becuase it's polite
print("\nThanks for letting me use your name for this program, ",users_answer)








