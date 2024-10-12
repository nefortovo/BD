import pandas as pd
import psycopg2


conn = psycopg2.connect(
    dbname="IvanDevelopLR2",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

statuses = "procurementstatuses"
providers = "providers"
procurements = "souvenirprocurements"
ps = "ProcurementSouvenirs"
souvenir = "Souvenirs"
stories = "SouvenirStores"

cur = conn.cursor()

cur.execute(f"INSERT INTO {statuses} (Name) VALUES ('bad') RETURNING ID")
statusId = cur.fetchone()

cur.execute(f"INSERT INTO {providers} (Name, Email, ContactPerson) VALUES ('SBERBANK', 'test@mail.ru', 'IVAN') RETURNING ID")
providerId = cur.fetchone()

cur.execute(f"INSERT INTO {procurements} (IdProvider, Data, IdStatus) VALUES ('{providerId[0]}', '2024-04-05', '{statusId[0]}') RETURNING ID")
procurementsId = cur.fetchone()

cur.execute(f"SELECT ID FROM {souvenir} WHERE Id = '2'")
souvenirId = cur.fetchone()

cur.execute(f"INSERT INTO {ps} (IdSouvenir, IdProcurement, Amount, Price) VALUES ('{souvenirId[0]}', '{procurementsId[0]}', '12', '10') RETURNING ID")
psId = cur.fetchone()

cur.execute(f"INSERT INTO {stories} (IdProcurement, IdSouvenir, Amount) VALUES ('{procurementsId[0]}', '{souvenirId[0]}', '11') RETURNING ID")
storiesId = cur.fetchone()

conn.commit()
conn.close()