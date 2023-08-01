Прототип проекта на тему "Разработка информационной системы для автоматизации тестирования персонала".

Database: "easy_tests"
Queryes in dir: src/BD.

How creat BD: create database "easy_tests", then execute queryes "create_tables_types.sql" → "create_function_view.sql" → "insert.sql".
*Before as execute "create_function_view.sql" check extension BD, must exist pgcrypto. If its not, execute "create extension pgcrypto" for "easy_tests" database.

After work done can start program src/__main__.py
