-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 140.131.114.140    Database: 112-112501
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `game_pictures`
--

DROP TABLE IF EXISTS `game_pictures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_pictures` (
  `id` int NOT NULL AUTO_INCREMENT,
  `game_type` tinyint NOT NULL,
  `group` tinyint NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_type_idx3_idx` (`game_type`),
  CONSTRAINT `fk_type_idx3` FOREIGN KEY (`game_type`) REFERENCES `game_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_pictures`
--

LOCK TABLES `game_pictures` WRITE;
/*!40000 ALTER TABLE `game_pictures` DISABLE KEYS */;
INSERT INTO `game_pictures` VALUES (1,1,1,'net'),(2,1,1,'baseball'),(3,1,2,'net'),(4,1,2,'basketball'),(5,1,3,'net'),(6,1,3,'masterball'),(7,2,1,'hammer-1'),(8,2,1,'hammer-2'),(9,2,1,'Rat-1'),(10,2,1,'Rat-2'),(11,2,2,'paper-1'),(12,2,2,'paper-2'),(13,2,2,'Ratt-1'),(14,2,2,'Ratt-2'),(15,2,3,'stick-1'),(16,2,3,'stick-2'),(17,2,3,'Rattt-1'),(18,2,3,'Rattt-2'),(19,3,1,'cat_1'),(20,3,1,'cat_2'),(21,3,2,'ghost_1'),(22,3,2,'ghost_2'),(23,3,3,'slime_1'),(24,3,3,'slime_2');
/*!40000 ALTER TABLE `game_pictures` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-29  7:57:40
