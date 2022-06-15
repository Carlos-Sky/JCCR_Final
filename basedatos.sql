CREATE DATABASE IF NOT EXISTS J_C_C_R_python;
USE J_C_C_R_python;
-- #******************************************
CREATE TABLE doctores(
  id int(25) auto_increment not null,
  nombre varchar(100),
  consultorio varchar(100),
  apellidos varchar(255),
  email varchar(255) not null,
  password varchar(255) not null,
  fecha date not null,
  CONSTRAINT pk_doctores PRIMARY KEY(id),
  CONSTRAINT uq_email UNIQUE(email)
) ENGINE = InnoDb;
-- #******************************************
CREATE TABLE citas(
  id int(25) auto_increment not null,
  doctor_id int(25) not null,
  consultorio varchar(100),
  titulo varchar(255) not null,
  descripcion MEDIUMTEXT,
  fecha date not null,
  CONSTRAINT pk_citas PRIMARY KEY(id),
  CONSTRAINT fk_consulta_doctor FOREIGN KEY(doctor_id) REFERENCES doctores(id)
) ENGINE = InnoDb;