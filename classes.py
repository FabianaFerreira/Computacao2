class vector3D:
    #Exercicio 15
    def __init__(self,dx,dy,dz):        
        self.__dx, boolean = checarValores(dx)
        if (not boolean):
            print('A variável dx tem um valor inválido. Atribuindo valor padrão 1')
        self.__dy, boolean = checarValores(dy)
        if (not boolean):
            print('A variável dy tem um valor inválido. Atribuindo valor padrão 1')
        self.__dz, boolean = checarValores(dz)
        if (not boolean):
            print('A variável dz tem um valor inválido. Atribuindo valor padrão 1')

    #Exercicio 15
    def __getitem__ (self, key):
        if (key == 1 or key == 'dx'):
            return self.__dx
        if (key == 2 or key == 'dy'):
            return self.__dy
        if (key == 3 or key == 'dz'):
            return self.__dz
        return None
    
    #Exercicio 16
    def __setitem__ (self, key, value):
        if (key == 1 or key == 'dx'):            
            self.__dx, boolean = checarValores(value)
            if (not boolean):
                print('A variável dx tem um valor inválido. Atribuindo valor padrão 1')
        if (key == 2 or key == 'dy'):
            self.__dy, boolean = checarValores(value)
            if (not boolean):
                print('A variável dy tem um valor inválido. Atribuindo valor padrão 1')
        if (key == 3 or key == 'dz'):
            self.__dz, boolean = checarValores(value)
            if (not boolean):
                print('A variável dz tem um valor inválido. Atribuindo valor padrão 1')
        return None        
        
    #Exercicio 7
    def __abs__(self):
        return (self.__dx**2 + self.__dy**2 + self.__dz**2)**0.5

    #Extra para não ter que ficar convertendo com str()
    def __str__ (self):
        return "(" + str(self.__dx) + "," + str(self.__dy) + "," + str(self.__dz) + ")"
    
    #Exercicio 8
    def unitario(self):
        modulo = abs(self)
        xn = self.__dx/modulo
        yn = self.__dy/modulo
        zn = self.__dz/modulo
        return vector3D(xn,yn,zn)

    #Exercicio 9/14
    def __add__ (self, outro):
        if (isinstance(outro, ponto3D)):
            return outro + self
        return vector3D(self.__dx + outro['dx'], 
                        self.__dy + outro['dy'], 
                        self.__dz + outro['dz'])

    #Exercicio 10    
    def __neg__ (self):        
        return vector3D(self.__dx*(-1), self.__dy*(-1), self.__dz*(-1))

    #Exercicio 11    
    def __sub__ (self, v2): 
        return self + (-v2)    
    
    #Exercicio 18
    def produtoEscalar (self, vector):
        return float(self.__dx*vector['dx'] + self.__dy*vector['dy'] + self.__dz*vector['dz'])


class ponto2D (ponto3D):
    def __init__(self,x,y):
        ponto3D.__init__(self,x,y,0)
        
class vector2D (vector3D):
    def __init__(self,dx,dy):
        vector3D.__init__(self,dx,dy,0)'