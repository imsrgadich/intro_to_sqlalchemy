import logging
from sqlalchemy import *

print('Creating a engine now')
engine = create_engine('sqlite:///')

print('Connecting to the engine')
connection = engine.connect()

print('Running a sql statement')
result = connection.execute('select 2+2')

print('The result is: %d' % (result.scalar()))

# Creation of the table
print('\nNow creating a table named `Person`.')
print('For creating table first we need to create a metadata object. '
      'Metadata object holds all the schemas and indexes of all the tables'
      ' created in the session.')
metadata = MetaData()
table = Table('person', metadata,
              Column('id', INTEGER, primary_key=True),
              Column('name', String(25), nullable=False))  # as this required field, use nullable
                                                           # as false

print('Check the table columns')
print(table.columns)
repr(table)

print('Check the metadata.')
print(metadata.tables)

print("The table is not yet created in the database. Its only defined."
      " Lets create it in the database. We use `create_all` def from "
      "metadata class.")
metadata.create_all(engine)  # metadata.drop_all(engine) to drop all the tables from the database

print("Manipulation of the tables in database"
      "We write here an insert clause.")
clause_insert = table.insert()

print("\nWe are printing here the clause\n")
print(clause_insert)

print("BEWARE that it just creates the clause not executes it.")
print("`clause` is an python object which contains SQL. use print(clause)` to check its contents."
      " Printing should give `INSERT INTO person (id, name) VALUES (:id, :name)`.")

print("Executing the insert clause next")
engine.execute(clause_insert, name='Srikant')

print("Lets confirm that the record has been inserted into the table."
      "We do it by using the select statement.")

clause_select = table.select()
print(clause_select)
engine.execute(clause_select)

print("We can add limit to the select statement also."
      "We could have simple done"
      "clause = table.select().limit(1).")
clause_select = clause_select.limit(1)
print(clause_select)

print("Adding the `order by to the select clause"
      "We are ")
clause_select = clause_select.order_by(table.column.name)