----------------------Drop tables----------------------
DROP TABLE IF EXISTS admins;
DROP TABLE IF EXISTS results;
DROP TABLE IF EXISTS assigned_tests;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tests;
DROP TABLE IF EXISTS answers;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS groups_users;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS tags;
--------------------------------------------


----------------------Drop types----------------------
DROP TYPE IF EXISTS types_questions;
DROP TYPE IF EXISTS types_tests;
--------------------------------------------


----------------------Create types----------------------
--For column 'tupe_quest' in table question
CREATE TYPE types_questions AS ENUM('ONE ANSWER', 'MANY ANSWERS', 'SCALE', 'FREE RESPONSE');

--For column 'tupe_test' in table tests
CREATE TYPE types_tests AS ENUM('SCALE', 'FREE RESPONSE', 'MIXED', 'PREDEFINED');
--------------------------------------------


----------------------Create tables----------------------
--Name: admins, type: TABLE
CREATE TABLE admins(
	admin_id int GENERATED ALWAYS AS IDENTITY (START WITH 10000 INCREMENT BY 1) NOT NULL,
	login varchar(64) UNIQUE NOT NULL,
	password varchar(60) NOT NULL,
	salt varchar(32) NOT NULL,
	name varchar(64) NOT NULL,
	surname varchar(64) NOT NULL,
	patronymic varchar(64) NULL,
	note text NULL,
	
	CONSTRAINT PK_admins_admin_id PRIMARY KEY(admin_id)
);

--Name: questions, type: TABLE
CREATE TABLE questions(
	quest_id int GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
	type_quest types_questions NOT NULL,
	bals int DEFAULT NULL,
	image bytea DEFAULT NULL,
	question text NOT NULL,
	answer1 text DEFAULT NULL,
	answer2 text DEFAULT NULL,
	answer3 text DEFAULT NULL,
	answer4 text DEFAULT NULL,
	right_answer text DEFAULT NULL,
	
	CONSTRAINT PK_questions_quest_id PRIMARY KEY(quest_id)
);

--Name: tags, type: TABLE
CREATE TABLE tags(
	tag_id int GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
	name varchar(100) UNIQUE NOT NULL,
	
	CONSTRAINT PK_tags_tag_id PRIMARY KEY(tag_id)
);

--Name: groups_users, type: TABLE
CREATE TABLE groups_users(
	group_id int GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
	name varchar(100) NOT NULL,
	available_tags int[] NOT NULL,
	
	CONSTRAINT PK_group_users_group_id PRIMARY KEY(group_id)
);

--Name: lessons, type: TABLE
CREATE TABLE lessons(
	lesson_id int GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
	tag_id int DEFAULT 1 NOT NULL,
	name varchar(200) UNIQUE NOT NULL,
	content text NOT NULL,
	
	CONSTRAINT PK_lessons_lesson_id PRIMARY KEY(lesson_id),
	CONSTRAINT FK_lessons_tags FOREIGN KEY(tag_id) REFERENCES tags
);

--Name: tests, type: TABLE
CREATE TABLE tests(
	test_id int GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
	quest_id int[] NOT NULL,
	tag_id int NOT NULL,
	name varchar(200) UNIQUE NOT NULL,
	type_test types_tests NOT NULL,
	quantity_of_questions int DEFAULT 10 NOT NULL,
	time_to_complete int DEFAULT 15 NOT NULL,
	note text NULL,
	
	CONSTRAINT PK_tests_test_id PRIMARY KEY(test_id),
	CONSTRAINT CHK_quantity_of_questions CHECK(quantity_of_questions BETWEEN 5 AND 60),
	CONSTRAINT CHL_time_to_complete CHECK(time_to_complete BETWEEN 5 AND 60),
	CONSTRAINT FK_tests_tags FOREIGN KEY(tag_id) REFERENCES tags
);

--Name: answers, type: TABLE
CREATE TABLE answers(
	answer_id int GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
	quest_id int NOT NULL,
	answered text NOT NULL,
	correct boolean DEFAULT FALSE,
	
	CONSTRAINT PK_answers_answer_id PRIMARY KEY(answer_id),
	CONSTRAINT FK_answers_questions FOREIGN KEY(quest_id) REFERENCES questions
);

--Name: users, type: TABLE
CREATE TABLE users(
	user_id int GENERATED ALWAYS AS IDENTITY (START WITH 10000 INCREMENT BY 1) NOT NULL,
	group_id int DEFAULT 1 NOT NULL,
	login varchar(64) UNIQUE NOT NULL,
	password varchar(60) NOT NULL,
	salt varchar(32) NOT NULL,
	name varchar(64) NOT NULL,
	surname varchar(64) NOT NULL,
	patronymic varchar(64) NULL,
	date_registration timestamp without time zone DEFAULT now() NOT NULL,
	note text NULL,
	
	CONSTRAINT PK_users_user_id PRIMARY KEY(user_id),
	CONSTRAINT FK_users_groups_users FOREIGN KEY(group_id) REFERENCES groups_users
);

--Name: assigned_tests, type: TABLE
CREATE TABLE assigned_tests(
	assigned_test_id int GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
	test_id int NOT NULL,
	user_id int NOT NULL,
	appointment_time timestamp without time zone DEFAULT now() NOT NULL,
	deadline timestamp without time zone NOT NULL,
	completed boolean DEFAULT FALSE NOT NULL,
	number_of_attempts int DEFAULT 1 NOT NULL,
	note text NULL,
	
	CONSTRAINT PK_assigned_tests_assigned_test_id PRIMARY KEY(assigned_test_id),
	CONSTRAINT CHK_number_of_attempts CHECK(number_of_attempts BETWEEN 0 AND 5),
	CONSTRAINT FK_assigned_tests_tests FOREIGN KEY(test_id) REFERENCES tests,
	CONSTRAINT FK_assigned_tests_users FOREIGN KEY(user_id) REFERENCES users
);

CREATE TABLE results(
	result_id int GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
	user_id int NOT NULL,
	test_id int NOT NULL,
	answer_id int[] NOT NULL,
	time_start timestamp without time zone NOT NULL,
	time_finish timestamp without time zone NOT NULL,
	comment_admin text NULL,
	comment_user text NULL,
	verified boolean DEFAULT FALSE,
	
	CONSTRAINT PK_results_result_id PRIMARY KEY(result_id),
	CONSTRAINT FK_results_users FOREIGN KEY(user_id) REFERENCES users,
	CONSTRAINT FK_results_tests FOREIGN KEY(test_id) REFERENCES tests
);
--------------------------------------------
