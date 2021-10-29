#Jorge Misael GalÃ¡n Santana

import os

os.system('mode con: cols=150 lines=40')

    
ciclo = 1
while ciclo == 1:
    
    #Informacion de motor
    bv = ["metal", "madera", "concreto", "alta velocidad", "baja velocidad", "", "", ""]
    material = ["metal", "acero inoxidable", "madera", "concreto", "aluminio"]

    #Saludos
    print("Hola, buen dia")
    print("Mi nombre es Broc y estoy aqui para ayudarte en la realizacion de tus perforaciones en el lugar que te encuentres")
    print("Vamos a comenzar, ¿Cual es la duda sobre el barreno que vas a realizar?")
    
    i=0
    #Primer pregunta
    for i in range(1):
        

        duda1 = int(input("\n¿Que quieres saber?\n 1)El tipo de broca segun el material\n 2)la velocidad a la que deberia girar\n 3)Consejos\n 4)Ninguna de las anteriores\n "))
        if duda1 == 1:
            duda2 = int(input("¿Que material es?\n 1)Metal\n 2)Acero inoxidable\n 3)Madera\n 4)Concreto\n 5)Aluminio\n"))
            if duda2 == 1:
                print("Para el " + material[0] + " se utiliza una broca para metal la cual es una broca helicoidal que tiene dos gabilanes en la punta solamente y es de color gris azulado o gris oscuro. \n")
            elif duda2 == 2:
                print("Para el " + material[1] + " se utiliza una broca para metal de alta la cual es una broca helicoidal que tiene dos gabilanes en la punta solamente y es de color metalico, dorado o los dos anteriores. \n")
            elif duda2 == 3:
                print("Para la " + material[2] + " se utiliza una broca de paleta la cual es una broca que esta plana en la punta, tiene una punta triangular y puede ser de color metalico, azul o negro. \n")
            elif duda2 == 4:
                print("Para el " + material[3] + " se utiliza una broca para concreto la cual es una broca helicoidal que tiene dos gabilanes con una punta de flecha en la punta de la broca y es de color gris azulado o gris oscuro. \n")
            elif duda2 == 5:
                print("Para el " + material[4] + " se utiliza una broca para metal la cual es una broca helicoidal que tiene dos gabilanes en la punta solamente y es de color gris azulado o gris oscuro. \n")
                
        elif duda1 == 2:
            duda2 = int(input("¿Que material es?\n 1)Metal\n 2)Acero inoxidable\n 3)Madera\n 4)Concreto\n 5)Aluminio\n"))
            if duda2 == 1:
                print("Para el " + material[0] + " se debe de utilizar una velocidad de entre 300 a 400 rpm si se trata de brocas de 3 mm(1/8) a 6 mm(1/4)\ny se deben utilizar menos revoluciones a medida que el diametro de la broca va aumentando. No se puede dar un valor exacto ya que los taladros no indican la velocidad a la cual estan girando pero como no se trata de un material muy duro no hay tanto riesgo.\n")
            elif duda2 == 2:
                print("Para el " + material[1] + " se debe de utilizar una velocidad de entre 250 a 300 rpm si se trata de brocas de 3 mm(1/8) a 6 mm(1/4)\ny se deben utilizar menos revoluciones a medida que el diametro de la broca va aumentando. No se puede dar un valor exacto ya que los taladros no indican la velocidad a la cual estan girando hay que tener un poco de precaucion como se trata de un material un poco duro ya que hay un poco de riesgo en que la broca se atore.\n")
            elif duda2 == 3:
                print("Para la " + material[2] + " se debe de utilizar una velocidad de entre 250 a 300 rpm si se trata de brocas de 3 mm(1/8) a 6 mm(1/4)\ny se deben utilizar menos revoluciones a medida que el diametro de la broca va aumentando. No se puede dar un valor exacto ya que los taladros no indican la velocidad a la cual estan girando pero como no se trata de un material muy duro no hay tanto riesgo.\n")
            elif duda2 == 4:
                print("Para el " + material[3] + " se debe de utilizar una velocidad de entre 250 a 300 rpm si se trata de brocas de 3 mm(1/8) a 6 mm(1/4)\ny se deben utilizar menos revoluciones a medida que el diametro de la broca va aumentando. No se puede dar un valor exacto ya que los taladros no indican la velocidad a la cual estan girando hay que tener un poco de precaucion como se trata de un material un poco duro ya que hay un poco de riesgo en que la broca se atore.\n")
            elif duda2 == 5:
                print("Para el " + material[4] + " se debe de utilizar una velocidad de entre 300 a 400 rpm si se trata de brocas de 3 mm(1/8) a 6 mm(1/4)\ny se deben utilizar menos revoluciones a medida que el diametro de la broca va aumentando. No se puede dar un valor exacto ya que los taladros no indican la velocidad a la cual estan girando pero como no se trata de un material muy duro no hay tanto riesgo.\n")
                
        elif duda1 == 3:
            print("Si quieres barrenar algun matal duro te recomiendo que utilices algun aceite para que la broca no se atore en ningun momento y barrene mejor.\n")
            print("Cuando comiences a barrenar carga con fuerza al taladro pero despues ya no apliques tanta fuerza para evitar golpearte o dañar el taladro.\n")
            print("Siempre que quieras hacer un barreno grande es mas facil si primero barrenas con una broca delgada y luego vas barrenando con una broca mas grande hasta que llegues al tamaño deseado.\n")
            print("Si en algun momento se te atora la broca en el material que estas barrenando nunca sueltes el taladro, solo suelta el interruptor de arranque y sosten con firmesa el taladro.\n")
            print("Antes de realizar algun barreno ayudaria mucho si con algun material punteagudo golpeas donde vas a realizar el barreno, esto con el fin de crear un orificio en el cual la broca se guie y no se mueva a todos lados.\n")
            print("Verifica siempre que la broca tenga filo porque si barrenas algun metal con una broca sin filo no solo no vas a barrenar sino que haras mas duro el material y en el peor de los casos se funde el material con la broca.\n")
            
        elif duda1 == 4:
            duda2 = input("¿Que te interesa saber?\n ")
            bv[5] = duda2
            duda3 = int(input("¿Tienes alguna otra duda?\n 1)Si\n 2)No\n"))
            if duda3 == 1:
                duda4 = input("¿Cual es tu duda?\n")
                bv[6] = duda4
                print("Investigare al respecto, gracias\n")
            elif duda3 == 2:
                print("investigare al respecto, gracias")
            
            
            
    ciclo = int(input("¿Quieres volver a preguntar algo?\n 1)Si \n 2)No\n"))
    
print("Hasta luego, si tienes otra duda no dudes en venir a preguntarme\n")
            
            