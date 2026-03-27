data = []

# CRUD
def create_item_service(item):
    data.append(item)
    return item

def get_items_service():
    return data

def delete_item_service(index):
    if index < len(data):
        data.pop(index)
        return True
    return False

# FUNCIONES (para tests + TDD)
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b