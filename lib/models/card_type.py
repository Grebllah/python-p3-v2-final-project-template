from models.__init__ import CURSOR, CONN

class Card_type:
    all = {}

    def __init__(self, name):
        self.name = name
    
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
        """ Create a new table to persist the attributes of card_type instances """
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
        """ Drop the table that persists card-type instances """
        sql = """
            DROP TABLE IF EXISTS card_types;
        """
        
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and id values of the current card_type object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's Primary Key as dictionary key"""
        sql = """
                INSERT INTO card_types (name)
                VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current card_type instance."""
        sql = """
            UPDATE card_types
            SET name = ?, id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current card_type instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM card_types
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name):
        """ Initialize a new card_type instance and save the object to the database """
        if name not in Card_type.all:
            card_type = cls(name)
            card_type.save()
            return card_type
        else: raise ValueError("Card type must be unused and valid!")

    @classmethod
    def instance_from_db(cls, row):
        """Return an card_type object having the attribute values from the table row."""

        # Check the dictionary for existing instance using the row's primary key
        card_type = cls.all.get(row[0])
        if card_type:
            # ensure attributes match row values in case local instance was modified
            card_type.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            card_type = cls(row[1])
            card_type.id = row[0]
            cls.all[card_type.id] = card_type
        return card_type


    @classmethod
    def get_all(cls):
        """Return a list containing one card_type object per table row"""
        sql = """
            SELECT *
            FROM card_types
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return card_type object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM card_types
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return card_type object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM card_types
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None