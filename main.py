import psycopg2

with psycopg2.connect(database="askar_homework", user="postgres", password="Luxury443") as conn:
    with conn.cursor() as cur:
        def create_db(conn):
            cur.execute("""
            DROP TABLE clients_phone;
            DROP TABLE clients;
            """)
            cur.execute("""
                CREATE TABLE clients(
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(80) NOT NULL,
                    last_name VARCHAR(80) NOT NULL,
                    email VARCHAR(80) NOT NULL
                );
                """)
            cur.execute("""
                CREATE TABLE clients_phone(
                    id SERIAL PRIMARY KEY,
                    phone VARCHAR(40),
                    clients_id INTEGER REFERENCES clients(id)
                );
                """)
            conn.commit()
        create_db(conn)

        def add_client(conn, first_name, last_name, email):
            cur.execute("""
                        INSERT INTO clients(first_name,last_name,email) VALUES(%s,%s,%s);
                      """, (first_name,last_name,email))
        conn.commit()
        add_client(conn,'Askar', 'Mullahanov', 'vfjhdsgg@gmail.com')
        add_client(conn, 'Nikita', 'Maslenikov', 'gidghdsgh@gmail.com')
        add_client(conn, 'Andrey', 'Hrulev', 'wqrukuwjytwg@gmail.com')
        cur.execute("""
            SELECT * FROM clients;
            """)
        print(cur.fetchall())

        def add_phone(conn, clients_id, phone):
            cur.execute("""
                INSERT INTO clients_phone(clients_id,phone) VALUES (%s,%s);
                """, (clients_id,phone))
        conn.commit()
        add_phone(conn, 1, '89874562156')
        add_phone(conn, 2, '89375433258')
        add_phone(conn, 3, '89276543734')

        cur.execute("""
            SELECT * from clients_phone;
        """)
        print(cur.fetchall())


        def update_data(id, first_name=None, last_name=None, email=None):
            if first_name != None:
                cur.execute("""
                    UPDATE clients SET first_name =%s
                    WHERE id =%s;
                    """, (id,first_name))
            conn.commit()
        update_data('Egor',3)

        cur.execute("""
            SELECT * FROM clients;
            """)
        print(cur.fetchall())

        def delete_phone(conn, clients_id):
            cur.execute("""
                    DELETE FROM clients_phone WHERE id=%s;
                    """, (clients_id,))
            conn.commit()
        delete_phone(conn,2)

        cur.execute("""
            SELECT * FROM clients_phone;
            """)
        print(cur.fetchall())

        def delete_client(conn,clients_id):
            cur.execute("""
            DELETE FROM clients WHERE id=%s;
            """,(clients_id,))
            conn.commit()
        delete_client(conn,2)

        cur.execute("""
                SELECT * FROM clients;
                """)
        print(cur.fetchall())


        def find_client(conn, first_name=None, last_name=None, email=None):
            cur.execute(""" SELECT * FROM clients
                        where first_name=%s or last_name=%s or email=%s""", (first_name, last_name, email,))

        find_client(conn, 'Askar', 'None', 'None',)
        print(cur.fetchall())

conn.close()