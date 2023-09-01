from collections import namedtuple

a=namedtuple('cursos', 'nombre, descripcion')
s=a('data science','Curso completo')
##print(s)

##b=namedtuple('cursos', 'nombre, descripcion')
t=a._make(['inteligencia artificial','conceptos basicos'])
print(t)
print(s)