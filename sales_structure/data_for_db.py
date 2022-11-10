from datetime import datetime

import psycopg2

"""
Скрипт для добавления минимальных тестовых данных в БД.
Пароль такой длинный, потому что пароли в БД храняться в зашифрованном виде.
"""

con = psycopg2.connect(
    "dbname=postgres user=postgres password=153794862 host=127.0.0.1"
)
cur = con.cursor()

insert_sql_user = """
INSERT INTO auth_user (
id, username, password, is_superuser, first_name,
last_name, email, is_staff, is_active, date_joined)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

users = [
    {
        'id': 5,
        'username': 'worker5',
        'password': 'pbkdf2_sha256$390000$7xabV8SLuYAvvBEtiC9jTd$mpeeGQHrnZblxPtzG8TuHcvHywvQow9Hpgi5pnaWjpI=',
        'is_superuser': False,
        'first_name': '',
        'last_name': '',
        'email': '',
        'is_staff': False,
        'is_active': True,
        'date_joined': datetime.now()


    },
    {
        'id': 6,
        'username': 'worker6',
        'password': 'pbkdf2_sha256$390000$7xabV8SLuYAvvBEtiC9jTd$mpeeGQHrnZblxPtzG8TuHcvHywvQow9Hpgi5pnaWjpI=',
        'is_superuser': False,
        'first_name': '',
        'last_name': '',
        'email': '',
        'is_staff': False,
        'is_active': True,
        'date_joined': datetime.now()
    },
    {
        'id': 7,
        'username': 'worker7',
        'password': 'pbkdf2_sha256$390000$7xabV8SLuYAvvBEtiC9jTd$mpeeGQHrnZblxPtzG8TuHcvHywvQow9Hpgi5pnaWjpI=',
        'is_superuser': False,
        'first_name': '',
        'last_name': '',
        'email': '',
        'is_staff': False,
        'is_active': True,
        'date_joined': datetime.now()
    },
    {
        'id': 8,
        'username': 'worker8',
        'password': 'pbkdf2_sha256$390000$7xabV8SLuYAvvBEtiC9jTd$mpeeGQHrnZblxPtzG8TuHcvHywvQow9Hpgi5pnaWjpI=',
        'is_superuser': False,
        'first_name': '',
        'last_name': '',
        'email': '',
        'is_staff': False,
        'is_active': True,
        'date_joined': datetime.now()
    },
    {
        'id': 9,
        'username': 'worker9',
        'password': 'pbkdf2_sha256$390000$7xabV8SLuYAvvBEtiC9jTd$mpeeGQHrnZblxPtzG8TuHcvHywvQow9Hpgi5pnaWjpI=',
        'is_superuser': False,
        'first_name': '',
        'last_name': '',
        'email': '',
        'is_staff': False,
        'is_active': True,
        'date_joined': datetime.now()
    },
]
for user in users:
    cur.execute(insert_sql_user, [
        user['id'],
        user['username'],
        user['password'],
        user['is_superuser'],
        user['first_name'],
        user['last_name'],
        user['email'],
        user['is_staff'],
        user['is_active'],
        user['date_joined']
    ])
con.commit()


insert_sql_product = """
INSERT INTO sale_objects_product (id, name, model, on_sale_date)
VALUES(%s, %s, %s, %s)
"""

products = [
    {
        'id': 5,
        'name': 'Швеллер',
        'model': '5',
        'on_sale_date': datetime.now()
    },
    {
        'id': 6,
        'name': 'Швеллер',
        'model': '6',
        'on_sale_date': datetime.now()
    },
    {
        'id': 7,
        'name': 'Швеллер',
        'model': '7',
        'on_sale_date': datetime.now()
    },
    {
        'id': 8,
        'name': 'Швеллер',
        'model': '8',
        'on_sale_date': datetime.now()
    },
    {
        'id': 9,
        'name': 'Швеллер',
        'model': '9',
        'on_sale_date': datetime.now()
    },
    {
        'id': 10,
        'name': 'Швеллер',
        'model': '10',
        'on_sale_date': datetime.now()
    },
    {
        'id': 11,
        'name': 'Молоко',
        'model': '3%',
        'on_sale_date': datetime.now()
    },
    {
        'id': 12,
        'name': 'Творог из молока',
        'model': '5%',
        'on_sale_date': datetime.now()
    },
]

for product in products:
    cur.execute(insert_sql_product, [
        product['id'],
        product['name'],
        product['model'],
        product['on_sale_date']
    ])
con.commit()

insert_sql_address = """
INSERT INTO sale_objects_address (id, country, city, street, house)
VALUES(%s, %s, %s, %s, %s)
"""

addresses = [
    {
        'id': 5,
        'country': 'Россия',
        'city': 'Москва',
        'street': 'Ленина',
        'house': '10'
    },
    {
        'id': 6,
        'country': 'Россия',
        'city': 'Казань',
        'street': 'Ленина',
        'house': '15'
    },
    {
        'id': 7,
        'country': 'Беларусь',
        'city': 'Минск',
        'street': 'Ленина',
        'house': '120'
    },
    {
        'id': 8,
        'country': 'Беларусь',
        'city': 'Брест',
        'street': 'Крепости',
        'house': '12'
    },
    {
        'id': 9,
        'country': 'Беларусь',
        'city': 'Гродно',
        'street': 'Творожная',
        'house': '12'
    },
]

for address in addresses:
    cur.execute(insert_sql_address, [
        address['id'],
        address['country'],
        address['city'],
        address['street'],
        address['house']
    ])
con.commit()

insert_sql_contact = """
INSERT INTO sale_objects_contact (id, email, address_id) VALUES(%s, %s, %s)
"""

contacts = [
    {
        'id': 5,
        'email': 'mainemail@company5.com',
        'address_id': 5
    },
    {
        'id': 6,
        'email': 'mainemail@company6.com',
        'address_id': 6
    },
    {
        'id': 7,
        'email': 'mainemail@company7.com',
        'address_id': 7
    },
    {
        'id': 8,
        'email': 'mainemail@company8.com',
        'address_id': 8
    },
    {
        'id': 9,
        'email': 'mainemail@company9.com',
        'address_id': 9
    },
]
for contact in contacts:
    cur.execute(insert_sql_contact, [
        contact['id'],
        contact['email'],
        contact['address_id']
    ])
con.commit()


insert_sql_saleobjects = """
INSERT INTO sale_objects_saleobject (
id, role, name, debt, tree_id, level,
contacts_id, parent_id, create_date, lft, rght
) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

saleobjects = [
    {
        'id': 5,
        'role': 'factory',
        'name': 'Швеллерный завод',
        'debt': 0,
        'tree_id': 5,
        'level': 0,
        'contacts_id': 5,
        # 'parent_id': ,
        'create_date': datetime.now(),
        'lft': 1,
        'rght': 4,

    },
    {
        'id': 6,
        'role': 'dealership',
        'name': 'Швеллерный импортер',
        'debt': 0,
        'tree_id': 5,
        'level': 1,
        'contacts_id': 6,
        'parent_id': 5,
        'create_date': datetime.now(),
        'lft': 2,
        'rght': 4,
    },
    {
        'id': 7,
        'role': 'retail',
        'name': 'Швеллерный местный поставщик',
        'debt': 0,
        'tree_id': 5,
        'level': 2,
        'contacts_id': 7,
        'parent_id': 6,
        'create_date': datetime.now(),
        'lft': 3,
        'rght': 4,
    },
    {
        'id': 8,
        'role': 'factory',
        'name': 'Молочный завод',
        'debt': 0,
        'tree_id': 6,
        'level': 0,
        'contacts_id': 8,
        # 'parent_id': 6,
        'create_date': datetime.now(),
        'lft': 1,
        'rght': 4,
    },
    {
        'id': 9,
        'role': 'individual',
        'name': 'Домашний творог',
        'debt': 0,
        'tree_id': 6,
        'level': 1,
        'contacts_id': 9,
        'parent_id': 8,
        'create_date': datetime.now(),
        'lft': 2,
        'rght': 4,
    },


]
for saleobject in saleobjects:
    cur.execute(insert_sql_saleobjects, [
        saleobject['id'],
        saleobject['role'],
        saleobject['name'],
        saleobject['debt'],
        saleobject['tree_id'],
        saleobject['level'],
        saleobject['contacts_id'],
        saleobject.get('parent_id'),
        saleobject['create_date'],
        saleobject['lft'],
        saleobject['rght']
    ])
con.commit()

insert_sql_saleobject_products = """
INSERT INTO sale_objects_saleobject_products (saleobject_id, product_id)
VALUES(%s, %s)
"""

saleobject_products = [
    {
        'saleobject_id': 5,
        'product_id': 5
    },
    {
        'saleobject_id': 5,
        'product_id': 6
    },
    {
        'saleobject_id': 5,
        'product_id': 7
    },
    {
        'saleobject_id': 5,
        'product_id': 8
    },
    {
        'saleobject_id': 5,
        'product_id': 9
    },
    {
        'saleobject_id': 5,
        'product_id': 10
    },
    {
        'saleobject_id': 6,
        'product_id': 5
    },
    {
        'saleobject_id': 6,
        'product_id': 6
    },
    {
        'saleobject_id': 6,
        'product_id': 7
    },
    {
        'saleobject_id': 7,
        'product_id': 8
    },
    {
        'saleobject_id': 6,
        'product_id': 9
    },
    {
        'saleobject_id': 7,
        'product_id': 10
    },
    {
        'saleobject_id': 6,
        'product_id': 10
    },
    {
        'saleobject_id': 8,
        'product_id': 11
    },
    {
        'saleobject_id': 9,
        'product_id': 12
    }
]
for saleobject_product in saleobject_products:
    cur.execute(insert_sql_saleobject_products, [
        saleobject_product['saleobject_id'],
        saleobject_product['product_id']
    ])
con.commit()

insert_sql_saleobject_workers = """
INSERT INTO sale_objects_saleobject_workers(saleobject_id, user_id)
VALUES(%s, %s)
"""

workers = [
    {
        'saleobject_id': 5,
        'user_id': 5
    },
    {
        'saleobject_id': 6,
        'user_id': 6
    },
    {
        'saleobject_id': 7,
        'user_id': 7
    },
    {
        'saleobject_id': 8,
        'user_id': 8
    },
    {
        'saleobject_id': 9,
        'user_id': 9
    },
]

for worker in workers:
    cur.execute(insert_sql_saleobject_workers, [
        worker['saleobject_id'],
        worker['user_id']
    ])
con.commit()
