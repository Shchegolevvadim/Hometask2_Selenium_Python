import pytest

@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""
@pytest.fixture()
def x_selector2():
    return """/html/body/div/main/div/div/div/form/div[2]/label/input"""

@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""
@pytest.fixture
def btn_selector():
    return "button"

@pytest.fixture
def result():
    return "401"



@pytest.fixture()
def hello_user():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""

@pytest.fixture()
def create_post():
    return """#create-btn"""

@pytest.fixture()
def x_selector4():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture()
def button_save_post():
    return """#create-item > div > div > div:nth-child(7) > div > button > span"""

@pytest.fixture()
def search_text():
    return """//*[@id="app"]/main/div/div[1]/h1"""
