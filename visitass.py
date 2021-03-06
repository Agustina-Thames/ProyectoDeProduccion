import sqlite3
import datetime

"""
datetime.datetime.now().replace(microsecond=0).isoformat()

devuelve fecha hora actual en formato ISO8601 simple

yyyymmddThh:mm:ss

"""

class Persona:
    def __init__(self, dni, apellido, nombre='', movil=''):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.movil= movil


def ingresa_visita(persona):
    """Guarda los datos de una persona al ingresar"""
    conn = sqlite3.connect('recepcion.db')
    destino = input("Ingrese destino> ")
    q = f"""SELECT dni FROM personas WHERE dni = '{persona.dni}'"""

    resu = conn.execute(q)

    if resu.fetchone():
        print("ya existe")
    else:
        q = f"""INSERT INTO personas (dni, nombre, apellido, movil)
                VALUES ('{persona.dni}',
                        '{persona.nombre}',
                        '{persona.apellido}',
                        '{persona.movil}');"""
        print(q)
        conn.execute(q)
        conn.commit()
    
    tiempo_ingreso = datetime.datetime.now().replace(microsecond=0).isoformat()
    q = f"""INSERT INTO ingresos_egresos(dni, fechahora_in, destino)
            VALUES('{persona.dni}',  '{tiempo_ingreso}', '{destino}'); """
    conn.execute(q)
    conn.commit()
    conn.close()

    

def egresa_visita (dni):
    """Coloca fecha y hora de egreso al visitante con dni dado"""
    tiempo_egreso = datetime.datetime.now().replace(microsecond=0).isoformat()
    conn = sqlite3.connect('recepcion.db')
   
    q = f"""UPDATE ingresos_egresos SET fechahora_out = '{tiempo_egreso}'  
                    WHERE dni = '{dni}' and fechahora_out IS NULL;"""
    print(q)
    conn.execute(q)
    conn.commit()

    conn.close()


def lista_visitantes_en_institucion ():
    """Devuelve una lista de objetos Persona presentes en la institución"""
    
    conn = sqlite3.connect('recepcion.db')
    q = f"""SELECT * FROM personas;"""

    resu = conn.execute(q)
    
    for fila in resu:
        print(fila)
    conn.close()

#saber que criterios y cuantos tengo que pedir

def busca_vistantes(fecha_desde, fecha_hasta, destino, dni):
    """ busca visitantes segun criterios """
    conn = sqlite3.connect('recepcion.db')

    c = ""
    if fecha_desde != "":
        c += f""" ingresos_egresos.fechahora_in = '{fecha_desde}'"""

    if fecha_hasta != "":
        if c != '':
            c += " and "
        c += f""" ingresos_egresos.fechahora_out = '{fecha_hasta}' """

    if fecha_hasta != "":
        if c != '':
            c += " and "
        c += f""" ingresos_egresos.destino = '{destino}' """
    
    if fecha_hasta != "":
        if c != '':
            c += " and "
        c += f""" ingresos_egresos.dni = '{dni}' """
    
   # q = f"""SELECT * FROM personas WHERE personas.dni = '{dni};'"""
    #r = f"""SELECT * FROM ingresos_egresos WHERE ingresos_egresos.fechahora_in = '{fecha_desde};'"""
    #s = f"""SELECT * FROM ingresos_egresos WHERE ingresos_egresos.fechahora_out = '{fecha_hasta};'"""
    #t = f"""SELECT * FROM ingresos_egresos WHERE ingresos_egresos.destino = '{destino};'"""
    
   # print(personas.nombre)
    q = "SELECT * FROM ingresos_egresos WHERE" + c 
    print(q)
    resu = conn.execute(q)
    for fila in resu:
        print(fila)
    conn.close()


def iniciar():
    conn = sqlite3.connect('recepcion.db')

    qry = '''CREATE TABLE IF NOT EXISTS
                            personas
                    (dni TEXT NOT NULL PRIMARY KEY,
                     nombre   TEXT,
                     apellido TEXT  NOT NULL,
                     movil    TEXT  NOT NULL

           );'''

    conn.execute(qry)

    qry = '''CREATE TABLE IF NOT EXISTS
                            ingresos_egresos
                    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     dni TEXT NOT NULL,
                     fechahora_in TEXT  NOT NULL,
                     fechahora_out TEXT,
                     destino TEXT

           );'''

    conn.execute(qry)


if __name__ == '__main__':
    iniciar()
    busca_vistantes('2022-05-10T12:37:47','2022-05-10T12:58:44', 'santi cueva', '28890925')
    
    #p = Persona('28890925', 'Bianchi', 'Agustina', '01278-455670')
    #ingresa_visita(p)
    
    #egresa_visita('28890925')

    """
    doc = input("Igrese dni> ")
    apellido = input("Igrese apellido> ")
    nombre = input("nombre> ")
    movil = input("móvil > ")

    p = Persona(doc, apellido, nombre, movil)
    
    ingresa_visita(p)
    """
    
    # lista_visitantes_en_institucion()
    
