
import doctores.doctor as modelo
import citas.consultas


class Consultas:

    def registro(self):

        print("Se procedera a realizar tu registro en el sistema.....")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("¿Introduce tu email?:")
        password = input("¿Introduce tu contraseña?: ")

        # ***************************************
        doctor = modelo.Doctor(nombre, apellidos, email, password)
        registro = doctor.registrar()

        if registro[0] >= 1:
            print(
                f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente !!")
        # ***************************************

    def login(self):

        print("\nIdentificacion en el sistema...... ")

        try:
            email = input("Introduce tu correo... ")
            password = input("Introduce tu password... ")

            doctor = modelo.Doctor('', '', email, password)
            login = doctor.identificador()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te az registrado {login[5]}")
                self.proxConsultas(login)

        except Exception as e:

            print("Login incorrecto")

    def proxConsultas(self, doctor):
        print("""
        
        Acciones disponibles:
            - Crear doctor (crear)
            - Mostrar doctor (mostrar)
            - Eliminar doctor  (eliminar)
            - Editar doctor (editar)
            - Salir        
        """)

        accion = input("¿Que quieres hacer ?: ")
        hazEl = citas.consultas.Consultas()

        if accion == "crear":
           # print("Vamos a crear notas")
            hazEl.crear(doctor)
            self.proxConsultas(doctor)

            self.proxConsultas(doctor)
        elif accion == "mostrar":
          #  print("Vamos a mostrar")
            hazEl.mostrar(doctor)
            self.proxConsultas(doctor)

        elif accion == "eliminar":
            #print("Vamos a eliminar")
            hazEl.borrar(doctor)
            self.proxConsultas(doctor)

        elif accion == "editar":
            #print("Vamos a eliminar")
            hazEl.borrar(doctor)
            self.proxConsultas(doctor)
        elif accion == "salir":
            exit()
        # return None
