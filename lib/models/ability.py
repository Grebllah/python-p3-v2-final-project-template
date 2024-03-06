from models.__init__ import CURSOR, CONN


class Ability:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def __repr__(self):
        return (f"<Ability {self.id}: {self.name}, {self.effect}>")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def effect(self):
        return self._effect

    @effect.setter
    def effect(self, effect):
        if isinstance(effect, str) and len(effect):
            self._effect = effect
        else:
            raise ValueError(
                "effect must be a non-empty string"
            )
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Ability instances """
        sql = """
            CREATE TABLE IF NOT EXISTS abilities (
            id INTEGER PRIMARY KEY,
            name TEXT,
            effect TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Ability instances """
        sql = """
            DROP TABLE IF EXISTS abilities;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, and effect values of the current Ability object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO abilities (name, effect)
                VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.effect))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Ability instance."""
        sql = """
            UPDATE abilities
            SET name = ?, effect = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.effect, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Ability instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM abilities
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, effect):
        """ Initialize a new Ability instance and save the object to the database """
        ability = cls(name, effect)
        ability.save()
        return ability

    @classmethod
    def instance_from_db(cls, row):
        """Return an Employee object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        ability = cls.all.get(row[0])
        if ability:
            # ensure attributes match row values in case local instance was modified
            ability.name = row[1]
            ability.effect = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            ability = cls(row[1], row[2])
            ability.id = row[0]
            cls.all[ability.id] = ability
        return ability

    @classmethod
    def get_all(cls):
        """Return a list containing one Ability object per table row"""
        sql = """
            SELECT *
            FROM abilities
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Ability object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM abilities
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Ability object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM abilities
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None