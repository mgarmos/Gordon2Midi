# TODO parametrize rhythm with constants: 
#    whole note, half note, quarter note, eighth note, sixteenth note, thirty-second note, sixty-fourth note
class Syllable:

    def __init__(self):
        raise NotImplementedError("Do not create raw Syllable objects.")

    def __str__(self):
        return self.name
        
    def getName(self):
        return self.name

    def getRythm(self):
        return self.rhythm
        
    
        
class A1(Syllable):
    def __init__(self):
        self.name = "DU"
        self.rhythm = [1]

class A2(Syllable):
    def __init__(self):
        self.name = "DU DE"
        self.rhythm = [0.5,0.5]
        
class A3(Syllable):
    def __init__(self):
        self.name = "DU-Ta DE-Ta"
        self.rhythm = [0.25, 0.25, 0.25, 0.25]

class A4(Syllable):
    def __init__(self):
        self.name = "DU DE-Ta"
        self.rhythm = [0.5, 0.25, 0.25]

class A5(Syllable):
    def __init__(self):
        self.name = "DU-Ta DE"
        self.rhythm = [0.25, 0.25, 0.5]

class B1(Syllable):
    def __init__(self):
        self.name = "DU"
        self.rhythm = [3]
        
class B2(Syllable):
    def __init__(self):
        self.name = "DU DA DI"
        self.rhythm = [1,1,1]

class B3(Syllable):
    def __init__(self):
        self.name = "DU-Ta DA DI"
        self.rhythm = [0.5, 0.5, 1, 1]

class B4(Syllable):
    def __init__(self):
        self.name = "DU DA-Ta DI"
        self.rhythm = [1, 0.5, 0.5, 1]

class B5(Syllable):
    def __init__(self):
        self.name = "DU DA DI-Ta"
        self.rhythm = [1, 1, 0.5, 0.5]

class B6(Syllable):
    def __init__(self):
        self.name = "DU-Ta DA-Ta DI-Ta"
        self.rhythm = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

class B7(Syllable): # Prueba de silencio
    def __init__(self):
        self.name = "DU-Ta # DI-Ta"
        self.rhythm = [0.5, 0.5, -1, 0.5, 0.5]
        
def main():
    print(B5().getRythm())
  
if __name__== "__main__":
    main()         

