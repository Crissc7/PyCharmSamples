from collections import namedtuple

a=namedtuple('cursos', 'nombre, descripcion')
s=a('data science','Curso completo')
##print(s)

##b=namedtuple('cursos', 'nombre, descripcion')
t=a._make(['inteligencia artificial','conceptos basicos'])
print(t)
print(s)

i = 0
while i<9:
    print("Number:",i)
    i+=1
print("Bye")

import random
to_be_guessed = int(20*random.random())+1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you are giving up!")
        break
else:
    print("Congratulation! You made it!")