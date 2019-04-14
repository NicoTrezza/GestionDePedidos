-- MySQL Script generated by MySQL Workbench
-- 04/13/19 21:44:04
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema GestorPedidos
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `GestorPedidos` ;

-- -----------------------------------------------------
-- Schema GestorPedidos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `GestorPedidos` DEFAULT CHARACTER SET utf8 ;
USE `GestorPedidos` ;

-- -----------------------------------------------------
-- Table `GestorPedidos`.`Login`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`Login` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`Login` (
  `idLogin` INT NOT NULL AUTO_INCREMENT,
  `mail` VARCHAR(45) NOT NULL,
  `contrasenia` VARCHAR(100) NOT NULL,
  `permisos` TINYINT(1) NOT NULL,
  `estado` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idLogin`),
  UNIQUE INDEX `mail_UNIQUE` (`mail` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`TipoPersona`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`TipoPersona` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`TipoPersona` (
  `idTipoPersona` INT NOT NULL AUTO_INCREMENT,
  `rol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idTipoPersona`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`Persona`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`Persona` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`Persona` (
  `idPersona` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `dni` INT NOT NULL,
  `emailPersona` VARCHAR(45) NULL,
  `tipoPersona` INT NOT NULL,
  `login` INT NULL,
  PRIMARY KEY (`idPersona`),
  INDEX `fk_Persona_Login_idx` (`login` ASC),
  INDEX `fk_Persona_TipoPersona1_idx` (`tipoPersona` ASC),
  UNIQUE INDEX `dni_UNIQUE` (`dni` ASC),
  CONSTRAINT `fk_Persona_Login`
    FOREIGN KEY (`login`)
    REFERENCES `GestorPedidos`.`Login` (`idLogin`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Persona_TipoPersona1`
    FOREIGN KEY (`tipoPersona`)
    REFERENCES `GestorPedidos`.`TipoPersona` (`idTipoPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`Departamento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`Departamento` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`Departamento` (
  `idDepartamento` INT NOT NULL AUTO_INCREMENT,
  `nombreDepartamento` VARCHAR(60) NOT NULL,
  PRIMARY KEY (`idDepartamento`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`Tutoria`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`Tutoria` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`Tutoria` (
  `idTutoria` INT NOT NULL AUTO_INCREMENT,
  `motivo` VARCHAR(45) NULL,
  `fecha1desde` DATETIME NOT NULL,
  `fecha1hasta` DATETIME NOT NULL,
  `fecha2desde` DATETIME NOT NULL,
  `fecha2hasta` DATETIME NOT NULL,
  `fecha3desde` DATETIME NOT NULL,
  `fecha3hasta` DATETIME NOT NULL,
  `personaTutoria` INT NOT NULL,
  `Departamento_idDepartamento` INT NOT NULL,
  `fechaactual` DATETIME NOT NULL,
  PRIMARY KEY (`idTutoria`),
  INDEX `fk_Tutoria_Persona1_idx` (`personaTutoria` ASC),
  INDEX `fk_Tutoria_Departamento1_idx` (`Departamento_idDepartamento` ASC),
  CONSTRAINT `fk_Tutoria_Persona1`
    FOREIGN KEY (`personaTutoria`)
    REFERENCES `GestorPedidos`.`Persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Tutoria_Departamento1`
    FOREIGN KEY (`Departamento_idDepartamento`)
    REFERENCES `GestorPedidos`.`Departamento` (`idDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`Carrera`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`Carrera` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`Carrera` (
  `idCarrera` INT NOT NULL AUTO_INCREMENT,
  `nombreCarrera` VARCHAR(45) NOT NULL,
  `Departamento_idDepartamento` INT NOT NULL,
  PRIMARY KEY (`idCarrera`),
  INDEX `fk_Carrera_Departamento1_idx` (`Departamento_idDepartamento` ASC),
  CONSTRAINT `fk_Carrera_Departamento1`
    FOREIGN KEY (`Departamento_idDepartamento`)
    REFERENCES `GestorPedidos`.`Departamento` (`idDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`Microtaller`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`Microtaller` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`Microtaller` (
  `idMicrotaller` INT NOT NULL AUTO_INCREMENT,
  `nombreMicrotaller` VARCHAR(45) NOT NULL,
  `motivoMicrotaller` VARCHAR(100) NULL,
  `tipo` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idMicrotaller`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`Aula`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`Aula` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`Aula` (
  `idAula` INT NOT NULL AUTO_INCREMENT,
  `nombreAula` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(100) NULL,
  `Departamento_idDepartamento` INT NOT NULL,
  PRIMARY KEY (`idAula`),
  INDEX `fk_Aula_Departamento1_idx` (`Departamento_idDepartamento` ASC),
  CONSTRAINT `fk_Aula_Departamento1`
    FOREIGN KEY (`Departamento_idDepartamento`)
    REFERENCES `GestorPedidos`.`Departamento` (`idDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`PersonaAula`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`PersonaAula` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`PersonaAula` (
  `idpersonaaula` INT NOT NULL AUTO_INCREMENT,
  `Persona_idPersona` INT NULL,
  `Aula_idAula` INT NULL,
  `descripcion` VARCHAR(100) NULL,
  `url` VARCHAR(60) NULL,
  `nombreNuevo` VARCHAR(45) NULL,
  `otrosReutilizar` VARCHAR(100) NULL,
  `motivoEliminacion` VARCHAR(45) NULL,
  `tipo` INT NOT NULL,
  `fechaactual` DATETIME NOT NULL,
  PRIMARY KEY (`idpersonaaula`),
  INDEX `fk_Persona_has_Aula_Aula1_idx` (`Aula_idAula` ASC),
  INDEX `fk_Persona_has_Aula_Persona1_idx` (`Persona_idPersona` ASC),
  CONSTRAINT `fk_Persona_has_Aula_Persona1`
    FOREIGN KEY (`Persona_idPersona`)
    REFERENCES `GestorPedidos`.`Persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Persona_has_Aula_Aula1`
    FOREIGN KEY (`Aula_idAula`)
    REFERENCES `GestorPedidos`.`Aula` (`idAula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`MicrotallerPersona`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`MicrotallerPersona` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`MicrotallerPersona` (
  `Microtaller_idMicrotaller` INT NOT NULL,
  `Persona_idPersona` INT NOT NULL,
  PRIMARY KEY (`Microtaller_idMicrotaller`, `Persona_idPersona`),
  INDEX `fk_Microtaller_has_Persona_Persona1_idx` (`Persona_idPersona` ASC),
  INDEX `fk_Microtaller_has_Persona_Microtaller1_idx` (`Microtaller_idMicrotaller` ASC),
  CONSTRAINT `fk_Microtaller_has_Persona_Microtaller1`
    FOREIGN KEY (`Microtaller_idMicrotaller`)
    REFERENCES `GestorPedidos`.`Microtaller` (`idMicrotaller`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Microtaller_has_Persona_Persona1`
    FOREIGN KEY (`Persona_idPersona`)
    REFERENCES `GestorPedidos`.`Persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`Matricular`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`Matricular` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`Matricular` (
  `idMatricular` INT NOT NULL AUTO_INCREMENT,
  `Departamento_idDepartamento` INT NOT NULL,
  `fechaactual` DATETIME NOT NULL,
  PRIMARY KEY (`idMatricular`),
  INDEX `fk_Matricular_Departamento1_idx` (`Departamento_idDepartamento` ASC),
  CONSTRAINT `fk_Matricular_Departamento1`
    FOREIGN KEY (`Departamento_idDepartamento`)
    REFERENCES `GestorPedidos`.`Departamento` (`idDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`Matricular_has_Persona`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`Matricular_has_Persona` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`Matricular_has_Persona` (
  `Matricular_idMatricular` INT NOT NULL,
  `Persona_idPersona` INT NOT NULL,
  PRIMARY KEY (`Matricular_idMatricular`, `Persona_idPersona`),
  INDEX `fk_Matricular_has_Persona_Persona1_idx` (`Persona_idPersona` ASC),
  INDEX `fk_Matricular_has_Persona_Matricular1_idx` (`Matricular_idMatricular` ASC),
  CONSTRAINT `fk_Matricular_has_Persona_Matricular1`
    FOREIGN KEY (`Matricular_idMatricular`)
    REFERENCES `GestorPedidos`.`Matricular` (`idMatricular`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Matricular_has_Persona_Persona1`
    FOREIGN KEY (`Persona_idPersona`)
    REFERENCES `GestorPedidos`.`Persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GestorPedidos`.`Usuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `GestorPedidos`.`Usuario` ;

CREATE TABLE IF NOT EXISTS `GestorPedidos`.`Usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `fechaactual` DATETIME NOT NULL,
  `Persona_idPersona` INT NOT NULL,
  PRIMARY KEY (`idUsuario`),
  INDEX `fk_Usuario_Persona1_idx` (`Persona_idPersona` ASC),
  CONSTRAINT `fk_Usuario_Persona1`
    FOREIGN KEY (`Persona_idPersona`)
    REFERENCES `GestorPedidos`.`Persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
