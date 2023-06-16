from cosas import *
def main():
    per1 = Persona("José",19)
    print(per1)
    print(Persona.descripcion)

    print("Herencia-Alumno")
    al1 = Alumno("José",19,"318088378","ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("---HERENCIAPROFESOR---")
    profe1 = Profesor("Jesus", 30 + 16, 737373, "Ingenieria de software")
    print(profe1)
    profe1.dormir()

    print("Herencia ayudante profe")
    ayudante = AyudanteProfesor("Adrian", 20, "37372727", "ICO", 2828833, "Ing. de Software", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase(("P.O.O"))

main()