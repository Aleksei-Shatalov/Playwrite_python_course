Автоматизация тестирования с помощью Playwright Python базовый курс

Создание виртуального окружения в новом проекте:  
python3 -m venv .venv  
Активировать его:  
source .venv/bin/activate
обновить pip:  
python -m pip install --upgrade pip
установить нужные зависимости, например:  
pip install pytest requests или pip install -r requirements.txt (если есть файл)
Проверить, что используется именно окружение:
which python - Должно показать примерно: .../my_project/.venv/bin/python
Создать тест в файле например test_api.py и pytest сам находит файл, запускается командой:
python -m pytest -v или pytest -v
либо: pytest (путь и имя файла если нужно запустить 1 файл)
А выйти из окружения:
deactivate


Запись сценария в код через Codegen:
playwright codegen demo.playwright.dev/todomvc/#/
Узнать доступные опции:
playwright codegen --help


Сайты для тренировки написания тестов:
https://www.globalsqa.com/samplepagetest/
https://demoqa.com/
Чек-боксы и переключатели
https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html
https://the-internet.herokuapp.com/checkboxes
https://demoqa.com/checkbox
https://demoqa.com/radio-button
Выпадающий список
https://the-internet.herokuapp.com/dropdown
Кнопки
https://demoqa.com/buttons
https://letcode.in/buttons
Загрузка и скачивание  
https://demoqa.com/upload-download
https://practice-automation.com/file-download/
https://practice-automation.com/file-upload/
Всплывающие окна и алерты
https://webdriveruniversity.com/Popup-Alerts/index.html
https://demoqa.com/modal-dialogs
https://practice-automation.com/popups/
Таблицы
https://the-internet.herokuapp.com/tables
https://demoqa.com/webtables
http://uitestingplayground.com/dynamictable
Авторизация
https://the-internet.herokuapp.com/login
https://webdriveruniversity.com/Login-Portal/index.html
Заполнение форм 
https://webdriveruniversity.com/Contact-Us/contactus.html
https://demoqa.com/automation-practice-form
https://practice-automation.com/form-fields/
https://letcode.in/edit
https://www.globalsqa.com/samplepagetest/
Тестовые сайты
https://www.saucedemo.com/
https://demo.applitools.com/
