'''

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema api_project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema api_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS api_project ;
USE api_project ;

-- -----------------------------------------------------
-- Table `api_project`.`channels`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS api_project.channels (
  id_channels INT NOT NULL,
  PRIMARY KEY (id_channels))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `api_project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS api_project.users (
  id_users INT NOT NULL,
  user_name VARCHAR(45) NULL,
  PRIMARY KEY (id_users))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `api_project`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS api_project.messages (
  id_messages INT NOT NULL,
  users_id_users INT NOT NULL,
  channels_id_channels INT NOT NULL,
  text VARCHAR(255) NULL,
  PRIMARY KEY (id_messages),
  INDEX fk_messages_users_idx (users_id_users ASC) VISIBLE,
  INDEX fk_messages_channels1_idx (channels_id_channels ASC) VISIBLE,
  CONSTRAINT fk_messages_users
    FOREIGN KEY (users_id_users)
    REFERENCES api_project.users (id_users)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_messages_channels1
    FOREIGN KEY (channels_id_channels)
    REFERENCES api_project.channels (id_channels)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


'''
