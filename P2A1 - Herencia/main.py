'''
Emilio Vega de Llergo Vargas
00549955
10/03/2025
'''

from Persona import Persona, Paciente, Medico, PacienteExterno, PacienteHospitalizado

print("BIENVENIDO AL EMR DEL HOSPITAL STAR MEDICA")
print("")

print("Seleccione la opción que desee:\n")

print("1. Registrar paciente externo")
print("2. Registrar paciente hospitalizado")
print("3. Registrar médico")
opcion = int(input("\nElige una opción: "))

if opcion == 1:
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    genero = input("Género: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))
    noConsultorio = int(input("No. Consultorio: "))
    horario = int(input("Horario: "))
    fecha = input("Fecha: ")
    pe = PacienteExterno(nombre, apellido, genero, edad, altura, peso, noConsultorio, horario, fecha)
    pe.printPaciente()
    pe.examenFisico()

elif opcion == 2:
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    genero = input("Género: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))
    habitacion = int(input("Habitación: "))
    tipoCirugia = input("Tipo de cirugía: ")
    ph = PacienteHospitalizado(nombre, apellido, genero, edad, altura, peso, habitacion, tipoCirugia)
    ph.printPaciente()
    ph.indicaciones()

elif opcion == 3:
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    genero = input("Género: ")
    edad = int(input("Edad: "))
    especialidad = input("Especialidad: ")
    cedulaProfesional = int(input("Cédula profesional: "))
    m = Medico(nombre, apellido, genero, edad, especialidad, cedulaProfesional)
    m.printMedico()