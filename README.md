# selenium_tests_page_object
Итоговый проект по автотестированию на selenium с использованием Page Object

запускается : 
pytest -v --tb=line --language=en test_main_page.py
суть теста - проверить что можно перейти на страницу логина с главной страницы

**pytest -v --tb=line --language=en -m need_review test_product_page.py
тест для peer-review**

pytest -s test_product_page_success_message.py
суть теста - проверки: сообщение о добавлении в корзину не появляется до добавления, сообщение исчезает по истечении 4 секунд
