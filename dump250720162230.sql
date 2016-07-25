-- --------------------------------------------------------
-- Хост:                         192.168.0.6
-- Версия сервера:               5.5.46-0ubuntu0.12.04.2 - (Ubuntu)
-- ОС Сервера:                   debian-linux-gnu
-- HeidiSQL Версия:              9.1.0.4867
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Дамп структуры базы данных terms
CREATE DATABASE IF NOT EXISTS `terms` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `terms`;


-- Дамп структуры для таблица terms.allTerms
CREATE TABLE IF NOT EXISTS `allTerms` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET latin1 NOT NULL,
  `term` varchar(50) CHARACTER SET latin1 NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы terms.allTerms: ~3 rows (приблизительно)
/*!40000 ALTER TABLE `allTerms` DISABLE KEYS */;
INSERT INTO `allTerms` (`id`, `name`, `term`) VALUES
	(1, 'term1', 'term_term'),
	(2, 'term2', 'term_term'),
	(3, 'term3', 'term_term');
/*!40000 ALTER TABLE `allTerms` ENABLE KEYS */;


-- Дамп структуры для таблица terms.relations
CREATE TABLE IF NOT EXISTS `relations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `block` int(11) NOT NULL DEFAULT '0',
  `term` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы terms.relations: ~2 rows (приблизительно)
/*!40000 ALTER TABLE `relations` DISABLE KEYS */;
INSERT INTO `relations` (`id`, `block`, `term`) VALUES
	(1, 1, 2),
	(2, 1, 3);
/*!40000 ALTER TABLE `relations` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
