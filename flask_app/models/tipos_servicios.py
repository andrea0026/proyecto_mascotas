from flask_app.config.mysqlconnection import connectToMySQL

class Tipo_Servicio:
    def __init__(self, data):
        self.id = data['id']
        self.service_type = data['service_type']
        self.description = data['description']
        self.price = data['price']
        self.animal_weight = data['animal_weight']
        self.animal_height = data['animal_height']
        
    @classmethod
    def get_all_services_types(cls):
        query = "SELECT * FROM services_types;"
        results = connectToMySQL('tienda_mascotas').query_db(query) #Lista de diccionarios
        services_types = []
        for service_type in results:
            services_types.append(cls(service_type))
        print(services_types)
        return services_types