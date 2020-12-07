"""Write a wrapper class TableData for database table,
that when initialized with database name and table acts
as collection object (implements Collection protocol).
Assume all data has unique values in 'name' column. So, if

    presidents = TableData(database_name='example.sqlite',
        table_name='presidents')
then
    len(presidents) will give current amount of rows in
presidents table in database
    presidents['Yeltsin'] should return single data row for
president with name Yeltsin
    'Yeltsin' in presidents should return if president with
same name exists in table object

implements iteration protocol. i.e. you could use it in for loops::
for president in presidents:
print(president['name'])

all above mentioned calls should reflect most recent data.
If data in table changed after you created collection instance,
your calls should return updated data.
Avoid reading entire table into memory. When iterating through
records, start reading the first record, then go to the next one,
until records are exhausted. When writing tests, it's not always
necessary to mock database calls completely. Use supplied
example.sqlite file as database fixture file."""
import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        self.db = database_name
        self.table = table_name

    def start_session(self):
        try:
            conn = sqlite3.connect(self.db)
            return conn
        except sqlite3.Error:
            print("Connection cannot be established.")

    def __len__(self):
        conn = self.start_session()
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {self.table}")
        return cursor.fetchone()[0]

    def __getitem__(self, item):
        conn = self.start_session()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {self.table} where name="{item}"')
        data = cursor.fetchone()
        return data

    def __contains__(self, item):
        conn = self.start_session()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {self.table} where name="{item}"')
        data = cursor.fetchone()
        return bool(data)

    def __iter__(self):
        conn = self.start_session()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table}")
        for _ in range(self.__len__()):
            yield cursor.fetchone()


if __name__ == "__main__":
    presidents = TableData(database_name="example.sqlite", table_name="presidents")
    print(len(presidents))
    print(presidents["Trump"])
    print(presidents["Yeltsin"])
    print("Yeltsin" in presidents)

    for president in presidents:
        print(president["name"])
