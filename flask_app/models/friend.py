# importar la función que devolverá una instancia de una conexión
from flask_app.config.mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('first_flask').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        friends = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for friend in results:
            friends.append( cls(friend) )
        return friends

    @classmethod
    def save(cls, data ):
        query = f"INSERT INTO friends ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        results = connectToMySQL('first_flask').query_db( query, data )
        return results
    
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM friends WHERE id = %(id)s;"
        
        results = connectToMySQL('first_flask').query_db(query, data)
        user = results[0]
        print(f"RESULTS: ", results[0])
        return user

    @classmethod
    def edit_user(cls, data):
        query = "UPDATE `friends` SET `first_name` = %(first_name)s, `last_name` = %(last_name)s, `email` = %(email)s, `updated_at` = NOW()  WHERE (`id` = %(id)s);"
        results = connectToMySQL('first_flask').query_db(query, data)
        print(results)
        return results

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM friends WHERE (id = %(id)s);"
        results = connectToMySQL('first_flask').query_db(query, data)
        print(results)
        return results
