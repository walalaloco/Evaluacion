try:
    listausuarios= []
    usuario= {"nombre": "", "genero": "", "contraseña": ""}


    def buscarpornombre(nombre):
        salida=False
        for i in range (len(listausuarios)):
            if listausuarios [i]['nombre']== nombre:
                salida=True
                break
        return salida     
    def devolverusuariopornombre(nombre):
        for i in range (len(listausuarios)):
            if listausuarios [i] ['nombre']== nombre:
                return listausuarios [i]
    def evaluargenero(genero):
        genero=genero.upper()
        if genero== "F" or genero == "M":
            return True
        else:
            return False        
    def evaluarcontraseña(contrasena):
         if len(contrasena) ==8 and contrasena.isalnum():
              return True
         else:
              return False    
    def eliminarusuario(nombre):
         salida=False
         for i in range (len (listausuarios)):
              if listausuarios[i]['nombre']== usuarioeliminar:
                   listausuarios.remove(listausuarios[i])
                   salida= True
                   break
         return salida          



    while True:

        print ("+++++++++++++++++++++++++MENU PRINCIPAL++++++++++++++++++++++")
        print ("1. Ingresar usuario")
        print ("2. Buscar usuario")
        print ("3. Eliminar usuario")
        print ("4. Salir")
        print ("**************************")
        opcionmenu=int(input("Ingrese una opcion: "))
        if opcionmenu>0 and opcionmenu<5:

            if opcionmenu==1:
                print ("++++++++++REGISTRAR USUARIO++++++++++++")
                print ("                                   ")

                nombre=input("nombre: ")
                genero=input("genero: ")
                contrasena=input("contraseña: ")
                if buscarpornombre(nombre)==False and evaluargenero(genero)== True and evaluarcontraseña(contrasena)==True:
                     usuario={"nombre": nombre, "genero": genero, "contraseña": contrasena}
                     listausuarios.append(usuario)
                     print ("Estudiante registrado exitosamente")
                else:
                     if buscarpornombre(nombre)== True:
                          print ("El nombre de usuario ya es existente")
                     if evaluargenero(genero)== False:
                          print ("El genero debe ser F o M")
                     if evaluarcontraseña(contrasena)== False:
                          print("La contraseña debe tener 8 caracteres")

                
            if opcionmenu==2:
                    print ("+++++++++++BUSCAR ESTUDIANTE++++++++++++")
                    print("                         ")
                    usuariobuscar=input("Ingrese nombre a buscar: ")

                    if buscarpornombre(usuariobuscar)==True:
                        infousuario=devolverusuariopornombre(usuariobuscar)
                        print ("Nombre del usuario: ", infousuario ['nombre'])
                        print ("El genero del usuario es: ", infousuario ['genero'])
                        print ("La contraseña del usuario es: ", infousuario ['contraseña'])
                    else:
                        print("El usuario no existe")



            if opcionmenu==3:
                    print ("++++++++++USUARIO A ELIMINAR++++++++")
                    print("                  ")
                    usuarioeliminar=input("Ingrese usuario a eliminar por su nombre: " )
                    if buscarpornombre(usuarioeliminar)== True:
                        if eliminarusuario(usuarioeliminar)== True:
                            print ("Estudiante eliminado")
                    else:
                        print ("estudiante no existe")           



            if opcionmenu==4:
                    print ("Programa terminado.")
                    break
        else:
             print ("Ingrese una opcion valida")






except Exception as e:
    print (f"excepcion {e}")    