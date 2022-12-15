class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre} y esto soltero y tengo {self.edad} años.'

# uso
david = Persona('David', 35)
erika = Persona('Erika', 32)
print(david.saluda(erika))