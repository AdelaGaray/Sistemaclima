from flask import Flask, jsonify, render_template  
import requests

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def home():
    # Renderiza el archivo HTML 'index.html' (crearemos este archivo en el Paso 4)
    return render_template('index.html')

# Ruta para obtener el clima de una ciudad
@app.route('/api/clima/<ciudad>')
def obtener_clima(ciudad):
    # Inserta tu clave de API de OpenWeather en esta variable
    api_key = '0ed773aa3d1ac700af5f88a0e9364762'
    
    # URL de la API de OpenWeather con el nombre de la ciudad, clave de API, unidades en Celsius y en español
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'
    
    # Realiza la solicitud HTTP a la API de OpenWeather
    response = requests.get(url)
    
    # Obtiene los datos en formato JSON
    data = response.json()
    
    # Devuelve los datos en formato JSON para que JavaScript en el navegador los interprete
    return jsonify(data)

# Ejecutamos la aplicación en modo de depuración
if __name__ == '__main__':
    app.run(debug=True)
from flask_talisman import Talisman

app = Flask(__name__)
talisman = Talisman(app)

from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

