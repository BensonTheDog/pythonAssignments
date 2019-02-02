
lastName = "Kim"

myId = 12345678
numLet = len(lastName)

print("My family name is " + str(lastName))
print("Number is " + str(myId))
print("The number of characters in my last name is " + str(numLet) + "\n")



result = myId % 17
print("Expression #1 ------------ :" + str(result) + "\n")
result = (numLet + 17) % 11
print("Expression #2 ------------ :" + str(result) + "\n")
result = myId / (numLet + 800)
print("Expression #3 ------------ :" + str(result) + "\n")
result = 1 + 2 + numLet
print("Expression #4 ------------ :" + str(result) + "\n")
result = 15000/(80+ ((myId -123456)/((numLet + 20)*(numLet + 20))))
print("Expression #5 ------------ :" + str(result) + "\n") 

""" --------------- RUN -----------------
My family name is Kim
Number is 12345678
The number of characters in my last name is 3

Expression #1 ------------ :6

Expression #2 ------------ :9

Expression #3 ------------ :15374.443337484434

Expression #4 ------------ :6

Expression #5 ------------ :0.6469870623786849
-------------------------------------- """
