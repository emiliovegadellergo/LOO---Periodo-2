class Persona:
    def __init__(self, n="", a="", g="", e =0):
        self.__nombre = n
        self.__apellido = a
        self.__genero = g
        self.__edad = e

    #nombre: getter y setter
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, n):
        self.__nombre = n

    #apellido: getter y setter
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, a):
        self.__apellido = a

    #genero: getter y setter
    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, g):
        self.__genero = g

    #edad: getter y setter
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, e):
        self.__edad = e

    def printPersona(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Genero: {self.genero}")
        print(f"Edad: {self.edad}")

class Paciente(Persona):
    def __init__(self, n="", a="", g="", e=0, al=0.0, p=0.0):
        super().__init__(n, a, g, e)
        self.__altura = al
        self.__peso = p

    #altura: getter y setter
    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, al):
        self.__altura = al

    #peso: getter y setter

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, p):
        self.__peso = p

    def imc(self, al, p):
        return p / (al**2)

    def printPaciente(self):
        self.printPersona()
        print(f"Altura: {self.__altura} cm")
        print(f"Peso: {self.__peso} kg")
        print(f"IMC: {self.imc(self.__altura, self.__peso)}")

class Medico(Persona):
    def __init__(self, n="", a="", g="", e=0, esp="",c=0):
        super().__init__(n, a, g, e)
        self.__especialidad = esp
        self.__cedulaProfesional = c

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, esp):
        self.__especialidad = esp

    @property
    def cedulaProfesional(self):
        return self.__cedulaProfesional

    @cedulaProfesional.setter
    def cedulaProfesional(self, c):
        self.__cedulaProfesional = c

    def printMedico(self):
        self.printMedico()
        print(f"Especialidad: {self.especialidad}")
        print(f"Cedula: {self.cedulaProfesional}")

