import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="comercializadora_lozano"
)



cursor=db.cursor()
cursor.execute('SHOW DATABASES')

for dbs in cursor:
    print(dbs)


print('--------------------')
cursor.execute("SHOW TABLES")
for n in cursor:
    print(n)

#cursor.execute("""INSERT INTO categorias (id_categoria, nombre)VALUES ('2','Productos') """)
#db.commit()
#cursor.execute("""DELETE FROM marcas WHERE id_marca=3""")
#db.commit()
#cursor.execute('select * from marcas')
#for ap in cursor:
#    print(ap[0])
#    print(ap[1])
    
#cursor.execute("""DELETE FROM marcas WHERE id_marca=3""")
#db.commit()
#cursor.execute("""UPDATE categorias SET nombre= 'PRODUCTOS' WHERE id_categoria=2""")
#db.commit()
#cursor.execute('select * from categorias')
#for ap in cursor:
#    print(ap[0])
#    print(ap[1])
cursor.execute("""CREATE TABLE pedidos(
    id_pedidos INT(20) UNSIGNED NOT NULL AUTO_INCREMENT, PRIMARY KEY,
    nombre VARCHAR (100) NOT NULL,
    fecha_pedido date NOT NULL
);""")
db.commit()
cursor.execute('select * from pedidos')
for ap in cursor:
    print(ap[0])
    print(ap[1])
    print(ap[2])
    print(ap[3])