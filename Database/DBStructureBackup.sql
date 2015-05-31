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
INSERT INTO `address` VALUES (1,'\'Glasgow\'','\'United Kingdom\'','\'University avenue\'',56,'\'main address\'');
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
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`BlockID`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `block`
--

LOCK TABLES `block` WRITE;
/*!40000 ALTER TABLE `block` DISABLE KEYS */;
INSERT INTO `block` VALUES (1,'2014-12-15','2014-12-15','Monday Morning','Morning'),(2,'2014-12-15','2014-12-15','MondayAfternoon','Afternoon'),(3,'2014-12-16','2014-12-16','Tuesday Morning','Morning'),(4,'2014-12-16','2014-12-16','TuesdayAfternoon','Afternoon'),(5,'2014-12-17','2014-12-17','Wednesday Morning','Morning'),(6,'2014-12-17','2014-12-17','Wednesday Afternoon','Afternoon'),(7,'2014-12-18','2014-12-18','Thursday Morning','Morning'),(8,'2014-12-18','2014-12-18','Thursday Afternoon','Afternoon'),(9,'2014-12-19','2014-12-19','Friday Morning','Morning'),(10,'2014-12-19','2014-12-19','Friday Afternoon','Afternoon'),(11,'2014-12-20','2014-12-20','Saturday Morning','Morning'),(12,'2014-12-20','2014-12-20','Saturday Afternoon','Afternoon'),(13,'2014-12-15','2014-12-21','Week n-1','Week'),(14,'2014-12-22','2014-12-28','Week n','Week'),(15,'2014-12-22','2014-12-22','Monday Morning','Morning'),(16,'2014-12-22','2014-12-22','Monday Afternoon','Afternoon'),(17,'2014-12-23','2014-12-23','Tuesday Morning','Morning'),(18,'2014-12-23','2014-12-23','Tuesday Afternoon','Afternoon'),(19,'2014-12-24','2014-12-24','Wednesday  Morning','Morning'),(20,'2014-12-24','2014-12-24','Wednesday Afternoon','Afternoon'),(21,'2014-12-25','2014-12-25','Thursday Morning','Morning'),(22,'2014-12-25','2014-12-25','Thursday Afternoon','Afternoon'),(23,'2014-12-26','2014-12-26','Friday Morning','Morning'),(24,'2014-12-26','2014-12-26','Friday Afternoon','Afternoon'),(25,'2014-12-27','2014-12-27','Saturday Morning','Morning'),(26,'2014-12-27','2014-12-27','Saturday Afternoon','Afternoon'),(27,'2015-01-19','2015-01-25','Week 1','Week'),(28,'2015-01-19','2015-01-19','Monday Morning','Morning'),(29,'2015-01-19','2015-01-19','Monday Afternoon','Afternoon'),(30,'2015-01-20','2015-01-20','Tuesday Morning','Morning'),(31,'2015-01-20','2015-01-20','Tuesday Afternoon','Afternoon'),(32,'2015-01-21','2015-01-21','Wednesday Morning','Morning'),(33,'2015-01-21','2015-01-21','Wednesday Afternoon','Afternoon'),(34,'2015-01-22','2015-01-22','Thursday Morning','Morning'),(35,'2015-01-22','2015-01-22','Thursday Afternoon','Afternoon'),(36,'2015-01-23','2015-01-23','Friday Morning','Morning'),(37,'2015-01-23','2015-01-23','Friday Afternoon','Afternoon'),(38,'2015-01-24','2015-01-24','Saturday Morning','Morning'),(39,'2015-01-24','2015-01-24','Saturday Afternoon','Afternoon'),(40,'2015-01-26','2015-02-01','Week 2','Week'),(41,'2015-01-26','2015-01-26','Monday Morning','Morning'),(42,'2015-01-26','2015-01-26','Monday Afternoon','Afternoon'),(43,'2015-01-27','2015-01-27','Tuesday Morning','Morning'),(44,'2015-01-27','2015-01-27','Tuesday Afternoon','Afternoon'),(45,'2015-01-28','2015-01-28','Wednesday Morning','Morning'),(46,'2015-01-28','2015-01-28','Wednesday Afternoon','Afternoon'),(47,'2015-01-29','2015-01-29','Thursday Morning','Morning'),(48,'2015-01-29','2015-01-29','Thursday Afternoon','Afternoon'),(49,'2015-01-30','2015-01-30','Friday Morning','Morning'),(50,'2015-01-30','2015-01-30','Friday Afternoon','Afternoon'),(51,'2015-01-31','2015-01-31','Saturday Morning','Morning'),(52,'2015-01-31','2015-01-31','Saturday Afternoon','Afternoon'),(53,'2015-02-02','2015-02-08','Week 3','Week'),(54,'2015-02-02','2015-02-02','Monday Morning','Morning'),(55,'2015-02-02','2015-02-02','Monday Afternoon','Afternoon'),(56,'2015-02-03','2015-02-03','Tuesday Morning','Morning'),(57,'2015-02-03','2015-02-03','Tuesday Afternoon','Afternoon'),(58,'2015-02-04','2015-02-04','Wednesday Morning','Morning'),(59,'2015-02-04','2015-02-04','Wednesday Afternoon','Afternoon'),(60,'2015-02-05','2015-02-05','Thursday Morning','Morning'),(61,'2015-02-05','2015-02-05','Thursday Afternoon','Afternoon'),(62,'2015-02-06','2015-02-06','Friday Morning','Morning'),(63,'2015-02-06','2015-02-06','Friday Afternoon','Afternoon'),(64,'2015-02-07','2015-02-07','Saturday Morning','Morning'),(65,'2015-02-07','2015-02-07','Saturday Afternoon','Afternoon');
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
  CONSTRAINT `uID` FOREIGN KEY (`uID`) REFERENCES `client` (`uID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='British Tennis Membership Rank';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `btm rank`
--

LOCK TABLES `btm rank` WRITE;
/*!40000 ALTER TABLE `btm rank` DISABLE KEYS */;
INSERT INTO `btm rank` VALUES (1,123456789,100),(2,132456789,20),(3,142356789,34),(4,152346789,11),(5,162345789,76),(6,172345689,55),(7,182345679,23),(8,192345678,0),(9,124356789,1),(10,125346789,-20);
/*!40000 ALTER TABLE `btm rank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `uID` int(11) NOT NULL,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL COMMENT 'Maby remove medical condition??',
  `email` varchar(45) DEFAULT NULL,
  `telephone` bigint(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `isMember` tinyint(1) DEFAULT NULL,
  `managedBy` int(11) DEFAULT NULL,
  `belongsTo` int(11) NOT NULL,
  `genderID` tinyint(1) DEFAULT NULL,
  `experienceLevel` int(11) NOT NULL,
  PRIMARY KEY (`uID`,`experienceLevel`),
  KEY `fk_client_experienceLevel1_idx` (`experienceLevel`),
  CONSTRAINT `fk_client_experienceLevel1` FOREIGN KEY (`experienceLevel`) REFERENCES `experiencelevel` (`levelID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'\'Atanas \'','\'Pamukchiev\'','\'burt.jules@tintired.info\'',6920000869,8,0,0,10,1,9),(2,'\'Jorge \'','\'Strong\'','\'johnathon.silas.frederic@hope.edu\'',9925952894,15,0,0,15,61,1),(3,'\'Trisha \'','\'Childress\'','\'lucia.marta@money.me\'',3752410969,14,1,0,5,1,1),(4,'\'Mohamed \'','\'Sims\'','\'sheree.carly@putquality.me\'',5079494990,15,1,0,1,1,2),(5,'\'Margo \'','\'Shafer\'','\'garry.geoffrey@field.info\'',5884869039,13,1,0,1,1,1),(6,'\'Ezekiel \'','\'Childs\'','\'deon@digestiondirection.me\'',6145256480,9,1,0,2,0,2),(7,'\'Ericka \'','\'Duke\'','\'carmelo.barney.nestor@healthyhear.org\'',1006363469,17,0,0,1,1,3),(8,'\'Vicky \'','\'Coffey\'','\'stuart.fredrick@ringriver.edu\'',2310430901,7,1,0,5,1,1),(9,'\'Catrina \'','\'Ortega\'','\'dylan.chuck@kiss.info\'',3104981171,18,1,0,36,0,5),(10,'\'Gladys \'','\'Britton\'','\'domingo.santos@healthy.me\'',7739120218,14,0,0,27,0,4),(11,'\'Krista \'','\'Gonzalez\'','\'kurt.allan.nelson@woundwriting.info\'',1889529318,7,1,0,20,0,4),(12,'\'Hector \'','\'Dixon\'','\'dee.winnie@breath.me\'',2716488017,6,1,0,12,1,5),(13,'\'Stacey \'','\'Holley\'','\'tamra.aisha.wilda@straight.me\'',6325418616,18,0,0,57,0,9),(14,'\'Arleen \'','\'Reilly\'','\'brigitte@writingwrong.edu\'',4285598932,12,0,0,34,1,2),(15,'\'Dwain \'','\'Miranda\'','\'nathaniel@wood.org\'',4387881187,16,1,0,45,1,8),(16,'\'Iola \'','\'Deleon\'','\'carmelo@soundsoup.org\'',9230718937,6,1,0,12,0,4),(17,'\'Frances \'','\'Sawyer\'','\'patti@first.com\'',9387288723,6,0,0,28,0,7),(18,'\'Carmine \'','\'Warren\'','\'werner.theo.geraldo@suddensugar.org\'',8392512936,18,0,0,87,0,6),(19,'\'Jeffry \'','\'Carson\'','\'sonja.lila@talltaste.org\'',5438798984,11,0,0,23,0,5),(20,'\'Lon \'','\'Huffman\'','\'felix.jimmie@position.info\'',4594176770,11,0,0,12,1,1),(21,'\'Beverley \'','\'Fischer\'','\'graciela.imogene@sandsay.info\'',7157211283,13,1,0,70,0,2),(22,'\'Perry \'','\'Jordan\'','\'johnny.earl.jimmy@sex.org\'',5662262975,8,0,0,73,1,1),(23,'\'Bret \'','\'Rutherford\'','\'lauren.cathy@false.edu\'',9149145502,14,1,0,5,1,2),(24,'\'Doug \'','\'Madden\'','\'edith.kim@touchtown.com\'',1604126505,6,0,0,71,1,3),(25,'\'Sonny \'','\'Snider\'','\'vince.quincy.eddy@cookcopper.com\'',1999479435,18,0,0,55,1,1),(26,'\'Nellie \'','\'Cash\'','\'lilia@behaviour.org\'',7602689351,10,1,0,3,1,5),(27,'\'Harriett \'','\'Shaffer\'','\'claudia.jackie.marcia@still.org\'',2416224815,15,0,0,1,1,4),(28,'\'Brendon \'','\'Calderon\'','\'scotty@thumbthunder.com\'',4184470083,13,1,0,80,0,4),(29,'\'Clement \'','\'Saunders\'','\'morton.jonas.forest@flatflight.edu\'',7222260385,12,1,0,56,0,5),(30,'\'Elias \'','\'Monroe\'','\'rosalinda@answerant.org\'',9409612404,11,0,0,9,0,9),(31,'\'Walter \'','\'Moses\'','\'ross.virgil.andy@expansion.me\'',8120476356,9,0,0,9,1,2),(32,'\'Megan \'','\'Hutchinson\'','\'teri.cristina@jewel.org\'',1168307510,17,0,0,15,1,8),(33,'\'Renee \'','\'Sparks\'','\'dick@while.org\'',1117403540,12,0,0,29,0,4),(34,'\'Carl \'','\'Anderson\'','\'frederick@have.com\'',6398894956,16,0,0,16,0,7),(35,'\'Marcelino \'','\'Hastings\'','\'thanh.dillon.amado@measuremeat.org\'',6976600147,12,0,0,87,0,6),(36,'\'Lily \'','\'Merrill\'','\'shelley@damagedanger.org\'',9856862707,6,0,0,28,0,5),(37,'\'Issac \'','\'Krause\'','\'susie.olivia@againstagreement.edu\'',5171824782,17,0,0,24,1,1),(38,'\'Viola \'','\'Morales\'','\'hilario.bud.sal@certain.org\'',9801608083,17,1,0,31,1,2),(39,'\'Lamont \'','\'Cabrera\'','\'rex@sneezesnow.edu\'',3069091271,7,0,0,71,0,1),(40,'\'Eddie \'','\'Fitzpatrick\'','\'joni@goldgood.me\'',9282517683,12,0,0,36,1,2),(41,'\'Katherine \'','\'Salinas\'','\'kira@personphysical.com\'',6356430271,10,0,0,45,0,3),(42,'\'Pamala \'','\'Farmer\'','\'adrian.rhea.marquita@army.org\'',6216708005,8,1,0,83,0,1),(43,'\'Theron \'','\'Benjamin\'','\'denny.davis@view.org\'',2242769060,8,0,0,1,1,5),(44,'\'Max \'','\'Farley\'','\'carly.james@night.me\'',4648468923,8,1,0,73,1,4),(45,'\'Hubert \'','\'Moss\'','\'deshawn@burstbusiness.com\'',7086014328,9,1,0,95,0,4),(46,'\'Jeanie \'','\'Foley\'','\'cole.denny@family.edu\'',5327048547,9,0,0,31,1,5),(47,'\'Zachary \'','\'Hartley\'','\'quinton@dropdry.edu\'',3743587228,11,1,0,12,1,9),(48,'\'Karyn \'','\'Donahue\'','\'raleigh@hanging.me\'',8672779193,9,0,0,1,0,2),(49,'\'Shonda \'','\'Sykes\'','\'issac.mary.dudley@interest.me\'',6975984086,10,0,0,93,1,8),(50,'\'Charles \'','\'Kaufman\'','\'renato.jc.hoyt@curve.com\'',7758441835,9,0,0,52,0,4),(51,'\'Rudolph \'','\'Finch\'','\'wm@leatherleft.info\'',5633261376,7,1,0,68,1,7),(52,'\'Art \'','\'Bradshaw\'','\'ashley@illimportant.me\'',4365898032,7,1,0,91,1,6),(53,'\'Michele \'','\'Kelly\'','\'concetta.bertie.alba@hope.edu\'',3053853477,13,0,0,21,0,5),(54,'\'Trevor \'','\'Rouse\'','\'lillian@face.me\'',7178817845,12,1,0,16,0,1),(55,'\'Kitty \'','\'Gilliam\'','\'carey@animal.me\'',2005893944,12,0,0,71,1,2),(56,'\'Rigoberto \'','\'Lindsey\'','\'lily@level.edu\'',4995285932,12,1,0,93,0,1),(57,'\'Riley \'','\'Burke\'','\'paula.diana@shamesharp.org\'',9930400306,16,1,0,39,0,2),(58,'\'Arturo \'','\'Benson\'','\'virgilio.mary@wind.org\'',5832038579,6,0,0,47,0,3),(59,'\'Fred \'','\'Webber\'','\'august.leonardo.jasper@burstbusiness.com\'',7314332354,6,1,0,45,1,1),(60,'\'Nona \'','\'Shelton\'','\'anthony.kevin.jason@existence.edu\'',7621731512,10,0,0,43,0,5),(61,'\'Randi \'','\'Francis\'','\'tonya@laugh.info\'',1691334125,17,1,0,85,0,4),(62,'\'Alisha \'','\'Hale\'','\'calvin.alex@cruel.edu\'',2762980394,6,0,0,19,1,4),(63,'\'Maura \'','\'Flynn\'','\'jaclyn.gracie.sondra@otherout.info\'',8839543135,11,1,0,53,0,5),(64,'\'Earlene \'','\'Madden\'','\'geraldine@kindkiss.info\'',2991345161,16,0,0,55,0,9),(65,'\'Beverly \'','\'Sykes\'','\'marilynn.lucretia.karrie@threadthroat.com\'',4502323924,7,1,0,86,1,2),(66,'\'Alphonse \'','\'Gibson\'','\'elisabeth@knife.info\'',1470853413,11,1,0,35,1,8),(67,'\'Mina \'','\'Levy\'','\'larissa@hollow.org\'',9561845063,17,1,0,100,0,4),(68,'\'Kenny \'','\'Fitzgerald\'','\'nora.margie@bulb.org\'',1755427936,10,0,0,53,1,7),(69,'\'Frankie \'','\'King\'','\'elise@start.info\'',2937260970,9,1,0,59,1,6),(70,'\'Danielle \'','\'Boyle\'','\'therese.frankie.dena@stopstore.org\'',7248466717,14,0,0,52,0,5),(71,'\'Cyrus \'','\'Aguirre\'','\'warren@branch.info\'',7922146103,18,1,0,78,0,1),(72,'\'Susie \'','\'Cochran\'','\'maynard@disgust.info\'',1619520853,9,0,0,75,1,2),(73,'\'Tanya \'','\'Sparks\'','\'amalia.savannah.anastasia@punishment.com\'',7327599609,7,0,0,67,1,1),(74,'\'Rosalee \'','\'Starr\'','\'joni@propertyprose.edu\'',7980738516,6,0,0,84,0,2),(75,'\'Claud \'','\'Ibarra\'','\'lauren@circle.org\'',4563594324,12,0,0,46,0,3),(76,'\'Julio \'','\'Ford\'','\'kristopher@jelly.org\'',9194111341,15,0,0,3,1,1),(77,'\'Mervin \'','\'Potter\'','\'samatha.oralia@canvascard.org\'',5934337532,13,1,0,44,1,5),(78,'\'Marcelino \'','\'Singleton\'','\'jodi@purposepush.me\'',1315529629,15,0,0,85,1,4),(79,'\'Demetria \'','\'Jackson\'','\'normand.kieth@tradetrain.edu\'',3092212329,14,0,0,48,1,4),(80,'\'Alec \'','\'Mendez\'','\'juliana.aline@farm.me\'',4942235249,7,0,0,79,0,5),(81,'\'Cecelia \'','\'Braun\'','\'reina.lauretta.kylie@backbad.org\'',9411636031,15,0,0,66,1,9),(82,'\'Tana \'','\'Gill\'','\'ezequiel.erasmo@left.com\'',1335300112,10,0,0,36,1,2),(83,'\'Randall \'','\'Dailey\'','\'mindy@country.me\'',3468966458,18,0,0,58,1,8),(84,'\'Cesar \'','\'Neely\'','\'allison.tamara.joy@earearly.edu\'',4312076039,17,0,0,42,0,4),(85,'\'Donnell \'','\'Puckett\'','\'jimmie.everett@brushbucket.info\'',6456069612,13,1,0,100,0,7),(86,'\'Francis \'','\'Bland\'','\'tad@scissorsscrew.edu\'',7979036497,7,1,0,68,0,6),(87,'\'Josh \'','\'Barker\'','\'archie@leftleg.org\'',6706864194,10,1,0,22,0,5),(88,'\'Clarice \'','\'Bowers\'','\'alonzo.elias@enoughequal.com\'',6199000765,13,0,0,72,1,1),(89,'\'Owen \'','\'Kline\'','\'janna.juliette.deena@militarymilk.org\'',4120087460,13,1,0,93,1,2),(90,'\'Catrina \'','\'Olsen\'','\'inez.lynda@windowwine.me\'',8911067040,8,0,0,48,1,1),(91,'\'Solomon \'','\'Henry\'','\'ben.chester.cecil@warwarm.com\'',9670109418,13,1,0,37,0,2),(92,'\'Jack \'','\'Porter\'','\'heriberto.donnell.cole@tonguetooth.edu\'',3264255196,12,1,0,82,0,3),(93,'\'Vicky \'','\'Case\'','\'joanne.eleanor.valerie@painpaint.org\'',1388632536,15,0,0,10,0,1),(94,'\'Ron \'','\'Pacheco\'','\'mona@distance.com\'',9025616952,17,1,0,84,1,5),(95,'\'Briana \'','\'Williamson\'','\'latisha.barbra@come.info\'',5700218162,7,0,0,18,1,4),(96,'\'Lauri \'','\'Carson\'','\'shannon.sheila.ethel@wellwest.me\'',8745632775,18,0,0,87,1,4),(97,'\'Ronald \'','\'Logan\'','\'lyndon@futuregarden.me\'',2878355270,9,1,0,76,0,5),(98,'\'Loretta \'','\'Molina\'','\'chloe@mark.edu\'',8684603623,16,0,0,43,0,9),(99,'\'Loyd \'','\'Dennis\'','\'ebony@penpencil.edu\'',2404013488,7,1,0,23,1,2),(100,'\'Agatha \'','\'Smith\'','\'minh@old.edu\'',7479587950,18,0,0,92,0,8);
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
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
INSERT INTO `experiencelevel` VALUES (0,'Mega noob'),(1,'Noob'),(2,'Novice'),(3,'Amateur'),(4,'Semi-Pro'),(5,'Pro-Wannaby'),(6,'Pro-Wannaby'),(7,'Expert'),(8,'Grand SlamWinner'),(9,'Godlike'),(10,'Almost at my level ');
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
INSERT INTO `extras` VALUES (1,'Pizza',10,NULL,23),(2,'Candy',20,NULL,34),(3,'Drinks',15,NULL,36),(4,'Raquets',25,NULL,41),(5,'Transport',30,NULL,28),(6,'Stuff',5,NULL,11);
/*!40000 ALTER TABLE `extras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicalcondition`
--

DROP TABLE IF EXISTS `medicalcondition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medicalcondition` (
  `ownerID` int(11) NOT NULL,
  `condition` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ownerID`),
  KEY `fk_medicalCondition_client1_idx` (`ownerID`),
  CONSTRAINT `fk_medicalCondition_client1` FOREIGN KEY (`ownerID`) REFERENCES `client` (`uID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicalcondition`
--

LOCK TABLES `medicalcondition` WRITE;
/*!40000 ALTER TABLE `medicalcondition` DISABLE KEYS */;
INSERT INTO `medicalcondition` VALUES (1,'Too Musch SWAG'),(2,'In da Thug Life'),(3,'Broken Leg'),(4,'Headache'),(5,'Seriously Ill'),(6,'Broken Arm');
/*!40000 ALTER TABLE `medicalcondition` ENABLE KEYS */;
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
INSERT INTO `notes` VALUES (1,'It was really Rainy',23,1),(2,'Atanas was the Best!',25,1),(3,'A UFO Crashed near the Venue',26,1),(4,'Day 1 of alien abduction: its dark',27,1),(6,NULL,29,0);
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
  `userToPay` int(11) NOT NULL,
  `paymentType` int(11) NOT NULL,
  `amount` int(11) DEFAULT NULL,
  `label` varchar(45) DEFAULT NULL,
  `hasPayed` tinyint(1) DEFAULT NULL,
  `dueDate` date DEFAULT NULL,
  `payedDate` date DEFAULT NULL,
  PRIMARY KEY (`paymentID`,`userToPay`),
  KEY `fk_Payment_paymentType1_idx` (`paymentType`),
  KEY `fk_payment_client1_idx` (`userToPay`),
  CONSTRAINT `fk_Payment_paymentType1` FOREIGN KEY (`paymentType`) REFERENCES `paymenttype` (`typeID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_payment_client1` FOREIGN KEY (`userToPay`) REFERENCES `client` (`uID`) ON DELETE NO ACTION ON UPDATE NO ACTION
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
INSERT INTO `session` VALUES (1,'1,5','2014-12-15 08:00:00','2014-12-15 09:30:00',1,10,'13-25','1','0'),(2,'1,5','2014-12-15 10:00:00','2014-12-15 11:30:00',1,10,'13-25',NULL,'0'),(3,'1,5','2014-12-15 12:00:00','2014-12-15 13:30:00',1,10,'13-25',NULL,'0'),(4,'1,5','2014-12-15 15:00:00','2014-12-15 16:30:00',2,10,'13-25',NULL,'0'),(5,'1,5','2014-12-15 17:00:00','2014-12-15 18:30:00',2,10,'13-25',NULL,'0'),(6,'1','2014-12-15 19:00:00','2014-12-15 20:00:00',2,10,'13-25',NULL,'0'),(7,'1,5','2014-12-16 08:00:00','2014-12-16 09:30:00',3,10,'13-25',NULL,'0'),(8,'1,5','2014-12-16 10:00:00','2014-12-16 11:30:00',3,10,'13-25',NULL,'0'),(9,'1,5','2014-12-16 12:00:00','2014-12-16 13:30:00',3,10,'13-25',NULL,'0'),(10,'1,5','2014-12-16 15:00:00','2014-12-16 16:30:00',4,10,'13-25',NULL,'0'),(11,'1,5','2014-12-16 17:00:00','2014-12-16 18:30:00',4,10,'13-25',NULL,'0'),(12,'1','2014-12-16 19:00:00','2014-12-16 20:00:00',4,10,'13-25',NULL,'0'),(13,'1,5','2014-12-17 08:00:00','2014-12-17 09:30:00',5,10,'13-25',NULL,'0'),(14,'1,5','2014-12-17 10:00:00','2014-12-17 11:30:00',5,10,'13-25',NULL,'0'),(15,'1,5','2014-12-17 12:00:00','2014-12-17 13:30:00',5,10,'13-25',NULL,'0'),(16,'1,5','2014-12-17 15:00:00','2014-12-17 16:30:00',6,10,'13-25',NULL,'0'),(17,'1,5','2014-12-17 17:00:00','2014-12-17 18:30:00',6,10,'13-25',NULL,'0'),(18,'1','2014-12-17 19:00:00','2014-12-17 20:00:00',6,10,'13-25',NULL,'0'),(19,'1,5','2014-12-18 08:00:00','2014-12-18 09:30:00',7,10,'13-25',NULL,'0'),(20,'1,5','2014-12-18 10:00:00','2014-12-18 11:30:00',7,10,'13-25',NULL,'0'),(21,'1,5','2014-12-18 12:00:00','2014-12-18 13:30:00',7,10,'13-25',NULL,'0'),(22,'1,5','2014-12-18 15:00:00','2014-12-18 16:30:00',8,10,'13-25',NULL,'0'),(23,'1,5','2014-12-18 17:00:00','2014-12-18 18:30:00',8,10,'13-25',NULL,'0'),(24,'1','2014-12-18 19:00:00','2014-12-18 20:00:00',8,10,'13-25',NULL,'0'),(25,'1,5','2014-12-19 08:00:00','2014-12-19 09:30:00',9,10,'13-25',NULL,'0'),(26,'1,5','2014-12-19 10:00:00','2014-12-19 11:30:00',9,10,'13-25',NULL,'0'),(27,'1,5','2014-12-19 12:00:00','2014-12-19 13:30:00',9,10,'13-25',NULL,'0'),(28,'1,5','2014-12-19 15:00:00','2014-12-19 16:30:00',10,10,'13-25',NULL,'0'),(29,'1,5','2014-12-19 17:00:00','2014-12-19 18:30:00',10,10,'13-25',NULL,'0'),(30,'1','2014-12-19 19:00:00','2014-12-19 20:00:00',10,10,'13-25',NULL,'0'),(31,'1,5','2014-12-15 08:00:00','2014-12-15 09:30:00',1,10,'08-25',NULL,'0'),(32,'1,5','2014-12-15 10:00:00','2014-12-15 11:30:00',1,10,'08-25',NULL,'0'),(33,'1,5','2014-12-15 12:00:00','2014-12-15 13:30:00',1,10,'08-25',NULL,'0'),(34,'1,5','2014-12-15 15:00:00','2014-12-15 16:30:00',2,10,'08-25',NULL,'0'),(35,'1,5','2014-12-15 17:00:00','2014-12-15 18:30:00',2,10,'08-25',NULL,'0'),(36,'1','2014-12-15 19:00:00','2014-12-15 20:00:00',2,10,'08-35',NULL,'0'),(37,'1,5','2015-01-26 08:00:00','2015-01-26 09:30:00',41,10,'13-25',NULL,'0'),(38,'1,5','2015-01-26 10:00:00','2015-01-26 11:30:00',41,10,'13-25',NULL,'0'),(39,'1,5','2015-01-26 12:00:00','2015-01-26 13:30:00',41,10,'13-25',NULL,'0'),(40,'1,5','2015-01-26 15:00:00','2015-01-26 16:30:00',42,10,'13-25',NULL,'0'),(41,'1,5','2015-01-26 17:00:00','2015-01-26 18:30:00',42,10,'13-25',NULL,'0'),(42,'1','2015-01-26 19:00:00','2015-01-26 20:00:00',42,10,'13-25',NULL,'0'),(43,'1,5','2015-01-27 08:00:00','2015-01-27 09:30:00',43,10,'13-25',NULL,'0'),(44,'1,5','2015-01-27 10:00:00','2015-01-27 11:30:00',43,10,'13-25',NULL,'0'),(45,'1,5','2015-01-27 12:00:00','2015-01-27 13:30:00',43,10,'13-25',NULL,'0'),(46,'1,5','2015-01-27 15:00:00','2015-01-27 16:30:00',44,10,'13-25',NULL,'0'),(47,'1,5','2015-01-27 17:00:00','2015-01-27 18:30:00',44,10,'13-25',NULL,'0'),(48,'1','2015-01-27 19:00:00','2015-01-27 20:00:00',44,10,'13-25',NULL,'0'),(49,'1,5','2015-01-28 08:00:00','2015-01-28 09:30:00',45,10,'13-25',NULL,'0'),(50,'1,5','2015-01-28 10:00:00','2015-01-28 11:30:00',45,10,'13-25',NULL,'0'),(51,'1,5','2015-01-28 12:00:00','2015-01-28 13:30:00',45,10,'13-25',NULL,'0'),(52,'1,5','2015-01-28 15:00:00','2015-01-28 16:30:00',46,10,'13-25',NULL,'0'),(53,'1,5','2015-01-28 17:00:00','2015-01-28 18:30:00',46,10,'13-25',NULL,'0'),(54,'1','2015-01-28 19:00:00','2015-01-28 20:00:00',46,10,'13-25',NULL,'0'),(55,'1,5','2015-01-28 08:00:00','2015-01-28 09:30:00',45,10,'13-25',NULL,'0'),(56,'1,5','2015-01-28 10:00:00','2015-01-28 11:30:00',45,10,'13-25',NULL,'0'),(57,'1,5','2015-01-28 12:00:00','2015-01-28 13:30:00',45,10,'13-25',NULL,'0'),(58,'1,5','2015-01-28 15:00:00','2015-01-28 16:30:00',46,10,'13-25',NULL,'0'),(59,'1,5','2015-01-28 17:00:00','2015-01-28 18:30:00',46,10,'13-25',NULL,'0'),(60,'1','2015-01-28 19:00:00','2015-01-28 20:00:00',46,10,'13-25',NULL,'0'),(61,'1,5','2015-01-29 08:00:00','2015-01-29 09:30:00',47,10,'13-25',NULL,'0'),(62,'1,5','2015-01-29 10:00:00','2015-01-29 11:30:00',47,10,'13-25',NULL,'0'),(63,'1,5','2015-01-29 12:00:00','2015-01-29 13:30:00',47,10,'13-25',NULL,'0'),(64,'1,5','2015-01-29 15:00:00','2015-01-29 16:30:00',48,10,'13-25',NULL,'0'),(65,'1,5','2015-01-29 17:00:00','2015-01-29 18:30:00',48,10,'13-25',NULL,'0'),(66,'1','2015-01-29 19:00:00','2015-01-29 20:00:00',48,10,'13-25',NULL,'0'),(67,'1,5','2015-01-30 08:00:00','2015-01-30 09:30:00',47,10,'13-25',NULL,'0'),(68,'1,5','2015-01-30 10:00:00','2015-01-30 11:30:00',47,10,'13-25',NULL,'0'),(69,'1,5','2015-01-30 12:00:00','2015-01-30 13:30:00',47,10,'13-25',NULL,'0'),(70,'1,5','2015-01-30 15:00:00','2015-01-30 16:30:00',48,10,'13-25',NULL,'0'),(71,'1,5','2015-01-30 17:00:00','2015-01-30 18:30:00',48,10,'13-25',NULL,'0'),(72,'1','2015-01-30 19:00:00','2015-01-30 20:00:00',48,10,'13-25',NULL,'0'),(73,'1,5','2015-01-31 08:00:00','2015-01-31 09:30:00',49,10,'13-25',NULL,'0'),(74,'1,5','2015-01-31 10:00:00','2015-01-31 11:30:00',49,10,'13-25',NULL,'0'),(75,'1,5','2015-01-31 12:00:00','2015-01-31 13:30:00',49,10,'13-25',NULL,'0'),(76,'1,5','2015-01-31 15:00:00','2015-01-31 16:30:00',50,10,'13-25',NULL,'0'),(77,'1,5','2015-01-31 17:00:00','2015-01-31 18:30:00',50,10,'13-25',NULL,'0'),(78,'1','2015-01-31 19:00:00','2015-01-31 20:00:00',50,10,'13-25',NULL,'0');
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
INSERT INTO `subvenue` VALUES (1,'\'Court1\'','\'10\'',1),(2,'\'Court2\'','\'10\'',1),(3,'\'Court3\'','\'10\'',1),(4,'\'Court4\'','\'10\'',1),(5,'\'Court5\'','\'10\'',1),(6,'\'Court6\'','\'10\'',1),(7,'\'Court7\'','\'10\'',1),(8,'\'Court8\'','\'10\'',1);
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
INSERT INTO `subvenue_usedfor_session` VALUES (37,1,1),(38,1,1),(39,1,1),(40,2,1),(41,2,1),(42,1,1),(43,1,1),(44,1,1),(45,3,1),(46,1,1),(47,1,1),(48,1,1),(49,2,1),(50,2,1),(51,1,1),(52,1,1),(53,1,1),(54,1,1),(55,3,1),(56,1,1),(57,4,1),(58,2,1),(59,1,1),(60,1,1),(61,3,1),(62,1,1),(63,1,1),(64,1,1),(65,1,1),(66,1,1),(67,1,1),(68,1,1),(69,1,1),(70,1,1),(71,1,1),(72,1,1),(73,1,1),(74,1,1),(75,1,1),(76,1,1),(77,1,1);
/*!40000 ALTER TABLE `subvenue_usedfor_session` ENABLE KEYS */;
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
  `status` char(1) DEFAULT NULL,
  PRIMARY KEY (`User_uID`,`Session_sessionID`),
  KEY `fk_User_has_Session_Session1_idx` (`Session_sessionID`),
  KEY `fk_User_has_Session_User1_idx` (`User_uID`),
  CONSTRAINT `fk_User_has_Session_Session1` FOREIGN KEY (`Session_sessionID`) REFERENCES `session` (`sessionID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_Session_User1` FOREIGN KEY (`User_uID`) REFERENCES `client` (`uID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_selects_session`
--

LOCK TABLES `user_selects_session` WRITE;
/*!40000 ALTER TABLE `user_selects_session` DISABLE KEYS */;
INSERT INTO `user_selects_session` VALUES (3,37,'P'),(3,40,'P'),(3,43,'P'),(3,46,'P'),(3,49,'P'),(3,52,'P'),(3,55,'P'),(3,58,'P'),(3,61,'P'),(4,37,'C'),(4,38,'C');
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
  CONSTRAINT `fk_Venue_User1` FOREIGN KEY (`Manager`) REFERENCES `client` (`uID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venue`
--

LOCK TABLES `venue` WRITE;
/*!40000 ALTER TABLE `venue` DISABLE KEYS */;
INSERT INTO `venue` VALUES (1,100,'West End Venue',30,1,1);
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

-- Dump completed on 2015-01-24 21:09:05
