#pruebas
import threading
import random
from time import sleep

consultorios_disponibles = [1, 2, 3, 4, 5, 6, 7, 8]
camillas_disponibles = [1, 2, 3, 4, 5, 6, 7]
quirofanos_disponibles = [1, 2, 3, 4, 5]
medicos_disponibles = ["Maria", "Luisa", "Oscar", "Alberto", "Luna"]
fisios_disponibles = ["Juana", "Pablo", "Carlos"]

cola_ninos = []  
cola_adultos_mayores = []
cola_adultos = []
cola_consulta = []
cola_terapia = []
cola_cirugia = [] 
cola_hospitalizacion = [] 
 

nombres= ["Emilio", "Luis", "Stellla", "Mia", "Juan", "Carlos"]
def paciente_urgente():
    nombre_random=random.choice(nombres)
    nombre=nombres.pop(nombres.index(nombre_random))
    tipo=random.choice(["niño", "adulto", "adulto mayor"])
    paciente = {"nombre": nombre, 
                "tipo": tipo, 
                "estado": "grave"} 
    
    return paciente

def terapia():
        while len(fisios_disponibles) == 0 or len(consultorios_disponibles) == 0:
            print("\n No hay disponibilidad para terapia, esperando 10 segundos...")
            sleep(10)

        ninos_terapia= []
        am_terapia = []
        adulto_terapia = []
        for paciente in cola_terapia:
            if paciente["tipo"] == "niño":
                ninos_terapia.append(paciente)
                cola_terapia.remove(paciente)
                for paciente in ninos_terapia: 
                    paciente = ninos_terapia.pop(ninos_terapia.index(paciente)) 
                    fisioterapeuta = fisios_disponibles.pop(0)
                    consultorio = consultorios_disponibles.pop(0)
                    print(f"\n Fisioterapeuta {fisioterapeuta} atendiendo a paciente {paciente['nombre']}({paciente['tipo']}) de estado crónico en consultorio #{consultorio}, fisios disp. {fisios_disponibles}, consultorios disponibles: {consultorios_disponibles}")
                    sleep(5)
                    fisios_disponibles.insert(0,fisioterapeuta)
                    consultorios_disponibles.insert(0,consultorio)
                    redirigir(paciente)

            elif paciente["tipo"] == "adulto mayor":
                am_terapia.append(paciente)
                cola_terapia.remove(paciente)
                for paciente in am_terapia:
                    paciente = am_terapia.pop(am_terapia.index(paciente))
                    fisioterapeuta = fisios_disponibles.pop(0)
                    consultorio = consultorios_disponibles.pop(0)
                    print(f"\n Fisioterapeuta {fisioterapeuta} atendiendo a paciente {paciente['nombre']}({paciente['tipo']}) de estado crónico en consultorio #{consultorio}, fisios disp. {fisios_disponibles}, consultorios disponibles: {consultorios_disponibles}")
                    sleep(5)
                    # liberar los recursos
                    fisios_disponibles.insert(0,fisioterapeuta)
                    consultorios_disponibles.insert(0,consultorio)
                    redirigir(paciente)
            
            else:
                adulto_terapia.append(paciente)
                cola_terapia.remove(paciente)
                for paciente in adulto_terapia:
                    paciente = adulto_terapia.pop(adulto_terapia.index(paciente))
                    fisioterapeuta = fisios_disponibles.pop(0)
                    consultorio = consultorios_disponibles.pop(0)
                    print(f"\n Fisioterapeuta {fisioterapeuta} atendiendo a paciente {paciente['nombre']}({paciente['tipo']}) de estado crónico en consultorio #{consultorio}, fisios disp. {fisios_disponibles}, consultorios disponibles: {consultorios_disponibles}")
                    sleep(5)
                    fisios_disponibles.insert(0,fisioterapeuta)
                    consultorios_disponibles.insert(0,consultorio)
                    redirigir(paciente)
def cirugia():       
        #Variable para cortar el sleep:
        break_sleep = 0
        while len(medicos_disponibles) == 0 or len(quirofanos_disponibles) == 0:
            print("\n No hay disponibilidad para cirugia, esperando 10 segundos...") 
            sleep(10)

        ninos_cirugia = []
        am_cirugia = []
        adulto_cirugia = [] 
        
        urgente = paciente_urgente()
        if urgente is not None:
            print(f"\n HA ENTRADO UN PACIENTE URGENTE {urgente['nombre']}({urgente['tipo']})")
            break_sleep +=1
            medico = medicos_disponibles.pop(0)
            quirofano = quirofanos_disponibles.pop(0)
            print(f"\n Dr. {medico} operando a paciente {urgente['nombre']}({urgente['tipo']}) de estado grave en quirofano #{quirofano}, medicos disp. {medicos_disponibles}, quirofanos disponibles: {quirofanos_disponibles}")
            sleep(10)
            medicos_disponibles.insert(0,medico)
            quirofanos_disponibles.insert(0,quirofano)
            cola_hospitalizacion.insert(0,urgente)
            break_sleep = 0 #Aqui "reinicia" la variable
            hospitalizacion()

        for paciente in cola_cirugia:
            if paciente["tipo"] == "niño":
                ninos_cirugia.append(paciente)
                cola_cirugia.remove(paciente)
                for paciente in ninos_cirugia:
                    paciente = ninos_cirugia.pop(ninos_cirugia.index(paciente))
                    medico = medicos_disponibles.pop(0)
                    quirofano = quirofanos_disponibles.pop(0)
                    print(f"\n Dr. {medico} preparando a paciente {paciente['nombre']}({paciente['tipo']}) de estado grave en quirofano #{quirofano}, medicos disp. {medicos_disponibles}, quirofanos disponibles: {quirofanos_disponibles}")
                    sleep(20)
                    if break_sleep == 1:
                        print (f"\n Doctor debe atender a paciente urgente. Cirugía de {paciente['nombre']}({paciente['tipo']}) aplazada")
                        medicos_disponibles.insert(0,medico)
                        quirofanos_disponibles.insert(0,quirofano)
                    else:
                        print (f"\n Dr. {medico} operando a {paciente['nombre']}({paciente['tipo']}) en quirofano #{quirofano}, medicos disp. {medicos_disponibles}, quirofanos disponibles: {quirofanos_disponibles}")
                        medicos_disponibles.insert(0,medico)
                        quirofanos_disponibles.insert(0,quirofano)
                        #redirigir(paciente)
                        cola_hospitalizacion.append(paciente)
                        hospitalizacion()

            elif paciente["tipo"] == "adulto mayor":
                am_cirugia.append(paciente)
                cola_cirugia.remove(paciente)
                for paciente in am_cirugia: 
                    paciente = am_cirugia.pop(am_cirugia.index(paciente))
                    medico = medicos_disponibles.pop(0)
                    quirofano = quirofanos_disponibles.pop(0)
                    print(f"\n Dr. {medico} preparando a paciente {paciente['nombre']}({paciente['tipo']}) de estado grave en quirofano #{quirofano}, medicos disp. {medicos_disponibles}, quirofanos disponibles: {quirofanos_disponibles}")
                    sleep(20)
                    if break_sleep == 1:
                        print (f"\n Doctor debe atender a paciente urgente. Cirugía de {paciente['nombre']}({paciente['tipo']}) aplazada")
                        medicos_disponibles.insert(0,medico)
                        quirofanos_disponibles.insert(0,quirofano)
                    else:
                        print (f"\n Dr. {medico} operando a {paciente['nombre']}({paciente['tipo']}) en quirofano #{quirofano}, medicos disp. {medicos_disponibles}, quirofanos disponibles: {quirofanos_disponibles}")
                        medicos_disponibles.insert(0,medico)
                        quirofanos_disponibles.insert(0,quirofano)
                        #redirigir(paciente)
                        cola_hospitalizacion.append(paciente)
                        hospitalizacion()

            else:
                adulto_cirugia.append(paciente)
                cola_cirugia.remove(paciente)
                for paciente in adulto_cirugia: 
                    paciente = adulto_cirugia.pop(adulto_cirugia.index(paciente))
                    medico = medicos_disponibles.pop(0)
                    quirofano = quirofanos_disponibles.pop(0)
                    print(f"\n Dr. {medico} preparando a paciente {paciente['nombre']}({paciente['tipo']}) de estado grave en quirofano #{quirofano}, medicos disp. {medicos_disponibles}, quirofanos disponibles: {quirofanos_disponibles}")
                    sleep(20)
                    if break_sleep == 1:
                        print (f"\n Doctor debe atender a paciente urgente. Cirugía de {paciente['nombre']}({paciente['tipo']}) aplazada")
                        medicos_disponibles.insert(0,medico)
                        quirofanos_disponibles.insert(0,quirofano)
                    else:
                        print (f"\n Dr. {medico} operando a {paciente['nombre']}({paciente['tipo']}) en quirofano #{quirofano}, medicos disp. {medicos_disponibles}, quirofanos disponibles: {quirofanos_disponibles}")
                        medicos_disponibles.insert(0,medico)
                        quirofanos_disponibles.insert(0,quirofano)
                        #redirigir(paciente)
                        cola_hospitalizacion.append(paciente)
                        hospitalizacion()
 

def hospitalizacion():
        if len(camillas_disponibles) == 0:
            print("\n Lo sentimos, no hay más camillas disponibles por hoy")

        else:
            ninos_hospitalizacion = []
            am_hospitalizacion = []
            adulto_hospitalizacion = []
            for paciente in cola_hospitalizacion:
                if paciente["tipo"] == "niño":
                    ninos_hospitalizacion.append(paciente)
                    cola_hospitalizacion.remove(paciente)
                    for paciente in ninos_hospitalizacion:
                        paciente = ninos_hospitalizacion.pop(ninos_hospitalizacion.index(paciente))
                        camilla = camillas_disponibles.pop(0)
                        print(f"\n Paciente {paciente['nombre']}({paciente['tipo']}) de estado grave hospitalizado en camilla #{camilla}, camillas disponibles: {camillas_disponibles}")
                    
                elif paciente["tipo"] == "adulto mayor":
                    am_hospitalizacion.append(paciente)
                    cola_hospitalizacion.remove(paciente)
                    for paciente in am_hospitalizacion: 
                        paciente = am_hospitalizacion.pop(am_hospitalizacion.index(paciente))
                        camilla = camillas_disponibles.pop(0)
                        print(f"\n Paciente {paciente['nombre']}({paciente['tipo']}) de estado grave hospitalizado en camilla #{camilla}, camillas disponibles: {camillas_disponibles}")

                else:
                    adulto_hospitalizacion.append(paciente)
                    cola_hospitalizacion.remove(paciente)
                    for paciente in adulto_hospitalizacion: 
                        paciente = adulto_hospitalizacion.pop(adulto_hospitalizacion.index(paciente))
                        camilla = camillas_disponibles.pop(0)
                        print(f"\n Paciente {paciente['nombre']}({paciente['tipo']}) de estado grave hospitalizado en camilla #{camilla}, camillas disponibles: {camillas_disponibles}")

def consulta():
        while len(medicos_disponibles) == 0 or len(consultorios_disponibles) == 0:
            print("\n No hay disponibilidad para consulta, esperando 10 segundos...")
            sleep(10)

        ninos_consulta = []
        am_consulta = []
        adulto_consulta = []
        for paciente in cola_consulta:
            if paciente["tipo"] == "niño":
                ninos_consulta.append(paciente)
                cola_consulta.remove(paciente)
                for paciente in ninos_consulta: 
                    paciente = ninos_consulta.pop(ninos_consulta.index(paciente))
                    consultorio = consultorios_disponibles.pop(0)
                    medico = medicos_disponibles.pop(0)
                    print(f"\n Medico {medico} atendiendo a {paciente['nombre']}({paciente['tipo']}) de estado no grave en consultorio #{consultorio}, medicos disponibles: {medicos_disponibles}, consultorios disponibles: {consultorios_disponibles}")
                    sleep(3)
                    consultorios_disponibles.insert(0,consultorio) 
                    medicos_disponibles.insert(0,medico)
                    redirigir(paciente)

            elif paciente["tipo"] == "adulto mayor":
                am_consulta.append(paciente)
                cola_consulta.remove(paciente)
                for paciente in am_consulta:
                    paciente = am_consulta.pop(am_consulta.index(paciente))
                    consultorio = consultorios_disponibles.pop(0)
                    medico = medicos_disponibles.pop(0)
                    print(f"\n Medico {medico} atendiendo a {paciente['nombre']}({paciente['tipo']}) de estado no grave en consultorio #{consultorio}, medicos disponibles: {medicos_disponibles}, consultorios disponibles: {consultorios_disponibles}")
                    sleep(3)
                    consultorios_disponibles.insert(0,consultorio) 
                    medicos_disponibles.insert(0,medico)
                    redirigir(paciente)

            else:
                adulto_consulta.append(paciente)
                cola_consulta.remove(paciente)
                for paciente in adulto_consulta: 
                    paciente = adulto_consulta.pop(adulto_consulta.index(paciente))
                    consultorio = consultorios_disponibles.pop(0)
                    medico = medicos_disponibles.pop(0)
                    print(f"\n Medico {medico} atendiendo a {paciente['nombre']}({paciente['tipo']}) de estado no grave en consultorio #{consultorio}, medicos disponibles: {medicos_disponibles}, consultorios disponibles: {consultorios_disponibles}")
                    sleep(3)
                    consultorios_disponibles.insert(0,consultorio)
                    medicos_disponibles.insert(0,medico)
                    redirigir(paciente)

def redirigir(paciente):
    estado=random.choice(["no grave", "crónico", "grave", "de alta"])
    if estado == "no grave":
        cola_consulta.append(paciente) 
        consulta()
    elif estado == "crónico":
        cola_terapia.append(paciente)
        terapia()
    elif estado == "grave": 
        procedimiento = random.choice([1, 2])
        if procedimiento == 1:
            cola_hospitalizacion.append(paciente)
            hospitalizacion()
        else:
            cola_cirugia.append(paciente)
            cirugia()
    else:
        if paciente['tipo'] == "niño":
             cola_ninos.remove(paciente)
        elif paciente['tipo'] == "adulto":
             cola_adultos.remove(paciente)
        else:
            cola_adultos_mayores.remove(paciente)
        
        print(f"\n Paciente {paciente['nombre']}({paciente['tipo']}) dado de alta")
       
def ingresoPacientes():
    cant_pacientes = int(input("Ingrese la cantidad de pacientes: "))
    x = 0
    while x < cant_pacientes:
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        tipo = "niño" if edad < 18 else "adulto" if edad <= 60 else "adulto mayor"
        paciente = {
            "nombre": nombre,
            "tipo": tipo,
        }
        if tipo == "niño":
            cola_ninos.append(paciente)
        elif tipo == "adulto":
            cola_adultos.append(paciente)
        else:
            cola_adultos_mayores.append(paciente)
        print(f"\n Se agregó a {nombre} a la cola de: '{tipo}'") 
        x += 1
    return
    
if __name__ == "__main__":
    ingresoPacientes()

    tiempo_espera = random.randint(2,6)
    temporizador = threading.Timer(tiempo_espera, function=paciente_urgente)
    temporizador.start()

    for paciente_nino in cola_ninos:
        try:
            t=threading.Thread(target=redirigir, args=(paciente_nino,))
            print(f"\n---- Hilo de paciente {paciente_nino['nombre']} iniciado")
            t.start()
        except Exception as e:
            print(f"\n---- Hilo de paciente {paciente_nino['nombre']} NO iniciado {e}")

    for paciente_am in cola_adultos_mayores: 
        try:
            t=threading.Thread(target=redirigir, args=(paciente_am,))
            print(f"\n---- Hilo de paciente {paciente_am['nombre']} iniciado")
            t.start()
        except Exception as e:
            print(f"\n---- Hilo de paciente {paciente_am['nombre']} NO iniciado {e}")

    for paciente_adulto in cola_adultos:
        try:
            t=threading.Thread(target=redirigir, args=(paciente_adulto,))
            print(f"\n---- Hilo de paciente {paciente_adulto['nombre']} iniciado")
            t.start()
        except Exception as e:
            print(f"\n---- Hilo de paciente {paciente_adulto['nombre']} NO iniciado {e}")
    