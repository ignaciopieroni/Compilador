from AFDs import *

tipos_de_tokens_con_sus_automatas = [
    ("if", afd_if), ("then", afd_then), ("call", afd_call), ("begin", afd_begin), 
    ("end", afd_end), ("while", afd_while), ("do", afd_do), ("odd", afd_odd), 
    ("const", afd_const), ("var", afd_var), 
    (":=", afd_asignation), ("procedure", afd_procedure), ("id", afd_id), 
    ("+", afd_suma), ("*", afd_multiplication),("-", afd_resta), ("/", afd_division),
    ("#", afd_end_program), ("num", afd_numbers), (",", afd_coma), 
    (";", afd_punto_y_coma), ("(", afd_parentesis_inicial), (")", afd_parentesis_final), 
    ("blanckSpace", afd_white_space),(">",afd_mayor),(">=",afd_mayor_igual),("<",afd_menor),("<=",afd_menor_igual),("=",afd_igual),("<>",afd_distinto)
]

def lexer(codigoFuente):
    contador = 1
    inicio_del_lexema = 0
    fin_del_lexema = 0
    lexema = ''

    nuevos_tipos_de_tokens_posibles = []
    antiguos_tipos_de_tokens_posibles = []

    lista_final_de_tokens_con_sus_tipos = []

    analizar_lexema_mas_grande = False

    while contador <= len(codigoFuente):
        fin_del_lexema = contador
        lexema = codigoFuente[inicio_del_lexema:fin_del_lexema]

        for tipo_de_token, afd_del_token in tipos_de_tokens_con_sus_automatas:
            estado = afd_del_token(lexema)

            if estado == 'aceptado':
                nuevos_tipos_de_tokens_posibles.append(tipo_de_token)
            elif estado == 'no aceptado':
                analizar_lexema_mas_grande = True

        if analizar_lexema_mas_grande:
            analizar_lexema_mas_grande = False
            antiguos_tipos_de_tokens_posibles = nuevos_tipos_de_tokens_posibles
            nuevos_tipos_de_tokens_posibles = []
            contador += 1
        elif len(nuevos_tipos_de_tokens_posibles) >= 1:
            antiguos_tipos_de_tokens_posibles = nuevos_tipos_de_tokens_posibles
            nuevos_tipos_de_tokens_posibles = []
            contador += 1
        elif len(nuevos_tipos_de_tokens_posibles) == 0 and len(antiguos_tipos_de_tokens_posibles) >= 1:
            token = lexema[:-1]
            tipo_de_token_definitivo = antiguos_tipos_de_tokens_posibles[0]

            if tipo_de_token_definitivo != "blanckSpace":
                lista_final_de_tokens_con_sus_tipos.append((tipo_de_token_definitivo, token))

            inicio_del_lexema = fin_del_lexema - 1
            nuevos_tipos_de_tokens_posibles = []
            antiguos_tipos_de_tokens_posibles = []
        elif len(nuevos_tipos_de_tokens_posibles) == 0 and len(antiguos_tipos_de_tokens_posibles) == 0:
            print('Error: caracter o expresion invalidos')
            break
    
    # Manejar el último token
    if len(nuevos_tipos_de_tokens_posibles) == 0 and len(antiguos_tipos_de_tokens_posibles) >= 1:
        token = lexema
        tipo_de_token_definitivo = antiguos_tipos_de_tokens_posibles[0]
        if tipo_de_token_definitivo != "blanckSpace":
            lista_final_de_tokens_con_sus_tipos.append((tipo_de_token_definitivo, token))
    lista_final_de_tokens_con_sus_tipos.append(('EOF', 'EOF'))
    return lista_final_de_tokens_con_sus_tipos

