import sqlite3

def add_seasonal_flavor(name, start_date, end_date):
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO SeasonalFlavors (name, availability_start, availability_end)
        VALUES (?, ?, ?)
    """, (name, start_date, end_date))
    connection.commit()
    connection.close()

def add_ingredient(name, quantity):
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO IngredientInventory (ingredient_name, quantity)
        VALUES (?, ?)
    """, (name, quantity))
    connection.commit()
    connection.close()

def add_customer_feedback(name, flavor, allergy):
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO CustomerFeedback (customer_name, suggested_flavor, allergy_concern)
        VALUES (?, ?, ?)
    """, (name, flavor, allergy))
    connection.commit()
    connection.close()

def get_all_records(table_name):
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()
    connection.close()
    return records

def update_ingredient_quantity(ingredient_name, new_quantity):
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE IngredientInventory
        SET quantity = ?
        WHERE ingredient_name = ?
    """, (new_quantity, ingredient_name))
    connection.commit()
    connection.close()
