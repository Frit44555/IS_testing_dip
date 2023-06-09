----------------------Drop roles----------------------
DROP OWNED BY easy_tests_admins;
DROP ROLE IF EXISTS easy_tests_admins;
DROP USER IF EXISTS user_IS;
--------------------------------------------


----------------------Create role----------------------
CREATE ROLE easy_tests_admins;
CREATE USER user_IS WITH PASSWORD 'Q43Ndki87fF79fhLba';

----------------------WARNING----------------------
REVOKE CREATE ON SCHEMA public FROM public;
REVOKE ALL ON DATABASE easy_tests FROM public;
--------------------------------------------

--Даём доступ
--Возможность коннектиться
GRANT CONNECT ON DATABASE easy_tests TO easy_tests_admins;

--Проводить определённые операции на northwind
GRANT USAGE ON SCHEMA public TO easy_tests_admins;

--На уровне БД northwind_admins могут создовать схемы
GRANT CREATE ON SCHEMA public TO easy_tests_admins;
--Также позволить создавать внутри схемы (бд)
GRANT CREATE ON DATABASE easy_tests TO easy_tests_admins;

--Присоеденение пользователей к роли
GRANT easy_tests_admins TO user_IS;

--Доступ к таблицам роли easy_tests_admins
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE
public.groups_users,
public.users,
public.tags,
public.tests,
public.assigned_tests,
public.lessons,
public.questions
TO easy_tests_admins;

GRANT SELECT, INSERT, UPDATE ON TABLE
public.answers,
public.results
TO easy_tests_admins;

GRANT SELECT, UPDATE ON TABLE public.admins
TO easy_tests_admins;
--------------------------------------------
