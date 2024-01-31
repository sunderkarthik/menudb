from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import restaurant, user
from flask import flash

class Item:
    db = "menuDB"
    def __init__(self,item):
        self.item_id = item['item_id']
        self.item_name = item['item_name']
        self.ingredients = item['ingredients']
        self.vegetarian = item['vegetarian']
        self.vegan = item['vegan']
        self.egg_free = item['egg_free']
        self.gluten_free = item['gluten_free']
        self.nut_free = item['nut_free']
        self.seafood_free = item['seafood_free']
        self.pork_free = item['pork_free']

    @classmethod
    def save(cls,item_data):
        query = """
                INSERT INTO items (item_name, ingredients, vegetarian, vegan, egg_free, gluten_free, nut_free, seafood_free, pork_free)
                VALUES(%(item_name)s, %(ingredients)s, %(vegetarian)s, %(vegan)s, %(egg_free)s, %(gluten_free)s, %(nut_free)s, %(seafood_free)s, %(pork_free)s);
                """
        return connectToMySQL(cls.db).query_db(query,item_data)
    
    @classmethod
    def get_by_id(cls,restaurant_id, item_id):
        query = """
                SELECT * FROM items 
                JOIN restaurants ON items.restaurant_id = restaurant.restaurant_id
                JOIN user_items ON items.item_id = user_items.item_id
                WHERE items.item_id = %(item_id)s
                AND restaurants.restaurant_id = %(restaurant_id)s;
                """
        data = {
            "item_id": item_id,
            "restaurant_id": restaurant_id
        }
        item_dict = connectToMySQL(cls.db).query_db(query,data)[0]
        item_single_obj = Item(item_dict)
        # item_single_obj = item.Item({
        #     "item_id": restaurant_dict["items.item_id"],
        #     "item_name": restaurant_dict["items.item_name"],
        #     "ingredients": restaurant_dict["items.ingredients"],
        #     "vegetarian": restaurant_dict["items.vegetarian"],
        #     "egg_free": restaurant_dict["items.egg_free"],
        #     "vegan": restaurant_dict["items.vegan"],
        #     "gluten_free": restaurant_dict["items.gluten_free"],
        #     "nut_free": restaurant_dict["items.nut_free"],
        #     "seafood_free": restaurant_dict["items.seafood_free"],
        #     "pork_free": restaurant_dict["items.pork_free"],
        #     "created_at": restaurant_dict["items.created_at"],
        #     "updated_at": restaurant_dict["items.updated_at"]
        # })

        # item_obj.item = item_single_obj
        return item_single_obj