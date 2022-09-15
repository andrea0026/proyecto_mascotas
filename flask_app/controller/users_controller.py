from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app
from ..models.citas import Appointment
from flask_app.models.users import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/')
def register_template():
    return render_template('register.html')

@app.route('/login/')
def login_template():
    return render_template('login.html')
  
@app.route('/register/register_user/', methods=['POST'])
def register(): 
    #request.form = {'first_name.......'}
    if not User.valida_usuario(request.form):
        return redirect('/register/')
        # return jsonify(message='Correcto')

    pwd = bcrypt.generate_password_hash(request.form['password']) 

    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pwd
    }

    id = User.save(formulario) #Guardando a mi usuario y recibo el ID del nuevo registro
    session['usuario_id'] = id #Guardando en sesion el identificador
    
    return redirect('/dashboard')
    # return jsonify(message='Correcto')

@app.route('/login/login_user/', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user: #si user=False
        # flash('E-mail no Encontrado', 'login')
        # return redirect('/')
        return jsonify(message='Email no encontrado')

    #Comparando la contraseña encriptada con la contraseña del LOGIN
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        # flash('Password incorrecto', 'login')
        # return redirect('/')
        return jsonify(message='Password Incorrecto')
    
    session['usuario_id'] = user.id
    
    # return redirect('/dashboard')
    return jsonify(message='Correcto') 

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario) #Usuario que inicio sesión
    
    # formulario_appointments = {
    #     "id": session['usuario_id']
    # }
    
    current_appointments=Appointment.get_current()
    past_appointments = Appointment.get_past()
    return render_template('dashboard.html', user=user,current_appointments=current_appointments, past_appointments=past_appointments)

@app.route('/logout')
def logout():
    session.clear() #Elimine la sesión
    return redirect('/')