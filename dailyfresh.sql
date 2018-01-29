-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: dailyfresh
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1-log

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
-- Table structure for table `Order_mes`
--

DROP TABLE IF EXISTS `Order_mes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Order_mes` (
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `order_id` varchar(128) NOT NULL,
  `pay_way` smallint(6) NOT NULL,
  `total_count` int(11) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `transport_price` decimal(10,2) NOT NULL,
  `pay_state` smallint(6) NOT NULL,
  `pay_no` varchar(128) NOT NULL,
  `addr_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `Order_mes_5e1254c9` (`addr_id_id`),
  KEY `Order_mes_18624dd3` (`user_id_id`),
  CONSTRAINT `Order_mes_addr_id_id_7cda746bb184a3f3_fk_address_id` FOREIGN KEY (`addr_id_id`) REFERENCES `address` (`id`),
  CONSTRAINT `Order_mes_user_id_id_3a44a97a081dab26_fk_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Order_mes`
--

LOCK TABLES `Order_mes` WRITE;
/*!40000 ALTER TABLE `Order_mes` DISABLE KEYS */;
INSERT INTO `Order_mes` VALUES ('2018-01-21 15:50:52.605270','2018-01-21 15:50:52.605485',0,'201801212350521',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:50:54.262147','2018-01-21 15:50:54.262265',0,'201801212350541',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:50:55.473841','2018-01-21 15:50:55.474408',0,'201801212350551',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:52:23.324558','2018-01-21 15:52:23.324771',0,'201801212352231',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:52:30.475291','2018-01-21 15:52:30.475466',0,'201801212352301',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:52:32.245318','2018-01-21 15:52:32.245455',0,'201801212352321',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:52:33.557975','2018-01-21 15:52:33.558139',0,'201801212352331',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:53:34.844372','2018-01-21 15:53:34.844581',0,'201801212353341',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:54:12.899848','2018-01-21 15:54:12.900021',0,'201801212354121',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:54:14.046932','2018-01-21 15:54:14.047071',0,'201801212354141',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:54:37.366334','2018-01-21 15:54:37.366446',0,'201801212354371',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:55:06.682061','2018-01-21 15:55:06.682233',0,'201801212355061',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:55:41.239022','2018-01-21 15:55:41.239209',0,'201801212355411',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:56:18.329740','2018-01-21 15:56:18.329945',0,'201801212356181',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:56:19.929094','2018-01-21 15:56:19.929398',0,'201801212356191',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:56:25.138798','2018-01-21 15:56:25.138920',0,'201801212356251',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:56:48.450396','2018-01-21 15:56:48.451121',0,'201801212356481',1,0,0.00,10.00,1,'',4,1),('2018-01-21 15:58:09.770180','2018-01-21 15:58:09.770380',0,'201801212358091',1,0,0.00,10.00,1,'',4,1),('2018-01-21 16:00:54.925161','2018-01-21 16:00:54.925857',0,'201801220000541',1,0,0.00,10.00,1,'',4,1),('2018-01-21 16:00:56.278355','2018-01-21 16:00:56.278465',0,'201801220000561',1,0,0.00,10.00,1,'',4,1),('2018-01-21 16:01:45.434317','2018-01-21 16:01:45.503657',0,'201801220001451',1,2,22.12,10.00,1,'',4,1),('2018-01-21 16:01:50.491982','2018-01-21 16:01:50.492095',0,'201801220001501',1,0,0.00,10.00,1,'',4,1),('2018-01-21 16:05:00.997352','2018-01-21 16:05:01.048147',0,'201801220005001',1,1,20.00,10.00,1,'',4,1),('2018-01-22 09:05:44.496411','2018-01-22 09:05:44.673726',0,'201801221705441',1,9,229.70,10.00,1,'',2,1),('2018-01-22 11:35:34.535818','2018-01-22 11:35:34.620547',0,'201801221935341',1,19,624.00,10.00,1,'',4,1),('2018-01-22 11:41:20.550023','2018-01-22 11:41:20.593842',0,'201801221941201',1,11,352.00,10.00,1,'',4,1),('2018-01-22 11:41:26.106884','2018-01-22 11:41:26.142359',0,'201801221941262',1,3,96.00,10.00,1,'',5,2),('2018-01-22 11:44:15.994054','2018-01-22 11:44:16.025413',0,'201801221944151',1,12,384.00,10.00,1,'',4,1),('2018-01-22 11:45:36.134640','2018-01-22 11:45:36.176423',0,'201801221945361',1,8,256.00,10.00,1,'',4,1),('2018-01-22 11:46:52.797570','2018-01-22 11:47:00.151027',0,'201801221946522',1,2,64.00,10.00,1,'',5,2),('2018-01-22 11:49:07.277664','2018-01-22 11:49:07.312839',0,'201801221949072',1,3,96.00,10.00,1,'',5,2),('2018-01-22 11:49:13.359472','2018-01-22 11:49:13.393901',0,'201801221949131',1,6,192.00,10.00,1,'',4,1),('2018-01-22 11:50:42.963140','2018-01-22 11:50:43.000161',0,'201801221950422',1,1,32.00,10.00,1,'',5,2),('2018-01-22 12:46:03.690956','2018-01-22 12:46:03.720290',0,'201801222046031',1,1,10.00,10.00,1,'',4,1),('2018-01-24 02:07:51.055249','2018-01-24 02:07:51.092391',0,'201801241007511',3,1,10.00,10.00,1,'',4,1),('2018-01-24 04:01:25.961381','2018-01-24 04:01:26.063876',0,'201801241201251',3,3,135.00,10.00,1,'',4,1),('2018-01-24 04:19:14.061121','2018-01-24 04:19:14.216132',0,'201801241219141',3,3,119.40,10.00,1,'',4,1),('2018-01-24 04:25:16.155241','2018-01-24 04:25:16.224097',0,'201801241225161',3,1,100.90,10.00,1,'',4,1),('2018-01-24 04:34:28.633966','2018-01-24 06:36:06.744941',0,'201801241234281',3,1,45.00,10.00,4,'2018012421001004060200235772',4,1),('2018-01-24 04:38:04.317995','2018-01-24 04:38:04.395712',0,'201801241238042',3,1,20.00,10.00,1,'',5,2),('2018-01-24 05:04:54.937122','2018-01-24 05:04:55.146598',0,'201801241304542',3,1,29.90,10.00,1,'',5,2),('2018-01-24 05:06:45.455924','2018-01-24 05:06:45.529847',0,'201801241306451',3,1,50.00,10.00,1,'',4,1),('2018-01-24 05:15:51.826523','2018-01-24 05:15:51.902461',0,'201801241315512',3,3,60.00,10.00,1,'',5,2),('2018-01-24 05:28:16.712763','2018-01-24 05:28:16.893250',0,'201801241328161',3,1,12.12,10.00,1,'',4,1),('2018-01-24 06:05:13.072826','2018-01-24 06:05:13.135589',0,'201801241405131',1,1,34.00,10.00,1,'',4,1),('2018-01-24 06:05:34.988127','2018-01-24 06:05:35.008580',0,'201801241405341',3,1,34.00,10.00,1,'',4,1),('2018-01-24 06:16:02.971723','2018-01-24 06:16:03.010116',0,'201801241416021',3,1,45.00,10.00,1,'',4,1),('2018-01-24 06:22:28.286599','2018-01-24 06:23:30.407543',0,'201801241422281',3,1,50.00,10.00,4,'2018012421001004060200235771',4,1);
/*!40000 ALTER TABLE `Order_mes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `receiver` varchar(30) NOT NULL,
  `addr` varchar(200) NOT NULL,
  `zip_code` varchar(6) DEFAULT NULL,
  `phone` varchar(11) NOT NULL,
  `is_default` tinyint(1) NOT NULL,
  `User_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `address_User_id_id_566adc988b942ee0_fk_user_id` (`User_id_id`),
  CONSTRAINT `address_User_id_id_566adc988b942ee0_fk_user_id` FOREIGN KEY (`User_id_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (1,'2018-01-17 14:28:44.367015','2018-01-17 14:28:44.367224',0,'小王','北京市昌平区',NULL,'11111111111',1,1),(2,'2018-01-17 14:29:17.820307','2018-01-17 14:29:17.820499',0,'老王','北京市海淀区',NULL,'13333333333',0,1),(3,'2018-01-17 14:31:07.784776','2018-01-17 14:31:07.784882',0,'wangwu','北京市',NULL,'13335256039',0,1),(4,'2018-01-18 13:15:22.742231','2018-01-18 13:15:22.742348',0,'校长','北京',NULL,'11111111111',0,1),(5,'2018-01-22 11:38:03.381922','2018-01-22 11:38:03.382040',0,'wangfan','北京市',NULL,'13333333333',1,2);
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_2f7f7d522013a4f4_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_2f7f7d522013a4f4_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_4e497ed85dfd3be1_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_64c5810f62063890_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add 商品分类',6,'add_goodstype'),(17,'Can change 商品分类',6,'change_goodstype'),(18,'Can delete 商品分类',6,'delete_goodstype'),(19,'Can add 商品spu',7,'add_goodsspu'),(20,'Can change 商品spu',7,'change_goodsspu'),(21,'Can delete 商品spu',7,'delete_goodsspu'),(22,'Can add 商品sku',8,'add_goodssku'),(23,'Can change 商品sku',8,'change_goodssku'),(24,'Can delete 商品sku',8,'delete_goodssku'),(25,'Can add 商品图片',9,'add_goodsimg'),(26,'Can change 商品图片',9,'change_goodsimg'),(27,'Can delete 商品图片',9,'delete_goodsimg'),(28,'Can add 商品促销活动',10,'add_salespromotion'),(29,'Can change 商品促销活动',10,'change_salespromotion'),(30,'Can delete 商品促销活动',10,'delete_salespromotion'),(31,'Can add 首页图片轮播',11,'add_goodsimgactivity'),(32,'Can change 首页图片轮播',11,'change_goodsimgactivity'),(33,'Can delete 首页图片轮播',11,'delete_goodsimgactivity'),(34,'Can add 首页商品分类展示',12,'add_goodstypeshow'),(35,'Can change 首页商品分类展示',12,'change_goodstypeshow'),(36,'Can delete 首页商品分类展示',12,'delete_goodstypeshow'),(37,'Can add 订单信息',13,'add_order_mes'),(38,'Can change 订单信息',13,'change_order_mes'),(39,'Can delete 订单信息',13,'delete_order_mes'),(40,'Can add 订单商品',14,'add_ordergoods'),(41,'Can change 订单商品',14,'change_ordergoods'),(42,'Can delete 订单商品',14,'delete_ordergoods'),(43,'Can add 用户',15,'add_user'),(44,'Can change 用户',15,'change_user'),(45,'Can delete 用户',15,'delete_user'),(46,'Can add 地址',16,'add_address'),(47,'Can change 地址',16,'change_address'),(48,'Can delete 地址',16,'delete_address');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_66d73c6f14351e49_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_11271039fdabc38c_fk_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_66d73c6f14351e49_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_11271039fdabc38c_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-01-18 09:02:50.614543','2','SalesPromotion object',2,'已修改 promotion_addr 。',10,2),(2,'2018-01-18 09:03:55.912572','6','GoodsType object',2,'已修改 type_name 。',6,2),(3,'2018-01-18 09:04:29.873065','6','GoodsType object',2,'已修改 type_name 。',6,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3536eb14c9234c9c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(9,'goods','goodsimg'),(11,'goods','goodsimgactivity'),(8,'goods','goodssku'),(7,'goods','goodsspu'),(6,'goods','goodstype'),(12,'goods','goodstypeshow'),(10,'goods','salespromotion'),(14,'orders','ordergoods'),(13,'orders','order_mes'),(5,'sessions','session'),(16,'users','address'),(15,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-01-16 14:03:03.307527'),(2,'contenttypes','0002_remove_content_type_name','2018-01-16 14:03:03.449857'),(3,'auth','0001_initial','2018-01-16 14:03:03.800467'),(4,'auth','0002_alter_permission_name_max_length','2018-01-16 14:03:03.895012'),(5,'auth','0003_alter_user_email_max_length','2018-01-16 14:03:03.951054'),(6,'auth','0004_alter_user_username_opts','2018-01-16 14:03:03.996324'),(7,'auth','0005_alter_user_last_login_null','2018-01-16 14:03:04.041159'),(8,'auth','0006_require_contenttypes_0002','2018-01-16 14:03:04.058961'),(9,'users','0001_initial','2018-01-16 14:03:04.596518'),(10,'admin','0001_initial','2018-01-16 14:03:04.855766'),(11,'goods','0001_initial','2018-01-16 14:03:06.526646'),(12,'orders','0001_initial','2018-01-16 14:03:06.913276'),(13,'orders','0002_auto_20180116_2202','2018-01-16 14:03:07.999485'),(14,'sessions','0001_initial','2018-01-16 14:03:08.085793'),(15,'goods','0002_auto_20180117_0943','2018-01-17 01:43:59.369238');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_img`
--

DROP TABLE IF EXISTS `goods_img`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_img` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `goods_img` varchar(100) NOT NULL,
  `goods_sku_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_img_798c4bed` (`goods_sku_id_id`),
  CONSTRAINT `goods_img_goods_sku_id_id_7df23425787eb297_fk_goods_sku_id` FOREIGN KEY (`goods_sku_id_id`) REFERENCES `goods_sku` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_img`
--

LOCK TABLES `goods_img` WRITE;
/*!40000 ALTER TABLE `goods_img` DISABLE KEYS */;
/*!40000 ALTER TABLE `goods_img` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_img_activity`
--

DROP TABLE IF EXISTS `goods_img_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_img_activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `Activity_img` varchar(100) NOT NULL,
  `Activity_img_index` smallint(6) NOT NULL,
  `goods_sku_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_img_activity_798c4bed` (`goods_sku_id_id`),
  CONSTRAINT `goods_img_activ_goods_sku_id_id_29cf2981d2b1075b_fk_goods_sku_id` FOREIGN KEY (`goods_sku_id_id`) REFERENCES `goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_img_activity`
--

LOCK TABLES `goods_img_activity` WRITE;
/*!40000 ALTER TABLE `goods_img_activity` DISABLE KEYS */;
INSERT INTO `goods_img_activity` VALUES (1,'2017-11-14 08:48:05.549864','2017-11-14 08:48:05.549896',0,'group1/M00/00/00/rBCzg1oKrcWAX7y-AACpB-LsCdE6038911',0,5),(2,'2017-11-14 08:53:26.498965','2017-11-14 08:53:26.499001',0,'group1/M00/00/00/rBCzg1oKrwaAUerYAAC3B-z8J2c2488703',1,26),(3,'2017-11-14 08:53:40.586457','2017-11-14 08:53:40.586490',0,'group1/M00/00/00/rBCzg1oKrxSAac1BAAETwXb_pso9132934',2,13),(4,'2017-11-14 08:54:02.805958','2017-11-14 08:54:02.805992',0,'group1/M00/00/00/rBCzg1oKryqAPjmzAAD0akkXmFo4923405',3,9);
/*!40000 ALTER TABLE `goods_img_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_sku`
--

DROP TABLE IF EXISTS `goods_sku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_sku` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `goods_name` varchar(20) NOT NULL,
  `goods_intro` varchar(256) NOT NULL,
  `goods_price` decimal(10,2) NOT NULL,
  `goods_unit` varchar(30) NOT NULL,
  `goods_img` varchar(100) NOT NULL,
  `goods_stock` int(11) NOT NULL,
  `goods_annul` int(11) NOT NULL,
  `goods_state` smallint(6) NOT NULL,
  `goods_spu_id_id` int(11) NOT NULL,
  `goods_type_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_sku_95a06766` (`goods_spu_id_id`),
  KEY `goods_sku_4307b960` (`goods_type_id_id`),
  CONSTRAINT `goods_sku_goods_spu_id_id_62153f0df68d7197_fk_goods_spu_id` FOREIGN KEY (`goods_spu_id_id`) REFERENCES `goods_spu` (`id`),
  CONSTRAINT `goods_sku_goods_type_id_id_7d3dd3382e4a9d_fk_goods_type_id` FOREIGN KEY (`goods_type_id_id`) REFERENCES `goods_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_sku`
--

LOCK TABLES `goods_sku` WRITE;
/*!40000 ALTER TABLE `goods_sku` DISABLE KEYS */;
INSERT INTO `goods_sku` VALUES (1,'2017-11-15 03:10:14.045538','2017-11-14 08:24:49.138489',0,'草莓 500g','草莓简介',10.00,'500g','group1/M00/00/00/rBCzg1oKqFGAR2tjAAAljHPuXJg4272079',96,2,1,1,1),(2,'2017-11-15 03:11:04.490384','2017-11-14 08:44:43.484243',0,'盒装草莓','草莓简介',20.00,'盒','group1/M00/00/00/rBCzg1oKrPuAKse1AAEc8FlxEvU2553153',10,0,1,1,1),(3,'2017-11-15 03:12:32.165020','2017-11-14 08:25:22.505620',0,'葡萄','葡萄简介',20.00,'500g','group1/M00/00/00/rBCzg1oKqHKAYfXaAAAjjiYTEkw5436358',3,4,1,2,1),(4,'2017-11-15 03:13:16.457844','2018-01-22 11:46:52.875187',0,'柠檬','简介',32.00,'500g','group1/M00/00/00/rBCzg1oKqH6AMZt_AAAgnaeGwNQ6246033',0,12,1,3,1),(5,'2017-11-15 03:14:05.799352','2017-11-14 08:25:56.427676',0,'奇异果','简介',12.12,'500g','group1/M00/00/00/rBCzg1oKqJSAS1xIAAAeuLYy0pU6253560',11,1,1,4,1),(6,'2017-11-15 03:15:09.971968','2017-11-14 08:26:09.113586',0,'大青虾','简介',34.00,'500g','group1/M00/00/00/rBCzg1oKqKGAFAV-AAA5OS4Kl4c4097622',10,2,1,5,2),(7,'2017-11-15 03:15:53.812181','2017-11-14 08:26:19.094675',0,'北海道秋刀鱼','简介',50.00,'500g','group1/M00/00/00/rBCzg1oKqKuAavf8AAAkaP_7_187862565',13,2,1,6,2),(8,'2017-11-15 03:16:24.763232','2017-11-14 08:26:31.121824',0,'扇贝','简介',56.60,'500g','group1/M00/00/00/rBCzg1oKqLeATLQAAAAk8WCqqmI2968215',13,0,1,7,2),(9,'2017-11-15 03:17:13.426611','2017-11-14 08:26:58.739624',0,'基围虾','简介',100.90,'500g','group1/M00/00/00/rBCzg1oKqNKANQKOAAAk0DN4-yE7007770',13,1,1,8,2),(10,'2017-11-15 03:17:47.656066','2017-11-14 08:29:56.158261',0,'猪肉','简介',23.99,'500g','group1/M00/00/00/rBCzg1oKqYSASWr0AAEVpb1YHUE4011268',100,0,1,9,3),(11,'2017-11-15 03:18:15.497630','2017-11-14 08:31:27.169999',0,'牛肉','简介',34.99,'500g','group1/M00/00/00/rBCzg1oKqd-AUsoBAAEExAU4yXU2908730',100,0,1,10,3),(12,'2017-11-15 03:18:44.453933','2017-11-14 08:32:22.493340',0,'羊肉','简介',56.99,'500g','group1/M00/00/00/rBCzg1oKqhaAKgwkAAB6NOQDrpk3374052',100,0,1,11,3),(13,'2017-11-15 03:19:10.209472','2017-11-14 08:33:15.061544',0,'牛排','简介',99.99,'500g','group1/M00/00/00/rBCzg1oKqkuAUD0WAACwa3rCDPQ3064181',100,0,1,12,3),(14,'2017-11-15 03:19:44.020204','2017-11-14 08:34:31.275370',0,'盒装鸡蛋','简介',23.00,'500g','group1/M00/00/00/rBCzg1oKqpeAZnSEAADUKbwLSqY1972845',100,0,1,13,4),(15,'2017-11-15 03:20:20.962831','2017-11-14 08:35:21.725162',0,'鸡肉','简介',32.00,'500g','group1/M00/00/00/rBCzg1oKqsmAVxzcAADUY5hC_sI5143658',100,0,1,14,4),(16,'2017-11-15 03:20:53.724305','2017-11-14 08:37:27.336911',0,'鸭蛋','简介',45.00,'盒','group1/M00/00/00/rBCzg1oKq0eAMxKFAAFC_2tSkFo4950479',117,4,1,15,4),(17,'2017-11-15 03:21:22.965398','2017-11-14 08:38:08.440778',0,'鸡腿','简介',45.00,'500g','group1/M00/00/00/rBCzg1oKq3CADiewAAA2_p7G96w3860045',11,1,1,16,4),(18,'2017-11-15 03:22:04.462490','2017-11-14 08:38:45.119926',0,'白菜','简介',4.50,'500g','group1/M00/00/00/rBCzg1oKq5WAQnWDAADWHYeKaNI7952227',100,0,1,17,5),(19,'2017-11-15 03:22:31.745392','2017-11-14 08:39:40.030728',0,'芹菜','简介',3.50,'500g','group1/M00/00/00/rBCzg1oKq8yAa_CvAACIrzuaK646641688',12,0,1,18,5),(20,'2017-11-15 03:23:21.161526','2017-11-14 08:40:08.185684',0,'香菜','简介',7.90,'500g','group1/M00/00/00/rBCzg1oKq-iAUG8xAACNpHC0IEY3849954',100,0,1,19,5),(21,'2017-11-15 03:23:46.986158','2017-11-14 08:40:38.330247',0,'冬瓜','简介',12.99,'500g','group1/M00/00/00/rBCzg1oKrAaAN1Z6AAENHrNG1-s8874196',100,0,1,20,5),(22,'2017-11-15 03:24:10.445214','2017-11-14 08:41:19.155821',0,'鱼丸','简介',66.00,'500g','group1/M00/00/00/rBCzg1oKrC-ACdOBAADZQphQJ2o3748807',12,0,1,21,6),(23,'2017-11-15 03:24:37.927158','2017-11-14 08:41:59.658787',0,'蟹棒','简介',68.00,'500g','group1/M00/00/00/rBCzg1oKrFeAJ9PuAABxy5vKkgY2006901',100,0,1,22,6),(24,'2017-11-15 03:25:18.235816','2017-11-14 08:42:25.868409',0,'虾丸','简介',89.99,'500g','group1/M00/00/00/rBCzg1oKrHGADF7jAABICav_wjk1418828',100,0,1,23,6),(25,'2017-11-15 03:25:56.170531','2017-11-14 08:43:18.768380',0,'速冻水饺','简介',20.00,'袋','group1/M00/00/00/rBCzg1oKrKaAFrRTAACMoBJXjDs3577358',100,0,1,24,6),(26,'2017-11-14 08:53:00.188619','2017-11-14 08:53:00.188652',0,'越南芒果','新鲜越南芒果',29.90,'2.5kg','group1/M00/00/00/rBCzg1oKruyABIIzAAByzTJcTjM7085820',99,1,1,25,1),(27,'2017-11-17 07:57:00.677981','2017-11-17 07:57:00.678022',0,'鹌鹑蛋','简介',39.80,'126枚','group1/M00/00/00/rBCzg1oOlkyAHiH3AAGZ6KapWiA5556935',97,3,1,26,4),(28,'2017-11-17 07:58:18.361078','2017-11-17 07:58:18.361122',0,'鹅蛋','简介',49.90,'6枚','group1/M00/00/00/rBCzg1oOlpqAOZ8gAADg_NUp5b47679136',80,0,1,27,4),(29,'2017-11-17 07:59:48.998394','2017-11-17 07:59:48.998431',0,'红辣椒','简介',11.00,'2.5kg','group1/M00/00/00/rBCzg1oOlvWAB6BMAAHXO8pdocY9345486',150,0,1,28,5);
/*!40000 ALTER TABLE `goods_sku` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_spu`
--

DROP TABLE IF EXISTS `goods_spu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_spu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `goods_name` varchar(20) NOT NULL,
  `goods_details` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_spu`
--

LOCK TABLES `goods_spu` WRITE;
/*!40000 ALTER TABLE `goods_spu` DISABLE KEYS */;
INSERT INTO `goods_spu` VALUES (1,'2017-11-15 03:03:05.257969','2017-11-15 03:03:05.258130',0,'草莓','<p><strong>很不错的草莓</strong></p>'),(2,'2017-11-15 03:05:36.964951','2017-11-15 03:05:36.965129',0,'葡萄',''),(3,'2017-11-15 03:05:52.323866','2017-11-15 03:05:52.323949',0,'柠檬',''),(4,'2017-11-15 03:06:01.267481','2017-11-15 03:06:01.267615',0,'奇异果',''),(5,'2017-11-15 03:06:30.418683','2017-11-15 03:06:30.418789',0,'大青虾',''),(6,'2017-11-15 03:06:35.994464','2017-11-15 03:06:35.994567',0,'秋刀鱼',''),(7,'2017-11-15 03:06:48.115318','2017-11-15 03:06:48.115410',0,'扇贝',''),(8,'2017-11-15 03:07:03.057514','2017-11-15 03:07:03.057601',0,'基围虾',''),(9,'2017-11-15 03:07:36.306725','2017-11-15 03:07:36.306926',0,'猪肉',''),(10,'2017-11-15 03:07:39.056064','2017-11-15 03:07:39.056145',0,'牛肉',''),(11,'2017-11-15 03:07:41.955755','2017-11-15 03:07:41.955833',0,'羊肉',''),(12,'2017-11-15 03:07:44.741474','2017-11-15 03:07:44.741574',0,'牛排',''),(13,'2017-11-15 03:07:51.748699','2017-11-15 03:07:51.748828',0,'鸡蛋',''),(14,'2017-11-15 03:07:56.413773','2017-11-15 03:07:56.413853',0,'鸡肉',''),(15,'2017-11-15 03:07:59.568405','2017-11-15 03:07:59.568554',0,'鸭蛋',''),(16,'2017-11-15 03:08:03.020608','2017-11-15 03:08:03.020764',0,'鸡腿',''),(17,'2017-11-15 03:08:10.063820','2017-11-15 03:08:10.063898',0,'白菜',''),(18,'2017-11-15 03:08:13.315906','2017-11-15 03:08:13.316025',0,'芹菜',''),(19,'2017-11-15 03:08:16.351445','2017-11-15 03:08:16.351526',0,'香菜',''),(20,'2017-11-15 03:08:24.232660','2017-11-15 03:08:24.232743',0,'冬瓜',''),(21,'2017-11-15 03:08:36.939678','2017-11-15 03:08:36.940113',0,'鱼丸',''),(22,'2017-11-15 03:08:43.194862','2017-11-15 03:08:43.194985',0,'蟹棒',''),(23,'2017-11-15 03:08:50.771785','2017-11-15 03:08:50.771931',0,'虾丸',''),(24,'2017-11-15 03:09:01.546052','2017-11-15 03:09:01.546152',0,'速冻水饺',''),(25,'2017-11-14 08:50:50.383071','2017-11-14 08:50:50.383115',0,'芒果',''),(26,'2017-11-17 07:54:26.657410','2017-11-17 07:54:26.657443',0,'鹌鹑蛋',''),(27,'2017-11-17 07:54:35.205668','2017-11-17 07:54:35.205703',0,'鹅蛋',''),(28,'2017-11-17 07:54:46.756236','2017-11-17 07:54:46.756272',0,'红辣椒','');
/*!40000 ALTER TABLE `goods_spu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_type`
--

DROP TABLE IF EXISTS `goods_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `type_name` varchar(20) NOT NULL,
  `goods_logo` varchar(10) NOT NULL,
  `type_img` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_type`
--

LOCK TABLES `goods_type` WRITE;
/*!40000 ALTER TABLE `goods_type` DISABLE KEYS */;
INSERT INTO `goods_type` VALUES (1,'2017-11-14 05:02:09.888544','2017-11-14 05:02:09.888598',0,'新鲜水果','fruit','group1/M00/00/00/rBCzg1oKeNKAEl87AAAmv27pX4k4942898'),(2,'2017-11-14 05:04:32.069517','2017-11-14 05:04:32.069561',0,'海鲜水产','seafood','group1/M00/00/00/rBCzg1oKeWCAOQBsAABHr3RQqFs4497074'),(3,'2017-11-14 05:05:34.514415','2017-11-14 05:05:34.514449',0,'猪牛羊肉','meet','group1/M00/00/00/rBCzg1oKeZ6AA5HjAAAy1Tlm9So7276786'),(4,'2017-11-14 05:05:58.366135','2017-11-14 05:05:58.366170',0,'禽类蛋品','egg','group1/M00/00/00/rBCzg1oKebaAcEWVAAAqR4DoSUg3788077'),(5,'2017-11-14 05:06:32.561861','2017-11-14 05:06:32.561895',0,'新鲜蔬菜','vegetables','group1/M00/00/00/rBCzg1oKediAdUaaAAA-0ZoYkpM9419116'),(6,'2017-11-14 05:06:55.562634','2018-01-18 09:04:28.697842',0,'速冻食品','ice','group1/M00/00/00/rBCzg1oKee-AGMXLAAA3sZPrVzQ0297876');
/*!40000 ALTER TABLE `goods_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_type_show`
--

DROP TABLE IF EXISTS `goods_type_show`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_type_show` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `show_type` smallint(6) NOT NULL,
  `show_index` smallint(6) NOT NULL,
  `goods_sku_id_id` int(11) NOT NULL,
  `goods_type_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_type_show_goods_sku_id_id_3f1354b1526ca864_fk_goods_sku_id` (`goods_sku_id_id`),
  KEY `goods_type_sh_goods_type_id_id_6457fe4cea041a03_fk_goods_type_id` (`goods_type_id_id`),
  CONSTRAINT `goods_type_sh_goods_type_id_id_6457fe4cea041a03_fk_goods_type_id` FOREIGN KEY (`goods_type_id_id`) REFERENCES `goods_type` (`id`),
  CONSTRAINT `goods_type_show_goods_sku_id_id_3f1354b1526ca864_fk_goods_sku_id` FOREIGN KEY (`goods_sku_id_id`) REFERENCES `goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_type_show`
--

LOCK TABLES `goods_type_show` WRITE;
/*!40000 ALTER TABLE `goods_type_show` DISABLE KEYS */;
INSERT INTO `goods_type_show` VALUES (1,'2017-11-14 08:57:41.509910','2017-11-14 08:57:41.509945',0,1,0,1,1),(2,'2017-11-14 08:57:50.129355','2017-11-14 08:57:50.129388',0,1,1,3,1),(3,'2017-11-14 08:58:00.896427','2017-11-14 08:58:00.896459',0,1,2,5,1),(4,'2017-11-14 08:58:20.417072','2017-11-14 08:58:20.417107',0,1,3,4,1),(5,'2017-11-14 08:58:32.934165','2017-11-14 08:58:32.934197',0,0,0,2,1),(6,'2017-11-14 08:58:53.943189','2017-11-14 08:58:53.943227',0,0,1,4,1),(7,'2017-11-14 08:59:16.396829','2017-11-14 08:59:16.396864',0,1,0,6,2),(8,'2017-11-14 08:59:25.723510','2017-11-14 08:59:25.723545',0,1,1,7,2),(9,'2017-11-14 08:59:37.353278','2017-11-14 08:59:37.353315',0,1,2,8,2),(10,'2017-11-14 08:59:48.082119','2017-11-14 09:30:28.117330',0,1,3,9,2),(11,'2017-11-14 08:59:59.725972','2017-11-14 08:59:59.726006',0,0,0,9,2),(12,'2017-11-14 09:00:11.685051','2017-11-14 09:00:11.685098',0,0,1,8,2),(13,'2017-11-14 09:00:20.409490','2017-11-14 09:00:20.409522',0,1,0,10,3),(15,'2017-11-14 09:00:41.325634','2017-11-14 09:00:41.325668',0,1,2,12,3),(16,'2017-11-14 09:00:56.193991','2017-11-14 09:00:56.194023',0,1,3,13,3),(17,'2017-11-14 09:01:09.550978','2017-11-14 09:01:09.551016',0,0,0,15,3),(18,'2017-11-14 09:01:18.798219','2017-11-14 09:01:18.798251',0,1,1,17,3),(19,'2017-11-14 09:01:29.182673','2017-11-14 09:01:29.182705',0,1,0,14,4),(20,'2017-11-14 09:01:44.702111','2017-11-14 09:01:44.702146',0,1,1,16,4),(21,'2017-11-14 09:02:01.490018','2017-11-14 09:02:01.490053',0,0,0,14,4),(22,'2017-11-14 09:02:14.000306','2017-11-14 09:02:14.000344',0,0,1,16,4),(23,'2017-11-14 09:02:29.300733','2017-11-14 09:02:29.300768',0,1,0,18,5),(24,'2017-11-14 09:02:38.655411','2017-11-14 09:02:38.655444',0,1,1,19,5),(25,'2017-11-14 09:02:48.641048','2017-11-14 09:02:48.641080',0,1,2,20,5),(26,'2017-11-14 09:03:01.896718','2017-11-14 09:03:01.896759',0,0,0,20,5),(27,'2017-11-14 09:03:14.583044','2017-11-14 09:03:14.583086',0,0,1,19,5),(28,'2017-11-14 09:03:27.597171','2017-11-14 09:03:27.597206',0,1,0,22,6),(29,'2017-11-14 09:03:37.078417','2017-11-14 09:03:37.078451',0,1,1,23,6),(30,'2017-11-14 09:03:48.459266','2017-11-14 09:03:48.459299',0,1,2,24,6),(31,'2017-11-14 09:03:58.834392','2017-11-14 09:03:58.834428',0,1,3,25,6),(32,'2017-11-14 09:04:11.118584','2017-11-14 09:04:11.118628',0,0,0,23,6),(33,'2017-11-14 09:04:21.235831','2017-11-14 09:04:21.235887',0,0,1,25,6),(34,'2017-11-17 08:00:09.522776','2017-11-17 08:00:09.522811',0,1,2,27,4),(35,'2017-11-17 08:00:19.382093','2017-11-17 08:00:19.382125',0,1,3,28,4),(36,'2017-11-17 08:00:31.352237','2017-11-17 08:00:31.352274',0,1,3,29,5);
/*!40000 ALTER TABLE `goods_type_show` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordergoods`
--

DROP TABLE IF EXISTS `ordergoods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ordergoods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `goods_count` int(11) NOT NULL,
  `goods_price` decimal(10,2) NOT NULL,
  `goods_comment` varchar(250) NOT NULL,
  `goods_sku_id_id` int(11) NOT NULL,
  `order_mes_id_id` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ordergoods_goods_sku_id_id_227fbd4c73f7196f_fk_goods_sku_id` (`goods_sku_id_id`),
  KEY `ordergood_order_mes_id_id_569cfcb4799e4c23_fk_Order_mes_order_id` (`order_mes_id_id`),
  CONSTRAINT `ordergood_order_mes_id_id_569cfcb4799e4c23_fk_Order_mes_order_id` FOREIGN KEY (`order_mes_id_id`) REFERENCES `Order_mes` (`order_id`),
  CONSTRAINT `ordergoods_goods_sku_id_id_227fbd4c73f7196f_fk_goods_sku_id` FOREIGN KEY (`goods_sku_id_id`) REFERENCES `goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordergoods`
--

LOCK TABLES `ordergoods` WRITE;
/*!40000 ALTER TABLE `ordergoods` DISABLE KEYS */;
INSERT INTO `ordergoods` VALUES (1,'2018-01-21 16:00:54.973569','2018-01-21 16:00:54.973717',0,1,12.12,'',5,'201801220000541'),(2,'2018-01-21 16:00:54.996181','2018-01-21 16:00:54.996332',0,1,10.00,'',1,'201801220000541'),(3,'2018-01-21 16:00:56.305197','2018-01-21 16:00:56.305307',0,1,12.12,'',5,'201801220000561'),(4,'2018-01-21 16:00:56.326712','2018-01-21 16:00:56.326921',0,1,10.00,'',1,'201801220000561'),(5,'2018-01-21 16:01:45.470678','2018-01-21 16:01:45.470791',0,1,12.12,'',5,'201801220001451'),(6,'2018-01-21 16:01:45.489830','2018-01-21 16:01:45.489938',0,1,10.00,'',1,'201801220001451'),(7,'2018-01-21 16:05:01.033586','2018-01-21 16:05:01.033705',0,1,20.00,'',3,'201801220005001'),(8,'2018-01-22 09:05:44.593952','2018-01-22 09:05:44.594081',0,5,10.00,'',1,'201801221705441'),(9,'2018-01-22 09:05:44.610363','2018-01-22 09:05:44.610464',0,1,45.00,'',17,'201801221705441'),(10,'2018-01-22 09:05:44.621008','2018-01-22 09:05:44.621130',0,1,39.80,'',27,'201801221705441'),(11,'2018-01-22 09:05:44.662403','2018-01-22 09:05:44.662507',0,1,49.90,'',28,'201801221705441'),(12,'2018-01-22 09:05:44.670970','2018-01-22 09:05:44.671071',0,1,45.00,'',16,'201801221705441'),(13,'2018-01-22 11:35:34.600198','2018-01-22 11:35:34.600319',0,8,34.00,'',6,'201801221935341'),(14,'2018-01-22 11:35:34.613818','2018-01-22 11:35:34.613933',0,11,32.00,'',4,'201801221935341'),(15,'2018-01-22 11:41:20.584415','2018-01-22 11:41:20.584554',0,11,32.00,'',4,'201801221941201'),(16,'2018-01-22 11:41:26.128687','2018-01-22 11:41:26.128801',0,3,32.00,'',4,'201801221941262'),(17,'2018-01-22 11:44:16.019355','2018-01-22 11:44:16.019462',0,12,32.00,'',4,'201801221944151'),(18,'2018-01-22 11:45:36.171606','2018-01-22 11:45:36.171940',0,8,32.00,'',4,'201801221945361'),(19,'2018-01-22 11:46:52.862692','2018-01-22 11:46:52.862929',0,2,32.00,'',4,'201801221946522'),(20,'2018-01-22 11:49:07.309948','2018-01-22 11:49:07.310058',0,3,32.00,'',4,'201801221949072'),(21,'2018-01-22 11:49:13.387927','2018-01-22 11:49:13.388034',0,6,32.00,'',4,'201801221949131'),(22,'2018-01-22 11:50:42.993685','2018-01-22 11:50:42.993839',0,1,32.00,'',4,'201801221950422'),(23,'2018-01-22 12:46:03.717020','2018-01-22 12:46:03.717124',0,1,10.00,'',1,'201801222046031'),(25,'2018-01-24 02:07:51.088969','2018-01-24 02:07:51.089071',0,1,10.00,'',1,'201801241007511'),(26,'2018-01-24 04:01:26.054038','2018-01-24 04:01:26.054163',0,3,45.00,'',16,'201801241201251'),(27,'2018-01-24 04:19:14.207635','2018-01-24 04:19:14.207822',0,3,39.80,'',27,'201801241219141'),(28,'2018-01-24 04:25:16.219584','2018-01-24 04:25:16.219704',0,1,100.90,'',9,'201801241225161'),(29,'2018-01-24 04:34:28.760110','2018-01-24 04:34:28.760242',0,1,45.00,'',16,'201801241234281'),(30,'2018-01-24 04:38:04.390875','2018-01-24 04:38:04.390980',0,1,20.00,'',3,'201801241238042'),(31,'2018-01-24 05:04:55.141410','2018-01-24 05:04:55.141530',0,1,29.90,'',26,'201801241304542'),(32,'2018-01-24 05:06:45.519866','2018-01-24 05:06:45.520029',0,1,50.00,'',7,'201801241306451'),(33,'2018-01-24 05:15:51.898222','2018-01-24 05:15:51.898328',0,3,20.00,'',3,'201801241315512'),(34,'2018-01-24 05:28:16.886794','2018-01-24 05:28:16.886919',0,1,12.12,'',5,'201801241328161'),(35,'2018-01-24 06:05:13.132378','2018-01-24 06:05:13.132484',0,1,34.00,'',6,'201801241405131'),(36,'2018-01-24 06:05:35.005649','2018-01-24 06:05:35.005760',0,1,34.00,'',6,'201801241405341'),(37,'2018-01-24 06:16:03.006724','2018-01-24 06:16:03.006827',0,1,45.00,'',17,'201801241416021'),(38,'2018-01-24 06:22:28.320299','2018-01-24 06:22:28.320410',0,1,50.00,'',7,'201801241422281');
/*!40000 ALTER TABLE `ordergoods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_promotion`
--

DROP TABLE IF EXISTS `sales_promotion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sales_promotion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `promotion_name` varchar(20) NOT NULL,
  `promotion_addr` varchar(100) NOT NULL,
  `promotion_img` varchar(100) NOT NULL,
  `promotion_index` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_promotion`
--

LOCK TABLES `sales_promotion` WRITE;
/*!40000 ALTER TABLE `sales_promotion` DISABLE KEYS */;
INSERT INTO `sales_promotion` VALUES (1,'2017-11-14 08:56:21.863522','2017-11-17 08:29:08.554743',0,'吃货暑假趴','#','group1/M00/00/00/rBCzg1oKr7aAdR-2AAA2pLUeB609027808',0),(2,'2017-11-14 08:56:53.522161','2018-01-18 09:02:49.616621',0,'盛夏尝鲜季','###','group1/M00/00/00/rBCzg1oKr9WADLksAAA98yvCs1I5148432',1);
/*!40000 ALTER TABLE `sales_promotion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'pbkdf2_sha256$20000$RcSGuTxDPwD2$q8oz7kKy4ITBAoS4ULcSqp5gyks7ClONkNP1nV/pOWk=','2018-01-24 02:15:44.634062',0,'wangfan','','','1343499279@qq.com',0,1,'2018-01-17 14:04:53.690135','2018-01-17 14:04:53.742413','2018-01-17 14:04:53.822304',0),(2,'pbkdf2_sha256$20000$H2kJvps3dRZg$QofaIgwMyzy2wwD3q3DVMjmao7Ksr85tlUt1UqleLkk=','2018-01-22 11:40:58.459067',1,'wangfan1314','','','',1,1,'2018-01-18 09:01:37.797194','2018-01-18 09:01:37.852396','2018-01-18 09:01:37.852487',0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_groups`
--

DROP TABLE IF EXISTS `user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `user_groups_group_id_2532a50ef4be22a9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `user_groups_group_id_2532a50ef4be22a9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_groups_user_id_6862f6664f3ab6c_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_groups`
--

LOCK TABLES `user_groups` WRITE;
/*!40000 ALTER TABLE `user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user_permissions`
--

DROP TABLE IF EXISTS `user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `user_user_p_permission_id_17239136f6b67790_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `user_user_p_permission_id_17239136f6b67790_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_user_permissions_user_id_649c96822d10d892_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user_permissions`
--

LOCK TABLES `user_user_permissions` WRITE;
/*!40000 ALTER TABLE `user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-29 19:49:36
