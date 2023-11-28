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
-- Table structure for table `avatar`
--

DROP TABLE IF EXISTS `avatar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avatar` (
  `id` tinyint NOT NULL,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avatar`
--

LOCK TABLES `avatar` WRITE;
/*!40000 ALTER TABLE `avatar` DISABLE KEYS */;
INSERT INTO `avatar` VALUES (1,'美夢喵窩'),(2,'晴空藍調'),(3,'藍夜星舞');
/*!40000 ALTER TABLE `avatar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cal_record_day`
--

DROP TABLE IF EXISTS `cal_record_day`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cal_record_day` (
  `user_id` tinyint NOT NULL,
  `tot_cal` float NOT NULL DEFAULT '0',
  `record_date` date DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_sum_id` FOREIGN KEY (`user_id`) REFERENCES `user_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cal_record_day`
--

LOCK TABLES `cal_record_day` WRITE;
/*!40000 ALTER TABLE `cal_record_day` DISABLE KEYS */;
INSERT INTO `cal_record_day` VALUES (1,273,'2023-11-18'),(2,1314,'2023-11-18'),(3,231,'2023-11-18'),(4,931,'2023-11-18'),(5,0,'2023-11-18'),(6,0,'2023-11-18'),(7,0,'2023-11-18'),(8,0,'2023-11-18'),(9,0,'2023-11-18'),(10,0,'2023-11-18'),(11,0,'2023-11-19'),(12,0,'2023-11-19'),(13,0,'2023-11-19'),(14,0,'2023-11-19'),(15,0,'2023-11-19');
/*!40000 ALTER TABLE `cal_record_day` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_score`
--

DROP TABLE IF EXISTS `daily_score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_score` (
  `user` tinyint NOT NULL,
  `score` tinyint NOT NULL,
  PRIMARY KEY (`user`),
  CONSTRAINT `fk_user_idx9` FOREIGN KEY (`user`) REFERENCES `user_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_score`
--

LOCK TABLES `daily_score` WRITE;
/*!40000 ALTER TABLE `daily_score` DISABLE KEYS */;
INSERT INTO `daily_score` VALUES (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0);
/*!40000 ALTER TABLE `daily_score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_tasks`
--

DROP TABLE IF EXISTS `daily_tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_tasks` (
  `user` tinyint NOT NULL,
  `task1` tinyint NOT NULL,
  `task2` tinyint NOT NULL,
  `task3` tinyint NOT NULL,
  PRIMARY KEY (`user`),
  CONSTRAINT `fk_user_idx2` FOREIGN KEY (`user`) REFERENCES `user_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_tasks`
--

LOCK TABLES `daily_tasks` WRITE;
/*!40000 ALTER TABLE `daily_tasks` DISABLE KEYS */;
INSERT INTO `daily_tasks` VALUES (1,2,2,4),(2,3,4,2),(3,1,4,2),(4,3,2,1),(5,2,4,4),(6,3,2,1),(7,2,3,4),(8,3,3,3),(9,4,2,4),(10,1,2,4),(11,2,1,2),(12,4,3,1),(13,4,4,4),(14,2,4,4),(15,3,3,1);
/*!40000 ALTER TABLE `daily_tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ding`
--

DROP TABLE IF EXISTS `ding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ding` (
  `id` int NOT NULL,
  `context` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ding`
--

LOCK TABLES `ding` WRITE;
/*!40000 ALTER TABLE `ding` DISABLE KEYS */;
/*!40000 ALTER TABLE `ding` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game` (
  `id` int NOT NULL,
  `user_id` tinyint NOT NULL,
  `game_type` tinyint NOT NULL,
  `game_time` datetime NOT NULL,
  `scores` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `user_idx` (`user_id`),
  KEY `type_idx` (`game_type`),
  CONSTRAINT `fk_type` FOREIGN KEY (`game_type`) REFERENCES `game_type` (`id`),
  CONSTRAINT `fk_user` FOREIGN KEY (`user_id`) REFERENCES `user_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
/*!40000 ALTER TABLE `game` ENABLE KEYS */;
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
/*!50003 CREATE*/ /*!50017 DEFINER=`112501`@`%`*/ /*!50003 TRIGGER `game_AFTER_INSERT` AFTER INSERT ON `game` FOR EACH ROW BEGIN
	update cal_record_day
    set tot_cal = tot_cal + (SELECT cal(ui.weight, gt.cal_value, 60) AS cal FROM (select * from game where user_id = new.user_id) as g, user_information as ui, game_type as gt
	WHERE g.user_id = ui.id AND g.game_type = gt.id and g.game_time = new.game_time)
    where user_id = new.user_id;
    
	update cal_record_day
    set record_date = date(new.game_time)
    where user_id = new.user_id;
    
    update score
    set score = score + new.scores
    where user = new.user_id;
    
	update daily_score
    set score = score + new.scores
    where user = new.user_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `game_pictures`
--

DROP TABLE IF EXISTS `game_pictures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_pictures` (
  `id` int NOT NULL,
  `game_type` tinyint NOT NULL,
  `group` tinyint NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_type_idx3_idx` (`game_type`),
  CONSTRAINT `fk_type_idx3` FOREIGN KEY (`game_type`) REFERENCES `game_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_pictures`
--

LOCK TABLES `game_pictures` WRITE;
/*!40000 ALTER TABLE `game_pictures` DISABLE KEYS */;
INSERT INTO `game_pictures` VALUES (1,1,1,'net'),(2,1,1,'baseball-1'),(3,1,2,'net'),(4,1,2,'basketball'),(5,1,3,'net'),(6,1,3,'masterball-1'),(7,2,1,'hammer-1'),(8,2,1,'hammer-2'),(9,2,1,'Rat-1'),(10,2,1,'Rat-2'),(11,2,2,'paper-1'),(12,2,2,'paper-2'),(13,2,2,'Ratt-1'),(14,2,2,'Ratt-2'),(15,2,3,'stick-1'),(16,2,3,'stick-2'),(17,2,3,'Rattt-1'),(18,2,3,'Rattt-2'),(19,3,1,'cat_1'),(20,3,1,'cat_2'),(21,3,2,'ghost_1'),(22,3,2,'ghost_2'),(23,3,3,'slime_1'),(24,3,3,'slime_2');
/*!40000 ALTER TABLE `game_pictures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_type`
--

DROP TABLE IF EXISTS `game_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_type` (
  `id` tinyint NOT NULL,
  `name` varchar(10) NOT NULL,
  `cal_value` float NOT NULL,
  `introduce` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_type`
--

LOCK TABLES `game_type` WRITE;
/*!40000 ALTER TABLE `game_type` DISABLE KEYS */;
INSERT INTO `game_type` VALUES (1,'守門員',4.2,'以左右移動與人體判定的方式去判斷是有成功將球擋下，並設置計時器，直到計時停止才會結算成績。'),(2,'打地鼠',5.1,'利用手部位置與手臂揮動的幅度去判斷是否成功砸中地鼠，並設置計時器，直到計時停止才會結算成績。'),(3,'跑酷',8.2,'以雙腳擺動的速度去判斷角色的行進速度，並利用位置的偏移判斷是否變換跑道，直到撞上障礙物才會停下。');
/*!40000 ALTER TABLE `game_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `hot_game`
--

DROP TABLE IF EXISTS `hot_game`;
/*!50001 DROP VIEW IF EXISTS `hot_game`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `hot_game` AS SELECT 
 1 AS `id`,
 1 AS `name`,
 1 AS `cal_value`,
 1 AS `introduce`,
 1 AS `cnt`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `old_cal_record`
--

DROP TABLE IF EXISTS `old_cal_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `old_cal_record` (
  `month` tinyint NOT NULL,
  `user` tinyint NOT NULL,
  `tot_cal` float NOT NULL,
  KEY `fk_user_idx11_idx` (`user`),
  CONSTRAINT `fk_user_idx11` FOREIGN KEY (`user`) REFERENCES `user_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `old_cal_record`
--

LOCK TABLES `old_cal_record` WRITE;
/*!40000 ALTER TABLE `old_cal_record` DISABLE KEYS */;
INSERT INTO `old_cal_record` VALUES (11,1,273),(11,2,252),(11,3,231),(11,4,931),(11,5,0),(11,6,0),(11,8,0),(11,7,0),(11,9,0),(11,10,0),(11,11,0),(11,12,0),(11,13,0),(11,14,0),(11,15,0);
/*!40000 ALTER TABLE `old_cal_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `old_information`
--

DROP TABLE IF EXISTS `old_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `old_information` (
  `id` tinyint NOT NULL,
  `user_name` char(10) NOT NULL,
  `height` float NOT NULL,
  `weight` float NOT NULL,
  `t_type` char(2) NOT NULL,
  `t_time` date NOT NULL,
  KEY `fk_user_i_idx` (`id`),
  CONSTRAINT `fk_user_i` FOREIGN KEY (`id`) REFERENCES `user_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `old_information`
--

LOCK TABLES `old_information` WRITE;
/*!40000 ALTER TABLE `old_information` DISABLE KEYS */;
INSERT INTO `old_information` VALUES (5,'56099',165,65,'UO','2023-11-15'),(5,'56043',165,65,'UN','2023-11-15'),(2,'56098',160,60,'UO','2023-11-15'),(2,'56005',160,60,'UN','2023-11-15'),(1,'56002',160,65,'UO','2023-11-19'),(1,'56002',160,65,'UN','2023-11-19'),(2,'56005',160,60,'UO','2023-11-19'),(2,'56005',160,60,'UN','2023-11-19'),(3,'56007',170,55,'UO','2023-11-19'),(3,'56007',170,55,'UN','2023-11-19'),(4,'56028',170,70,'UO','2023-11-19'),(4,'56028',170,70,'UN','2023-11-19'),(5,'56043',165,65,'UO','2023-11-19'),(5,'56043',165,65,'UN','2023-11-19'),(6,'56099',150,40,'UO','2023-11-19'),(6,'56099',150,40,'UN','2023-11-19'),(7,'56098',160,40,'UO','2023-11-19'),(7,'56098',160,40,'UN','2023-11-19'),(8,'56097',155,70,'UO','2023-11-19'),(8,'56097',155,70,'UN','2023-11-19'),(9,'56096',185,40,'UO','2023-11-19'),(9,'56096',185,40,'UN','2023-11-19'),(10,'56095',160,46,'UO','2023-11-19'),(10,'56095',160,46,'UN','2023-11-19'),(11,'56094',168,46,'UO','2023-11-19'),(11,'56094',168,46,'UN','2023-11-19'),(12,'56093',150,40,'UO','2023-11-19'),(12,'56093',150,40,'UN','2023-11-19'),(13,'56092',160,56,'UO','2023-11-19'),(13,'56092',160,56,'UN','2023-11-19'),(14,'56091',170,56,'UO','2023-11-19'),(14,'56091',170,56,'UN','2023-11-19'),(15,'56090',170,62,'UO','2023-11-19'),(15,'56090',170,62,'UN','2023-11-19');
/*!40000 ALTER TABLE `old_information` ENABLE KEYS */;
UNLOCK TABLES;

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

--
-- Table structure for table `old_set`
--

DROP TABLE IF EXISTS `old_set`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `old_set` (
  `user` tinyint NOT NULL,
  `avatar` tinyint NOT NULL,
  `update_time` date NOT NULL,
  KEY `fk_set_id_idx` (`user`),
  CONSTRAINT `fk_set_id` FOREIGN KEY (`user`) REFERENCES `user_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `old_set`
--

LOCK TABLES `old_set` WRITE;
/*!40000 ALTER TABLE `old_set` DISABLE KEYS */;
INSERT INTO `old_set` VALUES (3,1,'2023-11-15');
/*!40000 ALTER TABLE `old_set` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score`
--

DROP TABLE IF EXISTS `score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `score` (
  `user` tinyint NOT NULL,
  `score` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`user`),
  CONSTRAINT `fk_user_idx3` FOREIGN KEY (`user`) REFERENCES `user_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score`
--

LOCK TABLES `score` WRITE;
/*!40000 ALTER TABLE `score` DISABLE KEYS */;
INSERT INTO `score` VALUES (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0);
/*!40000 ALTER TABLE `score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `set`
--

DROP TABLE IF EXISTS `set`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `set` (
  `user` tinyint NOT NULL,
  `avatar` tinyint NOT NULL,
  PRIMARY KEY (`user`),
  UNIQUE KEY `user_UNIQUE` (`user`),
  KEY `avatar_idx` (`avatar`),
  CONSTRAINT `fk_avatar` FOREIGN KEY (`avatar`) REFERENCES `avatar` (`id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user`) REFERENCES `user_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `set`
--

LOCK TABLES `set` WRITE;
/*!40000 ALTER TABLE `set` DISABLE KEYS */;
INSERT INTO `set` VALUES (1,1),(4,1),(2,2),(3,2),(5,3);
/*!40000 ALTER TABLE `set` ENABLE KEYS */;
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
/*!50003 CREATE*/ /*!50017 DEFINER=`112501`@`%`*/ /*!50003 TRIGGER `set_BEFORE_UPDATE` BEFORE UPDATE ON `set` FOR EACH ROW BEGIN
	delete from old_set where `user` = old.`user` and update_time = current_date;  
	insert into old_set values (old.`user`, old.avatar, current_date);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task` (
  `id` tinyint NOT NULL,
  `type` tinyint NOT NULL,
  `content` varchar(20) DEFAULT NULL,
  `values` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_type_idx` (`type`),
  KEY `fk_task_type` (`type`),
  CONSTRAINT `fk_task_type` FOREIGN KEY (`type`) REFERENCES `task_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (1,1,'打地鼠：在一局內得20分',20),(2,1,'跑酷：在一局內得30分',30),(3,1,'足球守門員：在一局得30分',30),(4,2,'累計遊玩時長3分',3);
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_type`
--

DROP TABLE IF EXISTS `task_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task_type` (
  `id` tinyint NOT NULL,
  `type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_type`
--

LOCK TABLES `task_type` WRITE;
/*!40000 ALTER TABLE `task_type` DISABLE KEYS */;
INSERT INTO `task_type` VALUES (1,'遊戲分數'),(2,'遊戲時長');
/*!40000 ALTER TABLE `task_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `user_age`
--

DROP TABLE IF EXISTS `user_age`;
/*!50001 DROP VIEW IF EXISTS `user_age`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `user_age` AS SELECT 
 1 AS `id`,
 1 AS `user_name`,
 1 AS `age`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `user_have`
--

DROP TABLE IF EXISTS `user_have`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_have` (
  `id` int NOT NULL,
  `user_id` tinyint NOT NULL,
  `game_type` tinyint NOT NULL,
  `group` tinyint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_idx` (`user_id`),
  CONSTRAINT `fk_user_idx` FOREIGN KEY (`user_id`) REFERENCES `user_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_have`
--

LOCK TABLES `user_have` WRITE;
/*!40000 ALTER TABLE `user_have` DISABLE KEYS */;
INSERT INTO `user_have` VALUES (1,1,1,1),(2,2,1,1),(3,3,1,1),(4,4,1,1),(5,5,1,1),(6,6,1,1),(7,7,1,1),(8,8,1,1),(9,9,1,1),(10,10,1,1),(11,11,1,1),(12,12,1,1),(13,13,1,1),(14,14,1,1),(15,15,1,1),(16,1,2,1),(17,2,2,1),(18,3,2,1),(19,4,2,1),(20,5,2,1),(21,6,2,1),(22,7,2,1),(23,8,2,1),(24,9,2,1),(25,10,2,1),(26,11,2,1),(27,12,2,1),(28,13,2,1),(29,14,2,1),(30,15,2,1),(31,1,3,1),(32,2,3,1),(33,3,3,1),(34,4,3,1),(35,5,3,1),(36,6,3,1),(37,7,3,1),(38,8,3,1),(39,9,3,1),(40,10,3,1),(41,11,3,1),(42,12,3,1),(43,13,3,1),(44,14,3,1),(45,15,3,1);
/*!40000 ALTER TABLE `user_have` ENABLE KEYS */;
UNLOCK TABLES;

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
INSERT INTO `user_information` VALUES (1,'56002','l002','女',160,65,'2011-10-01',1,1,1,1),(2,'56005','c005','女',160,60,'2006-12-15',1,1,1,1),(3,'56007','c007','女',170,55,'2012-01-04',1,1,1,1),(4,'56028','c028','男',170,70,'2008-11-15',1,1,1,1),(5,'56043','l043','女',165,65,'2006-03-15',1,1,1,1),(6,'56099','n099','男',150,40,'2007-08-09',1,1,1,1),(7,'56098','n098','男',160,40,'2001-12-02',1,1,1,1),(8,'56097','n097','女',155,70,'2009-10-15',1,1,1,1),(9,'56096','n096','男',185,40,'2018-03-16',1,1,1,1),(10,'56095','n095','女',160,46,'2010-10-23',1,1,1,1),(11,'56094','n094','女',168,46,'2023-11-08',2,1,1,1),(12,'56093','n093','保密',150,40,'2017-11-23',3,1,1,1),(13,'56092','n092','保密',160,56,'2016-11-25',3,1,1,1),(14,'56091','n091','保密',170,56,'2019-06-19',3,1,1,1),(15,'56090','n090','保密',170,62,'2023-11-01',3,1,1,1);
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
    insert into score value (new.id, 0);
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

--
-- Dumping events for database '112501'
--
/*!50106 SET @save_time_zone= @@TIME_ZONE */ ;
/*!50106 DROP EVENT IF EXISTS `daily_task_event` */;
DELIMITER ;;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;;
/*!50003 SET character_set_client  = utf8mb4 */ ;;
/*!50003 SET character_set_results = utf8mb4 */ ;;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;;
/*!50003 SET @saved_time_zone      = @@time_zone */ ;;
/*!50003 SET time_zone             = 'SYSTEM' */ ;;
/*!50106 CREATE*/ /*!50117 DEFINER=`112501`@`%`*/ /*!50106 EVENT `daily_task_event` ON SCHEDULE EVERY 1 DAY STARTS '2023-11-18 11:59:00' ON COMPLETION NOT PRESERVE ENABLE DO CALL update_tasks() */ ;;
/*!50003 SET time_zone             = @saved_time_zone */ ;;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;;
/*!50003 SET character_set_client  = @saved_cs_client */ ;;
/*!50003 SET character_set_results = @saved_cs_results */ ;;
/*!50003 SET collation_connection  = @saved_col_connection */ ;;
/*!50106 DROP EVENT IF EXISTS `delete_cal_event` */;;
DELIMITER ;;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;;
/*!50003 SET character_set_client  = utf8mb4 */ ;;
/*!50003 SET character_set_results = utf8mb4 */ ;;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;;
/*!50003 SET @saved_time_zone      = @@time_zone */ ;;
/*!50003 SET time_zone             = 'SYSTEM' */ ;;
/*!50106 CREATE*/ /*!50117 DEFINER=`112501`@`%`*/ /*!50106 EVENT `delete_cal_event` ON SCHEDULE EVERY 1 DAY STARTS '2023-11-18 11:59:00' ON COMPLETION NOT PRESERVE ENABLE DO CALL delete_day_cal() */ ;;
/*!50003 SET time_zone             = @saved_time_zone */ ;;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;;
/*!50003 SET character_set_client  = @saved_cs_client */ ;;
/*!50003 SET character_set_results = @saved_cs_results */ ;;
/*!50003 SET collation_connection  = @saved_col_connection */ ;;
/*!50106 DROP EVENT IF EXISTS `delete_game_event` */;;
DELIMITER ;;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;;
/*!50003 SET character_set_client  = utf8mb4 */ ;;
/*!50003 SET character_set_results = utf8mb4 */ ;;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;;
/*!50003 SET @saved_time_zone      = @@time_zone */ ;;
/*!50003 SET time_zone             = 'SYSTEM' */ ;;
/*!50106 CREATE*/ /*!50117 DEFINER=`root`@`localhost`*/ /*!50106 EVENT `delete_game_event` ON SCHEDULE EVERY 1 DAY STARTS '2023-11-18 11:59:00' ON COMPLETION NOT PRESERVE ENABLE DO CALL delete_game() */ ;;
/*!50003 SET time_zone             = @saved_time_zone */ ;;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;;
/*!50003 SET character_set_client  = @saved_cs_client */ ;;
/*!50003 SET character_set_results = @saved_cs_results */ ;;
/*!50003 SET collation_connection  = @saved_col_connection */ ;;
/*!50106 DROP EVENT IF EXISTS `update_cal_event` */;;
DELIMITER ;;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;;
/*!50003 SET character_set_client  = utf8mb4 */ ;;
/*!50003 SET character_set_results = utf8mb4 */ ;;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;;
/*!50003 SET @saved_time_zone      = @@time_zone */ ;;
/*!50003 SET time_zone             = 'SYSTEM' */ ;;
/*!50106 CREATE*/ /*!50117 DEFINER=`root`@`localhost`*/ /*!50106 EVENT `update_cal_event` ON SCHEDULE EVERY 1 MONTH STARTS '2023-11-01 00:01:00' ON COMPLETION NOT PRESERVE ENABLE DO CALL update_month_cal() */ ;;
/*!50003 SET time_zone             = @saved_time_zone */ ;;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;;
/*!50003 SET character_set_client  = @saved_cs_client */ ;;
/*!50003 SET character_set_results = @saved_cs_results */ ;;
/*!50003 SET collation_connection  = @saved_col_connection */ ;;
/*!50106 DROP EVENT IF EXISTS `update_game_event` */;;
DELIMITER ;;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;;
/*!50003 SET character_set_client  = utf8mb4 */ ;;
/*!50003 SET character_set_results = utf8mb4 */ ;;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;;
/*!50003 SET @saved_time_zone      = @@time_zone */ ;;
/*!50003 SET time_zone             = 'SYSTEM' */ ;;
/*!50106 CREATE*/ /*!50117 DEFINER=`root`@`localhost`*/ /*!50106 EVENT `update_game_event` ON SCHEDULE EVERY 1 MONTH STARTS '2023-11-01 00:01:00' ON COMPLETION NOT PRESERVE ENABLE DO CALL update_month_game() */ ;;
/*!50003 SET time_zone             = @saved_time_zone */ ;;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;;
/*!50003 SET character_set_client  = @saved_cs_client */ ;;
/*!50003 SET character_set_results = @saved_cs_results */ ;;
/*!50003 SET collation_connection  = @saved_col_connection */ ;;
DELIMITER ;
/*!50106 SET TIME_ZONE= @save_time_zone */ ;

--
-- Dumping routines for database '112501'
--
/*!50003 DROP FUNCTION IF EXISTS `cal` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`112501`@`%` FUNCTION `cal`(weight FLOAT, cal_value FLOAT, play_time FLOAT) RETURNS float
BEGIN
    DECLARE cal FLOAT;
    SET cal = weight * play_time * (cal_value/60);
    RETURN cal;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `age` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`112501`@`%` PROCEDURE `age`()
BEGIN
	-- 計算年齡
	select *, TIMESTAMPDIFF(YEAR, born, CURDATE()) as age from user_information;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `cal_count` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`112501`@`%` PROCEDURE `cal_count`()
BEGIN
	-- 卡路里累積
	SELECT ui.*, round(sum(cal_value),2) FROM game as g, game_type as gt, user_information as ui
	where g.game_type = gt.id and g.user_id = ui.id
	group by g.user_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_day_cal` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_day_cal`()
BEGIN
	-- 每天11:59執行
	-- 保留當天卡路里記錄至當月紀錄
	insert into old_cal_record 
	select month(now()) , cal_record_day.* from cal_record_day where date(game_time) = date(now());

	--  清除每日卡路里累積資料(每天晚上11:59刪除當天紀錄)
	delete from cal_record_day;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_game` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`112501`@`%` PROCEDURE `delete_game`()
BEGIN
	-- 每天11:59執行
	-- 保留當天記錄至當月紀錄
	insert into old_month_game 
	select month(now()) , game.* from game where date(game_time) = date(now());
    
    -- 清除當日資料
	delete from game;
    delete from daily.score;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `game_type_count` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`112501`@`%` PROCEDURE `game_type_count`()
BEGIN
	-- 遊玩遊戲次數
	SELECT gt.*, count(game_type) FROM game as g, game_type as gt
	where g.game_type = gt.id
	group by gt.id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `note` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`112501`@`%` PROCEDURE `note`()
BEGIN
	-- 顯示排程
    show events;
	
    -- 開啟排程
	SET GLOBAL event_scheduler = ON;
    

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `pushfunction` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`112501`@`%` PROCEDURE `pushfunction`()
BEGIN
	SELECT ui.*, sum(cal_value) FROM game as g, game_type as gt, user_information as ui
	where g.game_type = gt.id and g.user_id = ui.id
	group by g.user_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `safe` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`112501`@`%` PROCEDURE `safe`()
BEGIN
	-- 關閉安全模式
	SET SQL_SAFE_UPDATES = 0;
    
    -- 開啟安全模式
    SET SQL_SAFE_UPDATES = 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_month_cal` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`112501`@`%` PROCEDURE `update_month_cal`()
BEGIN
	-- 刪除前月卡路里資料(每月第1天執行)
    delete from old_cal_record
	where `month` = month(now())-2;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_month_game` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`112501`@`%` PROCEDURE `update_month_game`()
BEGIN
	-- 刪除前月遊戲資料(每月第1天執行)
    delete from old_month_game
	where `month` = month(now())-2;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_tasks` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`112501`@`%` PROCEDURE `update_tasks`()
BEGIN
	-- 更新每日任務(每天11:59執行)
	update daily_tasks
	set task1 = floor(1 + rand() *(select count(*) from task)),
	task2 = floor(1 + rand() *(select count(*) from task)),
	task3 = floor(1 + rand() *(select count(*) from task))
	where `user` in (select id from user_information); 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `hot_game`
--

/*!50001 DROP VIEW IF EXISTS `hot_game`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`112501`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `hot_game` AS select 1 AS `id`,1 AS `name`,1 AS `cal_value`,1 AS `introduce`,1 AS `cnt` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `user_age`
--

/*!50001 DROP VIEW IF EXISTS `user_age`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`112501`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `user_age` AS select 1 AS `id`,1 AS `user_name`,1 AS `age` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-25 21:25:41
