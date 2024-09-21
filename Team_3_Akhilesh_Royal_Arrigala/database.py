import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('inventory_management.db')
        self.create_tables()

    def create_tables(self):
    
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS materials (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    stock INTEGER,
                    cost_of_goods_sold REAL,
                    historical_sales REAL
                )
            """)

    def add_item(self, item_id, name, stock, cost_of_goods_sold, historical_sales):
        with self.conn:
            self.conn.execute("""
                INSERT INTO materials (id, name, stock, cost_of_goods_sold, historical_sales)
                VALUES (?, ?, ?, ?, ?)
            """, (item_id, name, stock, cost_of_goods_sold, historical_sales))

    def update_item(self, item_id, quantity):
        with self.conn:
            self.conn.execute("""
                UPDATE materials
                SET stock = stock + ?
                WHERE id = ?
            """, (quantity, item_id))

    def get_item(self, item_id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM materials WHERE id = ?", (item_id,))
            return cur.fetchone()

    def get_all_items(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM materials")
            return cur.fetchall()

    def close(self):
        self.conn.close()
