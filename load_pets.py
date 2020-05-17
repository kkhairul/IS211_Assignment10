#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sqlite3 as lite

person = (
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23),
)

pet = (
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
)

person_pet = (
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
)


# In[9]:


def main():
    """Creates a database and checks if data already exists.
    If data exists, it will reset the database and re-insert the data. 
    """

    try:
        db = lite.connect('pets.db')
        cursor = db.cursor()

        cursor.execute('DROP TABLE IF EXISTS person')
        cursor.execute('DROP TABLE IF EXISTS pet')
        cursor.execute('DROP TABLE IF EXISTS person_pet')

        cursor.execute(
            '''CREATE TABLE person(
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER
                )'''
        )

        cursor.execute(
            '''CREATE TABLE pet(
                id INTEGER PRIMARY KEY,
                name TEXT, 
                breed TEXT,
                age INTEGER,
                dead INTEGER
                )'''
        )

        cursor.execute(
            '''CREATE TABLE person_pet(
                person_id INTEGER,
                pet_id INTEGER
                )'''
        )

        cursor.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", person)
        cursor.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pet)
        cursor.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)

        db.commit()
        db.close()

    except Exception:
        print('ERROR: Your database could not be loaded.')


if __name__ == '__main__':
    main()


# In[ ]:




