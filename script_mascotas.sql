-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema tienda_mascotas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tienda_mascotas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tienda_mascotas` DEFAULT CHARACTER SET utf8 ;
USE `tienda_mascotas` ;

-- -----------------------------------------------------
-- Table `tienda_mascotas`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_mascotas`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `email` VARCHAR(150) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tienda_mascotas`.`clients_types`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_mascotas`.`clients_types` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `client_type` INT NULL,
  `description` TEXT NULL,
  `price` INT NULL,
  `discount` FLOAT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tienda_mascotas`.`services_types`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_mascotas`.`services_types` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `service_type` INT NULL,
  `description` TEXT NULL,
  `price` INT NULL,
  `animal_weight` INT NULL,
  `animal_height` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tienda_mascotas`.`appointments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_mascotas`.`appointments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NULL,
  `site` VARCHAR(200) NULL,
  `pet_name` VARCHAR(100) NULL,
  `animal_type` VARCHAR(150) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `client_type_id` INT NOT NULL,
  `service_type_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_appointments_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_appointments_clients_types1_idx` (`client_type_id` ASC) VISIBLE,
  INDEX `fk_appointments_services_types1_idx` (`service_type_id` ASC) VISIBLE,
  CONSTRAINT `fk_appointments_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `tienda_mascotas`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_appointments_clients_types1`
    FOREIGN KEY (`client_type_id`)
    REFERENCES `tienda_mascotas`.`clients_types` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_appointments_services_types1`
    FOREIGN KEY (`service_type_id`)
    REFERENCES `tienda_mascotas`.`services_types` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
