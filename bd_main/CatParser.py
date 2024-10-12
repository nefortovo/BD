import csv
import psycopg2


def connect_to_db():
    return psycopg2.connect(
        dbname="IvanDevelopLR2",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )


def insert_data(cursor, table_name, columns, data):
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
    cursor.execute(query, data)


def main():
    conn = connect_to_db()
    cursor = conn.cursor()

    with open('categories.txt', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            row[1] = row[1] if row[1] else None
            insert_data(cursor, 'SouvenirCategories', ['ID', 'IdParent', 'Name'], row)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
