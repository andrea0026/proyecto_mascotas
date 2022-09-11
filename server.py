from flask_app import app

#Importando Controlador
from flask_app.controller import users_controller, citas_controller

if __name__=="__main__":
    app.run(debug=True)