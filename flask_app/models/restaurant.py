from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import item

class Restaurant:
    db = "menuDB"
    def __init__(self,restaurant):
        self.restaurant_id = restaurant['restaurant_id']
        self.restaurant_name = restaurant['restaurant_name']
        # self.user = None

    @classmethod
    def save(cls,restaurant_data):
        query = """
                INSERT INTO restaurants (restaurant_name)
                VALUES(%(restaurant_name)s);
                """
        return connectToMySQL(cls.db).query_db(query,restaurant_data)
    
    @classmethod
    def get_by_id(cls,restaurant_id):
        query = """
                SELECT * FROM restaurants 
                JOIN items ON restaurants.restaurant_id = items.restaurant_id
                WHERE restaurants.restaurant_id = %(restaurant_id)s;
                """
        data = {
            "restaurant_id": restaurant_id
        }
        restaurant_dict = connectToMySQL(cls.db).query_db(query,data)[0]
        restaurant_obj = Restaurant(restaurant_dict)
        item_obj = item.Item({
            "item_id": restaurant_dict["items.item_id"],
            "item_name": restaurant_dict["items.item_name"],
            "ingredients": restaurant_dict["items.ingredients"],
            "vegetarian": restaurant_dict["items.vegetarian"],
            "egg_free": restaurant_dict["items.egg_free"],
            "vegan": restaurant_dict["items.vegan"],
            "gluten_free": restaurant_dict["items.gluten_free"],
            "nut_free": restaurant_dict["items.nut_free"],
            "seafood_free": restaurant_dict["items.seafood_free"],
            "pork_free": restaurant_dict["items.pork_free"],
            "created_at": restaurant_dict["items.created_at"],
            "updated_at": restaurant_dict["items.updated_at"]
        })

        restaurant_obj.item = item_obj
        return restaurant_obj
    
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM restaurants
        JOIN items on restaurants.restaurant_id = items.item_id;"""
        results = connectToMySQL(cls.db).query_db(query)
        restaurants = []
        for restaurant_dict in results:
            restaurant_obj = Restaurant(restaurant_dict)
            item_obj = item.Item({
            "item_id": restaurant_dict["items.item_id"],
            "item_name": restaurant_dict["items.item_name"],
            "ingredients": restaurant_dict["items.ingredients"],
            "vegetarian": restaurant_dict["items.vegetarian"],
            "egg_free": restaurant_dict["items.egg_free"],
            "vegan": restaurant_dict["items.vegan"],
            "gluten_free": restaurant_dict["items.gluten_free"],
            "nut_free": restaurant_dict["items.nut_free"],
            "seafood_free": restaurant_dict["items.seafood_free"],
            "pork_free": restaurant_dict["items.pork_free"],
            "created_at": restaurant_dict["items.created_at"],
            "updated_at": restaurant_dict["items.updated_at"]
        })
            restaurant_obj.item = item_obj
            restaurants.append(item_obj)
        return restaurants