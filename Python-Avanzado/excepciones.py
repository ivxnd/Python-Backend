print('*** Excepciones en Python ***')

def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es igual a 0
        if denominador == 0:
            raise Exception('El denominador es igual a 0')
        
        resultado = numerador / denominador
        print(f'Resultado de la división: {resultado}')
    except Exception as e:
        print(f'Error: {e}')
    else:
        print('No ocurrió ningún error')
    finally:
        print('Se termina de procesar la excepción')
    """ except ZeroDivisionError:
        print('Error: No se puede dividir entre 0')
    except TypeError:
        print('Error: Solo se aceptan operandos numéricos') """
    
dividir(10, 0) # ZeroDivisionError
dividir(10, '0') # TypeError