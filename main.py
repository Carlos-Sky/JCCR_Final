from doctores import consultas
print("Cervantes Romero Juan carlos \n-9°A-DDI")


print("""
***     REGISTRARSE O INICIAR SESION Doctor:  ***\n
    - registro
    - login
""")

hazEl = consultas.Consultas()

accion = input("*** Elige la opcion:   ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()
