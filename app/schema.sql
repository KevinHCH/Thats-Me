-- CREACION DE LA BASE DE DATOS
CREATE DATABASE THATS_ME ENCODING='UTF8';
SET TIMEZONE=+2;--CEST TIMEZONE
--Conexion a la base de datos, el nombre debe en minusc
\c thats_me;
DROP TABLE IF EXISTS ROLES CASCADE;
CREATE TABLE ROLES (
	id SERIAL PRIMARY KEY,
	role_name VARCHAR(100)
);

DROP TABLE IF EXISTS PALETTES CASCADE;
CREATE TABLE PALETTES (
	id SERIAL PRIMARY KEY,
	short_name VARCHAR(100),
	palette_value VARCHAR(255)
);

DROP TABLE IF EXISTS USERS CASCADE;
CREATE TABLE USERS (
	id SERIAL PRIMARY KEY,
	role_id SERIAL,
	palette_id SERIAL,
	name VARCHAR(100),
	surname VARCHAR(100),
	mail_handle VARCHAR(100),
	mail_server VARCHAR(100),
	cookie VARCHAR(255),
	password VARCHAR(255),
	description TEXT,
	CONSTRAINT fk_roles FOREIGN KEY (role_id) REFERENCES ROLES(id) ON DELETE CASCADE,
	CONSTRAINT fk_palettes FOREIGN KEY (palette_id) REFERENCES PALETTES(id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS PHOTOS CASCADE;
CREATE TABLE PHOTOS (
	id SERIAL PRIMARY KEY,
	user_id SERIAL,
	name VARCHAR(100),
	path VARCHAR(255),
	tags VARCHAR(255),
	creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_users FOREIGN KEY (user_id) REFERENCES USERS(id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS CLIENTS;
CREATE TABLE CLIENTS (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	mail_handle VARCHAR(100),
	mail_server VARCHAR(100),
	description VARCHAR(255),
	send_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP	
);

-- DUMMY DATA
INSERT INTO public.palettes
(short_name, palette_value)
VALUES('base', 'darkred');

INSERT INTO ROLES (role_name) VALUES ('admin');
INSERT INTO ROLES (role_name) VALUES ('user');

INSERT INTO public.users
(palette_id, "name", surname, mail_handle, mail_server, "password", description,role_id)
VALUES(1,'test', 'surtest', 'test', 'gm.com', '1234', 'This is a test user', 2);

INSERT INTO public.users
(palette_id, "name", surname, mail_handle, mail_server, "password", description,role_id)
VALUES(1,'admin', 'admin', 'admin', 'gm.com', '1234', 'This is the admin user', 1);

INSERT INTO public.photos
("name", "path", tags, creation_date,user_id)
VALUES
('First photo', '1.jpg', 'photo, pex', CURRENT_TIMESTAMP, 2),
('Second Photo', '2.jpg', 'photo, pex', CURRENT_TIMESTAMP, 2),
('Third Photo', '3.jpg', 'photo, pex', CURRENT_TIMESTAMP, 1)