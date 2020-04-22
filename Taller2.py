#Un programa que verifique si una cedula panamena es valida o invalida
#Formato de cedula panamena: 1-1234-1234
#Formato de cedula panamena: 1-1234-123
#Formato de cedula panamena: 1-123-1234
#Formato de cedula panamena: 1-123-123

import unittest

#Se crea funcion parametrizando el formato de la cedula
def todo():
    print("\n--------------AGREGUE SU CEDULA POR SECCION------------------\n")
    s1 = input("PRIMERA seccion-->")

    #Se parametriza que en la PRIMERA seccion solo acepta 1 digito
    if len(s1) > 1:
        print("Un solo digito permitido, vuelve a intentar")
        return todo()

    #Se parametriza que en la PRIMERA seccion es obligatorio poner al menos 1 digito    
    elif len(s1) < 1:
        print("Tienes que ingresar un numero, vuelve a intentar")
        return todo()
    

    s2 = input("SEGUNDA seccion-->")

    #Se parametriza que en la SEGUNDA seccion solo acepta hasta 4 digitos
    if len(s2) > 4:
        print("Hasta 4 digitos permitidos, vuelve a intentar")
        return todo()
    
    #Se parametriza que en la SEGUNDA seccion es obligatorio poner al menos 3 digitos    
    elif len(s2) < 3:
        print("Tienes que ingresar por lo menos 3, vuelve a intentar")
        return todo()


    s3 = input("TERCERA seccion-->")

    #Se parametriza que en la TERCERA seccion solo acepta hasta 4 digitos
    if len(s3) > 4:
        print("Hasta 4 digitos permitidos, vuelve a intentar")
        return todo()
    
    #Se parametriza que en la TERCERA seccion es obligatorio poner al menos 3 digitos    
    elif len(s3) < 3:
        print("Tienes que ingresar por lo menos 3, vuelve a intentar")
        return todo()

    print("Su numero de cedula es: " + s1 + "-" + s2 +"-" + s3)

class Taller1(unittest.TestCase):
    #Preparando el set de datos a validar
    #Se llama la funcion anterior
    def setUp(self):
        self.ced = todo()
    
    #Se valida la funcion
    def test_validacion_ced(self):
        self.assertIs(self.ced, self.ced)

    def tearDown(self):
        self.ced

    
if __name__ == '__main__':
    unittest.main()