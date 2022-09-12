from flask_app.config.mysqlconnection import connectToMySQL

class Tipo_Cliente:
    def __init__(self, data):
        self.id = data['id']
        self.client_type = data['client_type']
        self.description = data['description']
        self.price = data['price']
        self.discount = data['discount']
        
    @classmethod
    def get_all_clients_types(cls):
        query = "SELECT * FROM clients_types;"
        results = connectToMySQL('tienda_mascotas').query_db(query) #Lista de diccionarios
        clients_types = []
        for client_type in results:
            clients_types.append(cls(client_type))
        print(clients_types)
        return clients_types