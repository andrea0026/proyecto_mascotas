from flask import render_template, redirect, session, request, flash #importaciones de módulos de flask
from flask_app import app
from flask_app.models.users import User
from flask_app.models.citas import Appointment
from flask_app.models.tipos_clientes import Tipo_Cliente
from flask_app.models.tipos_servicios import Tipo_Servicio



@app.route('/new/appointment')
def new_appointment():
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }
    user = User.get_by_id(formulario)
    
    clients_types = Tipo_Cliente.get_all_clients_types()
    services_types = Tipo_Servicio.get_all_services_types()
    
    return render_template('new_appointment.html', user=user, clients_types=clients_types, services=services_types)

@app.route('/create/appointment', methods=['POST'])
def create_appointment():
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    if not Appointment.valida_appointment(request.form):
        return redirect('/new/appointment')

    Appointment.save(request.form)
    return redirect('/dashboard')

@app.route('/edit/appointment/<int:id>') #Recibo el identificador de la cita que quiero editar
def edit_appointment(id):
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {
        "id": session['usuario_id']
    }
    user = User.get_by_id(formulario) #Usuario que inició sesión

    formulario_appointment = { "id": id }
    #llamar a una función y debo de recibir la cita
    appointment = Appointment.get_by_id(formulario_appointment)

    return render_template('edit_appointment.html', user=user, appointment=appointment)

@app.route('/update/appointment', methods=['POST'])
def update_appointment():
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    if not Appointment.valida_appointment(request.form):
        return redirect('/edit/appointment/'+request.form['id']) #/edit/appointment/1

    Appointment.update(request.form)
    return redirect('/dashboard')

@app.route('/delete/appointment/<int:id>')
def delete_appointment(id):
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    Appointment.delete(formulario)

    return redirect('/dashboard')