-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema biblioteca
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema biblioteca
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `biblioteca` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `biblioteca` ;

-- -----------------------------------------------------
-- Table `biblioteca`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`cliente` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `endereco` VARCHAR(150) NOT NULL,
  `telefone` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `biblioteca`.`livro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`livro` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(100) NOT NULL,
  `autor` VARCHAR(100) NOT NULL,
  `ano_publicacao` INT NOT NULL,
  `status` ENUM('disponível', 'emprestado') NOT NULL DEFAULT 'disponível',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `biblioteca`.`emprestimo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`emprestimo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `livro_id` INT NOT NULL,
  `cliente_id` INT NOT NULL,
  `data_emprestimo` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `livro_id` (`livro_id` ASC) VISIBLE,
  INDEX `cliente_id` (`cliente_id` ASC) VISIBLE,
  CONSTRAINT `emprestimo_ibfk_1`
    FOREIGN KEY (`livro_id`)
    REFERENCES `biblioteca`.`livro` (`id`),
  CONSTRAINT `emprestimo_ibfk_2`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `biblioteca`.`cliente` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;