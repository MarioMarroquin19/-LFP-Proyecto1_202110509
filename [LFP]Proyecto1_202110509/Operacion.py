import re
import math
import numpy as np

class Operacion:
    def __init__(self, tipo):
        self.tipo = tipo
        self.operandos = []
    
    def operar(self):
        res = ''
        if self.tipo.lower() == 'suma':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' + '
                else:
                    res += "(" + operando.operar() + ") + "  
       
        if self.tipo.lower() == 'resta':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' - '
                else:
                    res += "(" + operando.operar() + ") - "

        if self.tipo.lower() == 'multiplicacion':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' * '
                else:
                    res += "(" + operando.operar() + ") * "


        if self.tipo.lower() == 'division':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' / '
                else:
                    res += "(" + operando.operar() + ") / "
        
        if self.tipo.lower() == 'potencia':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' ^ '
                else:
                    res += "(" + operando.operar() + ") ^ "

        if self.tipo.lower() == 'raiz':
            #separar por comas y luego operar
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' , ' 
                    #+str(self.inverso(operando))
                else:
                    res += "(" + operando.operar() + ") , "

        if self.tipo.lower() == 'inverso':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' v '
                else:
                    res += "(" + operando.operar() + ") v "


        if self.tipo.lower() == 'seno':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando +" s "
                else:
                    res += "(" + operando.operar() + ") s "

        if self.tipo.lower() == 'coseno':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' c '
                else:
                    res += "(" + operando.operar() + ") c "

        if self.tipo.lower() == 'tangente':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' t '
                else:
                    res += "(" + operando.operar() + ") t "

        if self.tipo.lower() == 'mod':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' % '
                else:
                    res += "(" + operando.operar() + ") % "
        
        
        return res[0:-3]

    def nombreOperacion(self):
        if self.tipo.lower() == 'suma':
            return self.tipo.lower()
        
        if self.tipo.lower() == 'resta':
            return self.tipo.lower()
        
        if self.tipo.lower() == 'multiplicacion':
            return self.tipo.lower()
        
        if self.tipo.lower() == 'division':
            return self.tipo.lower()
        
        if self.tipo.lower() == 'potencia':
            return self.tipo.lower()

        if self.tipo.lower() == 'raiz':
            return self.tipo.lower()
        
        if self.tipo.lower() == 'inverso':
            return self.tipo.lower()
        
        if self.tipo.lower() == 'seno':
            return self.tipo.lower()
        
        if self.tipo.lower() == 'coseno':
            return self.tipo.lower()
        
        if self.tipo.lower() == 'tangente':
            return self.tipo.lower()
        
        if self.tipo.lower() == 'mod':
            return self.tipo.lower()
 
        

    def resultado(self, opera):
        if self.tipo.lower() == 'suma' or self.tipo.lower() == 'resta' or self.tipo.lower() == 'multiplicacion' or self.tipo.lower() == 'division' or self.tipo.lower() == 'mod':
            opera1 = opera.strip()
            opera2 = opera1.replace(' ', '')
            m = re.search(r'([\d*\.\d+\-/a%+*\]+)([\d*\.\d+\-/a%+*\\]+)', opera2)
            if not m:
                exit(1)
            expr = m[1]
            #print(expr)
            res = float(eval(expr))
            return res
        def pot():
            opera1 = opera.strip()
            opera2 = opera1.replace(' ', '')
            opera3 = opera2.split('^')
            opera4 = (opera3[1]+'**'+opera3[0])
            m = re.search(r'([\d*\.\d+\-/%+*\]+)([\d*\.\d+\-/%+*\\]+)', opera4)
            if not m:
                exit(1)
            expr = m[1]
            #print(expr)
            res = float(eval(expr))
            return res

        if self.tipo.lower() == 'potencia':
            opera1 = opera.strip()
            opera2 = opera1.replace(' ', '')
            opera3 = opera2.split('^')
            opera4 = (opera3[1]+'**'+opera3[0])
            m = re.search(r'([\d*\.\d+\-/%+*\]+)([\d*\.\d+\-/%+*\\]+)', opera4)
            if not m:
                exit(1)
            expr = m[1]
            #print(expr)
            res = float(eval(expr))
            return res

        if self.tipo.lower() == 'raiz':
            opera1 = opera.strip()
            print(opera1)
            opera2 = opera1.replace(' ', '')
            opera3 = opera2.split(',')
            opera4 = (opera3[1]+'**(1/'+opera3[0]+')')
            m = re.search(r'([\d*\.\d+\-/%+*\]+)([\d*\.\d+\-/%+*\\]+)', opera4)
            if not m:
                exit(1)
            expr = m[1]
            #print(expr)'''
            res = float(eval(expr))
            return res
        if self.tipo.lower()=='seno':
            opera1 = opera.strip()
            opera2 = opera1.replace(' ', '')
            m = re.search(r'([\d*\.\d+\-/%+*\]+)([\d*\.\d+\-/%+*\\]+)', opera2)
            if not m:
                exit(1)
            expr = m[1]
            #print(expr)
            res = float(eval(expr))
            seno = (res*math.pi)/180
            seno1 = math.sin(seno)
            return seno1
        if self.tipo.lower()=='coseno':
            opera1 = opera.strip()
            opera2 = opera1.replace(' ', '')
            m = re.search(r'([\d*\.\d+\-/%+*\]+)([\d*\.\d+\-/%+*\\]+)', opera2)
            if not m:
                exit(1)
            expr = m[1]
            #print(expr)
            res = float(eval(expr))
            coseno = (res*math.pi)/180
            coseno1 = math.cos(coseno)
            return coseno1
        if self.tipo.lower()=='tangente':
            opera1 = opera.strip()
            opera2 = opera1.replace(' ', '')
            m = re.search(r'([\d*\.\d+\-/%+*\]+)([\d*\.\d+\-/%+*\\]+)', opera2)
            if not m:
                exit(1)
            expr = m[1]
            #print(expr)
            res = float(eval(expr))
            tangente = (res*math.pi)/180
            tangente1 = math.tan(tangente)
            return tangente1
        if self.tipo.lower()=='inverso':
            opera1 = opera.strip()
            opera2 = opera1.replace(' ', '')
            m = re.search(r'([\d*\.\d+\-/%+*\]+)([\d*\.\d+\-/%+*\\]+)', opera2)
            if not m:
                exit(1)
            expr = m[1]
            #print(expr)
            res = float(eval(expr))
            inverso = 1/res
            return inverso
    

