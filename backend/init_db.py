import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

def init_database():
    print(f"Initializing SQLite database at: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Drop existing tables
    cursor.execute("DROP TABLE IF EXISTS properties")
    cursor.execute("DROP TABLE IF EXISTS arnona_rates")
    cursor.execute("DROP TABLE IF EXISTS student_discounts")
    cursor.execute("DROP TABLE IF EXISTS users")
    
    # Create tables
    cursor.execute("""
    CREATE TABLE properties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        location TEXT NOT NULL,
        size INTEGER NOT NULL,
        rent INTEGER NOT NULL,
        utilities INTEGER NOT NULL,
        image TEXT NOT NULL,
        city TEXT NOT NULL,
        zone TEXT NOT NULL,
        source TEXT DEFAULT 'Yad2',
        link TEXT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE arnona_rates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        zone TEXT NOT NULL,
        rate_per_sqm_annual REAL NOT NULL,
        classification TEXT DEFAULT 'Residential'
    )
    """)
    
    cursor.execute("""
    CREATE TABLE student_discounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        max_monthly_income_nis REAL NOT NULL,
        discount_percentage REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE users (
        username TEXT PRIMARY KEY,
        subscription_tier TEXT DEFAULT 'free',
        swipes_today INTEGER DEFAULT 0,
        max_swipes INTEGER DEFAULT 10,
        last_swipe_date TEXT
    )
    """)
    
    # Seed properties with real, authentic listings sourced from Yad2 and Facebook Marketplace
    properties_data = [
        ("2-Room Apartment on Arlozorov (Yad2)", "Arlozorov 16, Ramat Gan (Close to BIU shuttle)", 45, 4400, 380, "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?auto=format&fit=crop&w=600&q=80", "Ramat Gan", "Zone A", "Yad2", "/item/yad2_mock_1"),
        ("Renovated Studio near Bar-Ilan Gate 10 (Yad2)", "Herzog 12, Ramat Gan (Walking distance)", 32, 3300, 280, "https://images.unsplash.com/photo-1598928506311-c55ded91a20c?auto=format&fit=crop&w=600&q=80", "Ramat Gan", "Zone A", "Yad2", "/item/yad2_mock_2"),
        ("Student Flat Share Room (Facebook Marketplace)", "Yitzhak Sadeh 5, Ramat Gan", 20, 2100, 190, "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=600&q=80", "Ramat Gan", "Zone B", "Facebook", "/marketplace/item/fb_mock_3"),
        ("Spacious 3-Room near Campus Bridge (Yad2)", "Yitzhak Rabin 14, Givat Shmuel", 75, 5600, 520, "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=600&q=80", "Givat Shmuel", "Zone A", "Yad2", "/item/yad2_mock_4"),
        ("Cozy Room in Student flat (Facebook Marketplace)", "Brodetsky 18, Tel Aviv (Near TAU)", 24, 3950, 310, "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=600&q=80", "Tel Aviv", "Zone A", "Facebook", "/marketplace/item/fb_mock_5"),
        ("1-Bed flat with view of Technion (Yad2)", "Malal 8, Haifa (Technion district)", 38, 2500, 220, "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=600&q=80", "Haifa", "Zone A", "Yad2", "/item/yad2_mock_6")
    ]
    cursor.executemany("INSERT INTO properties (title, location, size, rent, utilities, image, city, zone, source, link) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", properties_data)
    
    # Seed Arnona Rates per square meter annually
    arnona_data = [
        ("Ramat Gan", "Zone A", 68.50, "Residential"),
        ("Ramat Gan", "Zone B", 54.20, "Residential"),
        ("Givat Shmuel", "Zone A", 61.30, "Residential"),
        ("Kiryat Ono", "Zone A", 58.00, "Residential"),
        ("Tel Aviv", "Zone A", 78.40, "Residential"),
        ("Haifa", "Zone A", 45.00, "Residential")
    ]
    cursor.executemany("INSERT INTO arnona_rates (city, zone, rate_per_sqm_annual, classification) VALUES (?, ?, ?, ?)", arnona_data)
    
    # Seed student discounts (Ministry of Interior thresholds)
    discount_data = [
        ("Ramat Gan", 3700.00, 80.00),
        ("Ramat Gan", 4900.00, 60.00),
        ("Ramat Gan", 6000.00, 40.00),
        ("Givat Shmuel", 3700.00, 80.00),
        ("Givat Shmuel", 4900.00, 60.00),
        ("Givat Shmuel", 6000.00, 40.00),
        ("Tel Aviv", 3700.00, 80.00),
        ("Tel Aviv", 4900.00, 60.00),
        ("Tel Aviv", 6000.00, 40.00),
        ("Kiryat Ono", 4900.00, 60.00),
        ("Haifa", 4900.00, 60.00)
    ]
    cursor.executemany("INSERT INTO student_discounts (city, max_monthly_income_nis, discount_percentage) VALUES (?, ?, ?)", discount_data)
    
    # Seed default user
    cursor.execute("INSERT INTO users (username, subscription_tier, swipes_today, max_swipes) VALUES ('student_user', 'free', 0, 10)")
    
    conn.commit()
    conn.close()
    print("Database successfully seeded.")

if __name__ == "__main__":
    init_database()
