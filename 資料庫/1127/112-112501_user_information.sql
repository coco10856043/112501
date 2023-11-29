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
-- Table structure for table `user_information`
--

DROP TABLE IF EXISTS `user_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_information` (
  `id` tinyint NOT NULL,
  `user_name` char(10) NOT NULL,
  `password` char(30) NOT NULL,
  `gender` char(2) DEFAULT NULL,
  `height` float NOT NULL,
  `weight` float NOT NULL,
  `born` date DEFAULT NULL,
  `avatar` tinyint DEFAULT '1',
  `game1` tinyint DEFAULT '1',
  `game2` tinyint DEFAULT '1',
  `game3` tinyint DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`user_name`),
  KEY `fk_avatar_idx_idx` (`avatar`),
  CONSTRAINT `fk_avatar_idx` FOREIGN KEY (`avatar`) REFERENCES `avatar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_information`
--

LOCK TABLES `user_information` WRITE;
/*!40000 ALTER TABLE `user_information` DISABLE KEYS */;
INSERT INTO `user_information` VALUES (1,'56002','l002','女',160,65,'2011-10-01',1,1,1,1),(2,'56005','c005','女',160,60,'2006-12-15',3,1,1,1),(3,'56007','c007','女',170,55,'2012-01-04',3,1,1,1),(4,'56028','c028','男',170,70,'2008-11-15',1,1,1,1),(5,'56043','l043','女',165,65,'2006-03-15',1,1,1,1),(6,'56099','n099','男',150,40,'2007-08-09',2,1,1,1),(7,'56098','n098','男',160,40,'2001-12-02',1,1,1,1),(8,'56097','n097','女',155,70,'2009-10-15',1,1,1,1),(9,'56096','n096','男',185,40,'2018-03-16',1,1,1,1),(10,'56095','n095','女',160,46,'2010-10-23',1,1,1,1),(11,'56094','n094','女',155,50,'2023-11-08',3,1,1,1),(12,'56093','n093','保密',150,40,'2017-11-23',3,1,1,1),(13,'56092','n092','保密',160,56,'2016-11-25',3,1,1,1),(14,'56091','n091','保密',170,56,'2019-06-19',3,1,1,1),(15,'56090','n090','保密',170,62,'2023-11-01',3,1,1,1),(16,'56089','n089','男',165,52,'2023-01-25',1,1,1,1),(17,'56088','n088','保密',155,45,'2023-11-10',1,1,1,1),(18,'rita','rita2607','保密',160,60,'2004-07-26',1,1,1,1),(19,'11111','11111','保密',11111,11111,'2023-11-25',1,1,1,1),(20,'56056','n056','保密',165,40,'1965-11-11',3,1,1,1),(21,'123123','123123','男',180,70,'2016-11-16',1,1,1,1),(22,'10000','11111','男',100,100,'2023-11-08',1,1,1,1),(23,'test1','test1','女',160,60,'1951-03-15',2,1,1,1);
/*!40000 ALTER TABLE `user_information` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `user_information_AFTER_INSERT` AFTER INSERT ON `user_information` FOR EACH ROW BEGIN
	insert into cal_record_day value(new.id , 0, date(now()));
    insert into old_cal_record value(month(now()) , new.id, 0);
    insert into daily_tasks value(new.id, floor(1 + rand() *(select count(*) from task)), floor(1 + rand() *(select count(*) from task)), floor(1 + rand() *(select count(*) from task)));
    insert into scores value (new.id, 0);
    insert into daily_score value (new.id, 0);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `user_information_BEFORE_UPDATE` BEFORE UPDATE ON `user_information` FOR EACH ROW BEGIN
	delete from old_information where id = old.id and t_type = "UO" and t_time = current_date;  
    INSERT INTO old_information values(old.id, OLD.user_name, OLD.height, OLD.weight, "UO", current_date);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`112501`@`%`*/ /*!50003 TRIGGER `user_information_AFTER_UPDATE` AFTER UPDATE ON `user_information` FOR EACH ROW BEGIN
	delete from old_information where id = new.id and t_type = "UN" and t_time = current_date;  
	INSERT INTO old_information values(new.id, NEW.user_name, NEW.height, NEW.weight, "UN", current_date);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-27 22:56:34
