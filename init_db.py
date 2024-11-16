import sqlite3

connection = sqlite3.connect("chocolate_house.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS SeasonalFlavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    availability_start DATE NOT NULL,
    availability_end DATE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS IngredientInventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CustomerFeedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    suggested_flavor TEXT,
    allergy_concern TEXT
)
""")

connection.commit()
connection.close()
