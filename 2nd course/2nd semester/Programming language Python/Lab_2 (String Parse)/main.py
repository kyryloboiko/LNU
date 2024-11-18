'''
Parse string and write them to dictionary and write to SQL database
record: "Record(id=1, date=26.02.2004, content=Some example, user=1, title=Example title)"
user: "User(id=1, first_name=test name, second_name=test surname, email=test@test.test, password=123)"
'''
import sqlite3

db = sqlite3.connect('database.db')
record = "Record(id=1, date=26.02.2004, content=Some example, user=1, title=Example title)"
user = "User(id=1, first_name=test name, second_name=test surname, email=test@test.test, password=123)"


def parse_string(string: str):
    result = {}
    if string[0] == 'R':
        string = string[7:-1]
    elif string[0] == 'U':
        string = string[5:-1]
    pairs = string.split(', ')
    for pair in pairs:
        key, value = pair.split('=')
        key = key.strip()
        value = value.strip()
        result[key] = value
    return result


def write_to_db(string: str, database):
    cursor = database.cursor()
    table = "Record" if string[2] == 'R' else "User"
    data = parse_string(string)
    print(table)

    # Check if the table exists
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
    result = cursor.fetchone()

    # Create the table if it doesn't exist
    if result is None:
        create_table_sql = f"CREATE TABLE {table} (id TEXT)"
        cursor.execute(create_table_sql)

    # Check if the columns exist
    cursor.execute(f"PRAGMA table_info({table})")
    existing_columns = [column[1] for column in cursor.fetchall()]

    # Add missing columns
    for key, value in data.items():
        if key not in existing_columns:
            add_column_sql = f"ALTER TABLE {table} ADD COLUMN {key} TEXT"
            cursor.execute(add_column_sql)

    # Insert data
    placeholders = ', '.join(['?'] * len(data))
    column_names = ', '.join(data.keys())
    insert_sql = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"
    cursor.execute(insert_sql, tuple(data.values()))

    database.commit()
    cursor.close()

print(parse_string(record))
write_to_db(record, db)
db.close()
