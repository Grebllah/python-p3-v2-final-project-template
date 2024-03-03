from models.__init__ import CURSOR, CONN

class Card:
    all = {}

    TYPES = ["unit", "spell"]

    def __init__(self, name, type):
        self.name = name
        self.type = type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name)>= 1 and len(name) < 20:
            self._name = name
        else: raise ValueError("Name must be a string between 1-20 characters")
        
    @property
    def type (self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Card instances """
        sql = """
            CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Card instances """
        sql = """
            DROP TABLE IF EXISTS cards;
        """
        
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, card type, and id values of the current Card object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's Primary Key as dictionary key"""
        sql = """
                INSERT INTO cards (name, type)
                VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.type))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Card instance."""
        sql = """
            UPDATE cards
            SET name = ?, card_type = ?, id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.card_type, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Card instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM cards
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, type):
        """ Initialize a new Card instance and save the object to the database """
        card = cls(name, type)
        card.save()
        return card

    @classmethod
    def instance_from_db(cls, row):
        """Return an Card object having the attribute values from the table row."""

        # Check the dictionary for existing instance using the row's primary key
        card = cls.all.get(row[0])
        if card:
            # ensure attributes match row values in case local instance was modified
            card.name = row[1]
            card.type = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            card = cls(row[1], row[2])
            card.id = row[0]
            cls.all[card.id] = card
        return card

    @classmethod
    def get_all(cls):
        """Return a list containing one Card object per table row"""
        sql = """
            SELECT *
            FROM cards
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Card object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM cards
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Card object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM cards
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None