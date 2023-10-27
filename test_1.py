# Условие: Добавить в наш тестовый проект шаг добавления поста после входа.
# Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
#
# Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.




import yaml
from module import Site
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])
def test_step1(x_selector1, x_selector2,x_selector3, btn_selector, result):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", "button")
    btn.click()
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == result
def test_step2(x_selector1, x_selector2, btn_selector, hello_user):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata['login'])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata['password'])
    time.sleep(3)
    btn = site.find_element("css", btn_selector)
    btn.click()
    time.sleep(3)
    element = site.find_element("xpath", hello_user)
    assert element.text == f"Hello, {testdata['login']}"
def test_step3(create_post, x_selector4, button_save_post, search_text):
    time.sleep(3)
    btn2 = site.find_element("css", create_post)
    btn2.click()
    time.sleep(3)
    input3 = site.find_element("xpath", x_selector4)
    input3.send_keys("New post for test")
    time.sleep(3)
    btn3 = site.find_element("css", button_save_post)
    btn3.click()
    time.sleep(3)
    element2 = site.find_element("xpath", search_text)
    assert element2.text == "New post for test"
    site.close()




