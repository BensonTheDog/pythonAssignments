"""

Jerame Kim 1/25/2019
Program name:  assignment_3
Three separate programs that use Lists, Loops, and Nested Lists

"""

#part1

print(dir(list))


#part2

a = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 34, 12, 13]

common_items=[]

b_length = len(b)

for i in range(0, b_length):
    if b[i] in a:
        common_items.append(b[i])
print(common_items)

#part3

purpose_actors = ["Buddie", "Margot Robbie", "Carrie Fisher"]
purpose = ["A Dogs Purpose", purpose_actors]

star_actors =  ["Harrison Ford", "Carrie Fisher", "Mark Hamill"]                  
star = ["Star Wars", star_actors]

legend_actors = ["Kona", "Will Smith", "Carrie Fisher"]                  
legend = ["I am Legend", legend_actors]

squad_actors = ["Viola Davis", "Margot Robbie", "Will Smith"]                  
squad = ["Suicide Squad", squad_actors]

movies = [purpose, star, legend, squad]


#States all movies that Carrie Fisher is in 
for i in range(len(movies)):
    for k in range (len(movies[i][1])):
        if movies[i][1][k] == "Carrie Fisher":
            print("Carrie Fisher is in", movies[i][0])
            break

#States all movies that don't feture Viola Davis

for i in range(len(movies)):
    viola_counter = 0
    for k in range (len(movies[i][1])):
        if movies[i][1][k] == "Viola Davis":
            viola_counter = viola_counter + 1
            break
    if viola_counter == 0:
        print ("Viola Davis is not in", movies[i][0])

#States all movies that have Margo Robbie but not Carrie Fisher
for i in range(len(movies)):
    carrie_counter = 0
    for k in range(len(movies[i][1])):
        if movies[i][1][k] == "Margot Robbie":
            for k in range(len(movies[i][1])):
                if movies[i][1][k] == "Carrie Fisher":
                    carrie_counter = carrie_counter + 1
            if carrie_counter == 0:
                    print (movies[i][0], "does not have Carrie Fisher but it does have Margot Robbie.")
                    break

"""
-------------------------- run ------------------------- 

= RESTART: /Users/jerame/Documents/PythonProjects/Foothill3/assignment_3.py =
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
[1, 2, 3, 4, 8, 34, 13]
Carrie Fisher is in A Dogs Purpose
Carrie Fisher is in Star Wars
Carrie Fisher is in I am Legend
Viola Davis is not in A Dogs Purpose
Viola Davis is not in Star Wars
Viola Davis is not in I am Legend
Suicide Squad does not have Carrie Fisher but it does have Margot Robbie.

-----------------------end of run-----------------------
"""


