'''
Emilio Vega de Llergo Vargas
00549955
10/03/2025
'''

class Persona:
    def __init__(self, nombre="", apellido="", genero="", edad =0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__genero = genero
        self.__edad = edad

    #nombre: getter y setter
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    #apellido: getter y setter
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    #genero: getter y setter
    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    #edad: getter y setter
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def printPersona(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Genero: {self.genero}")
        print(f"Edad: {self.edad}")

class Paciente(Persona):
    def __init__(self, nombre="", apellido="", genero="", edad=0, altura=0.0, peso=0.0):
        super().__init__(nombre, apellido, genero, edad)
        self.__altura = altura
        self.__peso = peso

    #altura: getter y setter
    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    #peso: getter y setter

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    def imc(self, altura, peso):
        return peso / (altura**2)

    def printPaciente(self):
        self.printPersona()
        print(f"Altura: {self.__altura} cm")
        print(f"Peso: {self.__peso} kg")
        print(f"IMC: {self.imc(self.__altura, self.__peso)}")

class Medico(Persona):
    def __init__(self, nombre="", apellido="", genero="", edad=0, especialidad="",cedulaProfesional=0):
        super().__init__(nombre, apellido, genero, edad)
        self.__especialidad = especialidad
        self.__cedulaProfesional = cedulaProfesional

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, especialidad):
        self.__especialidad = especialidad

    @property
    def cedulaProfesional(self):
        return self.__cedulaProfesional

    @cedulaProfesional.setter
    def cedulaProfesional(self, cedulaProfesional):
        self.__cedulaProfesional = cedulaProfesional

    def printMedico(self):
        self.printPersona()
        print(f"Especialidad: {self.__especialidad}")
        print(f"Cedula: {self.__cedulaProfesional}")

class PacienteExterno(Paciente):
    def __init__(self, nombre="", apellido="", genero="", edad=0, altura=0.0, peso=0.0, noConsultorio=0, horario=0 ,fecha=""):
        super().__init__(nombre, apellido, genero, edad, altura, peso)
        self.__noConsultorio = noConsultorio
        self.__horario = horario
        self.__fecha = fecha

    def examenFisico(self):
        print("Se realizó el examen físico al paciente")

class PacienteHospitalizado(Paciente):
    def __init__(self, nombre="", apellido="", genero="", edad=0, altura=0.0, peso=0.0, habitacion=0, tipoCirugia=""):
        super().__init__(nombre, apellido, genero, edad, altura, peso)
        self.__habitacion = habitacion
        self.__tipoCirugia = tipoCirugia

    def indicaciones(self):
        print("Las indicaciones para el hospitalizado son: ")