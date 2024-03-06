import sqlite3

CONN = sqlite3.connect('card.db')
CURSOR = CONN.cursor()
