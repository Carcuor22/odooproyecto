-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 07-02-2025 a las 08:14:46
-- Versión del servidor: 8.0.40
-- Versión de PHP: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `TallerMecanico`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Cliente`
--

CREATE TABLE `Cliente` (
  `NIF` char(9) NOT NULL,
  `tipo` enum('empresa','particular','Junta Andalucía','organismo público') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Cliente`
--

INSERT INTO `Cliente` (`NIF`, `tipo`) VALUES
('12345678A', 'particular'),
('23456789B', 'empresa'),
('34567890C', 'Junta Andalucía'),
('45678901D', 'organismo público'),
('56789012E', 'particular');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Conceptos`
--

CREATE TABLE `Conceptos` (
  `idConcepto` int NOT NULL,
  `descripcion` char(100) DEFAULT NULL,
  `precio` float DEFAULT NULL,
  `manoObra` float DEFAULT NULL,
  `reparacion_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Conceptos`
--

INSERT INTO `Conceptos` (`idConcepto`, `descripcion`, `precio`, `manoObra`, `reparacion_id`) VALUES
(1, 'Cambio de aceite', 50.5, 100, 1),
(2, 'Reparación de frenos', 200.75, 120, 2),
(3, 'Sustitución de embrague', 350, 100, 3),
(4, 'Revisión eléctrica', 100, 100, 4),
(5, 'Cambio de neumáticos', 300.25, 80, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `LineaReparacion`
--

CREATE TABLE `LineaReparacion` (
  `idLineaReparacion` int NOT NULL,
  `cantidad` int DEFAULT NULL,
  `descripcion` char(100) DEFAULT NULL,
  `importe` float DEFAULT NULL,
  `reparacion_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `LineaReparacion`
--

INSERT INTO `LineaReparacion` (`idLineaReparacion`, `cantidad`, `descripcion`, `importe`, `reparacion_id`) VALUES
(1, 2, 'Aceite 5W30', 30, 1),
(2, 1, 'Pastillas de freno', 120, 2),
(3, 1, 'Embrague completo', 300, 3),
(4, 1, 'Cableado eléctrico', 150, 4),
(5, 4, 'Neumáticos Pirelli', 380, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Mecanico`
--

CREATE TABLE `Mecanico` (
  `NIF` char(9) NOT NULL,
  `especializacion` enum('mecánica','electricidad','pintura') DEFAULT NULL,
  `salario` float DEFAULT NULL,
  `foto` blob,
  `fecha_contratacion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Mecanico`
--

INSERT INTO `Mecanico` (`NIF`, `especializacion`, `salario`, `foto`, `fecha_contratacion`) VALUES
('12345678A', 'mecánica', 2000.5, NULL, '2020-01-15'),
('23456789B', 'electricidad', 2200.75, NULL, '2019-03-20'),
('34567890C', 'pintura', 1800, NULL, '2021-05-10'),
('45678901D', 'mecánica', 2100, NULL, '2018-07-25'),
('56789012E', 'electricidad', 2300.25, NULL, '2020-09-30');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Mecanico_Reparacion`
--

CREATE TABLE `Mecanico_Reparacion` (
  `mecanico_id` char(9) NOT NULL,
  `reparacion_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Mecanico_Reparacion`
--

INSERT INTO `Mecanico_Reparacion` (`mecanico_id`, `reparacion_id`) VALUES
('12345678A', 1),
('23456789B', 2),
('34567890C', 3),
('45678901D', 4),
('56789012E', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Persona`
--

CREATE TABLE `Persona` (
  `NIF` char(9) NOT NULL,
  `nombre` char(50) DEFAULT NULL,
  `correo` char(50) DEFAULT NULL,
  `direccion` char(100) DEFAULT NULL,
  `telefono` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Persona`
--

INSERT INTO `Persona` (`NIF`, `nombre`, `correo`, `direccion`, `telefono`) VALUES
('12345678A', 'Juan Pérez', 'juan.perez@mail.com', 'Calle Mayor 10', 600123456),
('23456789B', 'María López', 'maria.lopez@mail.com', 'Avenida Central 5', 610234567),
('34567890C', 'Carlos Gómez', 'carlos.gomez@mail.com', 'Plaza España 20', 620345678),
('45678901D', 'Ana Sánchez', 'ana.sanchez@mail.com', 'Calle Luna 15', 630456789),
('56789012E', 'Luis Fernández', 'luis.fernandez@mail.com', 'Paseo del Sol 30', 640567890);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Reparacion`
--

CREATE TABLE `Reparacion` (
  `idReparacion` int NOT NULL,
  `fecha_ini` datetime DEFAULT NULL,
  `fecha_fin` datetime DEFAULT NULL,
  `total` float DEFAULT NULL,
  `descripcion` text,
  `cliente_id` char(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Reparacion`
--

INSERT INTO `Reparacion` (`idReparacion`, `fecha_ini`, `fecha_fin`, `total`, `descripcion`, `cliente_id`) VALUES
(1, '2023-01-10 08:00:00', '2023-01-10 14:00:00', 150.5, 'Cambio de aceite y revisión general', '12345678A'),
(2, '2023-02-15 09:00:00', '2023-02-15 16:00:00', 320.75, 'Reparación de frenos', '23456789B'),
(3, '2023-03-20 10:00:00', '2023-03-20 18:00:00', 450, 'Sustitución de embrague', '34567890C'),
(4, '2023-04-25 11:00:00', '2023-04-25 15:00:00', 200, 'Revisión eléctrica', '45678901D'),
(5, '2023-05-30 12:00:00', '2023-05-30 17:00:00', 380.25, 'Cambio de neumáticos', '56789012E');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Vehiculo`
--

CREATE TABLE `Vehiculo` (
  `matricula` char(10) NOT NULL,
  `marca` char(50) DEFAULT NULL,
  `modelo` char(50) DEFAULT NULL,
  `motor` enum('eléctrico','gasolina','diésel','híbrido','híbrido enchufable') DEFAULT NULL,
  `foto` blob,
  `cliente_id` char(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Vehiculo`
--

INSERT INTO `Vehiculo` (`matricula`, `marca`, `modelo`, `motor`, `foto`, `cliente_id`) VALUES
('1121JKL', 'BMW', 'i3', 'híbrido enchufable', NULL, '45678901D'),
('1234ABC', 'Toyota', 'Corolla', 'gasolina', NULL, '12345678A'),
('3141MNO', 'Honda', 'Civic', 'híbrido', NULL, '56789012E'),
('5678DEF', 'Tesla', 'Model 3', 'eléctrico', NULL, '23456789B'),
('9101GHI', 'Ford', 'Focus', 'diésel', NULL, '34567890C');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Cliente`
--
ALTER TABLE `Cliente`
  ADD PRIMARY KEY (`NIF`);

--
-- Indices de la tabla `Conceptos`
--
ALTER TABLE `Conceptos`
  ADD PRIMARY KEY (`idConcepto`),
  ADD KEY `reparacion_id` (`reparacion_id`);

--
-- Indices de la tabla `LineaReparacion`
--
ALTER TABLE `LineaReparacion`
  ADD PRIMARY KEY (`idLineaReparacion`),
  ADD KEY `reparacion_id` (`reparacion_id`);

--
-- Indices de la tabla `Mecanico`
--
ALTER TABLE `Mecanico`
  ADD PRIMARY KEY (`NIF`);

--
-- Indices de la tabla `Mecanico_Reparacion`
--
ALTER TABLE `Mecanico_Reparacion`
  ADD PRIMARY KEY (`mecanico_id`,`reparacion_id`),
  ADD KEY `reparacion_id` (`reparacion_id`);

--
-- Indices de la tabla `Persona`
--
ALTER TABLE `Persona`
  ADD PRIMARY KEY (`NIF`);

--
-- Indices de la tabla `Reparacion`
--
ALTER TABLE `Reparacion`
  ADD PRIMARY KEY (`idReparacion`),
  ADD KEY `cliente_id` (`cliente_id`);

--
-- Indices de la tabla `Vehiculo`
--
ALTER TABLE `Vehiculo`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `cliente_id` (`cliente_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Conceptos`
--
ALTER TABLE `Conceptos`
  MODIFY `idConcepto` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `LineaReparacion`
--
ALTER TABLE `LineaReparacion`
  MODIFY `idLineaReparacion` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `Reparacion`
--
ALTER TABLE `Reparacion`
  MODIFY `idReparacion` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Cliente`
--
ALTER TABLE `Cliente`
  ADD CONSTRAINT `Cliente_ibfk_1` FOREIGN KEY (`NIF`) REFERENCES `Persona` (`NIF`);

--
-- Filtros para la tabla `Conceptos`
--
ALTER TABLE `Conceptos`
  ADD CONSTRAINT `Conceptos_ibfk_1` FOREIGN KEY (`reparacion_id`) REFERENCES `Reparacion` (`idReparacion`);

--
-- Filtros para la tabla `LineaReparacion`
--
ALTER TABLE `LineaReparacion`
  ADD CONSTRAINT `LineaReparacion_ibfk_1` FOREIGN KEY (`reparacion_id`) REFERENCES `Reparacion` (`idReparacion`);

--
-- Filtros para la tabla `Mecanico`
--
ALTER TABLE `Mecanico`
  ADD CONSTRAINT `Mecanico_ibfk_1` FOREIGN KEY (`NIF`) REFERENCES `Persona` (`NIF`);

--
-- Filtros para la tabla `Mecanico_Reparacion`
--
ALTER TABLE `Mecanico_Reparacion`
  ADD CONSTRAINT `Mecanico_Reparacion_ibfk_1` FOREIGN KEY (`mecanico_id`) REFERENCES `Mecanico` (`NIF`),
  ADD CONSTRAINT `Mecanico_Reparacion_ibfk_2` FOREIGN KEY (`reparacion_id`) REFERENCES `Reparacion` (`idReparacion`);

--
-- Filtros para la tabla `Reparacion`
--
ALTER TABLE `Reparacion`
  ADD CONSTRAINT `Reparacion_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `Cliente` (`NIF`);

--
-- Filtros para la tabla `Vehiculo`
--
ALTER TABLE `Vehiculo`
  ADD CONSTRAINT `Vehiculo_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `Cliente` (`NIF`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
