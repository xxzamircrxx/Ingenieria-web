from src.service import suma, resta, multiplica, divide, create_item_service, get_items_service, delete_item_service

def test_suma():
    assert suma(2,3) == 5

def test_resta():
    assert resta(5,3) == 2

def test_multiplica():
    assert multiplica(2,3) == 6

def test_divide():
    assert divide(6,3) == 2

def test_divide_zero():
    assert divide(5,0) == None

def test_create_item():
    item = {"name": "test"}
    result = create_item_service(item)
    assert result == item

def test_get_items():
    items = get_items_service()
    assert isinstance(items, list)

def test_delete_item_success():
    create_item_service({"name": "delete"})
    result = delete_item_service(0)
    assert result == True

def test_delete_item_fail():
    result = delete_item_service(999)
    assert result == False

def test_multiple_items():
    create_item_service({"a":1})
    create_item_service({"b":2})
    assert len(get_items_service()) >= 2