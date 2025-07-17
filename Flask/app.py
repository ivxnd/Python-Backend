from flask import Flask, render_template
from cliente_dao import ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma

app = Flask(__name__)

app.config['SECRET_KEY'] = 'llave_secreta' # Ejemplo

titulo_app = 'Zona Fit App'

@app.route('/') #url: http://localhost:5000/
@app.route('/index.html') #url: http://localhost:5000/index.html

def inicio():
    app.logger.debug('Entramos al path de inicio /')
    
    # Recuperamos los clientes de la BD
    clientes_db = ClienteDAO.seleccionar()
    # Creamos el objeto cliente form vacio
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db,
                           forma=cliente_forma)

if __name__ == '__main__':
    app.run(debug=True)