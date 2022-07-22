# selenium_tests_page_object
Итоговый проект по автотестированию на selenium с использованием Page Object

содержание папки pages: 
1. **base_page.py** - основной класс с методами, которые применяются по всему проекту
2. **main_page.py** - класс с методами для главной страницы. Класс MainPage - наследник класса BasePage
3. **login_page.py** - класс с методами для авторизации, наследник класса BasePage
4. **product_page.py** - класс с методами для страницы продукта, наследник класса BasePage
5. **basket_page.py** - класс с методами для страницы корзина, наследник класса BasePage
6. **locators.py** - локаторы для всех классов выше, в виде констант.

тесты:
* **test_main_page.py** проверить что можно перейти на страницу логина с главной страницы
* **test_product_page_success_message.py** проверки: сообщение о добавлении в корзину не появляется до добавления товара в корзину, сообщение исчезает по истечении 4 секунд
* **test_product_page.py** тест-кейсы:
  -  **test_guest_can_add_product_to_basket** проверяем что гость может добавить товар в корзину
  -  **test_guest_cant_see_product_in_basket_opened_from_product_page** проверяем что корзина содержит добавленный гостем товар
  -  **test_guest_can_go_to_login_page_from_product_page** гость может перейти на страницу авторизации со страницы товара
  -  **test_user_can_add_product_to_basket** проверяем что авторизованный пользователь может добавить товар в корзину
  -  **test_user_cant_see_product_in_basket_opened_from_product_page** проверяем что авторизованный пользовательне видит товаров в корзине, елси ничего не добавлял
  

запускается : 
**pytest -v --tb=line --language=en -m need_review test_product_page.py
тест для peer-review**

pytest -s test_product_page_success_message.py
суть теста - проверки: сообщение о добавлении в корзину не появляется до добавления, сообщение исчезает по истечении 4 секунд

pytest -v --tb=line --language=en test_main_page.py
суть теста - проверить что можно перейти на страницу логина с главной страницы
