import psycopg2

conn = psycopg2.connect(
     database="greengrocer", user='postgres', password='T@fari2022')


# Getting Data
def get_data(table_name):
    cursor = conn.cursor()
    t= f"select * from {table_name}"
    cursor.execute(t)
    all_data = cursor.fetchall()
    return all_data


## Inserting new fruit
def insert_f(values):
    cur = conn.cursor()
    new_fruit = "INSERT INTO fruits(fruit_name,buying_price, selling_price,quantity) VALUES(%s,%s,%s,%s)"
    cur.execute(new_fruit,values)
    conn.commit()




## Inserting new sale
def add_sale(values):
    cursor= conn.cursor()
    new_sale = "INSERT INTO sales(fruit_id,sale_quantity,sale_date) Values(%s,%s,now())"
    cursor.execute(new_sale,values)
    conn.commit()






