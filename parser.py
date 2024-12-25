from lexer import *  

# Función que convierte la salida del lexer a una lista que el parser puede entender
#
def traduccionParser(salidaLexer):
    cadena = []
    # Ponemos cada primer elemento de cada tupla (token) en una lista
    for tupla in salidaLexer:
        cadena.append(tupla[0])
    return cadena

# Función que genera las derivaciones, recibe el elemento a derivar, en que cadena y por que se deriva
def generarDerivacion(topePila, produccionAnterior, derivacion):
    # Obtenemos en que posición se encuentra el elemento a derivar
    indice = produccionAnterior.index(topePila)
    # Eliminamos el elemento a derivar
    produccionAnterior.remove(topePila)
    # Damos vuelta la lista de 'derivacion' para que luego al insertarla quede en el orden original
    produccionReversed = []
    for i in derivacion:
        produccionReversed.insert(0, i)

    # Insertamos la lista dada vuelta en la cadena a derivar
    for i in produccionReversed:
        produccionAnterior.insert(indice, i)
    
    return produccionAnterior

# "Program -> Estructura Program" tiene como simbolos directrices a: mientras, si, mostrar, aceptar e id
# El EOF es el simbolo #

# tabla[Columna][Fila]
# Tabla de análisis predictivo
table = {
    'Program':{
        'const': ['Block','#'], 
        '#':     ['Block','#'],
        'var':['Block', '#'],
        'procedure':['Block', '#'],
        'id':['Block', '#'],
        'call':['Block', '#'],
        'begin':['Block', '#'],
        'if':['Block', '#'],
        'while':['Block', '#']
    },
    'Block':{
        'const': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        '#': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'var': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'procedure': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'id':['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'call':['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'begin':['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'if':['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'while':['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        ';':['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement']
    },
    'ConstDecl':{
        'const':   ['const','ConstAssigList',';'], 
        'var':     [],
        'procedure':[],
        'id':[],
        'call':[],
        'begin':[],
        'if':[],
        'while':[], 
        ';':[],
        '#':[]
    },
    'ConstAssigList':{
        'id':       ['id','=','num','ConstAssigList`'], 
    },
    'ConstAssigList`':{
        ',':       [',','id','=', 'num','ConstAssigList`'], 
        ';':       [],
    },
    'VarDecl':{
        'var':['var', 'IdList', ';'], 
        'procedure':[],
        'id':[],
        'call':[],
        'begin':[],
        'if':[],
        'while':[], 
        ';':[],
        '#':[]
    },
    'IdList':{
        'id':       ['id', 'IdList`']
    },
    'IdList`':{
        ',':        [',','id', 'IdList`'],
        ';':        []   
    },
    'ProcDecl':{
        'procedure':['procedure','id',';','Block',';','ProcDecl'],
        '#':[],
        ';':[],
        'id':[],
        'call':[],
        'begin':[],
        'if':[],
        'while':[]
    },
    'Statement':{
        'id': ['id',':=','Expression'],
        'call': ['call','id'],
        'begin': ['begin','StatementList','end'],
        'if': ['if','Condition','then','Statement'],
        'while': ['while','Condition','do','Statement'],
        '#': [],
        'end':[],
        ';': []
    },
    'StatementList':{
        'id':['Statement', 'StatementList`'],
        'call':['Statement', 'StatementList`'],
        'begin':['Statement', 'StatementList`'],
        'while':['Statement', 'StatementList`'],
        'if':['Statement', 'StatementList`'],
        'end':['Statement', 'StatementList`'],
        ';': ['Statement', 'StatementList`']
        },
    'StatementList`':{
        ';':[';','Statement', 'StatementList`'],
        'end':[]  
    },
    'Condition':{
        '+':['Expression','Relation','Expression'],
        '-':['Expression','Relation','Expression'],
        '(':['Expression','Relation','Expression'],
        'id':['Expression','Relation','Expression'],
        'num':['Expression','Relation','Expression'],
        'odd':['odd','Expression']
    },
    'Expression':{
        '+':['SumOperator','Term','Expression`'],
        '-':['SumOperator','Term','Expression`'],
        '(':['Term','Expression`'],
        'id':['Term','Expression`'],
        'num':['Term','Expression`'],     
    },
    'Expression`':{
        '+':['SumOperator','Term','Expression`'],
        '-':['SumOperator','Term','Expression`'],
        ')':[],
        'then':[],
        'do':[],
        '#':[],
        ';':[],
        '=':[],
        '<>':[],
        '<':[],
        '>':[],
        '<=':[],
        '>=':[],
        'end':[]  
    },
    'Term':{
        '(':['Factor', 'Term`'],
        'id':['Factor', 'Term`'],
        'num':['Factor', 'Term`']     
    },
    'Term`':{
        '*':['MultOperator', 'Factor', 'Term`'],
        '/':['MultOperator', 'Factor', 'Term`'],
        '+':[],
        '-':[],
        ')':[],
        'then':[],
        'do':[],
        '#':[],
        ';':[],
        '=':[],
        '<>':[],
        '<':[],
        '>':[],
        '<=':[],
        '>=':[],
        'end':[]  
    },
    'Relation':{
        '=':['='],
        '<>':['<>'],
        '<':['<'],
        '>':['>'],
        '<=':['<='],
        '>=':['>=']         
    },
    'SumOperator':{
        '+':['+'],
        '-':['-']
    },
    'MultOperator':{
        '*':['*'],
        '/':['/']
        },
    'Factor':{
    '(':['(','Expression',')'],
    'id': ['id'],
    'num': ['num']
    },
}

# Lista de terminales
VT = ['id', 'num', '#', 'const', 'var', ',' , ';' , '=', ':=', 'call', 'begin', 'procedure', 'end', 'if', 'then','while', 'do',
'odd', '<', '>', '<>', '<=', '>=', '+', '-', '*', '/', '(', ')','EOF']

# Función principal
def parser(cadena):
    # Iniciamos la pila con el simbolo EOF (#) y el simbolo distinguido
    pila = ['EOF', 'Program']
    simboloApuntado = 0
    # Lista donde se trabaja con las derivaciones en cada ciclo
    derivacion = ['Program']
    # Lista donde se guardan todas las derivaciones
    derivaciones = []

    # Flag para salir del ciclo principal
    continuar = True

    # Ciclo principal
    while continuar:
        # Actualizamos el valor del tope
        tope = pila[-1]

        # Condición de éxito
        if (tope == 'EOF') and (cadena[simboloApuntado] == 'EOF'):
            print("La cadena es aceptada por el lenguaje")
            print("Derivaciones:")
            for i in derivaciones:
                print(i)
            break

        if tope in VT:
            if tope == cadena[simboloApuntado]:
                # Consumimos el último elemento de la pila
                pila.pop()
                # Avanzamos el puntero en un elemento
                simboloApuntado += 1
            
            # Si no se cumple la condición salimos del ciclo
            else:
                continuar = False
                print("La cadena no pertenece al lenguaje")
        else:
            # Intentamos obtener el elemento de la tabla en la posición indicada
            try:
                produccionTabla = table[tope][cadena[simboloApuntado]]
                # Damos vuelta la producción
                produccionReversed = []
                for i in produccionTabla:
                    # Insertamos todos los elementos en la posición 0 de la nueva lista
                    produccionReversed.insert(0, i)
                # Consumimos el último elemento de la pila
                pila.pop()
                # Agregamos la producción dada vuelta a la pila
                pila.extend(produccionReversed)
                # Guardamos la derivación
                derivacion = generarDerivacion(tope, derivacion, produccionTabla)
                # El .copy() es necesario porque sino se copian las referencias y tendriamos una lista con 5 elementos iguales
                derivaciones.append(derivacion.copy())

            # Si hay error salimos del ciclo   
            except:
                continuar = False
                print("La cadena no pertenece al lenguaje")