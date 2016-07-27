CREATE DATABASE IF NOT EXISTS `CCDB` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `CCDB`;


-- --------------------------------------------------------
--CCDB - Content-Concept-DataBase
--
-- Структура таблицы `Concepts`
--

CREATE TABLE IF NOT EXISTS `Concepts` (
  `concept_id` int(10) NOT NULL AUTO_INCREMENT,
  `concept_URI` varchar(120) NOT NULL,
  `field_id` int(10) NOT NULL,
  `concept_label` varchar(120) NOT NULL,
  `concept_description` varchar(250) NOT NULL,
  PRIMARY KEY (`concept_id`),
  KEY `field_id` (`field_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `Concept_Content_Manager`
--

CREATE TABLE IF NOT EXISTS `Concept_Content_Manager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `block_id` int(11) NOT NULL,
  `concept_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `block_id` (`block_id`,`concept_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `Fields`
--

CREATE TABLE IF NOT EXISTS `Fields` (
  `field_id` int(11) NOT NULL AUTO_INCREMENT,
  `field_label` varchar(120) NOT NULL,
  PRIMARY KEY (`field_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
