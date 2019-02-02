"""

Jerame Kim 1/31/2019
Program name:  assignment_4

Part 1
A program that logs the number of occurrences of every digit in the years 1987-2012

Part 2
A program that outputs a Times Table with the values 0.5-5.5 increasing in increments of 1

"""


digitCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
number = 1986

while number < 2012:

    number = number + 1
    year = str(number)

    digitCountCurrent = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for digit in year:
        digitNumber = int(digit)
        for i in range(10):
            if digitNumber == i:
                digitCount[i] = digitCount[i] + 1
                digitCountCurrent[i] = digitCountCurrent[i] + 1

    print("The current year is", number, digitCount)

    duplicatesWereFound = False
    for i in range(len(digitCountCurrent)):
        if digitCountCurrent[i] > 1:
            print(f"There were {digitCountCurrent[i]} duplicates for {i} in the year {year}\n" )
            duplicatesWereFound = True

    if duplicatesWereFound == False:
        print (f"No duplicates were found for year {year}\n")
#
"""
-------------------------- run ------------------------- 
/Users/jerame/Documents/PythonProjects/Foothill4/venv/bin/python /Users/jerame/Documents/PythonProjects/Foothill4/venv/lib/assignment4.py
The current year is 1987 [0, 1, 0, 0, 0, 0, 0, 1, 1, 1]
No duplicates were found for year 1987

The current year is 1988 [0, 2, 0, 0, 0, 0, 0, 1, 3, 2]
There were 2 duplicates for 8 in the year 1988

The current year is 1989 [0, 3, 0, 0, 0, 0, 0, 1, 4, 4]
There were 2 duplicates for 9 in the year 1989

The current year is 1990 [1, 4, 0, 0, 0, 0, 0, 1, 4, 6]
There were 2 duplicates for 9 in the year 1990

The current year is 1991 [1, 6, 0, 0, 0, 0, 0, 1, 4, 8]
There were 2 duplicates for 1 in the year 1991

There were 2 duplicates for 9 in the year 1991

The current year is 1992 [1, 7, 1, 0, 0, 0, 0, 1, 4, 10]
There were 2 duplicates for 9 in the year 1992

The current year is 1993 [1, 8, 1, 1, 0, 0, 0, 1, 4, 12]
There were 2 duplicates for 9 in the year 1993

The current year is 1994 [1, 9, 1, 1, 1, 0, 0, 1, 4, 14]
There were 2 duplicates for 9 in the year 1994

The current year is 1995 [1, 10, 1, 1, 1, 1, 0, 1, 4, 16]
There were 2 duplicates for 9 in the year 1995

The current year is 1996 [1, 11, 1, 1, 1, 1, 1, 1, 4, 18]
There were 2 duplicates for 9 in the year 1996

The current year is 1997 [1, 12, 1, 1, 1, 1, 1, 2, 4, 20]
There were 2 duplicates for 9 in the year 1997

The current year is 1998 [1, 13, 1, 1, 1, 1, 1, 2, 5, 22]
There were 2 duplicates for 9 in the year 1998

The current year is 1999 [1, 14, 1, 1, 1, 1, 1, 2, 5, 25]
There were 3 duplicates for 9 in the year 1999

The current year is 2000 [4, 14, 2, 1, 1, 1, 1, 2, 5, 25]
There were 3 duplicates for 0 in the year 2000

The current year is 2001 [6, 15, 3, 1, 1, 1, 1, 2, 5, 25]
There were 2 duplicates for 0 in the year 2001

The current year is 2002 [8, 15, 5, 1, 1, 1, 1, 2, 5, 25]
There were 2 duplicates for 0 in the year 2002

There were 2 duplicates for 2 in the year 2002

The current year is 2003 [10, 15, 6, 2, 1, 1, 1, 2, 5, 25]
There were 2 duplicates for 0 in the year 2003

The current year is 2004 [12, 15, 7, 2, 2, 1, 1, 2, 5, 25]
There were 2 duplicates for 0 in the year 2004

The current year is 2005 [14, 15, 8, 2, 2, 2, 1, 2, 5, 25]
There were 2 duplicates for 0 in the year 2005

The current year is 2006 [16, 15, 9, 2, 2, 2, 2, 2, 5, 25]
There were 2 duplicates for 0 in the year 2006

The current year is 2007 [18, 15, 10, 2, 2, 2, 2, 3, 5, 25]
There were 2 duplicates for 0 in the year 2007

The current year is 2008 [20, 15, 11, 2, 2, 2, 2, 3, 6, 25]
There were 2 duplicates for 0 in the year 2008

The current year is 2009 [22, 15, 12, 2, 2, 2, 2, 3, 6, 26]
There were 2 duplicates for 0 in the year 2009

The current year is 2010 [24, 16, 13, 2, 2, 2, 2, 3, 6, 26]
There were 2 duplicates for 0 in the year 2010

The current year is 2011 [25, 18, 14, 2, 2, 2, 2, 3, 6, 26]
There were 2 duplicates for 1 in the year 2011

The current year is 2012 [26, 19, 16, 2, 2, 2, 2, 3, 6, 26]
There were 2 duplicates for 2 in the year 2012
-----------------------end of run-----------------------
"""

# Part 2 The non-integral Multiplication Table

# Using a loop to iterate the horizontal values
# Using values 5 to 56 and counting by 10 because you can only use int values in the range()
for row in range(5, 56, 10):
    # Using another loop to iterate the vertical values
    for column in range(5, 56, 10):
        # Printing the product of the row and column
        # Dividing the product by 1000 to get the intended decimal value
        # Ending each print line with \t to give consistent tab spacing
        print((row*column)/1000, end="\t")
    # Printing another line after the initial for loop so a table format is given
    print()

"""
-------------------------- run ------------------------- 
/Users/jerame/Documents/PythonProjects/Foothill4/venv/bin/python /Users/jerame/Documents/PythonProjects/Foothill4/venv/lib/assignment4.py
0.025	0.075	0.125	0.175	0.225	0.275	
0.075	0.225	0.375	0.525	0.675	0.825	
0.125	0.375	0.625	0.875	1.125	1.375	
0.175	0.525	0.875	1.225	1.575	1.925	
0.225	0.675	1.125	1.575	2.025	2.475	
0.275	0.825	1.375	1.925	2.475	3.025	

Process finished with exit code 0

-----------------------end of run-----------------------
"""