print('*** Decoradores en Python ***')

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de llamar la función saludar')
        resultado = funcion(*args, **kwargs)
        print('Después de llamar la función saludar')
        
        return resultado
    return wrapper


@decorador
def saludar(nombre):
    print(f'Bienvenido, {nombre}!')
    
saludar('Marcos')