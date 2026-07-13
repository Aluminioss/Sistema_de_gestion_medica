-- SCRIPT COMPLETO DE BASE DE DATOS - CLÍNICA SALUD INTEGRAL

-- Crear base de datos
CREATE DATABASE IF NOT EXISTS salud_integral;
USE salud_integral;

-- TABLA 1: PACIENTES

DROP TABLE IF EXISTS pacientes;

CREATE TABLE pacientes (
    historia_clinica INT AUTO_INCREMENT PRIMARY KEY,
    nombre_apellido VARCHAR(150) NOT NULL,
    dni VARCHAR(15) UNIQUE NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    edad INT NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    obra_social VARCHAR(100),
    grupo_sanguineo VARCHAR(5),
    alergias TEXT,
    antecedentes TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_ultima_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_dni (dni),
    INDEX idx_nombre (nombre_apellido)
);

-- TABLA 2: MÉDICOS

DROP TABLE IF EXISTS medicos;

CREATE TABLE medicos (
    id_medico INT AUTO_INCREMENT PRIMARY KEY,
    nombre_apellido VARCHAR(150) NOT NULL,
    dni VARCHAR(15) UNIQUE NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    matricula VARCHAR(50) UNIQUE NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    dias_atencion TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_ultima_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_dni (dni),
    INDEX idx_especialidad (especialidad)
);

-- INSERCIÓN DE DATOS DE PRUEBA - PACIENTES

INSERT INTO pacientes 
(nombre_apellido, dni, fecha_nacimiento, edad, direccion, telefono, obra_social, grupo_sanguineo, alergias, antecedentes) 
VALUES 
('Juan Pérez García', '12345678', '1980-05-15', 44, 'Calle Falsa 123', '1122334455', 'OSDE', 'O+', 'Ninguna', 'Cirugía de apéndice en 2010'),
('María Gómez López', '87654321', '1995-10-22', 28, 'Av. Siempre Viva 742', '1199887766', 'IOMA', 'A-', 'Penicilina', 'Asma leve'),
('Carlos López Martínez', '23456789', '1975-03-08', 49, 'San Martín 456', '1155667788', 'PAMI', 'B+', 'Ninguna', 'Hipertensión controlada'),
('Ana María Rodríguez', '34567890', '1988-07-20', 36, 'Córdoba 789', '1166778899', 'Farmacia del Dr', 'AB+', 'Ninguna', 'Diabetes tipo 2'),
('Roberto Fernández Silva', '45678901', '1965-12-10', 58, 'Flores 101', '1177889900', 'OSPLAD', 'O-', 'Ninguna', 'Infarto en 2015, Stent colocado');

-- INSERCIÓN DE DATOS DE PRUEBA - MÉDICOS

INSERT INTO medicos 
(nombre_apellido, dni, telefono, email, matricula, especialidad, dias_atencion) 
VALUES 
('Dra. Ana Martínez González', '30123456', '1133445566', 'ana.martinez@saludintegral.com', 'MN 14589', 'Cardiología', 'Martes y Jueves de 10:00 a 16:00 hs'),
('Dr. Carlos Rodríguez Pérez', '31234567', '1144556677', 'carlos.rodriguez@saludintegral.com', 'MN 15678', 'Traumatología', 'Lunes, Miércoles y Viernes de 09:00 a 15:00 hs'),
('Dra. María López Silva', '32345678', '1155667788', 'maria.lopez@saludintegral.com', 'MN 16789', 'Pediatría', 'Lunes a Viernes de 14:00 a 19:00 hs'),
('Dr. Juan Fernández García', '33456789', '1166778899', 'juan.fernandez@saludintegral.com', 'MN 17890', 'Medicina General', 'Lunes a Viernes de 08:00 a 14:00 hs'),
('Dra. Patricia Gómez Martínez', '34567890', '1177889900', 'patricia.gomez@saludintegral.com', 'MN 18901', 'Dermatología', 'Martes, Jueves y Sábado de 10:00 a 17:00 hs');
