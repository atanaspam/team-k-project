CREATE DATABASE  IF NOT EXISTS `mydb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `mydb`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.6.21-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `address` (
  `addressID` int(11) NOT NULL,
  `city` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `street` varchar(45) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `label` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`addressID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (1,'Glasgow','United Kingdom','University avenue',56,'main address');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `block`
--

DROP TABLE IF EXISTS `block`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `block` (
  `BlockID` int(11) NOT NULL,
  `beginDate` date NOT NULL,
  `endDate` date NOT NULL,
  `label` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`BlockID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `block`
--

LOCK TABLES `block` WRITE;
/*!40000 ALTER TABLE `block` DISABLE KEYS */;
INSERT INTO `block` VALUES (1,'2014-12-15','2014-12-15','Morning'),(2,'2014-12-15','2014-12-15','Afternoon'),(3,'2014-12-16','2014-12-16','Morning'),(4,'2014-12-16','2014-12-16','Afternoon'),(5,'2014-12-17','2014-12-17','Morning'),(6,'2014-12-17','2014-12-17','Afternoon'),(7,'2014-12-18','2014-12-18','Morning'),(8,'2014-12-18','2014-12-18','Afternoon'),(9,'2014-12-19','2014-12-19','Morning'),(10,'2014-12-19','2014-12-19','Afternoon'),(11,'2014-12-20','2014-12-20','Morning'),(12,'2014-12-20','2014-12-20','Afternoon'),(13,'2014-12-15','2014-12-21','Week'),(14,'2014-12-22','2014-12-28','Week'),(15,'2014-12-22','2014-12-22','Morning'),(16,'2014-12-22','2014-12-22','Afternoon');
/*!40000 ALTER TABLE `block` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `btm rank`
--

DROP TABLE IF EXISTS `btm rank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `btm rank` (
  `uID` int(11) NOT NULL,
  `membershipNum` int(11) DEFAULT NULL,
  `numOfPonts` int(11) DEFAULT NULL,
  PRIMARY KEY (`uID`),
  KEY `fk_BTM Rank_User1_idx` (`uID`),
  CONSTRAINT `fk_BTM Rank_User1` FOREIGN KEY (`uID`) REFERENCES `user` (`uID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='British Tennis Membership Rank';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `btm rank`
--

LOCK TABLES `btm rank` WRITE;
/*!40000 ALTER TABLE `btm rank` DISABLE KEYS */;
/*!40000 ALTER TABLE `btm rank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experience`
--

DROP TABLE IF EXISTS `experience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `experience` (
  `experienceID` int(11) NOT NULL,
  `XP` int(11) NOT NULL,
  PRIMARY KEY (`experienceID`),
  KEY `fk_Experience_ExperienceLevel1_idx` (`XP`),
  CONSTRAINT `fk_Experience_ExperienceLevel1` FOREIGN KEY (`XP`) REFERENCES `experiencelevel` (`levelID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experience`
--

LOCK TABLES `experience` WRITE;
/*!40000 ALTER TABLE `experience` DISABLE KEYS */;
INSERT INTO `experience` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(11,5),(12,5),(13,5),(14,5),(15,5),(16,5),(17,5),(18,5),(19,5),(20,5),(21,5),(22,5),(23,5),(24,5),(25,5),(26,5),(27,5),(28,5),(29,5),(30,5),(31,5),(32,5),(33,5),(34,5),(35,5),(36,5),(37,5),(38,5),(39,5),(40,5),(41,5),(42,5),(43,5),(44,5),(45,5),(46,5),(47,5),(48,5),(49,5),(50,5),(51,5),(52,5),(53,5),(54,5),(55,5),(56,5),(57,5),(58,5),(59,5),(60,5),(61,5),(62,5),(63,5),(64,5),(65,5),(66,5),(67,5),(68,5),(69,5),(70,5),(71,5),(72,5),(73,5),(74,5),(75,5),(76,5),(77,5),(78,5),(79,5),(80,5),(81,5),(82,5),(83,5),(84,5),(85,5),(86,5),(87,5),(88,5),(89,5),(90,5),(91,5),(92,5),(93,5),(94,5),(95,5),(96,5),(97,5),(98,5),(99,5),(100,5),(101,5),(102,5),(6,6),(7,7),(8,8),(9,9),(10,10);
/*!40000 ALTER TABLE `experience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiencelevel`
--

DROP TABLE IF EXISTS `experiencelevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `experiencelevel` (
  `levelID` int(11) NOT NULL,
  `label` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`levelID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiencelevel`
--

LOCK TABLES `experiencelevel` WRITE;
/*!40000 ALTER TABLE `experiencelevel` DISABLE KEYS */;
INSERT INTO `experiencelevel` VALUES (1,'First time player'),(2,'Semi-Newbie'),(3,'Newbie'),(4,'Semi-Average'),(5,'Average'),(6,'Above Average'),(7,'Great'),(8,'Semi-Pro'),(9,'Pro'),(10,'Godlike');
/*!40000 ALTER TABLE `experiencelevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `extras`
--

DROP TABLE IF EXISTS `extras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `extras` (
  `extrasID` int(11) NOT NULL,
  `label` varchar(45) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `ownerSessionID` int(11) NOT NULL,
  PRIMARY KEY (`extrasID`,`ownerSessionID`),
  KEY `fk_Extras_Session1_idx` (`ownerSessionID`),
  CONSTRAINT `fk_Extras_Session1` FOREIGN KEY (`ownerSessionID`) REFERENCES `session` (`sessionID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `extras`
--

LOCK TABLES `extras` WRITE;
/*!40000 ALTER TABLE `extras` DISABLE KEYS */;
/*!40000 ALTER TABLE `extras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logindetails`
--

DROP TABLE IF EXISTS `logindetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logindetails` (
  `password` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `User_uID` int(11) NOT NULL,
  PRIMARY KEY (`User_uID`),
  CONSTRAINT `fk_LoginDetails_User1` FOREIGN KEY (`User_uID`) REFERENCES `user` (`uID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logindetails`
--

LOCK TABLES `logindetails` WRITE;
/*!40000 ALTER TABLE `logindetails` DISABLE KEYS */;
INSERT INTO `logindetails` VALUES ('admin','admin',1),('manager','manager',2),('user','user1',3),('user','user2',4),('user','user3',5),('user','user4',6),('user','user5',7),('user','user6',8),('user','user7',9),('user','user8',10),('user','user9',11),('user','user10',12),('user','user11',13),('user','user12',14),('user','user13',15),('user','user14',16),('user','user15',17),('user','user16',18),('user','user17',19),('user','user18',20),('user','user19',21),('user','user20',22),('user','user21',23),('user','user22',24),('user','user23',25),('user','user24',26),('user','user25',27),('user','user26',28),('user','user27',29),('user','user28',30),('user','user29',31),('user','user30',32),('user','user31',33),('user','user32',34),('user','user33',35),('user','user34',36),('user','user35',37),('user','user36',38),('user','user37',39),('user','user38',40),('user','user39',41),('user','user40',42),('user','user41',43),('user','user42',44),('user','user43',45),('user','user44',46),('user','user45',47),('user','user46',48),('user','user47',49),('user','user48',50),('user','user49',51),('user','user50',52),('user','user51',53),('user','user52',54),('user','user53',55),('user','user54',56),('user','user55',57),('user','user56',58),('user','user57',59),('user','user58',60),('user','user59',61),('user','user60',62),('user','user61',63),('user','user62',64),('user','user63',65),('user','user64',66),('user','user65',67),('user','user66',68),('user','user67',69),('user','user68',70),('user','user69',71),('user','user70',72),('user','user71',73),('user','user72',74),('user','user73',75),('user','user74',76),('user','user75',77),('user','user76',78),('user','user77',79),('user','user78',80),('user','user79',81),('user','user80',82),('user','user81',83),('user','user82',84),('user','user83',85),('user','user84',86),('user','user85',87),('user','user86',88),('user','user87',89),('user','user88',90),('user','user89',91),('user','user90',92),('user','user91',93),('user','user92',94),('user','user93',95),('user','user94',96),('user','user95',97),('user','user96',98),('user','user97',99),('user','user98',100);
/*!40000 ALTER TABLE `logindetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notes`
--

DROP TABLE IF EXISTS `notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notes` (
  `noteID` int(11) NOT NULL,
  `Note` mediumtext,
  `Session_sessionID` int(11) NOT NULL,
  `hasNotes` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`noteID`,`Session_sessionID`),
  KEY `fk_Notes_Session1_idx` (`Session_sessionID`),
  CONSTRAINT `fk_Notes_Session1` FOREIGN KEY (`Session_sessionID`) REFERENCES `session` (`sessionID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notes`
--

LOCK TABLES `notes` WRITE;
/*!40000 ALTER TABLE `notes` DISABLE KEYS */;
/*!40000 ALTER TABLE `notes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment` (
  `paymentID` int(11) NOT NULL,
  `amount` int(11) DEFAULT NULL,
  `label` varchar(45) DEFAULT NULL,
  `hasPayed` tinyint(1) DEFAULT NULL,
  `dueDate` date DEFAULT NULL,
  `payedDate` date DEFAULT NULL,
  `userToPay` int(11) NOT NULL,
  `paymentType` int(11) NOT NULL,
  PRIMARY KEY (`paymentID`,`userToPay`),
  KEY `fk_Payment_User1_idx` (`userToPay`),
  KEY `fk_Payment_paymentType1_idx` (`paymentType`),
  CONSTRAINT `fk_Payment_User1` FOREIGN KEY (`userToPay`) REFERENCES `user` (`uID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Payment_paymentType1` FOREIGN KEY (`paymentType`) REFERENCES `paymenttype` (`typeID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paymenttype`
--

DROP TABLE IF EXISTS `paymenttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paymenttype` (
  `typeID` int(11) NOT NULL,
  `typeLabel` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`typeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paymenttype`
--

LOCK TABLES `paymenttype` WRITE;
/*!40000 ALTER TABLE `paymenttype` DISABLE KEYS */;
/*!40000 ALTER TABLE `paymenttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `privelegetypes`
--

DROP TABLE IF EXISTS `privelegetypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `privelegetypes` (
  `priveleges` bit(8) NOT NULL,
  `privelegeLabel` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`priveleges`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `privelegetypes`
--

LOCK TABLES `privelegetypes` WRITE;
/*!40000 ALTER TABLE `privelegetypes` DISABLE KEYS */;
INSERT INTO `privelegetypes` VALUES ('','User'),('','Parent'),('','Supervisor'),('','Coach'),('','Manager'),('','Admin'),('','Other1'),('','Other2'),('	','Other3');
/*!40000 ALTER TABLE `privelegetypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `privileges`
--

DROP TABLE IF EXISTS `privileges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `privileges` (
  `privilegeID` int(11) NOT NULL,
  `privilege` bit(8) NOT NULL,
  PRIMARY KEY (`privilegeID`),
  KEY `fk_Privileges_PrivelegeTypes1_idx` (`privilege`),
  CONSTRAINT `fk_Privileges_PrivelegeTypes1` FOREIGN KEY (`privilege`) REFERENCES `privelegetypes` (`priveleges`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `privileges`
--

LOCK TABLES `privileges` WRITE;
/*!40000 ALTER TABLE `privileges` DISABLE KEYS */;
INSERT INTO `privileges` VALUES (1,''),(2,''),(3,''),(4,''),(5,''),(6,''),(63,''),(7,''),(8,''),(9,''),(10,''),(11,''),(12,''),(13,''),(14,''),(15,''),(16,''),(17,''),(18,''),(19,''),(20,''),(21,''),(22,''),(23,''),(24,''),(25,''),(26,''),(27,''),(28,''),(29,''),(30,''),(31,''),(32,''),(33,''),(34,''),(35,''),(36,''),(37,''),(38,''),(39,''),(40,''),(41,''),(42,''),(43,''),(44,''),(45,''),(46,''),(47,''),(48,''),(49,''),(50,''),(51,''),(52,''),(53,''),(54,''),(55,''),(56,''),(57,''),(58,''),(59,''),(60,''),(61,''),(62,''),(64,''),(65,''),(66,''),(67,''),(68,''),(69,''),(70,''),(71,''),(72,''),(73,''),(74,''),(75,''),(76,''),(77,''),(78,''),(79,''),(80,''),(81,''),(82,''),(83,''),(84,''),(85,''),(86,''),(87,''),(88,''),(89,''),(90,''),(91,''),(92,''),(93,''),(94,''),(95,''),(96,''),(97,''),(98,''),(99,''),(100,''),(101,''),(102,''),(103,'');
/*!40000 ALTER TABLE `privileges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `session` (
  `sessionID` int(11) NOT NULL,
  `duration` varchar(45) DEFAULT NULL,
  `beginTime` datetime DEFAULT NULL,
  `endTime` datetime DEFAULT NULL,
  `Block_BlockID` int(11) NOT NULL,
  `capacity` int(11) DEFAULT NULL,
  `ageGroup` varchar(45) DEFAULT NULL,
  `skillGroup` varchar(45) DEFAULT NULL,
  `isFull` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sessionID`,`Block_BlockID`),
  KEY `fk_Session_Block1_idx` (`Block_BlockID`),
  CONSTRAINT `fk_Session_Block1` FOREIGN KEY (`Block_BlockID`) REFERENCES `block` (`BlockID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
INSERT INTO `session` VALUES (1,'1,5','2014-12-15 08:00:00','2014-12-15 09:30:00',1,10,'13-25',NULL,'0'),(2,'1,5','2014-12-15 10:00:00','2014-12-15 11:30:00',1,10,'13-25',NULL,'0'),(3,'1,5','2014-12-15 12:00:00','2014-12-15 13:30:00',1,10,'13-25',NULL,'0'),(4,'1,5','2014-12-15 15:00:00','2014-12-15 16:30:00',2,10,'13-25',NULL,'0'),(5,'1,5','2014-12-15 17:00:00','2014-12-15 18:30:00',2,10,'13-25',NULL,'0'),(6,'1','2014-12-15 19:00:00','2014-12-15 20:00:00',2,10,'13-25',NULL,'0'),(7,'1,5','2014-12-16 08:00:00','2014-12-16 09:30:00',3,10,'13-25',NULL,'0'),(8,'1,5','2014-12-16 10:00:00','2014-12-16 11:30:00',3,10,'13-25',NULL,'0'),(9,'1,5','2014-12-16 12:00:00','2014-12-16 13:30:00',3,10,'13-25',NULL,'0'),(10,'1,5','2014-12-16 15:00:00','2014-12-16 16:30:00',4,10,'13-25',NULL,'0'),(11,'1,5','2014-12-16 17:00:00','2014-12-16 18:30:00',4,10,'13-25',NULL,'0'),(12,'1','2014-12-16 19:00:00','2014-12-16 20:00:00',4,10,'13-25',NULL,'0'),(13,'1,5','2014-12-17 08:00:00','2014-12-17 09:30:00',5,10,'13-25',NULL,'0'),(14,'1,5','2014-12-17 10:00:00','2014-12-17 11:30:00',5,10,'13-25',NULL,'0'),(15,'1,5','2014-12-17 12:00:00','2014-12-17 13:30:00',5,10,'13-25',NULL,'0'),(16,'1,5','2014-12-17 15:00:00','2014-12-17 16:30:00',6,10,'13-25',NULL,'0'),(17,'1,5','2014-12-17 17:00:00','2014-12-17 18:30:00',6,10,'13-25',NULL,'0'),(18,'1','2014-12-17 19:00:00','2014-12-17 20:00:00',6,10,'13-25',NULL,'0'),(19,'1,5','2014-12-18 08:00:00','2014-12-18 09:30:00',7,10,'13-25',NULL,'0'),(20,'1,5','2014-12-18 10:00:00','2014-12-18 11:30:00',7,10,'13-25',NULL,'0'),(21,'1,5','2014-12-18 12:00:00','2014-12-18 13:30:00',7,10,'13-25',NULL,'0'),(22,'1,5','2014-12-18 15:00:00','2014-12-18 16:30:00',8,10,'13-25',NULL,'0'),(23,'1,5','2014-12-18 17:00:00','2014-12-18 18:30:00',8,10,'13-25',NULL,'0'),(24,'1','2014-12-18 19:00:00','2014-12-18 20:00:00',8,10,'13-25',NULL,'0'),(25,'1,5','2014-12-19 08:00:00','2014-12-19 09:30:00',9,10,'13-25',NULL,'0'),(26,'1,5','2014-12-19 10:00:00','2014-12-19 11:30:00',9,10,'13-25',NULL,'0'),(27,'1,5','2014-12-19 12:00:00','2014-12-19 13:30:00',9,10,'13-25',NULL,'0'),(28,'1,5','2014-12-19 15:00:00','2014-12-19 16:30:00',10,10,'13-25',NULL,'0'),(29,'1,5','2014-12-19 17:00:00','2014-12-19 18:30:00',10,10,'13-25',NULL,'0'),(30,'1','2014-12-19 19:00:00','2014-12-19 20:00:00',10,10,'13-25',NULL,'0'),(31,'1,5','2014-12-15 08:00:00','2014-12-15 09:30:00',1,10,'08-25',NULL,'0'),(32,'1,5','2014-12-15 10:00:00','2014-12-15 11:30:00',1,10,'08-25',NULL,'0'),(33,'1,5','2014-12-15 12:00:00','2014-12-15 13:30:00',1,10,'08-25',NULL,'0'),(34,'1,5','2014-12-15 15:00:00','2014-12-15 16:30:00',2,10,'08-25',NULL,'0'),(35,'1,5','2014-12-15 17:00:00','2014-12-15 18:30:00',2,10,'08-25',NULL,'0'),(36,'1','2014-12-15 19:00:00','2014-12-15 20:00:00',2,10,'08-35',NULL,'0');
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subvenue`
--

DROP TABLE IF EXISTS `subvenue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subvenue` (
  `subVenueID` int(11) NOT NULL,
  `label` varchar(45) DEFAULT NULL,
  `capacity` varchar(45) DEFAULT NULL,
  `ownerVenue` int(11) NOT NULL,
  PRIMARY KEY (`subVenueID`,`ownerVenue`),
  KEY `fk_SubVenue_Venue1_idx` (`ownerVenue`),
  CONSTRAINT `fk_SubVenue_Venue1` FOREIGN KEY (`ownerVenue`) REFERENCES `venue` (`venueID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subvenue`
--

LOCK TABLES `subvenue` WRITE;
/*!40000 ALTER TABLE `subvenue` DISABLE KEYS */;
INSERT INTO `subvenue` VALUES (1,'Court1','10',1),(2,'Court2','10',1),(3,'Court3','10',1),(4,'Court4','10',1),(5,'Court5','10',1),(6,'Court6','10',1),(7,'Court7','10',1),(8,'Court8','10',1);
/*!40000 ALTER TABLE `subvenue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subvenue_usedfor_session`
--

DROP TABLE IF EXISTS `subvenue_usedfor_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subvenue_usedfor_session` (
  `Session_sessionID` int(11) NOT NULL,
  `SubVenue_subVenueID` int(11) NOT NULL,
  `SubVenue_ownerVenue` int(11) NOT NULL,
  PRIMARY KEY (`Session_sessionID`,`SubVenue_subVenueID`,`SubVenue_ownerVenue`),
  KEY `fk_Session_has_SubVenue_SubVenue1_idx` (`SubVenue_subVenueID`,`SubVenue_ownerVenue`),
  KEY `fk_Session_has_SubVenue_Session1_idx` (`Session_sessionID`),
  CONSTRAINT `fk_Session_has_SubVenue_Session1` FOREIGN KEY (`Session_sessionID`) REFERENCES `session` (`sessionID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Session_has_SubVenue_SubVenue1` FOREIGN KEY (`SubVenue_subVenueID`, `SubVenue_ownerVenue`) REFERENCES `subvenue` (`subVenueID`, `ownerVenue`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subvenue_usedfor_session`
--

LOCK TABLES `subvenue_usedfor_session` WRITE;
/*!40000 ALTER TABLE `subvenue_usedfor_session` DISABLE KEYS */;
INSERT INTO `subvenue_usedfor_session` VALUES (1,1,1),(2,1,1),(3,1,1),(4,1,1),(5,1,1),(6,1,1),(7,1,1),(8,1,1),(9,1,1),(10,1,1),(11,1,1),(12,1,1),(13,1,1),(14,1,1),(15,1,1),(16,1,1),(17,1,1),(18,1,1),(19,1,1),(20,1,1),(21,1,1),(22,1,1),(23,1,1),(24,1,1),(25,1,1),(26,1,1),(27,1,1),(28,1,1),(29,1,1),(30,1,1),(31,2,1),(32,2,1),(33,2,1),(34,2,1),(35,2,1),(36,2,1);
/*!40000 ALTER TABLE `subvenue_usedfor_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `uID` int(11) NOT NULL,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL COMMENT 'Maby remove medical condition??',
  `email` varchar(45) DEFAULT NULL,
  `telephone` bigint(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `medicalCondition` varchar(45) DEFAULT NULL,
  `isMember` tinyint(1) DEFAULT NULL,
  `managedBy` int(11) DEFAULT NULL,
  `privilegeID` int(11) NOT NULL,
  `xperienceID` int(11) NOT NULL,
  `belongsTo` int(11) NOT NULL,
  `genderID` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`uID`,`privilegeID`,`xperienceID`),
  KEY `fk_User_Privileges1_idx` (`privilegeID`),
  KEY `fk_User_Experience1_idx` (`xperienceID`),
  CONSTRAINT `fk_User_Experience1` FOREIGN KEY (`xperienceID`) REFERENCES `experience` (`experienceID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_Privileges1` FOREIGN KEY (`privilegeID`) REFERENCES `privileges` (`privilegeID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Atanas ','Pamukchiev','burt.jules@tintired.info',6920000869,8,'linen island able',0,10,63,94,19,1),(2,'Jorge ','Strong','johnathon.silas.frederic@hope.edu',9925952894,15,'wall produce decision',0,10,15,61,46,0),(3,'Trisha ','Childress','lucia.marta@money.me',3752410969,14,'equal',1,9,28,25,1,1),(4,'Mohamed ','Sims','sheree.carly@putquality.me',5079494990,15,'memory to again',1,5,92,56,64,1),(5,'Margo ','Shafer','garry.geoffrey@field.info',5884869039,13,'army flag credit',1,3,91,93,91,1),(6,'Ezekiel ','Childs','deon@digestiondirection.me',6145256480,9,'possible',1,3,45,62,96,0),(7,'Ericka ','Duke','carmelo.barney.nestor@healthyhear.org',1006363469,17,'burn slope ornament',0,3,5,31,77,1),(8,'Vicky ','Coffey','stuart.fredrick@ringriver.edu',2310430901,7,'complete back push at week',1,8,35,21,34,1),(9,'Catrina ','Ortega','dylan.chuck@kiss.info',3104981171,18,'before separate pain mine',1,6,36,87,55,0),(10,'Gladys ','Britton','domingo.santos@healthy.me',7739120218,14,'country clear',0,4,27,28,34,0),(11,'Krista ','Gonzalez','kurt.allan.nelson@woundwriting.info',1889529318,7,'disease hanging go month',1,6,20,5,85,0),(12,'Hector ','Dixon','dee.winnie@breath.me',2716488017,6,'do',1,5,12,7,10,1),(13,'Stacey ','Holley','tamra.aisha.wilda@straight.me',6325418616,18,'let amount cup',0,4,57,73,97,0),(14,'Arleen ','Reilly','brigitte@writingwrong.edu',4285598932,12,'give glass grass white',0,7,34,31,41,1),(15,'Dwain ','Miranda','nathaniel@wood.org',4387881187,16,'opinion free birth man mine',1,9,45,79,52,1),(16,'Iola ','Deleon','carmelo@soundsoup.org',9230718937,6,'other quick light oven leg',1,4,12,20,5,0),(17,'Frances ','Sawyer','patti@first.com',9387288723,6,'condition reading organizatio substance',0,2,28,75,44,0),(18,'Carmine ','Warren','werner.theo.geraldo@suddensugar.org',8392512936,18,'kettle knot',0,3,87,73,6,0),(19,'Jeffry ','Carson','sonja.lila@talltaste.org',5438798984,11,'market if',0,9,23,93,90,0),(20,'Lon ','Huffman','felix.jimmie@position.info',4594176770,11,'private back cause noise',0,4,12,76,96,1),(21,'Beverley ','Fischer','graciela.imogene@sandsay.info',7157211283,13,'attack pot',1,4,70,96,77,0),(22,'Perry ','Jordan','johnny.earl.jimmy@sex.org',5662262975,8,'talk high industry',0,10,73,6,94,1),(23,'Bret ','Rutherford','lauren.cathy@false.edu',9149145502,14,'smooth',1,8,5,3,19,1),(24,'Doug ','Madden','edith.kim@touchtown.com',1604126505,6,'wave fertile',0,5,71,40,99,1),(25,'Sonny ','Snider','vince.quincy.eddy@cookcopper.com',1999479435,18,'coal there jelly',0,4,55,94,25,1),(26,'Nellie ','Cash','lilia@behaviour.org',7602689351,10,'land',1,6,3,24,90,1),(27,'Harriett ','Shaffer','claudia.jackie.marcia@still.org',2416224815,15,'kick rhythm',0,10,1,43,84,1),(28,'Brendon ','Calderon','scotty@thumbthunder.com',4184470083,13,'from stem sign in noise',1,9,80,60,70,0),(29,'Clement ','Saunders','morton.jonas.forest@flatflight.edu',7222260385,12,'wine hammer moon young spoon',1,8,56,24,98,0),(30,'Elias ','Monroe','rosalinda@answerant.org',9409612404,11,'worm sun',0,3,9,14,46,0),(31,'Walter ','Moses','ross.virgil.andy@expansion.me',8120476356,9,'by',0,2,9,3,21,1),(32,'Megan ','Hutchinson','teri.cristina@jewel.org',1168307510,17,'probable this grip profit',0,5,15,36,35,1),(33,'Renee ','Sparks','dick@while.org',1117403540,12,'milk sort cheap have field',0,7,29,57,94,0),(34,'Carl ','Anderson','frederick@have.com',6398894956,16,'law story soft market condition',0,5,16,22,27,0),(35,'Marcelino ','Hastings','thanh.dillon.amado@measuremeat.org',6976600147,12,'print',0,5,87,6,96,0),(36,'Lily ','Merrill','shelley@damagedanger.org',9856862707,6,'page',0,1,28,54,58,0),(37,'Issac ','Krause','susie.olivia@againstagreement.edu',5171824782,17,'muscle spade edge',0,4,24,51,87,1),(38,'Viola ','Morales','hilario.bud.sal@certain.org',9801608083,17,'special normal music dirty',1,4,31,80,82,1),(39,'Lamont ','Cabrera','rex@sneezesnow.edu',3069091271,7,'again',0,7,71,28,16,0),(40,'Eddie ','Fitzpatrick','joni@goldgood.me',9282517683,12,'wheel free loud metal',0,9,36,75,35,1),(41,'Katherine ','Salinas','kira@personphysical.com',6356430271,10,'brown tired account grass chief',0,7,45,12,63,0),(42,'Pamala ','Farmer','adrian.rhea.marquita@army.org',6216708005,8,'as',1,4,83,95,46,0),(43,'Theron ','Benjamin','denny.davis@view.org',2242769060,8,'act',0,2,1,94,90,1),(44,'Max ','Farley','carly.james@night.me',4648468923,8,'form earth trousers',1,7,73,56,6,1),(45,'Hubert ','Moss','deshawn@burstbusiness.com',7086014328,9,'do rat history reason design',1,5,95,98,48,0),(46,'Jeanie ','Foley','cole.denny@family.edu',5327048547,9,'cover some material',0,2,31,38,55,1),(47,'Zachary ','Hartley','quinton@dropdry.edu',3743587228,11,'when respect gun',1,1,12,20,56,1),(48,'Karyn ','Donahue','raleigh@hanging.me',8672779193,9,'basket attention year meal',0,9,1,35,27,0),(49,'Shonda ','Sykes','issac.mary.dudley@interest.me',6975984086,10,'book sugar special current black',0,2,93,87,82,1),(50,'Charles ','Kaufman','renato.jc.hoyt@curve.com',7758441835,9,'rod',0,9,52,14,46,0),(51,'Rudolph ','Finch','wm@leatherleft.info',5633261376,7,'expert force paper',1,3,68,55,91,1),(52,'Art ','Bradshaw','ashley@illimportant.me',4365898032,7,'story not expansion rate',1,3,91,68,15,1),(53,'Michele ','Kelly','concetta.bertie.alba@hope.edu',3053853477,13,'disease when normal',0,6,21,81,62,0),(54,'Trevor ','Rouse','lillian@face.me',7178817845,12,'baby toe blood',1,9,16,36,77,0),(55,'Kitty ','Gilliam','carey@animal.me',2005893944,12,'crush fork door mother',0,4,71,4,48,1),(56,'Rigoberto ','Lindsey','lily@level.edu',4995285932,12,'stage drawer brain',1,10,93,91,46,0),(57,'Riley ','Burke','paula.diana@shamesharp.org',9930400306,16,'war thumb thread birth',1,4,39,66,4,0),(58,'Arturo ','Benson','virgilio.mary@wind.org',5832038579,6,'waiting month hand',0,4,47,72,7,0),(59,'Fred ','Webber','august.leonardo.jasper@burstbusiness.com',7314332354,6,'ant walk bridge left roof',1,5,45,61,13,1),(60,'Nona ','Shelton','anthony.kevin.jason@existence.edu',7621731512,10,'reaction bell',0,9,43,44,9,0),(61,'Randi ','Francis','tonya@laugh.info',1691334125,17,'tree open',1,2,85,66,76,0),(62,'Alisha ','Hale','calvin.alex@cruel.edu',2762980394,6,'play',0,7,19,87,8,1),(63,'Maura ','Flynn','jaclyn.gracie.sondra@otherout.info',8839543135,11,'complex',1,1,53,36,17,0),(64,'Earlene ','Madden','geraldine@kindkiss.info',2991345161,16,'statement',0,8,55,88,83,0),(65,'Beverly ','Sykes','marilynn.lucretia.karrie@threadthroat.com',4502323924,7,'river healthy sneeze ever',1,3,86,59,68,1),(66,'Alphonse ','Gibson','elisabeth@knife.info',1470853413,11,'fall loud cry scale',1,5,35,23,81,1),(67,'Mina ','Levy','larissa@hollow.org',9561845063,17,'word way',1,1,100,39,10,0),(68,'Kenny ','Fitzgerald','nora.margie@bulb.org',1755427936,10,'dust',0,4,53,63,25,1),(69,'Frankie ','King','elise@start.info',2937260970,9,'elastic tall power father',1,6,59,35,16,1),(70,'Danielle ','Boyle','therese.frankie.dena@stopstore.org',7248466717,14,'shoe',0,1,52,74,77,0),(71,'Cyrus ','Aguirre','warren@branch.info',7922146103,18,'south opinion',1,5,78,21,75,0),(72,'Susie ','Cochran','maynard@disgust.info',1619520853,9,'dependent',0,9,75,31,90,1),(73,'Tanya ','Sparks','amalia.savannah.anastasia@punishment.com',7327599609,7,'brush debt',0,6,67,44,41,1),(74,'Rosalee ','Starr','joni@propertyprose.edu',7980738516,6,'iron',0,10,84,18,3,0),(75,'Claud ','Ibarra','lauren@circle.org',4563594324,12,'band',0,7,46,2,30,0),(76,'Julio ','Ford','kristopher@jelly.org',9194111341,15,'roof swim clock narrow push',0,4,3,96,15,1),(77,'Mervin ','Potter','samatha.oralia@canvascard.org',5934337532,13,'structure sharp brass month play',1,4,44,22,56,1),(78,'Marcelino ','Singleton','jodi@purposepush.me',1315529629,15,'sex',0,9,85,13,60,1),(79,'Demetria ','Jackson','normand.kieth@tradetrain.edu',3092212329,14,'skirt error stamp society',0,3,48,39,69,1),(80,'Alec ','Mendez','juliana.aline@farm.me',4942235249,7,'let school while',0,3,79,88,64,0),(81,'Cecelia ','Braun','reina.lauretta.kylie@backbad.org',9411636031,15,'when river spade cause',0,2,66,62,23,1),(82,'Tana ','Gill','ezequiel.erasmo@left.com',1335300112,10,'wet island liquid skin grey',0,6,36,29,80,1),(83,'Randall ','Dailey','mindy@country.me',3468966458,18,'ring control',0,7,58,85,91,1),(84,'Cesar ','Neely','allison.tamara.joy@earearly.edu',4312076039,17,'ill run general spoon',0,6,42,90,27,0),(85,'Donnell ','Puckett','jimmie.everett@brushbucket.info',6456069612,13,'hard whip band natural and',1,9,100,92,82,0),(86,'Francis ','Bland','tad@scissorsscrew.edu',7979036497,7,'leaf long blue air',1,9,68,52,63,0),(87,'Josh ','Barker','archie@leftleg.org',6706864194,10,'song feather',1,3,22,98,82,0),(88,'Clarice ','Bowers','alonzo.elias@enoughequal.com',6199000765,13,'waiting',0,3,72,61,43,1),(89,'Owen ','Kline','janna.juliette.deena@militarymilk.org',4120087460,13,'cord regret bad',1,8,93,24,8,1),(90,'Catrina ','Olsen','inez.lynda@windowwine.me',8911067040,8,'cry left balance',0,4,48,92,37,1),(91,'Solomon ','Henry','ben.chester.cecil@warwarm.com',9670109418,13,'view plough tongue twist high',1,1,37,16,6,0),(92,'Jack ','Porter','heriberto.donnell.cole@tonguetooth.edu',3264255196,12,'sticky support sex',1,4,82,25,13,0),(93,'Vicky ','Case','joanne.eleanor.valerie@painpaint.org',1388632536,15,'paper',0,2,10,38,46,0),(94,'Ron ','Pacheco','mona@distance.com',9025616952,17,'nut knee flower fowl get',1,4,84,46,96,1),(95,'Briana ','Williamson','latisha.barbra@come.info',5700218162,7,'tight feeble science bottle future',0,8,18,67,26,1),(96,'Lauri ','Carson','shannon.sheila.ethel@wellwest.me',8745632775,18,'ship foot attention quick',0,5,87,36,78,1),(97,'Ronald ','Logan','lyndon@futuregarden.me',2878355270,9,'idea tired get bent ticket',1,3,76,56,91,0),(98,'Loretta ','Molina','chloe@mark.edu',8684603623,16,'feather protest burn',0,8,43,44,49,0),(99,'Loyd ','Dennis','ebony@penpencil.edu',2404013488,7,'connection snake',1,10,23,71,12,1),(100,'Agatha ','Smith','minh@old.edu',7479587950,18,'serious canvas full',0,7,92,3,79,0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_selects_session`
--

DROP TABLE IF EXISTS `user_selects_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_selects_session` (
  `User_uID` int(11) NOT NULL,
  `Session_sessionID` int(11) NOT NULL,
  PRIMARY KEY (`User_uID`,`Session_sessionID`),
  KEY `fk_User_has_Session_Session1_idx` (`Session_sessionID`),
  KEY `fk_User_has_Session_User1_idx` (`User_uID`),
  CONSTRAINT `fk_User_has_Session_Session1` FOREIGN KEY (`Session_sessionID`) REFERENCES `session` (`sessionID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_Session_User1` FOREIGN KEY (`User_uID`) REFERENCES `user` (`uID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_selects_session`
--

LOCK TABLES `user_selects_session` WRITE;
/*!40000 ALTER TABLE `user_selects_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_selects_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venue`
--

DROP TABLE IF EXISTS `venue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `venue` (
  `venueID` int(11) NOT NULL,
  `capacity` int(11) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `load` int(11) DEFAULT NULL,
  `Manager` int(11) NOT NULL,
  `Address_addressID` int(11) NOT NULL,
  PRIMARY KEY (`venueID`,`Manager`,`Address_addressID`),
  KEY `fk_Venue_User1_idx` (`Manager`),
  KEY `fk_Venue_Address1_idx` (`Address_addressID`),
  CONSTRAINT `fk_Venue_Address1` FOREIGN KEY (`Address_addressID`) REFERENCES `address` (`addressID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Venue_User1` FOREIGN KEY (`Manager`) REFERENCES `user` (`uID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venue`
--

LOCK TABLES `venue` WRITE;
/*!40000 ALTER TABLE `venue` DISABLE KEYS */;
INSERT INTO `venue` VALUES (1,100,'West End venue',90,1,1);
/*!40000 ALTER TABLE `venue` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-14  1:20:39
