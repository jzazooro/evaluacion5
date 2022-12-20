from io import open
import pickle

class Personaje:
    
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return '{} => vida: {} ataque: {} defensa: {} alcance: {}'.format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)

class Gestor:
    
    personajes = []
    
    def __init__(self):
        self.cargar()
        
    def agregar(self, p):
        for personaje in self.personajes:
            if personaje.nombre == p.nombre:
                return
        self.personajes.append(p)
        self.guardar()
        
    def mostrar(self):
        if len(self.personajes) == 0:
            print("No hay personajes")
            return
        for p in self.personajes:
            print(p)

    def borrar(self, nombre):
        for personaje in self .personajes:
            if personaje.nombre == nombre:
                self.personajes.remove(personaje)
                self.guardar()
                return

    def guardar(self):
        fichero = open('personajes.pckl', 'wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()
        
    def cargar(self):
        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            print("El fichero está vacío")
            pass
        finally:
            fichero.close()
            print("se han cargado {} personajes del fichero".format(len(self.personajes)))