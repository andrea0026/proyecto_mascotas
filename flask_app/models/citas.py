from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

class Appointment:

    def __init__(self, data):
        self.id = data['id']
        self.date = data['date']
        self.site = data['site']
        self.pet_name = data['pet_name']
        self.animal_type = data['animal_type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.user_id = data['user_id']
        self.client_type_id = data['client_type_id']
        self.service_type_id = data['service_type_id']

    def valida_appointment(formulario):
        es_valido = True

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d")
        print(formulario['date'])
                
        print(current_time)

        if formulario['date'] == "":
            flash("Seleccione una fecha", "appointment")
            es_valido = False
        if formulario['date'] < current_time and formulario['date'] != "":
            flash("La Fecha debe ser Posterior al dia de hoy", "appointment")
            es_valido = False  
        if formulario['site'] == "":
            flash("Ingrese una sede", "appointment")
            es_valido = False
        if formulario['pet_name'] == "":
            flash("Ingrese el nombre de la mascota", "appointment")
            es_valido = False 
        if formulario['service_type_id'] == "":
            flash("Seleccione un tipo de servicio para tu mascota", "appointment")
            es_valido = False 

        #Consultar si YA existe la hora y fecha
        query = "SELECT * FROM appointments WHERE date = %(date)s"
        results = connectToMySQL('tienda_mascotas').query_db(query, formulario)
        try:
            if len(results) >= 1:
                flash('Cita registrada previamente, eliga otro horario', 'appointment')
                es_valido = False 
        except:
                es_valido = False
                
        return es_valido 
    
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO appointments(date, site, pet_name, animal_type, user_id, client_type_id, service_type_id) VALUES (%(date)s, %(site)s, %(pet_name)s, %(animal_type)s, %(user_id)s, %(client_type_id)s, %(service_type_id)s)"
        print(query)
        result = connectToMySQL('tienda_mascotas').query_db(query, formulario) 
        return result

    @classmethod
    def get_all(cls):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d")
        query = "SELECT appointments.* FROM appointments LEFT JOIN users ON users.id = appointments.user_id where date >= '" + str(current_time)  + "'" #LEFT JOIN users
        results = connectToMySQL('tienda_mascotas').query_db(query) #Lista de diccionarios
        appointments = []
        for appointment in results:
            appointments.append(cls(appointment))
        return appointments

    @classmethod
    def get_past(cls):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d")
        query = "SELECT appointments.* FROM appointments LEFT JOIN users ON users.id = appointments.user_id where date < '" + str(current_time)  + "'"#LEFT JOIN users
        results = connectToMySQL('tienda_mascotas').query_db(query) #Lista de diccionarios
        past_appointments = []
        for appointment in results:
            past_appointments.append(cls(appointment))
        return past_appointments
    
    @classmethod
    def get_current(cls):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d")
        query = "SELECT appointments.* FROM appointments LEFT JOIN users ON users.id = appointments.user_id where date >= '" + str(current_time)  + "'"#LEFT JOIN users
        print(query)
        results = connectToMySQL('tienda_mascotas').query_db(query) #Lista de diccionarios
        current_appointments = []
        for appointment in results:
            current_appointments.append(cls(appointment))
        print(current_appointments)
        return current_appointments

    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT appointments.* FROM appointments LEFT JOIN users ON users.id = appointments.user_id WHERE appointments.id = %(id)s" 
        result = connectToMySQL('tienda_mascotas').query_db(query, formulario) #recibimos una lista 
        appointment = cls(result[0]) 
        print(appointment)
        return appointment

    @classmethod
    def update(cls, formulario): 
        query = "UPDATE appointments SET date = %(date)s, site = %(site)s, pet_name = %(pet_name)s, animal_type = %(animal_type)s WHERE id = %(id)s"
        result = connectToMySQL('tienda_mascotas').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario): #Recibe formulario con id
        query = "DELETE FROM appointments WHERE id = %(id)s"
        result = connectToMySQL('tienda_mascotas').query_db(query, formulario)
        return result
    
    @classmethod
    def get_appointment_by_user(cls, formulario): 
        query = "SELECT appointments.* FROM appointments LEFT JOIN users ON users.id = appointments.user_id WHERE user_id = %(id)s"
        print(query) 
        result = connectToMySQL('tienda_mascotas').query_db(query, formulario) #recibimos una lista 
        appointments =[]
        for appointment in result:
            appointments.append(cls(appointment))
        print(appointment)
        return appointments