PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "address" (
  "addressID" integer NOT NULL,
  "city" varchar(45) DEFAULT NULL,
  "country" varchar(45) DEFAULT NULL,
  "street" varchar(45) DEFAULT NULL,
  "number" integer DEFAULT NULL,
  "label" varchar(45) DEFAULT NULL
);
INSERT INTO "address" VALUES(1,'Glasgow','United Kingdom','Hyndland Rd',45,'main address');
CREATE TABLE "block" (
  "BlockID" integer NOT NULL,
  "beginDate" date NOT NULL,
  "endDate" date NOT NULL,
  "label" varchar(45) DEFAULT NULL,
  "type" varchar(45) NOT NULL
);
INSERT INTO "block" VALUES(2,'2015-03-02','2015-03-02','Monday Morning','Morning');
INSERT INTO "block" VALUES(3,'2015-03-02','2015-03-02','Monday Afternoon','Afternoon');
INSERT INTO "block" VALUES(4,'2015-03-03','2015-03-03','Tuesday Morning','Morning');
INSERT INTO "block" VALUES(5,'2015-03-03','2015-03-03','Tuesday Afternoon','Afternoon');
INSERT INTO "block" VALUES(6,'2015-03-04','2015-03-04','Wednesday Morning','Morning');
INSERT INTO "block" VALUES(7,'2015-03-04','2015-03-04','Wednesday Afternoon','Afternoon');
INSERT INTO "block" VALUES(8,'2015-03-05','2015-03-05','Thurday Morning','Morning');
INSERT INTO "block" VALUES(9,'2015-03-05','2015-03-05','Thurday Afternoon','Afternoon');
INSERT INTO "block" VALUES(10,'2015-03-06','2015-03-06','Friday Morning','Morning');
INSERT INTO "block" VALUES(11,'2015-03-06','2015-03-06','Friday Afternoon','Afternoon');
INSERT INTO "block" VALUES(13,'2015-03-09','2015-03-15','Week 2','Week');
INSERT INTO "block" VALUES(14,'2015-03-09','2015-03-09','Monday Morning','Morning');
INSERT INTO "block" VALUES(15,'2015-03-09','2015-03-09','Monday Afternoon','Afternoon');
INSERT INTO "block" VALUES(16,'2015-03-10','2015-03-10','Tuesday Morning','Morning');
INSERT INTO "block" VALUES(17,'2015-03-10','2015-03-10','Tuesday Afternoon','Afternoon');
INSERT INTO "block" VALUES(18,'2015-03-11','2015-03-11','Wednesday Morning','Morning');
INSERT INTO "block" VALUES(19,'2015-03-11','2015-03-11','Wednesday Afternoon','Afternoon');
INSERT INTO "block" VALUES(20,'2015-03-12','2015-03-12','Thurday Morning','Morning');
INSERT INTO "block" VALUES(21,'2015-03-12','2015-03-12','Thurday Afternoon','Afternoon');
INSERT INTO "block" VALUES(22,'2015-03-13','2015-03-13','Friday Morning','Morning');
INSERT INTO "block" VALUES(23,'2015-03-13','2015-03-13','Friday Afternoon','Afternoon');
CREATE TABLE "btm rank" (
  "uID" integer NOT NULL,
  "membershipNum" integer DEFAULT NULL,
  "numOfPonts" integer DEFAULT NULL,
  CONSTRAINT "uID" FOREIGN KEY ("uID") REFERENCES "client" ("uID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO "btm rank" VALUES(1,123456789,100);
INSERT INTO "btm rank" VALUES(2,132456789,20);
INSERT INTO "btm rank" VALUES(3,142356789,34);
INSERT INTO "btm rank" VALUES(4,152346789,11);
INSERT INTO "btm rank" VALUES(5,162345789,76);
INSERT INTO "btm rank" VALUES(6,172345689,55);
INSERT INTO "btm rank" VALUES(7,182345679,23);
INSERT INTO "btm rank" VALUES(8,192345678,0);
INSERT INTO "btm rank" VALUES(9,124356789,1);
INSERT INTO "btm rank" VALUES(10,125346789,-20);
CREATE TABLE "client" (
  "uID" integer NOT NULL PRIMARY KEY,         # Primary key has been added...
  "firstName" varchar(45) DEFAULT NULL,
  "lastName" varchar(45) DEFAULT NULL ,
  "email" varchar(45) DEFAULT NULL,
  "telephone" bigint(20) DEFAULT NULL,
  "dateofbirth" date NOT NULL,
  "isMember" bool DEFAULT NULL,
  "managedBy" integer DEFAULT NULL,
  "belongsTo" integer NOT NULL,
  "genderID" integer DEFAULT NULL,
  "experienceLevel" integer NOT NULL,
  CONSTRAINT "fk_client_experienceLevel1" FOREIGN KEY ("experienceLevel") REFERENCES "experiencelevel" ("levelID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO "client" VALUES(1,'Atanas ','Pamukchiev','sfors123@gmail.com',6920000869,'1993-10-09',0,0,1,1,9);
INSERT INTO "client" VALUES(2,'Jorge ','Strong','johnathon.silas.frederic@hope.edu',9925952894,'1997-03-15',0,0,1,61,1);
INSERT INTO "client" VALUES(3,'Trisha','Childress','lucia.marta@money.me',3752410969,'1997-03-15',1,0,1,1,1);
INSERT INTO "client" VALUES(4,'Mohamed ','Sims','sheree.carly@putquality.me',5079494990,'1997-03-15',1,0,1,1,2);
INSERT INTO "client" VALUES(5,'Margo ','Shafer','garry.geoffrey@field.info',5884869039,'1997-03-15',1,0,1,1,1);
INSERT INTO "client" VALUES(6,'Ezekiel ','Childs','deon@digestiondirection.me',6145256480,'1997-03-15',1,0,2,0,2);
INSERT INTO "client" VALUES(7,'Ericka ','Duke','carmelo.barney.nestor@healthyhear.org',1006363469,'1997-03-15',0,0,1,1,3);
INSERT INTO "client" VALUES(8,'Vicky ','Coffey','stuart.fredrick@ringriver.edu',2310430901,'1997-03-15',1,0,5,0,1);
INSERT INTO "client" VALUES(9,'Catrina ','Ortega','dylan.chuck@kiss.info',3104981171,'1997-03-15',1,0,5,0,5);
INSERT INTO "client" VALUES(10,'Gladys ','Britton','domingo.santos@healthy.me',7739120218,'1997-03-15',0,0,5,0,4);
INSERT INTO "client" VALUES(11,'Krista ','Gonzalez','kurt.allan.nelson@woundwriting.info',1889529318,'1997-03-15',1,0,5,0,4);
INSERT INTO "client" VALUES(12,'Hector ','Dixon','dee.winnie@breath.me',2716488017,'1997-03-15',1,0,5,1,5);
INSERT INTO "client" VALUES(13,'Stacey ','Holley','tamra.aisha.wilda@straight.me',6325418616,'1997-03-15',0,0,5,0,9);
INSERT INTO "client" VALUES(14,'Arleen ','Reilly','brigitte@writingwrong.edu',4285598932,'1997-03-15',0,0,5,1,2);
INSERT INTO "client" VALUES(15,'Dwain ','Miranda','nathaniel@wood.org',4387881187,'1997-03-15',1,0,4,1,8);
INSERT INTO "client" VALUES(16,'Iola ','Deleon','carmelo@soundsoup.org',9230718937,'1997-03-15',1,0,4,0,4);
INSERT INTO "client" VALUES(17,'Frances ','Sawyer','patti@first.com',9387288723,'1997-03-15',0,0,3,0,7);
INSERT INTO "client" VALUES(18,'Carmine ','Warren','werner.theo.geraldo@suddensugar.org',8392512936,'1997-03-15',0,0,2,0,6);
INSERT INTO "client" VALUES(19,'Jeffry ','Carson','sonja.lila@talltaste.org',5438798984,'1997-03-15',0,0,2,0,5);
INSERT INTO "client" VALUES(20,'Lon ','Huffman','felix.jimmie@position.info',4594176770,'1997-03-15',0,0,3,1,1);
INSERT INTO "client" VALUES(21,'Beverley ','Fischer','graciela.imogene@sandsay.info',7157211283,'1997-03-15',1,0,4,0,2);
INSERT INTO "client" VALUES(22,'Perry ','Jordan','johnny.earl.jimmy@sex.org',5662262975,'1997-03-15',0,0,5,1,1);
INSERT INTO "client" VALUES(23,'Bret ','Rutherford','lauren.cathy@false.edu',9149145502,'1997-03-15',1,0,5,0,2);
INSERT INTO "client" VALUES(24,'Doug ','Madden','edith.kim@touchtown.com',1604126505,'1997-03-15',0,0,5,1,3);
INSERT INTO "client" VALUES(25,'Sonny ','Snider','vince.quincy.eddy@cookcopper.com',1999479435,'1997-03-15',0,0,2,1,1);
INSERT INTO "client" VALUES(26,'Nellie ','Cash','lilia@behaviour.org',7602689351,'1997-03-15',1,0,1,1,5);
INSERT INTO "client" VALUES(27,'Harriett ','Shaffer','claudia.jackie.marcia@still.org',2416224815,'1997-03-15',0,0,1,1,4);
INSERT INTO "client" VALUES(28,'Brendon ','Calderon','scotty@thumbthunder.com',4184470083,'1994-03-15',1,0,4,0,4);
INSERT INTO "client" VALUES(29,'Clement ','Saunders','morton.jonas.forest@flatflight.edu',7222260385,'1994-03-15',1,0,5,0,5);
INSERT INTO "client" VALUES(30,'Elias ','Monroe','rosalinda@answerant.org',9409612404,'1994-03-15',0,0,2,0,9);
INSERT INTO "client" VALUES(31,'Walter ','Moses','ross.virgil.andy@expansion.me',8120476356,'1994-03-15',0,0,4,1,2);
INSERT INTO "client" VALUES(32,'Megan ','Hutchinson','teri.cristina@jewel.org',1168307510,'1994-03-15',0,0,2,1,8);
INSERT INTO "client" VALUES(33,'Renee ','Sparks','dick@while.org',1117403540,'1994-03-15',0,0,3,0,4);
INSERT INTO "client" VALUES(34,'Carl ','Anderson','frederick@have.com',6398894956,'1994-03-15',0,0,3,0,7);
INSERT INTO "client" VALUES(35,'Marcelino ','Hastings','thanh.dillon.amado@measuremeat.org',6976600147,'1994-03-15',0,0,3,0,6);
INSERT INTO "client" VALUES(36,'Lily ','Merrill','shelley@damagedanger.org',9856862707,'1994-03-15',0,0,3,0,5);
INSERT INTO "client" VALUES(37,'Issac ','Krause','susie.olivia@againstagreement.edu',5171824782,'1994-03-15',0,0,1,1,1);
INSERT INTO "client" VALUES(38,'Viola ','Morales','hilario.bud.sal@certain.org',9801608083,'1994-03-15',1,0,1,1,2);
INSERT INTO "client" VALUES(39,'Lamont ','Cabrera','rex@sneezesnow.edu',3069091271,'1994-03-15',0,0,5,0,1);
INSERT INTO "client" VALUES(40,'Eddie ','Fitzpatrick','joni@goldgood.me',9282517683,'1994-03-15',0,0,5,1,2);
INSERT INTO "client" VALUES(41,'Katherine ','Salinas','kira@personphysical.com',6356430271,'1994-03-15',0,0,5,0,3);
INSERT INTO "client" VALUES(42,'Pamala ','Farmer','adrian.rhea.marquita@army.org',6216708005,'1994-03-15',1,0,5,0,1);
INSERT INTO "client" VALUES(43,'Theron ','Benjamin','denny.davis@view.org',2242769060,'1994-03-15',0,0,5,1,5);
INSERT INTO "client" VALUES(44,'Max ','Farley','carly.james@night.me',4648468923,'1994-03-15',1,0,3,1,4);
INSERT INTO "client" VALUES(45,'Hubert ','Moss','deshawn@burstbusiness.com',7086014328,'1994-03-15',1,0,3,0,4);
INSERT INTO "client" VALUES(46,'Jeanie ','Foley','cole.denny@family.edu',5327048547,'1994-03-15',0,0,2,1,5);
INSERT INTO "client" VALUES(47,'Zachary ','Hartley','quinton@dropdry.edu',3743587228,'1994-03-15',1,0,3,1,9);
INSERT INTO "client" VALUES(48,'Karyn ','Donahue','raleigh@hanging.me',8672779193,'1994-03-15',0,0,4,0,2);
INSERT INTO "client" VALUES(49,'Shonda ','Sykes','issac.mary.dudley@interest.me',6975984086,'1994-03-15',0,0,2,1,8);
INSERT INTO "client" VALUES(50,'Charles ','Kaufman','renato.jc.hoyt@curve.com',7758441835,'1994-03-15',0,0,3,0,4);
INSERT INTO "client" VALUES(51,'Rudolph ','Finch','wm@leatherleft.info',5633261376,'1994-03-15',1,0,4,1,7);
INSERT INTO "client" VALUES(52,'Art ','Bradshaw','ashley@illimportant.me',4365898032,'1994-03-15',1,0,2,1,6);
INSERT INTO "client" VALUES(53,'Michele ','Kelly','concetta.bertie.alba@hope.edu',3053853477,'1994-03-15',0,0,3,0,5);
INSERT INTO "client" VALUES(54,'Trevor ','Rouse','lillian@face.me',7178817845,'1994-03-15',1,0,4,0,1);
INSERT INTO "client" VALUES(55,'Kitty ','Gilliam','carey@animal.me',2005893944,'1994-03-15',0,0,5,1,2);
INSERT INTO "client" VALUES(56,'Rigoberto ','Lindsey','lily@level.edu',4995285932,'1994-03-15',1,0,5,0,1);
INSERT INTO "client" VALUES(57,'Riley ','Burke','paula.diana@shamesharp.org',9930400306,'1994-03-15',1,0,5,0,2);
INSERT INTO "client" VALUES(58,'Arturo ','Benson','virgilio.mary@wind.org',5832038579,'1994-03-15',0,0,5,0,3);
INSERT INTO "client" VALUES(59,'Fred ','Webber','august.leonardo.jasper@burstbusiness.com',7314332354,'1994-03-15',1,0,5,1,1);
INSERT INTO "client" VALUES(60,'Nona ','Shelton','anthony.kevin.jason@existence.edu',7621731512,'1994-03-15',0,0,3,0,5);
INSERT INTO "client" VALUES(61,'Randi ','Francis','tonya@laugh.info',1691334125,'1994-03-15',1,0,3,0,4);
INSERT INTO "client" VALUES(62,'Alisha ','Hale','calvin.alex@cruel.edu',2762980394,'1994-03-15',0,0,2,1,4);
INSERT INTO "client" VALUES(63,'Maura ','Flynn','jaclyn.gracie.sondra@otherout.info',8839543135,'1994-03-15',1,0,1,0,5);
INSERT INTO "client" VALUES(64,'Earlene ','Madden','geraldine@kindkiss.info',2991345161,'1994-03-15',0,0,3,0,9);
INSERT INTO "client" VALUES(65,'Beverly ','Sykes','marilynn.lucretia.karrie@threadthroat.com',4502323924,'1994-03-15',1,0,2,1,2);
INSERT INTO "client" VALUES(66,'Alphonse ','Gibson','elisabeth@knife.info',1470853413,'1994-03-15',1,0,1,1,8);
INSERT INTO "client" VALUES(67,'Mina ','Levy','larissa@hollow.org',9561845063,'1994-03-15',1,0,1,0,4);
INSERT INTO "client" VALUES(68,'Kenny ','Fitzgerald','nora.margie@bulb.org',1755427936,'1994-03-15',0,0,1,1,7);
INSERT INTO "client" VALUES(69,'Frankie ','King','elise@start.info',2937260970,'1994-03-15',1,0,1,1,6);
INSERT INTO "client" VALUES(70,'Danielle ','Boyle','therese.frankie.dena@stopstore.org',7248466717,'1994-03-15',0,0,1,0,5);
INSERT INTO "client" VALUES(71,'Cyrus ','Aguirre','warren@branch.info',7922146103,'1994-03-15',1,0,1,0,1);
INSERT INTO "client" VALUES(72,'Susie ','Cochran','maynard@disgust.info',1619520853,'1994-03-15',0,0,1,1,2);
INSERT INTO "client" VALUES(73,'Tanya ','Sparks','amalia.savannah.anastasia@punishment.com',7327599609,'1994-03-15',0,0,1,1,1);
INSERT INTO "client" VALUES(74,'Rosalee ','Starr','joni@propertyprose.edu',7980738516,'1994-03-15',0,0,1,0,2);
INSERT INTO "client" VALUES(75,'Claud ','Ibarra','lauren@circle.org',4563594324,'1994-03-15',0,0,1,0,3);
INSERT INTO "client" VALUES(76,'Julio ','Ford','kristopher@jelly.org',9194111341,'1994-03-15',0,0,3,1,1);
INSERT INTO "client" VALUES(77,'Mervin ','Potter','samatha.oralia@canvascard.org',5934337532,'1994-03-15',1,0,2,1,5);
INSERT INTO "client" VALUES(78,'Marcelino ','Singleton','jodi@purposepush.me',1315529629,'1994-03-15',0,0,3,1,4);
INSERT INTO "client" VALUES(79,'Demetria ','Jackson','normand.kieth@tradetrain.edu',3092212329,'1994-03-15',0,0,4,1,4);
INSERT INTO "client" VALUES(80,'Alec ','Mendez','juliana.aline@farm.me',4942235249,'1994-03-15',0,0,5,0,5);
INSERT INTO "client" VALUES(81,'Cecelia ','Braun','reina.lauretta.kylie@backbad.org',9411636031,'1994-03-15',0,0,5,1,9);
INSERT INTO "client" VALUES(82,'Tana ','Gill','ezequiel.erasmo@left.com',1335300112,'1994-03-15',0,0,5,1,2);
INSERT INTO "client" VALUES(83,'Randall ','Dailey','mindy@country.me',3468966458,'1994-03-15',0,0,5,1,8);
INSERT INTO "client" VALUES(84,'Cesar ','Neely','allison.tamara.joy@earearly.edu',4312076039,'1994-03-15',0,0,5,0,4);
INSERT INTO "client" VALUES(85,'Donnell ','Puckett','jimmie.everett@brushbucket.info',6456069612,'1994-03-15',1,0,4,0,7);
INSERT INTO "client" VALUES(86,'Francis ','Bland','tad@scissorsscrew.edu',7979036497,'1994-03-15',1,0,3,0,6);
INSERT INTO "client" VALUES(87,'Josh ','Barker','archie@leftleg.org',6706864194,'1994-03-15',1,0,3,0,5);
INSERT INTO "client" VALUES(88,'Clarice ','Bowers','alonzo.elias@enoughequal.com',6199000765,'1994-03-15',0,0,3,1,1);
INSERT INTO "client" VALUES(89,'Owen ','Kline','janna.juliette.deena@militarymilk.org',4120087460,'1994-03-15',1,0,3,1,2);
INSERT INTO "client" VALUES(90,'Catrina ','Olsen','inez.lynda@windowwine.me',8911067040,'1994-03-15',0,0,3,1,1);
INSERT INTO "client" VALUES(91,'Solomon ','Henry','ben.chester.cecil@warwarm.com',9670109418,'1994-03-15',1,0,2,0,2);
INSERT INTO "client" VALUES(92,'Jack ','Porter','heriberto.donnell.cole@tonguetooth.edu',3264255196,'1994-03-15',1,0,2,0,3);
INSERT INTO "client" VALUES(93,'Vicky ','Case','joanne.eleanor.valerie@painpaint.org',1388632536,'1994-03-15',0,0,2,0,1);
INSERT INTO "client" VALUES(94,'Ron ','Pacheco','mona@distance.com',9025616952,'1994-03-15',1,0,1,1,5);
INSERT INTO "client" VALUES(95,'Briana ','Williamson','latisha.barbra@come.info',5700218162,'1994-03-15',0,0,4,1,4);
INSERT INTO "client" VALUES(96,'Lauri ','Carson','shannon.sheila.ethel@wellwest.me',8745632775,'1994-03-15',0,0,5,1,4);
INSERT INTO "client" VALUES(97,'Kiril','Ivanov','kivanov@google.com',98263217643,'1996-08-09',0,NULL,8,0,0);
CREATE TABLE "experiencelevel" (
  "levelID" integer NOT NULL,
  "label" varchar(45) DEFAULT NULL
);
INSERT INTO "experiencelevel" VALUES(0,'Mega noob');
INSERT INTO "experiencelevel" VALUES(1,'Noob');
INSERT INTO "experiencelevel" VALUES(2,'Novice');
INSERT INTO "experiencelevel" VALUES(3,'Amateur');
INSERT INTO "experiencelevel" VALUES(4,'Semi-Pro');
INSERT INTO "experiencelevel" VALUES(5,'Pro-Wannaby');
INSERT INTO "experiencelevel" VALUES(6,'Pro-Wannaby');
INSERT INTO "experiencelevel" VALUES(7,'Expert');
INSERT INTO "experiencelevel" VALUES(8,'Grand SlamWinner');
INSERT INTO "experiencelevel" VALUES(9,'Godlike');
INSERT INTO "experiencelevel" VALUES(10,'Almost at my level ');
CREATE TABLE "extras" (
  "extrasID" integer NOT NULL,
  "label" varchar(45) DEFAULT NULL,
  "price" integer DEFAULT NULL,
  "description" varchar(45) DEFAULT NULL,
  "ownerSessionID" integer NOT NULL,
  CONSTRAINT "fk_Extras_Session1" FOREIGN KEY ("ownerSessionID") REFERENCES "session" ("sessionID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO "extras" VALUES(1,'Pizza',10,NULL,23);
INSERT INTO "extras" VALUES(2,'Candy',20,NULL,34);
INSERT INTO "extras" VALUES(3,'Drinks',15,NULL,36);
INSERT INTO "extras" VALUES(4,'Raquets',25,NULL,41);
INSERT INTO "extras" VALUES(5,'Transport',30,NULL,28);
INSERT INTO "extras" VALUES(6,'Stuff',5,NULL,11);
CREATE TABLE "medicalcondition" (
  "ownerID" integer NOT NULL,
  "condition" varchar(45) DEFAULT NULL,
  CONSTRAINT "fk_medicalCondition_client1" FOREIGN KEY ("ownerID") REFERENCES "client" ("uID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO "medicalcondition" VALUES(1,'Too Musch SWAG');
INSERT INTO "medicalcondition" VALUES(2,'In da Thug Life');
INSERT INTO "medicalcondition" VALUES(3,'Broken Leg');
INSERT INTO "medicalcondition" VALUES(4,'Headache');
INSERT INTO "medicalcondition" VALUES(5,'Seriously Ill');
INSERT INTO "medicalcondition" VALUES(6,'Broken Arm');
INSERT INTO "medicalcondition" VALUES(97,'');
CREATE TABLE "notes" (
  "noteID" integer NOT NULL,
  "Note" mediumtext,
  "Session_sessionID" integer NOT NULL,
  "hasNotes" bool DEFAULT NULL,
  CONSTRAINT "fk_Notes_Session1" FOREIGN KEY ("Session_sessionID") REFERENCES "session" ("sessionID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO "notes" VALUES(1,'It was really Rainy',23,1);
INSERT INTO "notes" VALUES(2,'Atanas was the Best!',25,1);
INSERT INTO "notes" VALUES(3,'A UFO Crashed near the Venue',26,1);
INSERT INTO "notes" VALUES(4,'Day 1 of alien abduction: its dark',27,1);
INSERT INTO "notes" VALUES(6,NULL,29,0);
CREATE TABLE "payment" (
  "paymentID" integer NOT NULL,
  "userToPay" integer NOT NULL,
  "paymentType" integer NOT NULL,
  "amount" integer DEFAULT NULL,
  "label" varchar(45) DEFAULT NULL,
  "hasPayed" bool DEFAULT NULL,
  "dueDate" date DEFAULT NULL,
  "payedDate" date DEFAULT NULL,
  CONSTRAINT "fk_Payment_paymentType1" FOREIGN KEY ("paymentType") REFERENCES "paymenttype" ("typeID") ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT "fk_payment_client1" FOREIGN KEY ("userToPay") REFERENCES "client" ("uID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO "payment" VALUES(1,26,1,100,'Sessions: 1, 2, 3, ',0,'2015-01-30',NULL);
INSERT INTO "payment" VALUES(2,30,2,25,'Sessions: 1, ',0,'2015-01-27',NULL);
INSERT INTO "payment" VALUES(3,23,1,250,'Sessions: 2, 4, 5, 833683368336',0,'2015-04-01',NULL);
INSERT INTO "payment" VALUES(4,3,1,25,'Sessions: 1, ',0,'2015-3-25',NULL);
CREATE TABLE "paymenttype" (
  "typeID" integer NOT NULL,
  "typeLabel" varchar(45) DEFAULT NULL
);
INSERT INTO "paymenttype" VALUES(1,'Cash');
INSERT INTO "paymenttype" VALUES(2,'PayPal');
INSERT INTO "paymenttype" VALUES(3,'None');
CREATE TABLE "session_coachedby" (
    "id" integer NOT NULL PRIMARY KEY,
    "session_id" integer NOT NULL REFERENCES "session" ("sessionID"),
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    UNIQUE ("session_id", "user_id")
);
INSERT INTO "session_coachedby" VALUES(1,83,4);
INSERT INTO "session_coachedby" VALUES(3,82,5);
INSERT INTO "session_coachedby" VALUES(5,23,4);
INSERT INTO "session_coachedby" VALUES(6,45,4);
INSERT INTO "session_coachedby" VALUES(7,46,4);
INSERT INTO "session_coachedby" VALUES(8,47,4);
INSERT INTO "session_coachedby" VALUES(9,48,5);
INSERT INTO "session_coachedby" VALUES(10,53,5);
INSERT INTO "session_coachedby" VALUES(11,23,5);
INSERT INTO "session_coachedby" VALUES(12,21,5);
INSERT INTO "session_coachedby" VALUES(13,33,4);
INSERT INTO "session_coachedby" VALUES(14,31,4);
INSERT INTO "session_coachedby" VALUES(15,96,4);
INSERT INTO "session_coachedby" VALUES(16,100,4);
INSERT INTO "session_coachedby" VALUES(17,104,4);
INSERT INTO "session_coachedby" VALUES(18,27,4);
INSERT INTO "session_coachedby" VALUES(19,35,5);
INSERT INTO "session_coachedby" VALUES(20,55,5);
INSERT INTO "session_coachedby" VALUES(21,24,4);
INSERT INTO "session_coachedby" VALUES(22,49,4);
INSERT INTO "session_coachedby" VALUES(23,34,4);
INSERT INTO "session_coachedby" VALUES(24,143,4);
INSERT INTO "session_coachedby" VALUES(25,144,5);
INSERT INTO "session_coachedby" VALUES(26,145,5);
INSERT INTO "session_coachedby" VALUES(27,146,5);
INSERT INTO "session_coachedby" VALUES(28,147,5);
INSERT INTO "session_coachedby" VALUES(29,148,4);
INSERT INTO "session_coachedby" VALUES(30,149,4);
INSERT INTO "session_coachedby" VALUES(31,150,4);
INSERT INTO "session_coachedby" VALUES(32,151,4);
INSERT INTO "session_coachedby" VALUES(33,152,5);
INSERT INTO "session_coachedby" VALUES(34,153,5);
INSERT INTO "session_coachedby" VALUES(35,154,5);
INSERT INTO "session_coachedby" VALUES(36,155,5);
INSERT INTO "session_coachedby" VALUES(37,156,4);
INSERT INTO "session_coachedby" VALUES(38,157,4);
INSERT INTO "session_coachedby" VALUES(39,158,4);
INSERT INTO "session_coachedby" VALUES(40,159,4);
INSERT INTO "session_coachedby" VALUES(41,160,5);
INSERT INTO "session_coachedby" VALUES(42,161,5);
INSERT INTO "session_coachedby" VALUES(43,162,5);
INSERT INTO "session_coachedby" VALUES(44,163,5);
INSERT INTO "session_coachedby" VALUES(46,125,4);
INSERT INTO "session_coachedby" VALUES(47,126,4);
INSERT INTO "session_coachedby" VALUES(48,127,4);
INSERT INTO "session_coachedby" VALUES(49,128,4);
INSERT INTO "session_coachedby" VALUES(50,129,5);
INSERT INTO "session_coachedby" VALUES(51,130,5);
INSERT INTO "session_coachedby" VALUES(52,131,5);
INSERT INTO "session_coachedby" VALUES(53,132,5);
INSERT INTO "session_coachedby" VALUES(54,133,4);
INSERT INTO "session_coachedby" VALUES(55,134,4);
INSERT INTO "session_coachedby" VALUES(56,135,4);
INSERT INTO "session_coachedby" VALUES(57,136,4);
INSERT INTO "session_coachedby" VALUES(58,137,5);
INSERT INTO "session_coachedby" VALUES(59,138,5);
INSERT INTO "session_coachedby" VALUES(60,139,5);
INSERT INTO "session_coachedby" VALUES(61,140,5);
INSERT INTO "session_coachedby" VALUES(62,141,4);
INSERT INTO "session_coachedby" VALUES(63,142,4);
INSERT INTO "session_coachedby" VALUES(64,144,4);
INSERT INTO "session_coachedby" VALUES(65,148,5);
INSERT INTO "session_coachedby" VALUES(66,152,4);
INSERT INTO "session_coachedby" VALUES(67,156,5);
INSERT INTO "session_coachedby" VALUES(68,160,4);
INSERT INTO "session_coachedby" VALUES(69,164,5);
CREATE TABLE "subvenue" (
  "subVenueID" integer NOT NULL,
  "label" varchar(45) DEFAULT NULL,
  "capacity" varchar(45) DEFAULT NULL,
  "ownerVenue" integer NOT NULL,
  CONSTRAINT "fk_SubVenue_Venue1" FOREIGN KEY ("ownerVenue") REFERENCES "venue" ("venueID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO "subvenue" VALUES(1,'Court1','10',1);
INSERT INTO "subvenue" VALUES(2,'Court2','10',1);
INSERT INTO "subvenue" VALUES(3,'Court3','10',1);
INSERT INTO "subvenue" VALUES(4,'Court4','10',1);
INSERT INTO "subvenue" VALUES(5,'Court5','10',1);
INSERT INTO "subvenue" VALUES(6,'Court6','10',1);
CREATE TABLE "subvenue_usedfor_session" (
  "Session_sessionID" integer NOT NULL,
  "SubVenue_subVenueID" integer NOT NULL,
  "SubVenue_ownerVenue" integer NOT NULL,
  CONSTRAINT "fk_Session_has_SubVenue_Session1" FOREIGN KEY ("Session_sessionID") REFERENCES "session" ("sessionID") ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT "fk_Session_has_SubVenue_SubVenue1" FOREIGN KEY ("SubVenue_subVenueID", "SubVenue_ownerVenue") REFERENCES "subvenue" ("subVenueID", "ownerVenue") ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE "venue" (
  "venueID" integer NOT NULL,
  "capacity" integer DEFAULT NULL,
  "name" varchar(45) DEFAULT NULL,
  "load" integer DEFAULT NULL,
  "Manager" integer NOT NULL,
  "Address_addressID" integer NOT NULL,
  CONSTRAINT "fk_Venue_Address1" FOREIGN KEY ("Address_addressID") REFERENCES "address" ("addressID") ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT "fk_Venue_User1" FOREIGN KEY ("Manager") REFERENCES "client" ("uID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO "venue" VALUES(1,100,'West End Venue',0,5,1);
CREATE TABLE "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" varchar(100) NOT NULL,
    UNIQUE ("content_type_id", "codename")
);
INSERT INTO "auth_permission" VALUES(1,'Can add permission',1,'add_permission');
INSERT INTO "auth_permission" VALUES(2,'Can change permission',1,'change_permission');
INSERT INTO "auth_permission" VALUES(3,'Can delete permission',1,'delete_permission');
INSERT INTO "auth_permission" VALUES(4,'Can add group',2,'add_group');
INSERT INTO "auth_permission" VALUES(5,'Can change group',2,'change_group');
INSERT INTO "auth_permission" VALUES(6,'Can delete group',2,'delete_group');
INSERT INTO "auth_permission" VALUES(7,'Can add user',3,'add_user');
INSERT INTO "auth_permission" VALUES(8,'Can change user',3,'change_user');
INSERT INTO "auth_permission" VALUES(9,'Can delete user',3,'delete_user');
INSERT INTO "auth_permission" VALUES(10,'Can add content type',4,'add_contenttype');
INSERT INTO "auth_permission" VALUES(11,'Can change content type',4,'change_contenttype');
INSERT INTO "auth_permission" VALUES(12,'Can delete content type',4,'delete_contenttype');
INSERT INTO "auth_permission" VALUES(13,'Can add session',5,'add_session');
INSERT INTO "auth_permission" VALUES(14,'Can change session',5,'change_session');
INSERT INTO "auth_permission" VALUES(15,'Can delete session',5,'delete_session');
INSERT INTO "auth_permission" VALUES(16,'Can add site',6,'add_site');
INSERT INTO "auth_permission" VALUES(17,'Can change site',6,'change_site');
INSERT INTO "auth_permission" VALUES(18,'Can delete site',6,'delete_site');
INSERT INTO "auth_permission" VALUES(19,'Can add address',7,'add_address');
INSERT INTO "auth_permission" VALUES(20,'Can change address',7,'change_address');
INSERT INTO "auth_permission" VALUES(21,'Can delete address',7,'delete_address');
INSERT INTO "auth_permission" VALUES(22,'Can add block',8,'add_block');
INSERT INTO "auth_permission" VALUES(23,'Can change block',8,'change_block');
INSERT INTO "auth_permission" VALUES(24,'Can delete block',8,'delete_block');
INSERT INTO "auth_permission" VALUES(25,'Can add btm rank',9,'add_btmrank');
INSERT INTO "auth_permission" VALUES(26,'Can change btm rank',9,'change_btmrank');
INSERT INTO "auth_permission" VALUES(27,'Can delete btm rank',9,'delete_btmrank');
INSERT INTO "auth_permission" VALUES(28,'Can add client',10,'add_client');
INSERT INTO "auth_permission" VALUES(29,'Can change client',10,'change_client');
INSERT INTO "auth_permission" VALUES(30,'Can delete client',10,'delete_client');
INSERT INTO "auth_permission" VALUES(31,'Can add experiencelevel',11,'add_experiencelevel');
INSERT INTO "auth_permission" VALUES(32,'Can change experiencelevel',11,'change_experiencelevel');
INSERT INTO "auth_permission" VALUES(33,'Can delete experiencelevel',11,'delete_experiencelevel');
INSERT INTO "auth_permission" VALUES(34,'Can add extras',12,'add_extras');
INSERT INTO "auth_permission" VALUES(35,'Can change extras',12,'change_extras');
INSERT INTO "auth_permission" VALUES(36,'Can delete extras',12,'delete_extras');
INSERT INTO "auth_permission" VALUES(37,'Can add medicalcondition',13,'add_medicalcondition');
INSERT INTO "auth_permission" VALUES(38,'Can change medicalcondition',13,'change_medicalcondition');
INSERT INTO "auth_permission" VALUES(39,'Can delete medicalcondition',13,'delete_medicalcondition');
INSERT INTO "auth_permission" VALUES(40,'Can add notes',14,'add_notes');
INSERT INTO "auth_permission" VALUES(41,'Can change notes',14,'change_notes');
INSERT INTO "auth_permission" VALUES(42,'Can delete notes',14,'delete_notes');
INSERT INTO "auth_permission" VALUES(43,'Can add payment',15,'add_payment');
INSERT INTO "auth_permission" VALUES(44,'Can change payment',15,'change_payment');
INSERT INTO "auth_permission" VALUES(45,'Can delete payment',15,'delete_payment');
INSERT INTO "auth_permission" VALUES(46,'Can add paymenttype',16,'add_paymenttype');
INSERT INTO "auth_permission" VALUES(47,'Can change paymenttype',16,'change_paymenttype');
INSERT INTO "auth_permission" VALUES(48,'Can delete paymenttype',16,'delete_paymenttype');
INSERT INTO "auth_permission" VALUES(49,'Can add session',17,'add_session');
INSERT INTO "auth_permission" VALUES(50,'Can change session',17,'change_session');
INSERT INTO "auth_permission" VALUES(51,'Can delete session',17,'delete_session');
INSERT INTO "auth_permission" VALUES(52,'Can add subvenue',18,'add_subvenue');
INSERT INTO "auth_permission" VALUES(53,'Can change subvenue',18,'change_subvenue');
INSERT INTO "auth_permission" VALUES(54,'Can delete subvenue',18,'delete_subvenue');
INSERT INTO "auth_permission" VALUES(55,'Can add subvenue usedfor session',19,'add_subvenueusedforsession');
INSERT INTO "auth_permission" VALUES(56,'Can change subvenue usedfor session',19,'change_subvenueusedforsession');
INSERT INTO "auth_permission" VALUES(57,'Can delete subvenue usedfor session',19,'delete_subvenueusedforsession');
INSERT INTO "auth_permission" VALUES(58,'Can add user selects session',20,'add_userselectssession');
INSERT INTO "auth_permission" VALUES(59,'Can change user selects session',20,'change_userselectssession');
INSERT INTO "auth_permission" VALUES(60,'Can delete user selects session',20,'delete_userselectssession');
INSERT INTO "auth_permission" VALUES(61,'Can add venue',21,'add_venue');
INSERT INTO "auth_permission" VALUES(62,'Can change venue',21,'change_venue');
INSERT INTO "auth_permission" VALUES(63,'Can delete venue',21,'delete_venue');
INSERT INTO "auth_permission" VALUES(64,'Can add log entry',22,'add_logentry');
INSERT INTO "auth_permission" VALUES(65,'Can change log entry',22,'change_logentry');
INSERT INTO "auth_permission" VALUES(66,'Can delete log entry',22,'delete_logentry');
INSERT INTO "auth_permission" VALUES(70,'Can add additional info',24,'add_additionalinfo');
INSERT INTO "auth_permission" VALUES(71,'Can change additional info',24,'change_additionalinfo');
INSERT INTO "auth_permission" VALUES(72,'Can delete additional info',24,'delete_additionalinfo');
INSERT INTO "auth_permission" VALUES(73,'Can add session coached by',25,'add_sessioncoachedby');
INSERT INTO "auth_permission" VALUES(74,'Can change session coached by',25,'change_sessioncoachedby');
INSERT INTO "auth_permission" VALUES(75,'Can delete session coached by',25,'delete_sessioncoachedby');
INSERT INTO "auth_permission" VALUES(76,'Can add default coaches',26,'add_defaultcoaches');
INSERT INTO "auth_permission" VALUES(77,'Can change default coaches',26,'change_defaultcoaches');
INSERT INTO "auth_permission" VALUES(78,'Can delete default coaches',26,'delete_defaultcoaches');
CREATE TABLE "auth_group_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("group_id", "permission_id")
);
INSERT INTO "auth_group_permissions" VALUES(1,1,10);
INSERT INTO "auth_group_permissions" VALUES(2,1,22);
INSERT INTO "auth_group_permissions" VALUES(3,1,23);
INSERT INTO "auth_group_permissions" VALUES(4,1,24);
INSERT INTO "auth_group_permissions" VALUES(5,1,25);
INSERT INTO "auth_group_permissions" VALUES(6,1,26);
INSERT INTO "auth_group_permissions" VALUES(7,1,27);
INSERT INTO "auth_group_permissions" VALUES(8,1,28);
INSERT INTO "auth_group_permissions" VALUES(9,1,29);
INSERT INTO "auth_group_permissions" VALUES(10,1,30);
INSERT INTO "auth_group_permissions" VALUES(11,1,31);
INSERT INTO "auth_group_permissions" VALUES(12,1,32);
INSERT INTO "auth_group_permissions" VALUES(13,1,33);
INSERT INTO "auth_group_permissions" VALUES(14,1,34);
INSERT INTO "auth_group_permissions" VALUES(15,1,35);
INSERT INTO "auth_group_permissions" VALUES(16,1,36);
INSERT INTO "auth_group_permissions" VALUES(17,1,37);
INSERT INTO "auth_group_permissions" VALUES(18,1,38);
INSERT INTO "auth_group_permissions" VALUES(19,1,39);
INSERT INTO "auth_group_permissions" VALUES(20,1,40);
INSERT INTO "auth_group_permissions" VALUES(21,1,41);
INSERT INTO "auth_group_permissions" VALUES(22,1,42);
INSERT INTO "auth_group_permissions" VALUES(23,1,43);
INSERT INTO "auth_group_permissions" VALUES(24,1,44);
INSERT INTO "auth_group_permissions" VALUES(25,1,45);
INSERT INTO "auth_group_permissions" VALUES(26,1,46);
INSERT INTO "auth_group_permissions" VALUES(27,1,47);
INSERT INTO "auth_group_permissions" VALUES(28,1,48);
INSERT INTO "auth_group_permissions" VALUES(29,1,49);
INSERT INTO "auth_group_permissions" VALUES(30,1,50);
INSERT INTO "auth_group_permissions" VALUES(31,1,51);
CREATE TABLE "auth_group" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
);
INSERT INTO "auth_group" VALUES(1,'Manager');
INSERT INTO "auth_group" VALUES(2,'Parent');
INSERT INTO "auth_group" VALUES(3,'Coach');
CREATE TABLE "auth_user_groups" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id"),
    UNIQUE ("user_id", "group_id")
);
INSERT INTO "auth_user_groups" VALUES(3,4,3);
INSERT INTO "auth_user_groups" VALUES(4,3,2);
INSERT INTO "auth_user_groups" VALUES(5,5,1);
INSERT INTO "auth_user_groups" VALUES(6,5,2);
INSERT INTO "auth_user_groups" VALUES(7,5,3);
INSERT INTO "auth_user_groups" VALUES(8,8,2);
INSERT INTO "auth_user_groups" VALUES(10,7,1);
INSERT INTO "auth_user_groups" VALUES(11,9,3);
CREATE TABLE "auth_user_user_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("user_id", "permission_id")
);
CREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "password" varchar(128) NOT NULL,
    "last_login" datetime NOT NULL,
    "is_superuser" bool NOT NULL,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "date_joined" datetime NOT NULL
);
INSERT INTO "auth_user" VALUES(1,'pbkdf2_sha256$10000$I08MVZGZXcbK$SH99yKVcEyUQtq8kpqN+Qzy75S9t6b6RiLhYOQQ8pVI=','2015-01-25 01:11:26.424717',1,'atanaspam','','','sfors123@gmail.com',1,1,'2015-01-24 22:32:36.032633');
INSERT INTO "auth_user" VALUES(2,'pbkdf2_sha256$12000$Vs1tQHke2l8r$PvLEyP49BA+JTNYhKGQakYjwDFwt4/HFWlsDvrpdJdI=','2015-01-27 16:43:37.233680',1,'dimitris','Dimitris','Kiker','dimitris.kiker@teamk.com',1,1,'2015-01-25 01:14:31');
INSERT INTO "auth_user" VALUES(3,'pbkdf2_sha256$12000$LEd3NVboCvJe$anYYTZKgKvQsPwx5OdbRBpHH00ygmp4EySU4l8s9+/g=','2015-02-28 23:33:56.443350',1,'zoe','Zoe','Gerolemou','zoe.gerolemou@teamk.com',1,1,'2015-01-25 01:15:25');
INSERT INTO "auth_user" VALUES(4,'pbkdf2_sha256$12000$4qxRcVaxlgb3$9mqnXEN5RI46gXPqsbwydkOi0lIM2WHKV5h/eiESnXk=','2015-03-10 01:57:52.958100',1,'pedro','Pedro','Quintas','pedro.quintas@teamk.com',1,1,'2015-01-25 01:16:04');
INSERT INTO "auth_user" VALUES(5,'pbkdf2_sha256$12000$uTnYqdApT7Jn$Pu+u5GYp7cdxBia3v6yzc09NN4wKu9kx5NImF4Yt7j4=','2015-03-10 02:34:27.745708',1,'karl','Karl','Drouven','karl.drouven@google.com',1,1,'2015-01-25 01:16:56');
INSERT INTO "auth_user" VALUES(6,'pbkdf2_sha256$10000$Fec9MI6rCP2C$QG9Om/kV1uPRR1L4xyilx2F02D5dXISpgvnxkeX/aQE=','2015-01-25 01:17:45.036092',0,'ross','','','ross.imlach@teamk.com',0,1,'2015-01-25 01:17:45.036118');
INSERT INTO "auth_user" VALUES(7,'pbkdf2_sha256$10000$xeuMlUUawXEj$biTz0tQgnipHdfynYBS0k7VTaaV6/6eiD4vXrI2ck+c=','2015-05-31 00:00:34.665128',1,'atanas','Atanas','Pamukchiev','atanas.pamukchiev@teamk.com',1,1,'2015-01-25 01:18:05');
INSERT INTO "auth_user" VALUES(8,'pbkdf2_sha256$10000$pyB0TyOO0haz$U6ELvDm6P4UQd0dpj857Zj347MoLYvN7dpaCNcQsqVk=','2015-03-10 01:50:46.223756',0,'atanasP','Atanas','Pamukchiev','atanasP@team-k.com',0,1,'2015-03-10 01:50:26.318373');
INSERT INTO "auth_user" VALUES(9,'pbkdf2_sha256$10000$Js5g8hmHub24$r4vqDRoyLQ79Ys6GswCcokEXZMe2U7n8Lnm+INV+v20=','2015-03-10 02:34:05',0,'manager','manager','manager','manager@team-k-project.com',0,1,'2015-03-10 02:34:05');
CREATE TABLE "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL,
    UNIQUE ("app_label", "model")
);
INSERT INTO "django_content_type" VALUES(1,'permission','auth','permission');
INSERT INTO "django_content_type" VALUES(2,'group','auth','group');
INSERT INTO "django_content_type" VALUES(3,'user','auth','user');
INSERT INTO "django_content_type" VALUES(4,'content type','contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(5,'session','sessions','session');
INSERT INTO "django_content_type" VALUES(6,'site','sites','site');
INSERT INTO "django_content_type" VALUES(7,'address','bookingsystem','address');
INSERT INTO "django_content_type" VALUES(8,'block','bookingsystem','block');
INSERT INTO "django_content_type" VALUES(9,'btm rank','bookingsystem','btmrank');
INSERT INTO "django_content_type" VALUES(10,'client','bookingsystem','client');
INSERT INTO "django_content_type" VALUES(11,'experiencelevel','bookingsystem','experiencelevel');
INSERT INTO "django_content_type" VALUES(12,'extras','bookingsystem','extras');
INSERT INTO "django_content_type" VALUES(13,'medicalcondition','bookingsystem','medicalcondition');
INSERT INTO "django_content_type" VALUES(14,'notes','bookingsystem','notes');
INSERT INTO "django_content_type" VALUES(15,'payment','bookingsystem','payment');
INSERT INTO "django_content_type" VALUES(16,'paymenttype','bookingsystem','paymenttype');
INSERT INTO "django_content_type" VALUES(17,'session','bookingsystem','session');
INSERT INTO "django_content_type" VALUES(18,'subvenue','bookingsystem','subvenue');
INSERT INTO "django_content_type" VALUES(19,'subvenue usedfor session','bookingsystem','subvenueusedforsession');
INSERT INTO "django_content_type" VALUES(20,'user selects session','bookingsystem','userselectssession');
INSERT INTO "django_content_type" VALUES(21,'venue','bookingsystem','venue');
INSERT INTO "django_content_type" VALUES(22,'log entry','admin','logentry');
INSERT INTO "django_content_type" VALUES(24,'additional info','bookingsystem','additionalinfo');
INSERT INTO "django_content_type" VALUES(25,'session coached by','bookingsystem','sessioncoachedby');
INSERT INTO "django_content_type" VALUES(26,'default coaches','bookingsystem','defaultcoaches');
CREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
);
INSERT INTO "django_session" VALUES('fs5vrv8n7rxvp4s5ldpuwx3s9cngrm92','YzE5MTBiMjAwZDE1M2YzMTI4Yzk3MDQ3MzMyZTUxNDI5NzBlZDlmZDp7Il9hdXRoX3VzZXJfaWQiOjcsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-02-08 18:09:05.811094');
INSERT INTO "django_session" VALUES('sb5h41brofk5k89qulfvuq6n4pen6k3i','NjIyMGJiOWYzNzEzNTJlMmI0NDA1YjIzODU2MTk2M2NhMDNmMzRjYTp7fQ==','2015-02-08 19:26:00.257647');
INSERT INTO "django_session" VALUES('n68biy7l34zbgfy78t5uciwjngb4vun5','NjIyMGJiOWYzNzEzNTJlMmI0NDA1YjIzODU2MTk2M2NhMDNmMzRjYTp7fQ==','2015-02-08 23:49:16.516000');
INSERT INTO "django_session" VALUES('beekah3m5ulkwu19caq77pv2kn414kik','NWNlMDQ1MjVkZmMxNmUxNTA3MTJmZGUwODhmMmMxNWZmZTQ3Zjg4NDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6N30=','2015-02-09 01:22:45.742000');
INSERT INTO "django_session" VALUES('xf6yfn2v2tchszdydzlnajfbp65a2f1m','OTE5Mzk4MzI4YThkOTgyNWU4YzQwODdkYjNkY2RhNTk2OTYwYjJkNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2015-02-09 03:35:52.625065');
INSERT INTO "django_session" VALUES('tqfszo7kmc2a6f4bmtuk85or7x87vgdg','NWNlMDQ1MjVkZmMxNmUxNTA3MTJmZGUwODhmMmMxNWZmZTQ3Zjg4NDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6N30=','2015-02-09 15:12:58.807000');
INSERT INTO "django_session" VALUES('tmhk8hf23d5qr820eecyjshxdhnje55h','NWNlMDQ1MjVkZmMxNmUxNTA3MTJmZGUwODhmMmMxNWZmZTQ3Zjg4NDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6N30=','2015-02-09 15:13:00.748000');
INSERT INTO "django_session" VALUES('odzle9phjbfw7ryz8j7hpqsebamlh0l9','NWNlMDQ1MjVkZmMxNmUxNTA3MTJmZGUwODhmMmMxNWZmZTQ3Zjg4NDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6N30=','2015-02-09 15:49:44.623000');
INSERT INTO "django_session" VALUES('3ek2zep2qma4osupuzyq634rpf7qpep1','NjIyMGJiOWYzNzEzNTJlMmI0NDA1YjIzODU2MTk2M2NhMDNmMzRjYTp7fQ==','2015-02-10 15:45:41.028269');
INSERT INTO "django_session" VALUES('stnjwvityhmcfm7ozojg97mqtgr1aurs','NTlkNTE0YmY1OGFiOGZmZTFkYjFhMDM2YmFlMGYxNWY2MDM2OTZiOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImIzNTIyNmM3MzExZTA1YWVlZjJmN2YwZDE1ZjczMGVjOGExNzNiYzEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjR9','2015-02-10 16:53:10.741213');
INSERT INTO "django_session" VALUES('n0krjnc5oac6qrwqu9n591rkl5g2z85f','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-02-10 20:40:01.301942');
INSERT INTO "django_session" VALUES('weqmd0qcgezmuiccqqr0xsjcsmgeyfgu','NjIyMGJiOWYzNzEzNTJlMmI0NDA1YjIzODU2MTk2M2NhMDNmMzRjYTp7fQ==','2015-02-10 22:00:57.632160');
INSERT INTO "django_session" VALUES('eew142rv5ygmv5fouvj6d4gdzqmd2u3c','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-02-11 13:14:16.454955');
INSERT INTO "django_session" VALUES('bqe1btwi4anyjl4ynl5grneancv10t0z','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-02-11 23:48:45.539557');
INSERT INTO "django_session" VALUES('3g3os77jcifhc05vlmozt9prf8io6w0q','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-02-12 11:49:07.840440');
INSERT INTO "django_session" VALUES('sovcmchinwplufpu8iqmzqbsgpot80ra','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-02-12 13:23:35.456284');
INSERT INTO "django_session" VALUES('b2gxuyjv5w7cs9yzo8i5fuocmhlg4jim','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-02-12 13:24:33.699569');
INSERT INTO "django_session" VALUES('08z2fgho91oy11obkm9dpuc7lkm0whck','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-02-12 14:18:29.095374');
INSERT INTO "django_session" VALUES('1omkxnqwqg2rad7e7cnblrg4hteabk3f','NWNlMDQ1MjVkZmMxNmUxNTA3MTJmZGUwODhmMmMxNWZmZTQ3Zjg4NDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6N30=','2015-02-14 14:07:55.589000');
INSERT INTO "django_session" VALUES('ifeg73i73kozxwtvvccjwsblmodmy82a','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-02-16 00:31:40.262103');
INSERT INTO "django_session" VALUES('9rs7lfmdt7x78okm86rmjs18r8oo5p14','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-02-16 13:22:13.215183');
INSERT INTO "django_session" VALUES('ky2qus1xvro7ueez9kvmig5reyhy7m80','NWNlMDQ1MjVkZmMxNmUxNTA3MTJmZGUwODhmMmMxNWZmZTQ3Zjg4NDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6N30=','2015-02-18 00:38:18.341895');
INSERT INTO "django_session" VALUES('s6lar9y30r5awai2rnquzyx8lwzb6kwr','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-02-19 21:54:37.747000');
INSERT INTO "django_session" VALUES('cnw1h8nd4fh4p26qwj6az06lbfhn7rcl','NjIyMGJiOWYzNzEzNTJlMmI0NDA1YjIzODU2MTk2M2NhMDNmMzRjYTp7fQ==','2015-02-20 03:42:09.886495');
INSERT INTO "django_session" VALUES('4pbmbj4gunn8mnmqhmblpg8kp6mj6nh0','NjIyMGJiOWYzNzEzNTJlMmI0NDA1YjIzODU2MTk2M2NhMDNmMzRjYTp7fQ==','2015-03-04 22:58:32.536511');
INSERT INTO "django_session" VALUES('30aa6cnhu3c99a7ysh56rtomytug5yon','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-06 22:48:24.199818');
INSERT INTO "django_session" VALUES('vyjxomu6wcw9092o14bfwam8hb6xexlg','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-09 11:16:49.441714');
INSERT INTO "django_session" VALUES('ct5cxao3h18a9sqg9v3f70vcscfs3n1f','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-09 11:50:17.668350');
INSERT INTO "django_session" VALUES('v8xgvsptqs10ws5fgs6juc59nwb7y4qu','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-09 13:21:54.715047');
INSERT INTO "django_session" VALUES('rjtgdnf5pevkdc7dt9csjanu3bem1gl3','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-09 14:47:10.584723');
INSERT INTO "django_session" VALUES('x3grrjankx9aaimwrhuhfvnp68irogff','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-10 18:30:33.492842');
INSERT INTO "django_session" VALUES('pwmuaioboedinc6qwjqqpy1ipoujgplp','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-11 13:46:49.705649');
INSERT INTO "django_session" VALUES('5j270fux1il2vv4u7ca3kzujoc32q76o','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-14 22:23:19.249965');
INSERT INTO "django_session" VALUES('jld6bik7sh6ioaakte5zp3bnl5j5pcko','OTE5Mzk4MzI4YThkOTgyNWU4YzQwODdkYjNkY2RhNTk2OTYwYjJkNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2015-03-14 22:26:46.451917');
INSERT INTO "django_session" VALUES('ye0yugjq89i3eb6kwlq503icv28azi03','OTE5Mzk4MzI4YThkOTgyNWU4YzQwODdkYjNkY2RhNTk2OTYwYjJkNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2015-03-14 22:28:19.697203');
INSERT INTO "django_session" VALUES('57j00h25qymkjanmsv342nc41v3b7udi','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-14 22:38:29.428073');
INSERT INTO "django_session" VALUES('er7jgmnz0ljzr2asrgbfvh55lm64yk47','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-14 23:21:45.790022');
INSERT INTO "django_session" VALUES('lbnk93sodzmmjr9pe37t3e6v0ys204hh','OTE5Mzk4MzI4YThkOTgyNWU4YzQwODdkYjNkY2RhNTk2OTYwYjJkNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2015-03-14 23:33:56.446790');
INSERT INTO "django_session" VALUES('eq2k7ypdwc4goz3xx1a8lvboopn21ufy','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-17 15:50:40.903441');
INSERT INTO "django_session" VALUES('2km8twvfsib7fw2a33uxz6hlroxgoiin','NjIyMGJiOWYzNzEzNTJlMmI0NDA1YjIzODU2MTk2M2NhMDNmMzRjYTp7fQ==','2015-03-19 14:58:59.984458');
INSERT INTO "django_session" VALUES('zxisqypgce9g49ixiu2g0xdgb2cy7stq','NjIyMGJiOWYzNzEzNTJlMmI0NDA1YjIzODU2MTk2M2NhMDNmMzRjYTp7fQ==','2015-03-19 15:13:41.882786');
INSERT INTO "django_session" VALUES('9w84o0j13hr0avshqt4bkirtjgs9fkhe','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-19 15:28:27.094540');
INSERT INTO "django_session" VALUES('p188li2w23y2smnpfazjl3khj96wrxuw','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-21 18:24:03.272852');
INSERT INTO "django_session" VALUES('z35uoykam2cpka66lgcfcywcrjro6k5p','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-22 23:55:07.042527');
INSERT INTO "django_session" VALUES('befyaxnnb3ytf20fn75k69pqp0u4od5h','OWI4NzIyMjU5M2M2YzY5ODZjMzcyMzU2NjRjMWQ0NWY3ZWI0Yjc2NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2015-03-24 00:54:33.188387');
INSERT INTO "django_session" VALUES('r3uvf6qmewo6c8mhkp8tsht8f06dndhy','NjIyMGJiOWYzNzEzNTJlMmI0NDA1YjIzODU2MTk2M2NhMDNmMzRjYTp7fQ==','2015-03-24 01:39:22.983796');
INSERT INTO "django_session" VALUES('bcgt3thx514a33qbibxi9yv5ohh5gwo2','NjIyMGJiOWYzNzEzNTJlMmI0NDA1YjIzODU2MTk2M2NhMDNmMzRjYTp7fQ==','2015-03-24 02:12:38.900663');
INSERT INTO "django_session" VALUES('w8ppm2zn6xqceck09kcue8nrwgv3xrd7','NjIyMGJiOWYzNzEzNTJlMmI0NDA1YjIzODU2MTk2M2NhMDNmMzRjYTp7fQ==','2015-03-24 02:36:03.858080');
INSERT INTO "django_session" VALUES('5ttd5843xyilkvs5wtg7b73cm97xxrpb','NWNlMDQ1MjVkZmMxNmUxNTA3MTJmZGUwODhmMmMxNWZmZTQ3Zjg4NDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6N30=','2015-06-14 00:00:34.668801');
CREATE TABLE "django_site" (
    "id" integer NOT NULL PRIMARY KEY,
    "domain" varchar(100) NOT NULL,
    "name" varchar(50) NOT NULL
);
INSERT INTO "django_site" VALUES(1,'example.com','example.com');
CREATE TABLE "django_admin_log" (
    "id" integer NOT NULL PRIMARY KEY,
    "action_time" datetime NOT NULL,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "content_type_id" integer REFERENCES "django_content_type" ("id"),
    "object_id" text,
    "object_repr" varchar(200) NOT NULL,
    "action_flag" smallint unsigned NOT NULL,
    "change_message" text NOT NULL
);
INSERT INTO "django_admin_log" VALUES(1,'2015-01-25 01:13:53.573245',1,3,'4','asd',3,'');
INSERT INTO "django_admin_log" VALUES(2,'2015-01-25 01:14:01.365384',1,3,'2','naseto123',3,'');
INSERT INTO "django_admin_log" VALUES(3,'2015-01-25 01:14:07.284889',1,3,'3','naseto123asd',3,'');
INSERT INTO "django_admin_log" VALUES(4,'2015-01-25 01:14:31.438083',1,3,'2','dimitris',1,'');
INSERT INTO "django_admin_log" VALUES(5,'2015-01-25 01:15:17.559858',1,3,'2','dimitris',2,'Changed password, first_name, last_name, is_staff and is_superuser.');
INSERT INTO "django_admin_log" VALUES(6,'2015-01-25 01:15:25.923574',1,3,'3','zoe',1,'');
INSERT INTO "django_admin_log" VALUES(7,'2015-01-25 01:15:49.603375',1,3,'3','zoe',2,'Changed password, first_name, last_name, is_staff and is_superuser.');
INSERT INTO "django_admin_log" VALUES(8,'2015-01-25 01:16:04.703047',1,3,'4','pedro',1,'');
INSERT INTO "django_admin_log" VALUES(9,'2015-01-25 01:16:33.688749',1,3,'4','pedro',2,'Changed password, first_name, last_name, is_staff and is_superuser.');
INSERT INTO "django_admin_log" VALUES(10,'2015-01-25 01:16:56.455518',1,3,'5','karl',1,'');
INSERT INTO "django_admin_log" VALUES(11,'2015-01-25 01:17:16.538387',1,3,'5','karl',2,'Changed password, first_name, last_name, is_staff and is_superuser.');
INSERT INTO "django_admin_log" VALUES(12,'2015-01-25 01:17:45.108310',1,3,'6','ross',1,'');
INSERT INTO "django_admin_log" VALUES(13,'2015-01-25 01:18:05.137603',1,3,'7','atanas',1,'');
INSERT INTO "django_admin_log" VALUES(14,'2015-01-25 01:18:18.435739',1,3,'7','atanas',2,'Changed password, first_name, last_name, is_staff and is_superuser.');
INSERT INTO "django_admin_log" VALUES(15,'2015-01-25 01:18:40.563364',1,3,'7','atanas',2,'Changed password and last_name.');
INSERT INTO "django_admin_log" VALUES(16,'2015-01-25 15:29:29.424320',7,2,'1','Manager',1,'');
INSERT INTO "django_admin_log" VALUES(17,'2015-01-25 15:29:59.688121',7,3,'7','atanas',2,'Changed password and groups.');
INSERT INTO "django_admin_log" VALUES(18,'2015-01-25 19:24:43.287268',5,2,'2','Parent',1,'');
INSERT INTO "django_admin_log" VALUES(19,'2015-01-25 19:24:53.755817',5,2,'3','Coach',1,'');
INSERT INTO "django_admin_log" VALUES(20,'2015-01-25 19:25:04.311566',5,3,'5','karl',2,'Changed password and groups.');
INSERT INTO "django_admin_log" VALUES(21,'2015-01-25 19:25:16.761224',5,3,'4','pedro',2,'Changed password and groups.');
INSERT INTO "django_admin_log" VALUES(22,'2015-01-25 19:25:24.479834',5,3,'3','zoe',2,'Changed password and groups.');
INSERT INTO "django_admin_log" VALUES(23,'2015-01-27 20:19:42.086616',5,3,'5','karl',2,'Changed password and groups.');
INSERT INTO "django_admin_log" VALUES(24,'2015-02-05 10:30:20.195473',5,10,'101','Client object',3,'');
INSERT INTO "django_admin_log" VALUES(25,'2015-03-10 02:34:52.919122',5,3,'9','manager',2,'Changed password and groups.');
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
CREATE TABLE "btm_rank" (
    "uID" integer NOT NULL PRIMARY KEY,
    "membershipNum" integer,
    "numOfPonts" integer
);
CREATE TABLE "session" (
	`sessionID`	integer NOT NULL,
	`duration`	varchar(45) DEFAULT NULL,
	`beginTime`	datetime DEFAULT NULL,
	`endTime`	datetime DEFAULT NULL,
	`Block_BlockID`	integer NOT NULL,
	`capacity`	integer DEFAULT NULL,
	`ageGroup`	varchar(45) DEFAULT NULL,
	`skillGroup`	varchar(45) DEFAULT NULL,
	`isFull`	bool DEFAULT NULL,
	FOREIGN KEY(`Block_BlockID`) REFERENCES "block" ( "BlockID" ) ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO "session" VALUES(1,'1','2015-03-02 08:00:00','2015-03-02 09:00:00',2,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(2,'1','2015-03-02 08:00:00','2015-03-02 09:00:00',2,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(3,'1','2015-03-02 08:00:00','2015-03-02 09:00:00',2,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(4,'1','2015-03-02 08:00:00','2015-03-02 09:00:00',2,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(5,'1','2015-03-02 13:00:00','2015-03-02 14:00:00',3,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(6,'1','2015-03-02 13:00:00','2015-03-02 14:00:00',3,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(7,'1','2015-03-02 13:00:00','2015-03-02 14:00:00',3,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(8,'1','2015-03-02 13:00:00','2015-03-02 14:00:00',3,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(9,'1','2015-03-03 08:00:00','2015-03-03 09:00:00',4,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(10,'1','2015-03-03 08:00:00','2015-03-03 09:00:00',4,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(11,'1','2015-03-03 08:00:00','2015-03-03 09:00:00',4,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(12,'1','2015-03-03 08:00:00','2015-03-03 09:00:00',4,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(13,'1','2015-03-03 13:00:00','2015-03-03 14:00:00',5,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(14,'1','2015-03-03 13:00:00','2015-03-03 14:00:00',5,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(15,'1','2015-03-03 13:00:00','2015-03-03 14:00:00',5,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(16,'1','2015-03-03 13:00:00','2015-03-03 14:00:00',5,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(17,'1','2015-03-04 08:00:00','2015-03-04 09:00:00',6,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(18,'1','2015-03-04 08:00:00','2015-03-04 09:00:00',6,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(19,'1','2015-03-04 08:00:00','2015-03-04 09:00:00',6,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(20,'1','2015-03-04 08:00:00','2015-03-04 09:00:00',6,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(21,'1','2015-03-04 13:00:00','2015-03-04 14:00:00',7,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(22,'1','2015-03-04 13:00:00','2015-03-04 14:00:00',7,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(23,'1','2015-03-04 13:00:00','2015-03-04 14:00:00',7,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(24,'1','2015-03-04 13:00:00','2015-03-04 14:00:00',7,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(25,'1','2015-03-05 08:00:00','2015-03-05 09:00:00',8,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(26,'1','2015-03-05 08:00:00','2015-03-05 09:00:00',8,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(27,'1','2015-03-05 08:00:00','2015-03-05 09:00:00',8,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(28,'1','2015-03-05 08:00:00','2015-03-05 09:00:00',8,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(29,'1','2015-03-05 13:00:00','2015-03-05 14:00:00',9,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(30,'1','2015-03-05 13:00:00','2015-03-05 14:00:00',9,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(31,'1','2015-03-05 13:00:00','2015-03-05 14:00:00',9,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(32,'1','2015-03-05 13:00:00','2015-03-05 14:00:00',9,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(33,'1','2015-03-06 08:00:00','2015-03-06 09:00:00',10,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(34,'1','2015-03-06 08:00:00','2015-03-06 09:00:00',10,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(35,'1','2015-03-06 08:00:00','2015-03-06 09:00:00',10,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(36,'1','2015-03-06 08:00:00','2015-03-06 09:00:00',10,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(37,'1','2015-03-06 13:00:00','2015-03-06 14:00:00',11,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(38,'1','2015-03-06 13:00:00','2015-03-06 14:00:00',11,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(39,'1','2015-03-06 13:00:00','2015-03-06 14:00:00',11,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(40,'1','2015-03-06 13:00:00','2015-03-06 14:00:00',11,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(82,'1','2015-03-09 08:00:00','2015-03-09 09:00:00',14,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(83,'1','2015-03-09 08:00:00','2015-03-09 09:00:00',14,9,'10-12','RANDOM','False');
INSERT INTO "session" VALUES(84,'1','2015-03-09 08:00:00','2015-03-09 09:00:00',14,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(85,'1','2015-03-09 08:00:00','2015-03-09 09:00:00',14,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(86,'1','2015-03-09 13:00:00','2015-03-09 14:00:00',15,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(87,'1','2015-03-09 13:00:00','2015-03-09 14:00:00',15,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(88,'1','2015-03-09 13:00:00','2015-03-09 14:00:00',15,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(89,'1','2015-03-09 13:00:00','2015-03-09 14:00:00',15,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(90,'1','2015-03-10 08:00:00','2015-03-10 09:00:00',16,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(91,'1','2015-03-10 08:00:00','2015-03-10 09:00:00',16,9,'10-12','RANDOM','False');
INSERT INTO "session" VALUES(92,'1','2015-03-10 08:00:00','2015-03-10 09:00:00',16,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(93,'1','2015-03-10 08:00:00','2015-03-10 09:00:00',16,9,'15-21','RANDOM','False');
INSERT INTO "session" VALUES(94,'1','2015-03-10 13:00:00','2015-03-10 14:00:00',17,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(95,'1','2015-03-10 13:00:00','2015-03-10 14:00:00',17,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(96,'1','2015-03-10 13:00:00','2015-03-10 14:00:00',17,8,'12-15','RANDOM','False');
INSERT INTO "session" VALUES(97,'1','2015-03-10 13:00:00','2015-03-10 14:00:00',17,9,'15-21','RANDOM','False');
INSERT INTO "session" VALUES(98,'1','2015-03-11 08:00:00','2015-03-11 09:00:00',18,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(99,'1','2015-03-11 08:00:00','2015-03-11 09:00:00',18,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(100,'1','2015-03-11 08:00:00','2015-03-11 09:00:00',18,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(101,'1','2015-03-11 08:00:00','2015-03-11 09:00:00',18,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(102,'1','2015-03-11 13:00:00','2015-03-11 14:00:00',19,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(103,'1','2015-03-11 13:00:00','2015-03-11 14:00:00',19,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(104,'1','2015-03-11 13:00:00','2015-03-11 14:00:00',19,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(105,'1','2015-03-11 13:00:00','2015-03-11 14:00:00',19,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(106,'1','2015-03-12 08:00:00','2015-03-12 09:00:00',20,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(107,'1','2015-03-12 08:00:00','2015-03-12 09:00:00',20,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(108,'1','2015-03-12 08:00:00','2015-03-12 09:00:00',20,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(109,'1','2015-03-12 08:00:00','2015-03-12 09:00:00',20,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(110,'1','2015-03-12 13:00:00','2015-03-12 14:00:00',21,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(111,'1','2015-03-12 13:00:00','2015-03-12 14:00:00',21,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(112,'1','2015-03-12 13:00:00','2015-03-12 14:00:00',21,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(113,'1','2015-03-12 13:00:00','2015-03-12 14:00:00',21,10,'15-21','RANDOM',0);
INSERT INTO "session" VALUES(114,'1','2015-03-13 08:00:00','2015-03-13 09:00:00',22,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(115,'1','2015-03-13 08:00:00','2015-03-13 09:00:00',22,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(116,'1','2015-03-13 08:00:00','2015-03-13 09:00:00',22,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(117,'1','2015-03-13 08:00:00','2015-03-13 09:00:00',22,8,'15-21','RANDOM','False');
INSERT INTO "session" VALUES(118,'1','2015-03-13 13:00:00','2015-03-13 14:00:00',23,10,'7-10','RANDOM',0);
INSERT INTO "session" VALUES(119,'1','2015-03-13 13:00:00','2015-03-13 14:00:00',23,10,'10-12','RANDOM',0);
INSERT INTO "session" VALUES(120,'1','2015-03-13 13:00:00','2015-03-13 14:00:00',23,10,'12-15','RANDOM',0);
INSERT INTO "session" VALUES(121,'1','2015-03-13 13:00:00','2015-03-13 14:00:00',23,10,'15-21','RANDOM',0);
CREATE TABLE "user_selects_session" (
	`id`	INTEGER NOT NULL,
	`User_uID`	integer NOT NULL,
	`Session_sessionID`	integer NOT NULL,
	`status`	NUMERIC DEFAULT NULL,
	`hasattended`	bool DEFAULT 0,
	PRIMARY KEY(id),
	FOREIGN KEY(`User_uID`) REFERENCES "client" ( "uID" ) ON DELETE NO ACTION ON UPDATE NO ACTION,
	FOREIGN KEY(`Session_sessionID`) REFERENCES "session" ( "sessionID" ) ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO "user_selects_session" VALUES(3,23,83,'P',0);
INSERT INTO "user_selects_session" VALUES(7,23,36,'P',0);
INSERT INTO "user_selects_session" VALUES(8,23,117,'P',0);
INSERT INTO "user_selects_session" VALUES(9,23,96,'P',0);
INSERT INTO "user_selects_session" VALUES(10,24,96,'C',1);
INSERT INTO "user_selects_session" VALUES(22,34,104,'P',0);
INSERT INTO "user_selects_session" VALUES(23,97,93,'P',0);
INSERT INTO "user_selects_session" VALUES(24,97,97,'P',0);
CREATE TABLE "bookingsystem_additionalinfo" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"),
    "telephone" integer NOT NULL
);
INSERT INTO "bookingsystem_additionalinfo" VALUES(1,5,9867876);
INSERT INTO "bookingsystem_additionalinfo" VALUES(2,1,289313231);
INSERT INTO "bookingsystem_additionalinfo" VALUES(3,2,2438923);
INSERT INTO "bookingsystem_additionalinfo" VALUES(4,4,0);
CREATE TABLE "bookingsystem_defaultcoaches" (
    "id" integer NOT NULL PRIMARY KEY,
    "monMor_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "monAft_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "tueMor_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "tueAft_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "wedMor_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "wedAft_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "thuMor_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "thuAft_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "friMor_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "friAft_id" integer NOT NULL REFERENCES "auth_user" ("id")
);
INSERT INTO "bookingsystem_defaultcoaches" VALUES(1,4,5,4,5,4,5,4,5,4,5);
CREATE TABLE "bookingsystem_client" (
    "uID" integer NOT NULL PRIMARY KEY,
    "firstName" varchar(45) NOT NULL,
    "lastName" varchar(45) NOT NULL,
    "email" varchar(45) NOT NULL,
    "telephone" text NOT NULL,
    "dateofbirth" date NOT NULL,
    "isMember" integer,
    "managedBy" integer,
    "belongsTo" integer NOT NULL REFERENCES "auth_user" ("id"),
    "genderID" integer,
    "experienceLevel" integer NOT NULL
);
CREATE INDEX "auth_permission_37ef4eb4" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_permissions_5f412f9a" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_83d7f98b" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_user_groups_6340c63c" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_5f412f9a" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_user_user_permissions_6340c63c" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_83d7f98b" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_session_b7b81f0c" ON "django_session" ("expire_date");
CREATE INDEX "django_admin_log_6340c63c" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_37ef4eb4" ON "django_admin_log" ("content_type_id");
CREATE INDEX "bookingsystem_defaultcoaches_baf2aea3" ON "bookingsystem_defaultcoaches" ("monMor_id");
CREATE INDEX "bookingsystem_defaultcoaches_4c0de0f2" ON "bookingsystem_defaultcoaches" ("monAft_id");
CREATE INDEX "bookingsystem_defaultcoaches_8047deaa" ON "bookingsystem_defaultcoaches" ("tueMor_id");
CREATE INDEX "bookingsystem_defaultcoaches_a4bbdefa" ON "bookingsystem_defaultcoaches" ("tueAft_id");
CREATE INDEX "bookingsystem_defaultcoaches_fc12cab5" ON "bookingsystem_defaultcoaches" ("wedMor_id");
CREATE INDEX "bookingsystem_defaultcoaches_c35c4bfd" ON "bookingsystem_defaultcoaches" ("wedAft_id");
CREATE INDEX "bookingsystem_defaultcoaches_595391af" ON "bookingsystem_defaultcoaches" ("thuMor_id");
CREATE INDEX "bookingsystem_defaultcoaches_b3c115cc" ON "bookingsystem_defaultcoaches" ("thuAft_id");
CREATE INDEX "bookingsystem_defaultcoaches_a73f2428" ON "bookingsystem_defaultcoaches" ("friMor_id");
CREATE INDEX "bookingsystem_defaultcoaches_eb019a3b" ON "bookingsystem_defaultcoaches" ("friAft_id");
CREATE INDEX "bookingsystem_client_bc36dd36" ON "bookingsystem_client" ("belongsTo");
COMMIT;
