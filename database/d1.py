import sqlite3
conn=sqlite3.connect('database.db')
c=conn.cursor()

#c.execute('select * from ((customers inner join orders on customers.customerid=orders.customerid) inner join shippers on orders.shipperid = shippers.shipperid)')
#c.execute('select * from customers left join shippers on customers.customerid = shippers.shipperid')
#c.execute('select customername, orderid from customers left join orders on customers.customerid = orders.customerid')
#c.execute('select city from customers c, orders o where o.customerid = c.customerid')
#c.execute('select city from customers union select city from suppliers')
#c.execute('select city from customers union all select city from suppliers')
#c.execute('select city from customers where country = "Germany" union select city from suppliers where country = "Germany"')
#c.execute('select city from customers where country = "Germany" union all select city from suppliers where country = "Germany"')
#c.execute('select customername from customers union select suppliername from suppliers')
#c.execute('select count(customerid), country from customers group by country')
#c.execute('select count(customerid), country from customers group by country order by count(customerid) desc')
#c.execute('select count(shipperid) from orders group by shipperid') 
c.execute('select count(country), country from customers group by country ')
for n in c.fetchall():
    print(n)
conn.commit()
c.close()
