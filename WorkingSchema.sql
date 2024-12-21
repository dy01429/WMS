-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: capstone
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
-- Table structure for table `barcode_scans`
--

DROP TABLE IF EXISTS `barcode_scans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barcode_scans` (
  `scan_id` int NOT NULL AUTO_INCREMENT,
  `barcode_data` varchar(255) NOT NULL,
  `scan_time` datetime NOT NULL,
  `zone` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`scan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1092 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barcode_scans`
--

LOCK TABLES `barcode_scans` WRITE;
/*!40000 ALTER TABLE `barcode_scans` DISABLE KEYS */;
INSERT INTO `barcode_scans` VALUES (930,'18806','2024-12-06 21:50:52','A'),(931,'18806','2024-12-06 21:50:52','C'),(932,'18806','2024-12-06 21:50:58','A'),(933,'18806','2024-12-06 21:50:58','C'),(934,'18806','2024-12-06 21:51:00','A'),(935,'18806','2024-12-06 21:51:00','C'),(936,'18806','2024-12-06 21:51:00','A'),(937,'18806','2024-12-06 21:51:00','C'),(938,'18806','2024-12-06 21:51:00','A'),(939,'18806','2024-12-06 21:51:01','C'),(940,'18806','2024-12-06 21:51:01','A'),(941,'18806','2024-12-06 21:51:01','C'),(942,'18806','2024-12-06 21:51:01','A'),(943,'18806','2024-12-06 21:51:01','C'),(944,'18806','2024-12-06 21:51:01','A'),(945,'18806','2024-12-06 21:51:01','C'),(946,'18806','2024-12-06 21:51:01','A'),(947,'18806','2024-12-06 21:51:01','C'),(948,'18806','2024-12-06 21:51:01','A'),(949,'18806','2024-12-06 21:51:01','C'),(950,'18806','2024-12-06 21:51:01','A'),(951,'18806','2024-12-06 21:51:01','C'),(952,'18806','2024-12-06 21:51:01','A'),(953,'18806','2024-12-06 21:51:01','C'),(954,'18806','2024-12-06 21:51:01','A'),(955,'18806','2024-12-06 21:51:01','C'),(956,'18806','2024-12-06 21:51:03','D'),(957,'18806','2024-12-06 21:51:05','B'),(958,'18806','2024-12-06 21:51:05','D'),(959,'18806','2024-12-06 21:51:05','B'),(960,'18806','2024-12-06 21:51:05','D'),(961,'18806','2024-12-06 21:51:05','B'),(962,'18806','2024-12-06 21:51:05','D'),(963,'18806','2024-12-06 21:51:05','B'),(964,'18806','2024-12-06 21:51:05','D'),(965,'18806','2024-12-06 21:51:06','B'),(966,'18806','2024-12-06 21:51:06','D'),(967,'18806','2024-12-06 21:51:06','B'),(968,'18806','2024-12-06 21:51:22','C'),(969,'18806','2024-12-06 21:51:35','D'),(970,'18806','2024-12-07 21:17:30','B'),(971,'18806','2024-12-07 21:17:30','D'),(972,'18806','2024-12-07 21:17:35','B'),(973,'18806','2024-12-07 21:21:20','A'),(974,'18806','2024-12-07 21:21:21','C'),(975,'18806','2024-12-07 21:21:27','A'),(976,'18806','2024-12-07 21:21:27','C'),(977,'18806','2024-12-07 21:21:29','A'),(978,'18806','2024-12-07 21:21:29','C'),(979,'18806','2024-12-07 21:21:29','A'),(980,'18806','2024-12-07 21:21:29','C'),(981,'18806','2024-12-07 21:21:29','A'),(982,'18806','2024-12-07 21:21:29','C'),(983,'18806','2024-12-07 21:21:29','A'),(984,'18806','2024-12-07 21:21:29','C'),(985,'18806','2024-12-07 21:21:29','A'),(986,'18806','2024-12-07 21:21:29','C'),(987,'18806','2024-12-07 21:21:29','A'),(988,'18806','2024-12-07 21:21:29','C'),(989,'18806','2024-12-07 21:21:29','A'),(990,'18806','2024-12-07 21:21:29','C'),(991,'18806','2024-12-07 21:21:29','A'),(992,'18806','2024-12-07 21:21:29','C'),(993,'18806','2024-12-07 21:21:29','A'),(994,'18806','2024-12-07 21:21:29','C'),(995,'18806','2024-12-07 21:21:29','A'),(996,'18806','2024-12-07 21:21:30','C'),(997,'18806','2024-12-07 21:21:30','A'),(998,'18806','2024-12-07 21:21:30','C'),(999,'18806','2024-12-07 21:21:31','D'),(1000,'18806','2024-12-07 21:21:34','B'),(1001,'18806','2024-12-07 21:21:34','D'),(1002,'18806','2024-12-07 21:21:34','B'),(1003,'18806','2024-12-07 21:21:34','D'),(1004,'18806','2024-12-07 21:21:34','B'),(1005,'18806','2024-12-07 21:21:34','D'),(1006,'18806','2024-12-07 21:21:34','B'),(1007,'18806','2024-12-07 21:21:34','D'),(1008,'18806','2024-12-07 21:21:34','B'),(1009,'18806','2024-12-07 21:21:34','D'),(1010,'18806','2024-12-07 21:21:34','B'),(1011,'18806','2024-12-08 09:16:44','C'),(1012,'18806','2024-12-08 09:16:58','D'),(1013,'18806','2024-12-09 12:37:46','B'),(1014,'18806','2024-12-09 12:37:46','D'),(1015,'18806','2024-12-09 12:37:51','B'),(1016,'18806','2024-12-09 16:11:18','C'),(1017,'18806','2024-12-09 16:11:40','D'),(1018,'18806','2024-12-09 16:12:15','B'),(1019,'18806','2024-12-09 16:12:15','D'),(1020,'18806','2024-12-09 16:12:21','B'),(1021,'18806','2024-12-09 16:13:45','C'),(1022,'18806','2024-12-09 16:14:05','D'),(1023,'18806','2024-12-09 16:14:12','B'),(1024,'18806','2024-12-09 16:14:31','D'),(1025,'18806','2024-12-09 16:16:17','C'),(1026,'18806','2024-12-09 16:16:19','B'),(1027,'1427157','2024-12-09 16:17:01','B'),(1028,'1427157','2024-12-09 16:17:03','C'),(1029,'1427157','2024-12-09 16:17:20','D'),(1030,'1427157','2024-12-09 16:17:26','B'),(1031,'1427157','2024-12-09 16:17:43','D'),(1032,'1427157','2024-12-09 16:17:47','C'),(1033,'1427157','2024-12-09 16:17:47','D'),(1034,'1427157','2024-12-09 16:17:47','C'),(1035,'1427157','2024-12-09 16:17:48','D'),(1036,'1427157','2024-12-09 16:17:48','C'),(1037,'1427157','2024-12-09 16:17:50','D'),(1038,'1427157','2024-12-09 16:17:51','C'),(1039,'1427157','2024-12-09 16:17:51','D'),(1040,'1427157','2024-12-09 16:17:51','C'),(1041,'1427157','2024-12-09 16:17:51','D'),(1042,'1427157','2024-12-09 16:17:51','C'),(1043,'1427157','2024-12-09 16:17:52','D'),(1044,'1427157','2024-12-09 16:17:52','C'),(1045,'1427157','2024-12-09 16:17:52','D'),(1046,'1427157','2024-12-09 16:17:52','C'),(1047,'1427157','2024-12-09 16:17:52','D'),(1048,'1427157','2024-12-09 16:18:03','B'),(1049,'1427157','2024-12-09 16:18:07','A'),(1050,'1427157','2024-12-09 16:18:13','C'),(1051,'63029','2024-12-10 08:45:30','A'),(1052,'63029','2024-12-10 08:45:32','C'),(1053,'63029','2024-12-10 08:45:38','A'),(1054,'63029','2024-12-10 08:45:39','C'),(1055,'63029','2024-12-10 08:45:41','A'),(1056,'63029','2024-12-10 08:45:41','C'),(1057,'63029','2024-12-10 08:45:41','A'),(1058,'63029','2024-12-10 08:45:41','C'),(1059,'63029','2024-12-10 08:45:41','A'),(1060,'63029','2024-12-10 08:45:41','C'),(1061,'63029','2024-12-10 08:45:41','A'),(1062,'63029','2024-12-10 08:45:41','C'),(1063,'63029','2024-12-10 08:45:41','A'),(1064,'63029','2024-12-10 08:45:41','C'),(1065,'63029','2024-12-10 08:45:41','A'),(1066,'63029','2024-12-10 08:45:41','C'),(1067,'63029','2024-12-10 08:45:41','A'),(1068,'63029','2024-12-10 08:45:41','C'),(1069,'63029','2024-12-10 08:45:41','A'),(1070,'63029','2024-12-10 08:45:41','C'),(1071,'63029','2024-12-10 08:45:41','A'),(1072,'63029','2024-12-10 08:45:42','C'),(1073,'63029','2024-12-10 08:45:42','A'),(1074,'63029','2024-12-10 08:45:42','C'),(1075,'63029','2024-12-10 08:45:42','A'),(1076,'63029','2024-12-10 08:45:42','C'),(1077,'63029','2024-12-10 08:45:43','D'),(1078,'63029','2024-12-10 08:45:46','B'),(1079,'63029','2024-12-10 08:45:46','D'),(1080,'63029','2024-12-10 08:45:46','B'),(1081,'63029','2024-12-10 08:45:46','D'),(1082,'63029','2024-12-10 08:45:46','B'),(1083,'63029','2024-12-10 08:45:46','D'),(1084,'63029','2024-12-10 08:45:46','B'),(1085,'63029','2024-12-10 08:45:46','D'),(1086,'63029','2024-12-10 08:45:46','B'),(1087,'63029','2024-12-10 08:45:46','D'),(1088,'63029','2024-12-10 08:46:21','B'),(1089,'1427157','2024-12-10 08:49:17','B'),(1090,'63029','2024-12-10 08:49:40','C'),(1091,'63029','2024-12-10 10:45:21','B');
/*!40000 ALTER TABLE `barcode_scans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `box_stacking`
--

DROP TABLE IF EXISTS `box_stacking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `box_stacking` (
  `stack_id` int NOT NULL AUTO_INCREMENT,
  `pallet_id` int NOT NULL,
  `box_id` int NOT NULL,
  `stack_level` int NOT NULL,
  PRIMARY KEY (`stack_id`),
  UNIQUE KEY `pallet_id` (`pallet_id`,`box_id`),
  KEY `box_id` (`box_id`),
  CONSTRAINT `box_stacking_ibfk_1` FOREIGN KEY (`pallet_id`) REFERENCES `pallets` (`pallet_id`),
  CONSTRAINT `box_stacking_ibfk_2` FOREIGN KEY (`box_id`) REFERENCES `boxes` (`box_id`),
  CONSTRAINT `box_stacking_chk_1` CHECK ((`stack_level` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `box_stacking`
--

LOCK TABLES `box_stacking` WRITE;
/*!40000 ALTER TABLE `box_stacking` DISABLE KEYS */;
/*!40000 ALTER TABLE `box_stacking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boxes`
--

DROP TABLE IF EXISTS `boxes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boxes` (
  `box_id` int NOT NULL AUTO_INCREMENT,
  `box_label` varchar(255) NOT NULL,
  `length` decimal(10,2) NOT NULL,
  `width` decimal(10,2) NOT NULL,
  `height` decimal(10,2) NOT NULL,
  `weight` decimal(10,2) NOT NULL,
  `pallet_id` int DEFAULT NULL,
  PRIMARY KEY (`box_id`),
  UNIQUE KEY `box_label` (`box_label`),
  KEY `pallet_id` (`pallet_id`),
  CONSTRAINT `boxes_ibfk_1` FOREIGN KEY (`pallet_id`) REFERENCES `pallets` (`pallet_id`),
  CONSTRAINT `boxes_chk_1` CHECK ((`weight` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boxes`
--

LOCK TABLES `boxes` WRITE;
/*!40000 ALTER TABLE `boxes` DISABLE KEYS */;
INSERT INTO `boxes` VALUES (1,'defaultclient1',24.00,29.00,29.00,1.00,NULL),(2,'defaultclient2',21.00,38.00,38.00,1.00,NULL),(3,'defaultclient3',24.00,29.00,29.00,1.00,NULL),(4,'defaultclient4',21.00,38.00,38.00,1.00,NULL),(5,'defaultclient5',13.00,8.00,8.00,1.00,NULL),(6,'defaultclient6',70.00,71.00,71.00,1.00,NULL),(7,'defaultclient7',18.00,9.00,9.00,1.00,NULL),(8,'defaultclient8',24.00,29.00,29.00,1.00,NULL),(9,'defaultclient9',21.00,38.00,38.00,1.00,NULL),(10,'defaultclient10',21.00,30.00,30.00,1.00,NULL),(11,'defaultclient11',48.00,41.00,41.00,1.00,NULL),(12,'defaultclient12',14.00,28.00,28.00,1.00,NULL),(13,'defaultclient13',19.00,55.00,55.00,1.00,NULL),(14,'defaultclient14',22.00,36.00,36.00,1.00,NULL),(15,'defaultclient15',39.00,33.00,33.00,1.00,NULL),(16,'defaultclient16',39.00,33.00,33.00,1.00,NULL),(17,'defaultclient17',45.00,73.00,73.00,1.00,NULL),(18,'defaultclient18',39.00,33.00,33.00,1.00,NULL),(19,'defaultclient19',45.00,73.00,73.00,1.00,NULL),(20,'defaultclient20',54.00,33.00,33.00,1.00,NULL),(21,'defaultclient21',90.00,73.00,73.00,1.00,NULL),(22,'defaultclient22',31.00,27.00,27.00,1.00,NULL),(23,'defaultclient23',96.00,67.00,67.00,1.00,NULL),(24,'defaultclient24',17.00,23.00,23.00,1.00,NULL),(25,'defaultclient25',37.00,26.00,26.00,1.00,NULL),(26,'defaultclient26',39.00,33.00,33.00,1.00,NULL);
/*!40000 ALTER TABLE `boxes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clients` (
  `client_id` int NOT NULL AUTO_INCREMENT,
  `client_name` varchar(255) NOT NULL,
  `client_address` varchar(255) DEFAULT NULL,
  `contact_details` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (1,'Default Client','123 Main St','contact@example.com');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `inventory_id` int NOT NULL AUTO_INCREMENT,
  `client_id` int NOT NULL,
  `description` varchar(255) NOT NULL,
  `quantity` int NOT NULL,
  `box_id` int DEFAULT NULL,
  PRIMARY KEY (`inventory_id`),
  KEY `client_id` (`client_id`),
  KEY `box_id` (`box_id`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `clients` (`client_id`),
  CONSTRAINT `inventory_ibfk_2` FOREIGN KEY (`box_id`) REFERENCES `boxes` (`box_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,1,'defaultclient1 24x29',1,1),(2,1,'defaultclient2 21x38',1,2),(3,1,'defaultclient3 24x29',1,3),(4,1,'defaultclient4 21x38',1,4),(5,1,'defaultclient5 13x8',1,5),(6,1,'defaultclient6 70x71',1,6),(7,1,'defaultclient7 18x9',1,7),(8,1,'defaultclient8 24x29',1,8),(9,1,'defaultclient9 21x38',1,9),(10,1,'defaultclient10 21x30',1,10),(11,1,'defaultclient11 48x41',1,11),(12,1,'defaultclient12 14x28',1,12),(13,1,'defaultclient13 19x55',1,13),(14,1,'defaultclient14 22x36',1,14),(15,1,'defaultclient15 39x33',1,15),(16,1,'defaultclient16 39x33',1,16),(17,1,'defaultclient17 45x73',1,17),(18,1,'defaultclient18 39x33',1,18),(19,1,'defaultclient19 45x73',1,19),(20,1,'defaultclient20 54x33',1,20),(21,1,'defaultclient21 90x73',1,21),(22,1,'defaultclient22 31x27',1,22),(23,1,'defaultclient23 96x67',1,23),(24,1,'defaultclient24 17x23',1,24),(25,1,'defaultclient25 37x26',1,25),(26,1,'defaultclient26 39x33',1,26);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pallet_movements`
--

DROP TABLE IF EXISTS `pallet_movements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pallet_movements` (
  `movement_id` int NOT NULL AUTO_INCREMENT,
  `pallet_id` int NOT NULL,
  `timestamp` datetime DEFAULT CURRENT_TIMESTAMP,
  `from_zone` varchar(50) DEFAULT NULL,
  `to_zone` varchar(50) DEFAULT NULL,
  `barcode` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`movement_id`),
  KEY `pallet_id` (`pallet_id`),
  CONSTRAINT `pallet_movements_ibfk_1` FOREIGN KEY (`pallet_id`) REFERENCES `pallets` (`pallet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pallet_movements`
--

LOCK TABLES `pallet_movements` WRITE;
/*!40000 ALTER TABLE `pallet_movements` DISABLE KEYS */;
/*!40000 ALTER TABLE `pallet_movements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pallets`
--

DROP TABLE IF EXISTS `pallets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pallets` (
  `pallet_id` int NOT NULL AUTO_INCREMENT,
  `pallet_label` varchar(255) NOT NULL,
  `pallet_quality` varchar(100) NOT NULL,
  `capacity` decimal(10,2) NOT NULL,
  PRIMARY KEY (`pallet_id`),
  UNIQUE KEY `pallet_label` (`pallet_label`),
  CONSTRAINT `pallets_chk_1` CHECK ((`pallet_quality` in (_utf8mb4'Good',_utf8mb4'Bad',_utf8mb4'Damaged'))),
  CONSTRAINT `pallets_chk_2` CHECK ((`capacity` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pallets`
--

LOCK TABLES `pallets` WRITE;
/*!40000 ALTER TABLE `pallets` DISABLE KEYS */;
/*!40000 ALTER TABLE `pallets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zone`
--

DROP TABLE IF EXISTS `zone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zone` (
  `zone_id` int NOT NULL AUTO_INCREMENT,
  `zone_name` varchar(10) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `video_path` varchar(255) NOT NULL,
  PRIMARY KEY (`zone_id`),
  UNIQUE KEY `zone_name` (`zone_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zone`
--

LOCK TABLES `zone` WRITE;
/*!40000 ALTER TABLE `zone` DISABLE KEYS */;
/*!40000 ALTER TABLE `zone` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-10 23:28:45
