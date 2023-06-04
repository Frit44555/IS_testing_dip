----------------------Options----------------------
/*
--Проверить расширения!!!
select * from pg_available_extensions;
select * from pg_extension;
--Обязательно к выполнению. Если нет расширения pgcrypto
create extension pgcrypto;
*/
--------------------------------------------


----------------------Drop functions----------------------
-- Функция поиска администратора
DROP FUNCTION IF EXISTS find_admin;

-- Функция регистрации администратора
DROP FUNCTION IF EXISTS registration_admin_on_easy_tests;

-- Функция изменения пароля администратора
DROP FUNCTION IF EXISTS change_admin_password;

-- Функция регистрации пользователя
DROP FUNCTION IF EXISTS registration_user_on_easy_tests;

-- Функция поиска пользователей
DROP FUNCTION IF EXISTS find_user;

-- Функция отправки рабочих данных ПО ТЕСТАМ
DROP FUNCTION IF EXISTS working_data_on_tests;

-- Функция отправки рабочих данных ПО УЧЕБНОМУ МАТЕРИАЛУ
DROP FUNCTION IF EXISTS working_data_on_lessons;

-- Функция отправки названия теста, времяни, типа, количества вопросов и примечания
DROP FUNCTION IF EXISTS get_name_time_type_note_on_test;

-- Функция отправки вопросов
DROP FUNCTION IF EXISTS get_questions;

-- Функция отправки ответов
DROP FUNCTION IF EXISTS get_answers;

-- Функция отправки содержания учебного материала
DROP FUNCTION IF EXISTS get_lesson;

-- Функция отправки ID и имени учебного материала через тег и группу
DROP FUNCTION IF EXISTS get_lesson_via_tag;

--Функция получения теста через тег и группу пользователя
DROP FUNCTION IF EXISTS get_test_via_teg;

-- Функция получения ВСЕХ результатов для администратора
DROP FUNCTION IF EXISTS get_results_all;

-- Функция получения результатов по пользователю
DROP FUNCTION IF EXISTS get_results_user;

-- Функция отправки списка пользователей для администратора
DROP FUNCTION IF EXISTS get_list_users;

-- Функция изменения группы пользователя
DROP FUNCTION IF EXISTS set_user_group;

-- Функция получения тегов через группы
DROP FUNCTION IF EXISTS get_tags_on_group;

-- Функция получения тегов
DROP FUNCTION IF EXISTS get_tags;

-- Функция отправки всех групп пользователей
DROP FUNCTION IF EXISTS get_groups_users;

-- Функция создания ответов.  ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_result И ВЫЗЫВАЕТСЯ ДО НЕЁ. 1
DROP FUNCTION IF EXISTS create_answer;

-- Функция создания результата.  ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_answer И ВЫЗЫВАЕТСЯ ПОСЛЕ НЕЁ. 2
DROP FUNCTION IF EXISTS create_result;

-- Функция создания вопросов. ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_test И ВЫЗЫВАЕТСЯ ДО НЕЁ. 1
DROP FUNCTION IF EXISTS create_question;

-- Функция создания теста.  ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_question И ВЫЗЫВАЕТСЯ ПОСЛЕ НЕЁ. 2
DROP FUNCTION IF EXISTS create_test;

-- Функция создания назначенного теста
DROP FUNCTION IF EXISTS create_assigned_test;

--Функция уменьшает количество попыток
DROP FUNCTION IF EXISTS minus_number_of_attempts;

-- Функция изменения состояния проверки назначенного теста
DROP FUNCTION IF EXISTS set_completed_in_assigned_test;

-- Функция создания учебного материала
DROP FUNCTION IF EXISTS create_lesson;

-- Функция добавления тега в группу
DROP FUNCTION IF EXISTS add_tag_in_groups_users;

-- Функция создания группы
DROP FUNCTION IF EXISTS create_group_user;

-- Функция создания тега
DROP FUNCTION IF EXISTS create_tag;

-- Функция получения назначенного теста для пользователя
DROP FUNCTION IF EXISTS get_assigned_tests_for_user;

-- Функция удаления тега
DROP FUNCTION IF EXISTS delete_tag;

-- Функция удаления группы
DROP FUNCTION IF EXISTS delete_group_user;

-- Функция ужаления пользователя
DROP FUNCTION IF EXISTS delete_user;
--------------------------------------------


----------------------Create VIEW----------------------
/*
Представление содержащее средние баллы получаемые по тесту. Тип теста входит в
представление, чтобы лишний раз не отображать к БД из приложение.
*/
DROP VIEW IF EXISTS middle_bals CASCADE;

----------------------Create function for VIEW----------------------
--Функция возвращающая все баллы по тесту
DROP FUNCTION IF EXISTS return_bals_on_test;

-- Функция получения среднего балла из представления
DROP FUNCTION IF EXISTS get_middle_bals_all;

-- Функция получения среднего балла из представления по тесту
DROP FUNCTION IF EXISTS get_middle_bals_on_test;
--------------------------------------------


----------------------Create functions----------------------
-- Функция поиска администратора
CREATE OR REPLACE FUNCTION find_admin(in_login text, in_password text)
RETURNS  TABLE(admin_id int, login varchar(64), name varchar(64), surname varchar(64), patronymic varchar(64), note text) AS
$$
	/*
	Описание: Эта функция вернёт значение строку, если введенные логин и пароль правильные
	и существуют в таблице администраторов. Если совпадений нет вернёт пустую выборку
	Принимает аргументы: логин, пароль
	Возвращает: ID администратора, логин, имя, фималия, отчество, примечания
	*/
DECLARE
	salts text;
BEGIN
	-- Поиск логина пользователя и соли
	SELECT admins.salt INTO salts 
	FROM admins
	WHERE admins.login = in_login;
	
	--Возврат значения
	RETURN QUERY
	--Возврящает рабочии данные
	SELECT admins.admin_id, admins.login, admins.name, admins.surname, admins.patronymic, admins.note
	FROM admins
	WHERE EXISTS(
		--Ищет пользователя
		SELECT admins.login
		FROM admins
		WHERE admins.password = crypt(in_password, salts) AND admins.login = in_login
	);
END
$$
LANGUAGE plpgsql;

-- Функция регистрации администратора
CREATE OR REPLACE FUNCTION registration_admin_on_easy_tests(in_login varchar(64), in_password varchar(60), in_name varchar(64),
															in_surname varchar(64), in_patronymic varchar(64) DEFAULT NULL,
															in_note text DEFAULT NULL)
RETURNS void AS
$$
	/*
	Описание: Регистрация администратора в базе данный easy_tests. Добавляет строку в таблицу "admins",
	при этом создаёт соль, с помощью этой соли хэширует пароль, а затем выполняет вставку.
	Принимает аргументы: логин, пароль, имя, фамилия, отчество, примерания
	*/
DECLARE
	new_salt text = gen_salt('bf');
	crypt_hash text = crypt(in_password, new_salt);
BEGIN
	INSERT INTO admins(login, password, salt, name, surname, patronymic, note)
	VALUES(in_login, crypt_hash, new_salt, in_name, in_surname, in_patronymic, in_note);
END
$$
LANGUAGE plpgsql;

-- Функция изменения пароля администратора
CREATE OR REPLACE FUNCTION change_admin_password(in_admin_id int, in_password varchar(60))
RETURNS void AS
$$
	/*
	Описание: Эта функция устанавливает новое значение поля пароля у администратора
	Принимает аргументы: ID администратора, новый пароль
	*/
DECLARE
	new_salt text = gen_salt('bf');
	crypt_hash text = crypt(in_password, new_salt);
BEGIN
	UPDATE admins
	SET password = in_password, salt = new_salt
	WHERE admin_id = in_admin_id;
END
$$
LANGUAGE plpgsql;

-- Функция регистрации пользователя
CREATE OR REPLACE FUNCTION registration_user_on_easy_tests(in_login varchar(64), in_password varchar(60), in_name varchar(64),
														   in_surname varchar(64), in_patronymic varchar(64) DEFAULT NULL)
RETURNS void AS
$$
	/*
	Описание: Регистрация пользователя в базе данный easy_tests. Добавляет строку в таблицу "users",
	при этом создаёт соль, с помощью этой соли хэширует пароль, а затем выполняет вставку.
	Принимает аргументы: логин, пароль, имя, фамилия, отчество
	*/
DECLARE
	new_salt text = gen_salt('bf');
	crypt_hash text = crypt(in_password, new_salt);
BEGIN
	INSERT INTO users(login, password, salt, name, surname, patronymic)
	VALUES(in_login, crypt_hash, new_salt, in_name, in_surname, in_patronymic);
END
$$
LANGUAGE plpgsql;

-- Функция поиска пользователей
CREATE OR REPLACE FUNCTION find_user(in_login text, in_password text)
RETURNS  TABLE(user_id int, group_user int, login varchar(64), name varchar(64), surname varchar(64),
			   patronymic varchar(64), date_registration timestamp, note text) AS
$$
	/*
	Описание: Эта функция вернёт значение строку, если введенные логин и пароль правильные
	и существуют в таблице. Если совпадений нет вернёт пустую выборку
	Принимает аргументы: логин, пароль
	Возвращает: ID группы, логин, имя, фималия, отчество, дату регистрации, примечания
	*/
DECLARE
	salts text;
BEGIN
	-- Поиск логина пользователя и соли
	SELECT users.salt INTO salts 
	FROM users
	WHERE users.login = in_login;
	
	--Возврат значения
	RETURN QUERY
	--Возврящает рабочии данные
	SELECT users.user_id, users.group_id, users.login, users.name, users.surname, users.patronymic,
			users.date_registration, users.note
	FROM users
	WHERE EXISTS(
		--Ищет пользователя
		SELECT users.login
		FROM users
		WHERE users.password = crypt(in_password, salts) AND users.login = in_login
	);
END
$$
LANGUAGE plpgsql;

-- Функция отправки рабочих данных ПО ТЕСТАМ
CREATE OR REPLACE FUNCTION working_data_on_tests(in_group_user int)
RETURNS TABLE(test_id int, quest_id int[], tag_id int, name varchar(200), type_test types_tests,
			  quantity_of_questions int, time_to_complete int, note text) AS
$$
	/*
	Описание: Эта функция вернёт данные, которые необходимы для сборки приложения
	Принимает аргументы: ID группы пользавателя
	Возвращает: ID теста, массив ID вопросов, ID тега, название теста, тип теста
				количество вопросов, время прохождения, примечание
	*/
DECLARE
	available int[];
BEGIN
	SELECT groups_users.available_tags INTO available
	FROM groups_users
	WHERE groups_users.group_id = in_group_user;
	
	RETURN QUERY
	SELECT tests.test_id, tests.quest_id, tests.tag_id, tests.name, tests.type_test,
			tests.quantity_of_questions, tests.time_to_complete, tests.note
	FROM tests
	WHERE tests.tag_id = ANY(available);
END
$$
LANGUAGE plpgsql;

--Функция получения теста через тег и группу пользователя
CREATE OR REPLACE FUNCTION get_test_via_teg(in_tag_name varchar(100), in_group_user int)
RETURNS TABLE(test_id int, quest_id int[], tag_id int, name varchar(200), type_test types_tests,
			  quantity_of_questions int, time_to_complete int, note text) AS
$$
	/*
	Описание: Эта функция вернёт данные тестов, по переданному тегу в соответствии с ограничением по группе.
	Принимает аргументы: имя тега, ID группы пользователя
	Возвращает: ID теста, массив ID вопросов, ID тега, название теста, тип теста
				количество вопросов, время прохождения, примечание
	*/
DECLARE
	available int[];
BEGIN
	SELECT groups_users.available_tags INTO available
	FROM groups_users
	WHERE groups_users.group_id = in_group_user;
	
	RETURN QUERY
	SELECT tests.test_id, tests.quest_id, tests.tag_id, tests.name, tests.type_test,
			tests.quantity_of_questions, tests.time_to_complete, tests.note
	FROM tests
	JOIN tags USING(tag_id)
	WHERE tests.tag_id = ANY(available)
		AND tags.name = in_tag_name
		AND tests.tag_id = tags.tag_id;
END
$$
LANGUAGE plpgsql;

--Функция возвращающая все баллы по тесту
CREATE OR REPLACE FUNCTION return_bals_on_test(in_test_id int)
RETURNS SETOF int AS
$$
	/*
	Описание: Возвращяет все когда либо полученные баллы всеми пользователями по тесту.
	Принимает аргументы: ID теста
	Возвращает: таблицу баллов
	*/
DECLARE
	--запись которая будет содержать ID задания и верность ответа на него
	answer_bals record;
	--полученный балл за задание
	bal int;
BEGIN
	-- для кажждой записи в ответах ДЛЯ 1 ТЕСТА
	FOR answer_bals IN SELECT quest_id, correct FROM answers
					JOIN results on answers.answer_id = ANY(results.answer_id)
					WHERE results.test_id = in_test_id
	LOOP
		--если ответ был верным
		IF answer_bals.correct THEN
			--достать балл за это задание
			SELECT bals INTO bal
			FROM questions
			WHERE questions.quest_id = answer_bals.quest_id;
		ELSE
			--иначе задание проваленно
			bal := 0;
		END IF;
		--вернуть балл
		RETURN NEXT bal;
	END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Функция отправки названия теста, времяни, типа, количества вопросов и примечания
CREATE OR REPLACE FUNCTION get_name_time_type_note_on_test(in_test_id int)
RETURNS TABLE(name varchar(200), type_test types_tests, quantity_of_questions int, time_to_complete int, note text) AS
$$
	/*
	Описание: Эта функция вернёт названия теста, время прохождения, тип, количества вопросов и примечание
	Принимает аргументы: ID теста
	Возвращает: название теста, тип теста, количество вопросов, время прохождения, примечание
	*/
	SELECT tests.name, tests.type_test, tests.quantity_of_questions, tests.time_to_complete, tests.note
	FROM tests
	WHERE tests.tag_id = in_test_id;
$$
LANGUAGE SQL;

-- Функция отправки всех групп пользователей
CREATE OR REPLACE FUNCTION get_groups_users()
RETURNS SETOF groups_users AS
$$
	/*
	Описание: Эта функция вернёт все группы пользователей.
	Возвращает: ID группы, название, массив доступных тегов.
	*/
	SELECT *
	FROM groups_users;
$$
LANGUAGE SQL;

-- Функция отправки рабочих данных ПО УЧЕБНОМУ МАТЕРИАЛУ
CREATE OR REPLACE FUNCTION working_data_on_lessons(in_group_user int)
RETURNS TABLE(lesson_id int, name varchar(200)) AS
$$
	/*
	Описание: Эта функция вернёт данные, которые необходимы для сборки приложения
	Принимает аргументы: ID группы пользавателя
	Возвращает: ID учебного материала и его название
	*/
DECLARE
	available int[];
BEGIN
	-- Доступные теги для группы пользователей 
	SELECT groups_users.available_tags INTO available
	FROM groups_users
	WHERE groups_users.group_id = in_group_user;
	
	RETURN QUERY
	SELECT lessons.lesson_id, lessons.name
	FROM lessons
	WHERE lessons.tag_id = ANY(available);
END
$$
LANGUAGE plpgsql;

-- Функция отправки содержания учебного материала
CREATE OR REPLACE FUNCTION get_lesson(in_lesson int)
RETURNS text AS
$$
	/*
	Описание: Эта функция вернёт содержимое учебного материала
	Принимает аргументы: ID учебного материала
	Возвращает: текст
	*/
	SELECT lessons.content
	FROM lessons
	WHERE lessons.lesson_id = in_lesson;
$$
LANGUAGE SQL;

-- Функция отправки ID и имени учебного материала через тег и группу
CREATE OR REPLACE FUNCTION get_lesson_via_tag(in_tag_name varchar(100), in_group_user int)
RETURNS TABLE(lesson_id int, name varchar(200)) AS
$$
	/*
	Описание: Эта функция вернёт ID и имя учебного материала найденного по заданному тегу и ограничителю в виде группы пользователя.
	Принимает аргументы: имя тега, ID группы.
	Возвращает: текст
	*/
DECLARE
	available int[];
BEGIN
	-- Доступные теги для группы пользователей 
	SELECT groups_users.available_tags INTO available
	FROM groups_users
	WHERE groups_users.group_id = in_group_user;
	
	RETURN QUERY
	SELECT lessons.lesson_id, lessons.name
	FROM lessons
	JOIN tags USING(tag_id)
	WHERE lessons.tag_id = ANY(available)
			AND tags.name = in_tag_name
			AND tags.tag_id = lessons.tag_id;
END;
$$
LANGUAGE plpgsql;

-- Функция отправки вопросов
CREATE OR REPLACE FUNCTION get_questions(in_test int)
RETURNS SETOF questions AS
$$
	/*
	Описание: Эта функция вернёт все вопросы по заданному тесту
	Принимает аргументы: ID теста
	Возвращает: таблицу вопросов
	*/
DECLARE
	quantity_of_quest int[];
BEGIN
	SELECT tests.quest_id INTO quantity_of_quest
	FROM tests
	WHERE tests.test_id = in_test;
	
	RETURN QUERY
	SELECT * FROM questions
	WHERE questions.quest_id = ANY(quantity_of_quest);
END
$$
LANGUAGE plpgsql;

-- Функция отправки ответов
CREATE OR REPLACE FUNCTION get_answers(in_result_id int)
RETURNS SETOF answers AS
$$
	/*
	Описание: Эта функция вернёт все ответы по заданному результату
	Принимает аргументы: ID результата
	Возвращает: таблицу ответов
	*/
DECLARE
	quantity_of_quest int[];
BEGIN
	SELECT results.answer_id INTO quantity_of_quest
	FROM results
	WHERE results.result_id = in_result_id;
	
	RETURN QUERY
	SELECT * FROM answers
	WHERE answers.answer_id = ANY(quantity_of_quest);
END
$$
LANGUAGE plpgsql;

-- Функция отправки списка пользователей для администратора
CREATE OR REPLACE FUNCTION get_list_users()
RETURNS TABLE(user_id int, group_id int, login varchar(64), name varchar(64), surname varchar(64),
			  patronymic varchar(64), date_registration date, note text) AS		  
$$
	/*
	Описание: Эта функция отправляет необходимую информацию по пользователям для администратора
	Возвращает: ID пользователя, группу пользователя, логин, имя, фамилию, отчество, 
				дату регистрации примечание
	*/
	SELECT user_id, group_id, login, name, surname, patronymic, date_registration, note
	FROM users
	ORDER BY date_registration DESC;
$$
LANGUAGE SQL;

-- Функция изменения группы пользователя
CREATE OR REPLACE FUNCTION set_user_group(chenging_user int, user_group int)
RETURNS void AS
$$
	/*
	Описание: Эта функция устанавливает новое значение поля группы у пользователя в таблице "user_groups"
	Принимает аргументы: ID пользователя, ID группы
	*/
	UPDATE users
	SET group_id = user_group
	WHERE user_id = chenging_user;
$$
LANGUAGE SQL;

-- Функция получения тегов через группы
CREATE OR REPLACE FUNCTION get_tags_on_group(group_tags int)
RETURNS SETOF tags AS
$$
	/*
	Описание: Эта функция отправляет доступные теги, по одной группе
	Принимает аргументы: ID группы
	Возвращает: таблицу тегов
	*/
DECLARE
	available int[];
BEGIN
	-- Доступные теги для группы
	SELECT groups_users.available_tags INTO available
	FROM groups_users
	WHERE groups_users.group_id = group_tags;
	
	RETURN QUERY
	SELECT *
	FROM tags
	WHERE tags.tag_id = ANY(available);
END
$$
LANGUAGE plpgsql;

-- Функция получения тегов
CREATE OR REPLACE FUNCTION get_tags()
RETURNS SETOF tags AS
$$
	/*
	Описание: Эта функция отправляет все теги
	Возвращает: таблицу тегов
	*/
	SELECT *
	FROM tags;
$$
LANGUAGE SQL;

-- Функция получения результатов по пользователю
CREATE OR REPLACE FUNCTION get_results_user(in_user_id int)
RETURNS SETOF results AS
$$
	/*
	Описание: Эта функция отправляет результаты пользователя.
	Принимает аргументы: ID пользователя
	Возвращает: таблицу результатов
	*/
	SELECT *
	FROM results
	WHERE results.user_id = in_user_id;
$$
LANGUAGE SQL;

-- Функция получения ВСЕХ результатов
CREATE OR REPLACE FUNCTION get_results_all()
RETURNS SETOF results AS
$$
	/*
	Описание: Эта функция отправляет все результаты, предназначено для администратора.
	Возвращает: таблицу результатов
	*/
	SELECT *
	FROM results;
$$
LANGUAGE SQL;

-- Функция создания ответа
CREATE OR REPLACE FUNCTION create_answer(in_quest_id int, in_answered text, in_correct boolean DEFAULT FALSE)
RETURNS int AS
$$
	/*
	ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_result И ВЫЗЫВАЕТСЯ ДО НЕЁ. 1
	Описание: Эта функция создаёт запись ответа в таблице "answers"
	Принимает аргументы: ID вопроса, данный за задание ответ, правильность ответа
	Возвращает: ID только что созданного ответов
	*/
	INSERT INTO answers(quest_id, answered, correct)
	VALUES(in_quest_id, in_answered, in_correct)
	RETURNING answer_id;
$$
LANGUAGE SQL;

-- Функция создания результата
CREATE OR REPLACE FUNCTION create_result(in_user_id int, in_test_id int, in_answer_id int[], in_time_start timestamp without time zone,
										in_time_finish timestamp without time zone, in_comment_user text DEFAULT NULL,
										in_verified boolean DEFAULT FALSE)
RETURNS void AS
$$
	/*
	ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_answer И ВЫЗЫВАЕТСЯ ПОСЛЕ НЕЁ. 2
	Описание: Эта функция создаёт запись результатов в таблицу "result"
	Принимает аргументы: ID пользователя, ID теста, массив ID ответов, время начала, время конца, комментарии пользователя
	*/
	INSERT INTO results(user_id, test_id, answer_id, time_start, time_finish, comment_user, verified)
	VALUES(in_user_id, in_test_id, in_answer_id, in_time_start, in_time_finish, in_comment_user, in_verified);
$$
LANGUAGE SQL;

-- Функция создания вопроса
CREATE OR REPLACE FUNCTION create_question(in_type_quest types_questions, in_question text,
										  in_bals int DEFAULT NULL, in_image bytea DEFAULT NULL,
										  in_answer1 text DEFAULT NULL, in_answer2 text DEFAULT NULL,
										  in_answer3 text DEFAULT NULL, in_answer4 text DEFAULT NULL,
										  in_right_answer text DEFAULT NULL)
RETURNS int AS
$$
	/*
	ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_test И ВЫЗЫВАЕТСЯ ДО НЕЁ. 1
	Описание: Эта функция создаёт запись вопроса в таблице "questions"
	Принимает аргументы: тип вопроса, ВОПРОС, балл, картинка, четыре ответа, и правильный ответ
	Возвращает: ID только что созданного вопроса
	*/
	INSERT INTO questions(type_quest, question, bals, image, answer1, answer2, answer3, answer4, right_answer)
	VALUES(in_type_quest, in_question, in_bals, in_image, in_answer1, in_answer2, in_answer3, in_answer4,
			in_right_answer)
	RETURNING quest_id;
$$
LANGUAGE SQL;

-- Функция создания теста
CREATE OR REPLACE FUNCTION create_test(in_quest_id int[], in_tag_id int, in_name varchar(200), in_type_test types_tests,
									  in_quantity_of_questions int, in_time_to_complete int, in_note text DEFAULT NULL)
RETURNS void AS
$$
	/*
	ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_question И ВЫЗЫВАЕТСЯ ПОСЛЕ НЕЁ. 2
	Описание: Эта функция создаёт запись теста в таблице "tests"
	Принимает аргументы: массив ID вопросов, ID тег, название, тип теста, количество заданий,
						 время выполнения теста, примечание
	*/
	INSERT INTO tests(quest_id, tag_id, name, type_test, quantity_of_questions, time_to_complete, note)
	VALUES(in_quest_id, in_tag_id, in_name, in_type_test, in_quantity_of_questions, in_time_to_complete, in_note);
$$
LANGUAGE SQL;

--Функция уменьшает количество попыток
CREATE OR REPLACE FUNCTION minus_number_of_attempts(in_assigned_test_id int)
RETURNS void AS
$$
	/*
	Описание: Эта функция количество попыток у нужной записи в таблице "assigned_test".
	Принимает аргументы: ID назначенного теста. 
	*/
	UPDATE assigned_tests
	SET number_of_attempts = (CASE WHEN number_of_attempts = 0 THEN 0
							  ELSE number_of_attempts - 1
							 END)
	WHERE assigned_test_id = in_assigned_test_id;
$$
LANGUAGE SQL;

-- Функция создания назначенного теста
CREATE OR REPLACE FUNCTION create_assigned_test(in_test_id int, in_user_id int, in_deadline timestamp without time zone,
											   in_number_of_attempts int DEFAULT 1, in_note text DEFAULT NULL)
RETURNS void AS
$$
	/*
	Описание: Эта функция создаёт запись в таблице "assigned_test"
	Принимает аргументы: ID тест, ID пользователь, конечный срок, количество попыток, примечание 
	*/
	INSERT INTO assigned_tests(test_id, user_id, deadline, number_of_attempts, note)
	VALUES(in_test_id, in_user_id, in_deadline, in_number_of_attempts, in_note);
$$
LANGUAGE SQL;

-- Функция изменения состояния проверки назначенного теста
CREATE OR REPLACE FUNCTION set_completed_in_assigned_test(in_assigned_test_id int, in_completed boolean DEFAULT False)
RETURNS void AS
$$
	/*
	Описание: Эта функция устанавливает значение поля "completed" у таблицы "assigned_test"
	Принимает аргументы: ID назначеный тест, состояние проверки
	*/
	UPDATE assigned_tests
	SET completed = in_completed
	WHERE assigned_test_id = in_assigned_test_id;
$$
LANGUAGE SQL;

-- Функция создания учебного материала
CREATE OR REPLACE FUNCTION create_lesson(in_name varchar(200), in_content text, in_tag_id int DEFAULT 1)
RETURNS void AS
$$
	/*
	Описание: Эта функция создаёт запись в таблице "lessons"
	Принимает аргументы: название, содержимое
	*/
	INSERT INTO lessons(tag_id, name, content)
	VALUES(in_tag_id, in_name, in_content);
$$
LANGUAGE SQL;

-- Функция создания тега
CREATE OR REPLACE FUNCTION create_tag(in_name varchar(100))
RETURNS void AS
$$
	/*
	Описание: Эта функция создаёт запись в таблице "tags"
	Принимает аргументы: название тематики
	*/
	INSERT INTO tags(name)
	VALUES(in_name);
$$
LANGUAGE SQL;


-- Функция создания группы
CREATE OR REPLACE FUNCTION create_group_user(in_name varchar(200), in_available_tag int[])
RETURNS void AS
$$
	/*
	Описание: Эта функция создаёт запись в таблице "groups_users"
	Принимает аргументы: имя, массив доступных тегов
	*/
	INSERT INTO groups_users(name, available_tags)
	VALUES(in_name, in_available_tag);
$$
LANGUAGE SQL;

-- Функция добавления тега в группу
CREATE OR REPLACE FUNCTION add_tag_in_groups_users(in_group_id int, in_available_tag int[])
RETURNS void AS
$$
	/*
	Описание: Эта функция добавляет тег в поле "available_tags" в таблице "groups_users"
	Принимает аргументы: имя, содержимое
	*/
	UPDATE groups_users
	SET available_tags = available_tags || in_available_tag
	WHERE group_id = in_group_id;
$$
LANGUAGE SQL;

-- Функция получения назначенного теста для пользователя
CREATE OR REPLACE FUNCTION get_assigned_tests_for_user(in_user_id int)
RETURNS TABLE(assigned_test_id int, test_id int, appointment_time timestamp without time zone,
			 deadline timestamp without time zone, completed boolean, number_of_attempts int,
			 note text) AS
$$
	/*
	Описание: Эта функция отправляет данные о назначенных тестах по конкретному пользователю
	Принимает аргументы: ID пользователя
	Возвращает: ID назначенного теста, ID теста, назначенное время, крайний срок, состояние о завершённости,
				кол-во попыток, примечания
	*/
	SELECT assigned_test_id, test_id, appointment_time, deadline, completed,
			number_of_attempts, note
	FROM assigned_tests
	WHERE user_id = in_user_id;
$$
LANGUAGE SQL;

-- Функция удаления тега
CREATE OR REPLACE FUNCTION delete_tag(in_tag_id int)
RETURNS void AS
$$
	/*
	Описание: Эта функция удаляет тег по заданному ID.
	Принимает аргументы: ID тега.
	*/
	UPDATE groups_users SET available_tags = array_remove(available_tags, in_tag_id);
	DELETE FROM tags WHERE tag_id = in_tag_id;
$$
LANGUAGE SQL;

-- Функция получения тегов через группы
CREATE OR REPLACE FUNCTION delete_group_user(in_group_id int)
RETURNS void AS
$$
	/*
	Описание: Эта функция удаляет группу по заданному ID.
	Принимает аргументы: ID группы.
	*/
	UPDATE users
	SET group_id = 1
	WHERE group_id = in_group_id;
	
	DELETE FROM groups_users WHERE groups_users.group_id = in_group_id;
$$
LANGUAGE SQL;

-- Функция ужаления пользователя
CREATE OR REPLACE FUNCTION delete_user(in_user_id int)
RETURNS void AS
$$
	/*
	Описание: Эта функция удаляет пользователя по заданному ID.
	Принимает аргументы: ID пользователя.
	*/
	DELETE FROM assigned_tests WHERE user_id = in_user_id;
	DELETE FROM results WHERE user_id = in_user_id;
	DELETE FROM users WHERE user_id = in_user_id;
$$
LANGUAGE SQL;
--------------------------------------------


----------------------Create view----------------------
/*
Представление содержащее средние баллы получаемые по тесту. Тип теста входит в
представление, чтобы лишний раз не ображаться к БД из приложение.
*/
CREATE VIEW middle_bals AS
SELECT tests.test_id, type_test, SUM(rbt)::float8 / (COUNT(rbt)/tests.quantity_of_questions)::float8 AS middle_bal
FROM tests
JOIN LATERAL return_bals_on_test(tests.test_id) AS rbt on TRUE
GROUP BY tests.test_id;
--------------------------------------------


----------------------Create function for view----------------------
-- Функция получения среднего балла из представления
CREATE OR REPLACE FUNCTION get_middle_bals_all()
RETURNS SETOF middle_bals AS
$$
	/*
	Описание: Эта функция отправляет все средние баллы по тестам
	Возвращает: представление middle_bals
	*/
	SELECT *
	FROM middle_bals;
$$
LANGUAGE SQL;

-- Функция получения среднего балла из представления по тесту
CREATE OR REPLACE FUNCTION get_middle_bals_on_test(in_test_id int)
RETURNS SETOF middle_bals AS
$$
	/*
	Описание: Эта функция отправляет средниЙ балл по тесту
	Принимает аргументы: ID теста
	Возвращает: представление middle_bals
	*/
	SELECT *
	FROM middle_bals
	WHERE test_id = in_test_id;
$$
LANGUAGE SQL;
--------------------------------------------
