-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 140.131.114.140    Database: 112501
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
-- Table structure for table `old_month_game`
--

DROP TABLE IF EXISTS `old_month_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `old_month_game` (
  `month` int NOT NULL,
  `id` tinyint NOT NULL,
  `user_id` tinyint NOT NULL,
  `game_type` tinyint NOT NULL,
  `play_time` datetime NOT NULL,
  `scores` tinyint NOT NULL,
  KEY `fk_user_idx10_idx` (`user_id`),
  CONSTRAINT `fk_user_idx10` FOREIGN KEY (`user_id`) REFERENCES `user_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `old_month_game`
--

LOCK TABLES `old_month_game` WRITE;
/*!40000 ALTER TABLE `old_month_game` DISABLE KEYS */;
INSERT INTO `old_month_game` VALUES (10,3,2,1,'2023-10-10 00:00:00',50),(11,4,4,3,'2023-11-12 00:00:00',20),(11,5,3,1,'2023-11-12 00:00:00',20),(11,4,4,3,'2023-11-12 00:00:00',20),(11,5,3,1,'2023-11-12 00:00:00',20),(11,6,2,1,'2023-11-10 00:00:00',10),(11,7,2,2,'2023-11-18 00:00:00',50);
/*!40000 ALTER TABLE `old_month_game` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-25 21:25:23
