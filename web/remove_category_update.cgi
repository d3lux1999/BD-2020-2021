#!/usr/bin/python3 

import psycopg2, cgi
import login
form = cgi.FieldStorage()
#getvalue uses the names from the form in previous page 
category = form.getvalue('name')

print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Remove Category</title>') 
print('</head>')
print('<body>') 
connection = None

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials) 
    cursor = connection.cursor()
    # Making query
    data = (category)
    sql0 = f"DELETE FROM displayed_in WHERE name = '{category}';"
    cursor.execute(sql0, data)
    sql1 = f"DELETE FROM consists_of WHERE super_name = '{category}';"
    cursor.execute(sql1, data)
    sql2 = f"DELETE FROM consists_of WHERE sub_name = '{category}';"
    cursor.execute(sql2, data)
    sql3 = f"DELETE FROM simple_category WHERE category_name = '{category}';"
    cursor.execute(sql3, data)
    sql4 = f"DELETE FROM super_category WHERE category_name = '{category}';"
    cursor.execute(sql4, data)
    sql5 = f"DELETE FROM category WHERE name = '{category}';"
    cursor.execute(sql5, data)

    if data == None:
        raise Exception('None exception, check your input')
    # Feed the data to the SQL query as follows to avoid SQL injection 
    # The string has the {}, the variables inside format() will replace the {} 
    print('<h2>Query executed</h2>')
    print(f"<p>'{data}' removed if it exists</p>")
    # Commit the update (without this step the database will not change) 
    connection.commit()
    # Closing connection
    cursor.close() 
except Exception as e:
# Print errors on the webpage if they occur 
    print('<h1>An error occurred. :(</h1>') 
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
        connection.close() 
print('</body>')