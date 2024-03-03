from models.__init__ import CURSOR, CONN

class Card_type:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name)>= 1 and len(name) < 20:
            self._name = name
        else: raise ValueError("Name must be a string between 1-20 characters")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Card instances """
        sql = """
            CREATE TABLE IF NOT EXISTS card_types (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Card_type instances """
        sql = """
            DROP TABLE IF EXISTS card_types;
        """
        
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, card type, and id values of the current Card_type object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's Primary Key as dictionary key"""
        sql = """
                INSERT INTO Card_types (name, id)
                VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Card_type instance."""
        sql = """
            UPDATE Card_types
            SET name = ?, id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.card_type, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Card instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM Card_types
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