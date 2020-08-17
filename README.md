# Local_library_SF_D6
## Приложение "Личная библиотека" напписанное с помощью Django framework
***
### Функционал
Приложение позволяет добавлять, просматривать и редактировать книги и их авторов, а также хранить информацию об издательствах и друзьях, которым данные книги можно одалживать.
***
### Установка и запуск с помощью командной строки
- Клонируем репозиторий

    `git clone https://github.com/NikolaySorokin/Local_library_SF_D6.git`
- Заходим в папку проекта

    `cd Local_library_SF_D6`
- Создаем виртуальное окружение

    `python -m venv env`
- Активируем его

    для Windows: `env\Scripts\activate.bat`  
    для Linux: `source env/bin/activate`  
- Устанавливаем зависимости

    `pip install -r requirements.txt`
- Запускаем сервер

    `python manage.py runserver`
- Заходим по адресу http://127.0.0.1:8000/
***
### Доступ к админке
Создать суперюзера: `python manage.py createsuperuser`  
http://127.0.0.1:8000/admin  

