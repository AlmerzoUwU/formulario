-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS mibasededatos;

-- Usar la base de datos recién creada
USE mibasededatos;

-- Crear la tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255)
);
