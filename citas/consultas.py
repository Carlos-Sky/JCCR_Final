import citas.cita as modelo


class Consultas:
    def crear(self, doctor):
        print(f"Ok {doctor[1]}!! Vamos a crear una nueva  consulta..")
        titulo = input("Introdusca el titulo de la consulta: ")
        descripcion = input("Escribe el contenido de tu consulta: ")

        cita = modelo.Cita(doctor[0], titulo, descripcion)
        guardar = cita.guardar()

        if guardar[0] >= 1:
            print(f"\n Perfecto ! Has guardado la consulta: {cita.titulo} ")
        else:
            print(
                f"\n NO se guardo tu consulta, Intentalo mas tarde: {doctor[1]}")

    def mostrar(self, doctor):
        print(f"\n{doctor[1]}!!! Estas son tus consultas: ")

        cita = modelo.Cita(doctor[0])
        citas = cita.listar()

        # print(consultas)

        for cita in citas:
            print("\n**************************")
            print(citas[2])
            print(citas[3])
            print("\n**************************")

    def borrar(self, doctor):
        print(f"\n{doctor[1]}!!! Borrar tus consultas")

        titulo = input("Introduce titulo a la consulta a borrar : ")
        cita = modelo.Cita(doctor[0], titulo)
        eliminar = cita.eliminar()

        if eliminar >= 1:
            print(f"Se borro tu consulta: ")

        else:
            print("No se borro la consulta, preube mas tarde..")
