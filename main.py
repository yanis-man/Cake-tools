import re

BASE_URL = "C:/wamp64/www"
APP_NAME = "AgoraSite"
TABLE_PATH = f"{BASE_URL}/{APP_NAME}/src/Model/Table"
ENTITY_PATH = f"{BASE_URL}/{APP_NAME}/src/Model/Entity"

print("Enter table name (CakePhP form) :")
table_name = str(input())

print("Enter entity name (CakePhP form) :")
entity_name = str(input())

print(f"\nTable name : {table_name} \nEntity name : {entity_name} \n\nConfirm (y/n) ?")
confirm = str(input())

if confirm.lower() == "y":
    table_file = open(f"{TABLE_PATH}/{table_name}.php", "w")
    entity_file = open(f"{ENTITY_PATH}/{entity_name}.php", "w")

    table_template = open("./templates/table.txt", 'r').read()
    table_template = re.sub('{}', table_name, table_template)

    entity_template = open("./templates/entity.txt", 'r').read()
    entity_template = re.sub('{}', entity_name, entity_template)

    table_file.write(table_template)
    entity_file.write(entity_template)

    print(entity_template)
