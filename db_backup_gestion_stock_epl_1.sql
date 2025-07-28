-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: gestion_stock_epl
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add classe',1,'add_classe'),(2,'Can change classe',1,'change_classe'),(3,'Can delete classe',1,'delete_classe'),(4,'Can view classe',1,'view_classe'),(5,'Can add custom user',2,'add_customuser'),(6,'Can change custom user',2,'change_customuser'),(7,'Can delete custom user',2,'delete_customuser'),(8,'Can view custom user',2,'view_customuser'),(9,'Can add professeur',3,'add_professeur'),(10,'Can change professeur',3,'change_professeur'),(11,'Can delete professeur',3,'delete_professeur'),(12,'Can view professeur',3,'view_professeur'),(13,'Can add secretaire classe',4,'add_secretaireclasse'),(14,'Can change secretaire classe',4,'change_secretaireclasse'),(15,'Can delete secretaire classe',4,'delete_secretaireclasse'),(16,'Can view secretaire classe',4,'view_secretaireclasse'),(17,'Can add Cahiertexte',5,'add_cahiertexte'),(18,'Can change Cahiertexte',5,'change_cahiertexte'),(19,'Can delete Cahiertexte',5,'delete_cahiertexte'),(20,'Can view Cahiertexte',5,'view_cahiertexte'),(21,'Can add secretaire general',6,'add_secretairegeneral'),(22,'Can change secretaire general',6,'change_secretairegeneral'),(23,'Can delete secretaire general',6,'delete_secretairegeneral'),(24,'Can view secretaire general',6,'view_secretairegeneral'),(25,'Can add UE',7,'add_ue'),(26,'Can change UE',7,'change_ue'),(27,'Can delete UE',7,'delete_ue'),(28,'Can view UE',7,'view_ue'),(29,'Can add seance',8,'add_seance'),(30,'Can change seance',8,'change_seance'),(31,'Can delete seance',8,'delete_seance'),(32,'Can view seance',8,'view_seance'),(33,'Can add fichier_ ue',9,'add_fichier_ue'),(34,'Can change fichier_ ue',9,'change_fichier_ue'),(35,'Can delete fichier_ ue',9,'delete_fichier_ue'),(36,'Can view fichier_ ue',9,'view_fichier_ue'),(37,'Can add validation',10,'add_validation'),(38,'Can change validation',10,'change_validation'),(39,'Can delete validation',10,'delete_validation'),(40,'Can view validation',10,'view_validation'),(41,'Can add log entry',11,'add_logentry'),(42,'Can change log entry',11,'change_logentry'),(43,'Can delete log entry',11,'delete_logentry'),(44,'Can view log entry',11,'view_logentry'),(45,'Can add permission',12,'add_permission'),(46,'Can change permission',12,'change_permission'),(47,'Can delete permission',12,'delete_permission'),(48,'Can view permission',12,'view_permission'),(49,'Can add group',13,'add_group'),(50,'Can change group',13,'change_group'),(51,'Can delete group',13,'delete_group'),(52,'Can view group',13,'view_group'),(53,'Can add content type',14,'add_contenttype'),(54,'Can change content type',14,'change_contenttype'),(55,'Can delete content type',14,'delete_contenttype'),(56,'Can view content type',14,'view_contenttype'),(57,'Can add session',15,'add_session'),(58,'Can change session',15,'change_session'),(59,'Can delete session',15,'delete_session'),(60,'Can view session',15,'view_session'),(61,'Can add blacklisted token',16,'add_blacklistedtoken'),(62,'Can change blacklisted token',16,'change_blacklistedtoken'),(63,'Can delete blacklisted token',16,'delete_blacklistedtoken'),(64,'Can view blacklisted token',16,'view_blacklistedtoken'),(65,'Can add outstanding token',17,'add_outstandingtoken'),(66,'Can change outstanding token',17,'change_outstandingtoken'),(67,'Can delete outstanding token',17,'delete_outstandingtoken'),(68,'Can view outstanding token',17,'view_outstandingtoken');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cahiertexte`
--

DROP TABLE IF EXISTS `cahiertexte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cahiertexte` (
  `id_cahier` int NOT NULL AUTO_INCREMENT,
  `date_de_creation` datetime(6) NOT NULL,
  `date_de_mise_a_jour` datetime(6) NOT NULL,
  `id_classe` int NOT NULL,
  `id_secretaire` bigint NOT NULL,
  PRIMARY KEY (`id_cahier`),
  KEY `Cahiertexte_id_classe_a1c5f806_fk_classe_id_classe` (`id_classe`),
  KEY `Cahiertexte_id_secretaire_70133660_fk_secretaireclasse_id` (`id_secretaire`),
  CONSTRAINT `Cahiertexte_id_classe_a1c5f806_fk_classe_id_classe` FOREIGN KEY (`id_classe`) REFERENCES `classe` (`id_classe`),
  CONSTRAINT `Cahiertexte_id_secretaire_70133660_fk_secretaireclasse_id` FOREIGN KEY (`id_secretaire`) REFERENCES `secretaireclasse` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cahiertexte`
--

LOCK TABLES `cahiertexte` WRITE;
/*!40000 ALTER TABLE `cahiertexte` DISABLE KEYS */;
INSERT INTO `cahiertexte` VALUES (1,'2025-07-28 07:57:19.103723','2025-07-28 07:57:19.103723',3,2),(2,'2025-07-28 07:57:19.124875','2025-07-28 07:57:19.124875',4,3),(3,'2025-07-28 07:57:19.143851','2025-07-28 07:57:19.143851',5,4),(4,'2025-07-28 07:57:19.168806','2025-07-28 07:57:19.168806',6,5),(5,'2025-07-28 07:57:19.188913','2025-07-28 07:57:19.188913',8,6),(6,'2025-07-28 07:57:19.203825','2025-07-28 07:57:19.203825',9,7),(7,'2025-07-28 07:57:19.224577','2025-07-28 07:57:19.224577',10,8),(8,'2025-07-28 07:57:19.243693','2025-07-28 07:57:19.243693',11,9),(9,'2025-07-28 07:57:19.256315','2025-07-28 07:57:19.256315',14,10),(10,'2025-07-28 07:57:19.278616','2025-07-28 07:57:19.278616',15,11),(11,'2025-07-28 07:57:19.293682','2025-07-28 07:57:19.293682',16,12),(12,'2025-07-28 07:57:19.313743','2025-07-28 07:57:19.313743',17,13),(13,'2025-07-28 07:57:19.333708','2025-07-28 07:57:19.333708',1,14),(14,'2025-07-28 07:57:19.367731','2025-07-28 07:57:19.367731',2,15),(15,'2025-07-28 07:57:19.393925','2025-07-28 07:57:19.393925',7,16),(16,'2025-07-28 07:57:19.416479','2025-07-28 07:57:19.416479',12,17),(17,'2025-07-28 07:57:19.433554','2025-07-28 07:57:19.433554',13,18),(18,'2025-07-28 07:57:19.453922','2025-07-28 07:57:19.453922',18,19),(19,'2025-07-28 07:57:19.473698','2025-07-28 07:57:19.473698',19,20),(20,'2025-07-28 07:57:19.495677','2025-07-28 07:57:19.495677',20,21),(21,'2025-07-28 07:57:19.513620','2025-07-28 07:57:19.513620',22,22);
/*!40000 ALTER TABLE `cahiertexte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classe`
--

DROP TABLE IF EXISTS `classe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classe` (
  `id_classe` int NOT NULL AUTO_INCREMENT,
  `nom_licence` varchar(100) NOT NULL,
  `niveau` varchar(50) NOT NULL,
  `departement` varchar(100) NOT NULL,
  `mention` varchar(23) NOT NULL,
  PRIMARY KEY (`id_classe`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classe`
--

LOCK TABLES `classe` WRITE;
/*!40000 ALTER TABLE `classe` DISABLE KEYS */;
INSERT INTO `classe` VALUES (1,'GE_S6','Licence','GE','LF'),(2,'GC_S6','Licence','GC','LF'),(3,'GC_S2','Licence','GC','LP'),(4,'GE_S4','Licence','GE','LP'),(5,'GL_S2','Licence','GI','LP'),(6,'GE_S2','Licence','GE','LP'),(7,'TC_S4','Licence','TC','LF'),(8,'GM_S4','Licence','GM','LP'),(9,'GL_S4','Licence','GI','LP'),(10,'GC_S4','Licence','GC','LP'),(11,'GM_S2','Licence','GM','LP'),(12,'TC_S2','Licence','TC','LF'),(13,'IA_S4','Licence','GI','LF'),(14,'SR_S4','Licence','GI','LP'),(15,'GL_S6','Licence','GI','LP'),(16,'SR_S2','Licence','GI','LP'),(17,'SR_S6','Licence','GI','LP'),(18,'GM_S6','Licence','GM','LF'),(19,'IA_S','Licence','GI','LF'),(20,'IA_S6','Licence','GI','LF'),(22,'IS_S6','Licence','GI','LF');
/*!40000 ALTER TABLE `classe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_utilisateur_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_utilisateur_id` FOREIGN KEY (`user_id`) REFERENCES `utilisateur` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-07-27 19:39:20.903992','1','2GEL1625 - Utilisation de l’automate programmable- None',3,'',7,1),(2,'2025-07-27 20:21:08.338125','21','ctionnemen',3,'',1,1),(3,'2025-07-27 20:59:09.357961','5','GL_S2',2,'[]',1,1),(4,'2025-07-28 07:52:10.468758','114','test_secretaire_classe_0',3,'',2,1),(5,'2025-07-28 07:54:42.673488','1','SecretaireClasse object (1)',3,'',4,1),(6,'2025-07-28 07:56:19.345701','115','test_secretaire_classe_0',3,'',2,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (5,'accounts','cahiertexte'),(1,'accounts','classe'),(2,'accounts','customuser'),(9,'accounts','fichier_ue'),(3,'accounts','professeur'),(8,'accounts','seance'),(4,'accounts','secretaireclasse'),(6,'accounts','secretairegeneral'),(7,'accounts','ue'),(10,'accounts','validation'),(11,'admin','logentry'),(13,'auth','group'),(12,'auth','permission'),(14,'contenttypes','contenttype'),(15,'sessions','session'),(16,'token_blacklist','blacklistedtoken'),(17,'token_blacklist','outstandingtoken');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-07-27 19:36:50.230058'),(2,'contenttypes','0002_remove_content_type_name','2025-07-27 19:36:50.484324'),(3,'auth','0001_initial','2025-07-27 19:36:51.836600'),(4,'auth','0002_alter_permission_name_max_length','2025-07-27 19:36:52.018445'),(5,'auth','0003_alter_user_email_max_length','2025-07-27 19:36:52.041351'),(6,'auth','0004_alter_user_username_opts','2025-07-27 19:36:52.055424'),(7,'auth','0005_alter_user_last_login_null','2025-07-27 19:36:52.067954'),(8,'auth','0006_require_contenttypes_0002','2025-07-27 19:36:52.071956'),(9,'auth','0007_alter_validators_add_error_messages','2025-07-27 19:36:52.089342'),(10,'auth','0008_alter_user_username_max_length','2025-07-27 19:36:52.100881'),(11,'auth','0009_alter_user_last_name_max_length','2025-07-27 19:36:52.116060'),(12,'auth','0010_alter_group_name_max_length','2025-07-27 19:36:52.216903'),(13,'auth','0011_update_proxy_permissions','2025-07-27 19:36:52.232451'),(14,'auth','0012_alter_user_first_name_max_length','2025-07-27 19:36:52.260334'),(15,'accounts','0001_initial','2025-07-27 19:36:58.010870'),(16,'admin','0001_initial','2025-07-27 19:36:58.416344'),(17,'admin','0002_logentry_remove_auto_add','2025-07-27 19:36:58.434512'),(18,'admin','0003_logentry_add_action_flag_choices','2025-07-27 19:36:58.456968'),(19,'sessions','0001_initial','2025-07-27 19:36:58.523995'),(20,'token_blacklist','0001_initial','2025-07-27 19:36:58.924378'),(21,'token_blacklist','0002_outstandingtoken_jti_hex','2025-07-27 19:36:59.097300'),(22,'token_blacklist','0003_auto_20171017_2007','2025-07-27 19:36:59.140335'),(23,'token_blacklist','0004_auto_20171017_2013','2025-07-27 19:36:59.306315'),(24,'token_blacklist','0005_remove_outstandingtoken_jti','2025-07-27 19:36:59.448115'),(25,'token_blacklist','0006_auto_20171017_2113','2025-07-27 19:36:59.503875'),(26,'token_blacklist','0007_auto_20171017_2214','2025-07-27 19:36:59.948800'),(27,'token_blacklist','0008_migrate_to_bigautofield','2025-07-27 19:37:00.714498'),(28,'token_blacklist','0010_fix_migrate_to_bigautofield','2025-07-27 19:37:00.763300'),(29,'token_blacklist','0011_linearizes_history','2025-07-27 19:37:00.765835'),(30,'token_blacklist','0012_alter_outstandingtoken_user','2025-07-27 19:37:00.802251');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('hdalelz4kh0m0z0u1bfdfwy2oitqx0xx','.eJxVjDsOwjAQBe_iGln-b0xJzxkse3eDA8iR4qRC3B0ipYD2zcx7iZS3taat85ImEmehxel3Kxkf3HZA99xus8S5rctU5K7Ig3Z5nYmfl8P9O6i5129tPDrrPJCBkUxgYrLagUZwTsWCaIN2zEOxo-IBvAZlsXBkH03IIYv3B9VQN6c:1ugGjj:4E1xjEEqfSUB71N1tWVUq6NxFmIIXrgE5ybZZidkUdw','2025-08-11 05:49:23.960180'),('twxqm7hla470konxkay0jn0o7v5qg3yn','.eJxVjDsOwjAQBe_iGln-b0xJzxkse3eDA8iR4qRC3B0ipYD2zcx7iZS3taat85ImEmehxel3Kxkf3HZA99xus8S5rctU5K7Ig3Z5nYmfl8P9O6i5129tPDrrPJCBkUxgYrLagUZwTsWCaIN2zEOxo-IBvAZlsXBkH03IIYv3B9VQN6c:1ugGlU:DAEr0QIgLiEVXw1zqzl63pgO7vmMAVrJlORBOytnEmE','2025-08-11 05:51:12.894229');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fichiers_ue`
--

DROP TABLE IF EXISTS `fichiers_ue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fichiers_ue` (
  `id_Fichiers_Ue` int NOT NULL AUTO_INCREMENT,
  `lien_fichier` varchar(100) NOT NULL,
  `id_UEs` int NOT NULL,
  PRIMARY KEY (`id_Fichiers_Ue`),
  KEY `Fichiers_Ue_id_UEs_2934b9f7_fk_UEs_id_UEs` (`id_UEs`),
  CONSTRAINT `Fichiers_Ue_id_UEs_2934b9f7_fk_UEs_id_UEs` FOREIGN KEY (`id_UEs`) REFERENCES `ues` (`id_UEs`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fichiers_ue`
--

LOCK TABLES `fichiers_ue` WRITE;
/*!40000 ALTER TABLE `fichiers_ue` DISABLE KEYS */;
/*!40000 ALTER TABLE `fichiers_ue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professeur`
--

DROP TABLE IF EXISTS `professeur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `professeur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `signature` varchar(100) DEFAULT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id_id` (`user_id_id`),
  CONSTRAINT `professeur_user_id_id_685e7555_fk_utilisateur_id` FOREIGN KEY (`user_id_id`) REFERENCES `utilisateur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professeur`
--

LOCK TABLES `professeur` WRITE;
/*!40000 ALTER TABLE `professeur` DISABLE KEYS */;
INSERT INTO `professeur` VALUES (1,'',2),(2,'',3),(3,'',4),(4,'',5),(5,'',6),(6,'',7),(7,'',8),(8,'',9),(9,'',10),(10,'',11),(11,'',12),(12,'',13),(13,'',14),(14,'',15),(15,'',16),(16,'',17),(17,'',18),(18,'',19),(19,'',20),(20,'',21),(21,'',22),(22,'',23),(23,'',24),(24,'',25),(25,'',26),(26,'',27),(27,'',28),(28,'',29),(29,'',30),(30,'',31),(31,'',32),(32,'',33),(33,'',34),(34,'',35),(35,'',36),(36,'',37),(37,'',38),(38,'',39),(39,'',40),(40,'',41),(41,'',42),(42,'',43),(43,'',44),(44,'',45),(45,'',46),(46,'',47),(47,'',48),(48,'',49),(49,'',50),(50,'',51),(51,'',52),(52,'',53),(53,'',54),(54,'',55),(55,'',56),(56,'',57),(57,'',58),(58,'',59),(59,'',60),(60,'',61),(61,'',62),(62,'',63),(63,'',64),(64,'',65),(65,'',66),(66,'',67),(67,'',68),(68,'',69),(69,'',70),(70,'',71),(71,'',72),(72,'',73),(73,'',74),(74,'',75),(75,'',76),(76,'',77),(77,'',78),(78,'',79),(79,'',80),(80,'',81),(81,'',82),(82,'',83),(83,'',84),(84,'',85),(85,'',86),(86,'',87),(87,'',88),(88,'',89),(89,'',90),(90,'',91),(91,'',92),(92,'',93),(93,'',94),(94,'',95),(95,'',96),(96,'',97),(97,'',98),(98,'',99),(99,'',100),(100,'',101),(101,'',102),(102,'',103),(103,'',104),(104,'',105),(105,'',106),(106,'',107),(107,'',108),(108,'',109),(109,'',110),(110,'',111),(111,'',112),(112,'',113);
/*!40000 ALTER TABLE `professeur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seance`
--

DROP TABLE IF EXISTS `seance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seance` (
  `id_seance` int NOT NULL AUTO_INCREMENT,
  `sous_session_seance` varchar(1000) NOT NULL,
  `date_heure` datetime(6) NOT NULL,
  `id_classe` int DEFAULT NULL,
  `id_professeur` bigint DEFAULT NULL,
  `id_UEs` int NOT NULL,
  PRIMARY KEY (`id_seance`),
  KEY `seance_id_classe_78366382_fk_classe_id_classe` (`id_classe`),
  KEY `seance_id_professeur_98b9fe6d_fk_professeur_id` (`id_professeur`),
  KEY `seance_id_UEs_5c578ed4_fk_UEs_id_UEs` (`id_UEs`),
  KEY `seance_date_heure_a87c18be` (`date_heure`),
  CONSTRAINT `seance_id_classe_78366382_fk_classe_id_classe` FOREIGN KEY (`id_classe`) REFERENCES `classe` (`id_classe`),
  CONSTRAINT `seance_id_professeur_98b9fe6d_fk_professeur_id` FOREIGN KEY (`id_professeur`) REFERENCES `professeur` (`id`),
  CONSTRAINT `seance_id_UEs_5c578ed4_fk_UEs_id_UEs` FOREIGN KEY (`id_UEs`) REFERENCES `ues` (`id_UEs`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seance`
--

LOCK TABLES `seance` WRITE;
/*!40000 ALTER TABLE `seance` DISABLE KEYS */;
/*!40000 ALTER TABLE `seance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `secretaireclasse`
--

DROP TABLE IF EXISTS `secretaireclasse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `secretaireclasse` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `id_classe` int DEFAULT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id_id` (`user_id_id`),
  KEY `secretaireclasse_id_classe_d602df8e_fk_classe_id_classe` (`id_classe`),
  CONSTRAINT `secretaireclasse_id_classe_d602df8e_fk_classe_id_classe` FOREIGN KEY (`id_classe`) REFERENCES `classe` (`id_classe`),
  CONSTRAINT `secretaireclasse_user_id_id_ae75c859_fk_utilisateur_id` FOREIGN KEY (`user_id_id`) REFERENCES `utilisateur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `secretaireclasse`
--

LOCK TABLES `secretaireclasse` WRITE;
/*!40000 ALTER TABLE `secretaireclasse` DISABLE KEYS */;
INSERT INTO `secretaireclasse` VALUES (2,3,117),(3,4,118),(4,5,119),(5,6,120),(6,8,121),(7,9,122),(8,10,123),(9,11,124),(10,14,125),(11,15,126),(12,16,127),(13,17,128),(14,1,129),(15,2,130),(16,7,131),(17,12,132),(18,13,133),(19,18,134),(20,19,135),(21,20,136),(22,22,137);
/*!40000 ALTER TABLE `secretaireclasse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `secretairegeneral`
--

DROP TABLE IF EXISTS `secretairegeneral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `secretairegeneral` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `departement` varchar(100) NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id_id` (`user_id_id`),
  CONSTRAINT `secretairegeneral_user_id_id_0792a987_fk_utilisateur_id` FOREIGN KEY (`user_id_id`) REFERENCES `utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `secretairegeneral`
--

LOCK TABLES `secretairegeneral` WRITE;
/*!40000 ALTER TABLE `secretairegeneral` DISABLE KEYS */;
/*!40000 ALTER TABLE `secretairegeneral` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_blacklistedtoken`
--

DROP TABLE IF EXISTS `token_blacklist_blacklistedtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_blacklistedtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_id` (`token_id`),
  CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_blacklistedtoken`
--

LOCK TABLES `token_blacklist_blacklistedtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_outstandingtoken`
--

DROP TABLE IF EXISTS `token_blacklist_outstandingtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_outstandingtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `jti` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq` (`jti`),
  KEY `token_blacklist_outs_user_id_83bc629a_fk_utilisate` (`user_id`),
  CONSTRAINT `token_blacklist_outs_user_id_83bc629a_fk_utilisate` FOREIGN KEY (`user_id`) REFERENCES `utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_outstandingtoken`
--

LOCK TABLES `token_blacklist_outstandingtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ues`
--

DROP TABLE IF EXISTS `ues`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ues` (
  `id_UEs` int NOT NULL AUTO_INCREMENT,
  `code_UEs` varchar(50) NOT NULL,
  `intitule_UEs` varchar(255) NOT NULL,
  `crenaux` json NOT NULL,
  `classe_id` int DEFAULT NULL,
  `id_prof` bigint DEFAULT NULL,
  PRIMARY KEY (`id_UEs`),
  UNIQUE KEY `code_UEs` (`code_UEs`),
  KEY `UEs_classe_id_dca815b8_fk_classe_id_classe` (`classe_id`),
  KEY `UEs_id_prof_819a95d2_fk_professeur_id` (`id_prof`),
  CONSTRAINT `UEs_classe_id_dca815b8_fk_classe_id_classe` FOREIGN KEY (`classe_id`) REFERENCES `classe` (`id_classe`),
  CONSTRAINT `UEs_id_prof_819a95d2_fk_professeur_id` FOREIGN KEY (`id_prof`) REFERENCES `professeur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ues`
--

LOCK TABLES `ues` WRITE;
/*!40000 ALTER TABLE `ues` DISABLE KEYS */;
INSERT INTO `ues` VALUES (2,'2GEL1625','Utilisation de l’automate programmable','[{\"Lundi\": \"7H-9H\"}]',1,1),(3,'2GEC1621','Justification des sections des ouvrages','[{\"Lundi\": \"7H-9H\"}]',2,2),(4,'1GEC1225','Introduction aux propriétés physiques et mécaniques des sol','[{\"Lundi\": \"7H-9H\"}]',3,3),(5,'MGT1420','Initiation à la vie Professionnelle','[{\"Lundi\": \"7H-9H\"}]',4,4),(6,'MTH1222/MTH1220','Structure Algébrique de base','[{\"Lundi\": \"7H-9H\"}]',5,5),(7,'ANG1220','Anglais : Lire et Ecrire','[{\"Lundi\": \"7H-9H\"}]',6,6),(8,'MTH1421','Statistiques inférentielles (décisionnelles)','[{\"Lundi\": \"7H-9H\"}]',7,7),(9,'INF1427','Informatique Industrielle : Mise en œuvre des microprocesseurs','[{\"Lundi\": \"7H-9H\"}]',4,8),(10,'GEM1428','Fabrication mécanique et procédés de montage','[{\"Lundi\": \"7H-9H\"}]',8,9),(11,'INF1426','Introduction à l’algorithme, à la Programmation et aux bases de Données','[{\"Lundi\": \"7H-9H\"}]',4,27),(12,'MTH1224','Calcul intégral et Applications','[{\"Lundi\": \"7H-9H\"}]',5,11),(13,'ANG1420','Anglais de spécialité : Approche thématique des textes, compréhension orale et écrite','[{\"Lundi\": \"7H-9H\"}]',7,12),(14,'1GEC1427','Conception géométrique','[{\"Lundi\": \"7H-9H\"}]',10,13),(15,'2GEL1221','Circuits Logiques Séquentiels','[{\"Lundi\": \"7H-9H\"}]',16,101),(16,'GEM1222','Construction mécanique : organes de transmission de mouvement','[{\"Lundi\": \"7H-9H\"}]',11,15),(17,'1MTH1121','Calcul différentiel dans IR','[{\"Lundi\": \"7H-9H\"}]',12,16),(18,'1GEL1221','Circuits Logiques combinatoires','[{\"Lundi\": \"7H-9H\"}]',5,80),(19,'GEM1223','Bureau des méthodes','[{\"Lundi\": \"7H-9H\"}]',11,18),(20,'INF1429','Normes documentaires','[{\"Lundi\": \"7H-9H\"}]',9,19),(21,'INF1428','Modélisation  UML','[{\"Lundi\": \"7H-9H\"}]',9,92),(22,'2GEC1422','Résistance des Matériaux pour GC','[{\"Lundi\": \"7H-9H\"}]',10,21),(23,'GEM1420','Organisation et méthodes de la maintenance','[{\"Lundi\": \"7H-9H\"}]',8,107),(24,'INF1225','Généralités sur les Réseaux','[{\"Lundi\": \"7H-9H\"}]',5,23),(25,'1INF1422','Généralités sur les réseaux Informatiques','[{\"Lundi\": \"7H-9H\"}]',14,24),(26,'INF1221','Programmation Python','[{\"Lundi\": \"7H-9H\"}]',12,25),(27,'2GEC1458','Elements de contrôle de chantier','[{\"Lundi\": \"7H-9H\"}]',10,26),(28,'INF1220','Eléments mathématiques sur les bases de données','[{\"Lundi\": \"7H-9H\"}]',5,65),(29,'1GEC1425','Thermique du bâtiment','[{\"Lundi\": \"7H-9H\"}]',10,29),(30,'INF1627','Initiation à l’ingénierie des Systèmes d’Information','[{\"Lundi\": \"7H-9H\"}]',15,30),(31,'1INF1223','Architecture Matérielle','[{\"Lundi\": \"7H-9H\"}]',16,31),(32,'MTH1420','Calcul différentiel dans Rn','[{\"Lundi\": \"7H-9H\"}]',7,32),(33,'GEL1428','Introduction à l’Electronique de Puissance','[{\"Lundi\": \"7H-9H\"}]',4,33),(34,'1GEM1220','Essai des mécanismes','[{\"Lundi\": \"7H-9H\"}]',11,79),(35,'2GEL1421','Commande des Machines par la Pratique','[{\"Lundi\": \"7H-9H\"}]',4,35),(36,'GEM1421','Asservissement et régulation','[{\"Lundi\": \"7H-9H\"}]',8,36),(37,'1INF1621/INF1628','Administration des réseaux Informatiques','[{\"Lundi\": \"7H-9H\"}]',17,37),(38,'FRA1220','Français : Lire et Ecrire','[{\"Lundi\": \"7H-9H\"}]',6,39),(39,'GEL1629','Traitement du Signal','[{\"Lundi\": \"7H-9H\"}]',1,40),(40,'GEM1622','Maintenance industrielle','[{\"Lundi\": \"7H-9H\"}]',18,41),(41,'1GEC1622','Hydrologie de Bases','[{\"Lundi\": \"7H-9H\"}]',2,42),(42,'1INF1220/INF1225','Informatique de base pour technicien supérieur (*)','[{\"Lundi\": \"7H-9H\"}]',3,43),(43,'INF1425','Généralités sur la sécurité informatique','[{\"Lundi\": \"7H-9H\"}]',9,44),(44,'1INF1620','Généralités sur la Sécurité Informatique','[{\"Lundi\": \"7H-9H\"}]',17,45),(45,'PHY1220','Mécanique du solide','[{\"Lundi\": \"7H-9H\"}]',12,46),(46,'1GEC1458','Organisation et planification de chantier','[{\"Lundi\": \"7H-9H\"}]',10,47),(47,'GEL1422','Electromagnétisme','[{\"Lundi\": \"7H-9H\"}]',8,55),(48,'2INF1226','Programmation web statique','[{\"Lundi\": \"7H-9H\"}]',5,49),(49,'DRT1420','Droit de l’Informatique','[{\"Lundi\": \"7H-9H\"}]',9,53),(50,'GEL1421','Réseaux','[{\"Lundi\": \"7H-9H\"}]',8,51),(51,'GEL1620','Asservissement et Régulation des Systèmes Linéaire','[{\"Lundi\": \"7H-9H\"}]',1,52),(52,'GEL1429','Installations électriques (H)','[{\"Lundi\": \"7H-9H\"}]',10,54),(53,'INF1621','Administration Système Linux','[{\"Lundi\": \"7H-9H\"}]',19,56),(54,'1GEL1622','Electrostatique et Electrocinétique','[{\"Lundi\": \"7H-9H\"}]',1,57),(55,'1GEM1221','outils','[{\"Lundi\": \"7H-9H\"}]',11,58),(56,'1GEL1420','Bases de l\'électronique','[{\"Lundi\": \"7H-9H\"}]',4,59),(57,'GEL1420','Introduction à l\'électronique et montage des circuits électroniques','[{\"Lundi\": \"7H-9H\"}]',8,60),(58,'GEM1422','Métallurgie et essai des matériaux','[{\"Lundi\": \"7H-9H\"}]',8,61),(59,'1INF1226','Programmation C','[{\"Lundi\": \"7H-9H\"}]',5,62),(60,'ANG1221','Anglais : compréhension orale et écrite','[{\"Lundi\": \"7H-9H\"}]',12,63),(61,'ANG1420/ANG1421','Anglais de Spécialité : Approche thématique des textes','[{\"Lundi\": \"7H-9H\"}]',4,64),(62,'1INF1420','Généralités sur les stockages de l\'information','[{\"Lundi\": \"7H-9H\"}]',14,66),(63,'GEL1423','Physique des Capteurs : Notions fondamentales','[{\"Lundi\": \"7H-9H\"}]',8,67),(64,'1GEC1621','Béton armé : Calcul des sollicitations','[{\"Lundi\": \"7H-9H\"}]',2,68),(65,'PHY1227','Mécanique Appliquée au Solide','[{\"Lundi\": \"7H-9H\"}]',6,69),(66,'1MTH1422','Analyse numérique','[{\"Lundi\": \"7H-9H\"}]',7,70),(67,'2GEC1424','Justification des sections','[{\"Lundi\": \"7H-9H\"}]',10,71),(68,'1GEL1421','Introduction à l’Asservissement et Régulation','[{\"Lundi\": \"7H-9H\"}]',4,72),(69,'GEM1429','Construction mécanique : organes de transmission de puissance','[{\"Lundi\": \"7H-9H\"}]',8,73),(70,'GEC1423','Hydraulique des bases','[{\"Lundi\": \"7H-9H\"}]',10,74),(71,'1GEM1621','Etude de fabrication assistée par ordinateur','[{\"Lundi\": \"7H-9H\"}]',18,75),(72,'2INF1620','Sécurité des réseaux informatiques','[{\"Lundi\": \"7H-9H\"}]',17,76),(73,'MTH1423','Théorie des graphes','[{\"Lundi\": \"7H-9H\"}]',7,77),(74,'1GEC1424','Introduction aux calculs de sollicitations','[{\"Lundi\": \"7H-9H\"}]',10,78),(75,'INF1622','Programmation distribuée pour le stockage et le calcul','[{\"Lundi\": \"7H-9H\"}]',20,81),(76,'1GEL1625','Automate Programmable Industriel (API)','[{\"Lundi\": \"7H-9H\"}]',1,82),(77,'1INF1423','Administration Système Linux','[{\"Lundi\": \"7H-9H\"}]',9,83),(78,'1GEL1623','Machines Electriques : Constitution et Principe de','[{\"Lundi\": \"7H-9H\"}]',NULL,84),(79,'GEC1624','Construction métallique : notions de bases et technologie','[{\"Lundi\": \"7H-9H\"}]',2,85),(80,'1GEC1226','Matériaux de construction des ouvrages de génie civil','[{\"Lundi\": \"7H-9H\"}]',3,86),(81,'PHY1225','Introduction à la Physique des capteurs','[{\"Lundi\": \"7H-9H\"}]',6,87),(82,'GEL1627','Electroniques : Fonctions et Systèmes','[{\"Lundi\": \"7H-9H\"}]',1,88),(83,'GEM1626','Thermodynamique avancée','[{\"Lundi\": \"7H-9H\"}]',18,89),(84,'1GEC1620','Routes : Conception Géométrique','[{\"Lundi\": \"7H-9H\"}]',2,90),(85,'2INF1220/2INF1225/INF1226','Introduction à la programmation','[{\"Lundi\": \"7H-9H\"}]',11,91),(86,'MTH1620','Statistiques exploratoires multidimensionnelles','[{\"Lundi\": \"7H-9H\"}]',20,93),(87,'INF1625','Développement d\'applications distribuées','[{\"Lundi\": \"7H-9H\"}]',22,94),(88,'GEM1624','Montage d\'usinage','[{\"Lundi\": \"7H-9H\"}]',18,95),(89,'MTH1225/MTH1220','Eléments d\'Analyse Mathématique','[{\"Lundi\": \"7H-9H\"}]',6,96),(90,'CPT1420','Comptabilité Générale de base','[{\"Lundi\": \"7H-9H\"}]',9,97),(91,'INF1623','Initiation à l\'ingénierie des Systèmes d\'Information','[{\"Lundi\": \"7H-9H\"}]',22,98),(92,'2GEC1427','Structure de chaussée, matériaux et entretien','[{\"Lundi\": \"7H-9H\"}]',10,99),(93,'GEL1425','Maintenance des Appareils Audio Visuels (MAAV)','[{\"Lundi\": \"7H-9H\"}]',4,100),(94,'ANG1620','Anglais','[{\"Lundi\": \"7H-9H\"}]',20,102),(95,'2GEL1622','Electromagnétisme','[{\"Lundi\": \"7H-9H\"}]',1,103),(96,'INF1624','Développement d\'applications de bureau','[{\"Lundi\": \"7H-9H\"}]',22,104),(97,'1GEL1626','Convertisseurs statiques','[{\"Lundi\": \"7H-9H\"}]',1,105),(98,'2GEC1625','Assainissement : notions de bases et technologie','[{\"Lundi\": \"7H-9H\"}]',2,106),(99,'MTH1621','Data Mining','[{\"Lundi\": \"7H-9H\"}]',20,108),(100,'GEL1624','Système de Maintenance','[{\"Lundi\": \"7H-9H\"}]',1,109),(101,'1GEM1627','Fabrication mécanique : Tournage et Fraisage','[{\"Lundi\": \"7H-9H\"}]',18,110),(102,'INF1620','Administration de bases de données','[{\"Lundi\": \"7H-9H\"}]',19,111),(103,'GEM1620','Métallurgie','[{\"Lundi\": \"7H-9H\"}]',18,112);
/*!40000 ALTER TABLE `ues` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `utilisateur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) NOT NULL,
  `nom` varchar(150) NOT NULL,
  `prenom` varchar(150) NOT NULL,
  `role` varchar(23) NOT NULL,
  `auth_provider` varchar(10) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `utilisateur_role_9fed923e` (`role`),
  KEY `utilisateur_is_active_721a8669` (`is_active`),
  KEY `utilisateur_is_staff_9f5ecf5b` (`is_staff`),
  KEY `utilisateur_is_verified_e35ac157` (`is_verified`)
) ENGINE=InnoDB AUTO_INCREMENT=138 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilisateur`
--

LOCK TABLES `utilisateur` WRITE;
/*!40000 ALTER TABLE `utilisateur` DISABLE KEYS */;
INSERT INTO `utilisateur` VALUES (1,'pbkdf2_sha256$870000$aBCq7tL0eJeIzJrv64oFyW$r9FziUnf5XlcsgBobZafF7cRNjEIgGMfakVRk2tuYoA=','2025-07-28 05:51:12.889246',1,'r@gmail.com','','','admin','email',1,1,1),(2,'123456',NULL,0,'text_email_0@gmail.com','GNAGLIGA','Unkown','professeur','email',1,0,1),(3,'123456',NULL,0,'text_email_1@gmail.com','AYITE','Unkown','professeur','email',1,0,1),(4,'123456',NULL,0,'text_email_2@gmail.com','BANAKINAO','Unkown','professeur','email',1,0,1),(5,'123456',NULL,0,'text_email_3@gmail.com','SABOUTOU','Unkown','professeur','email',1,0,1),(6,'123456',NULL,0,'text_email_4@gmail.com','MAGNANI','Unkown','professeur','email',1,0,1),(7,'123456',NULL,0,'text_email_5@gmail.com','MIHAM','Unkown','professeur','email',1,0,1),(8,'123456',NULL,0,'text_email_6@gmail.com','DAKITSE-BENISSAN','Unkown','professeur','email',1,0,1),(9,'123456',NULL,0,'text_email_7@gmail.com','KODJO','Unkown','professeur','email',1,0,1),(10,'123456',NULL,0,'text_email_8@gmail.com','AGBETOSSOU','Unkown','professeur','email',1,0,1),(11,'123456',NULL,0,'text_email_9@gmail.com','HOETOWOU','Unkown','professeur','email',1,0,1),(12,'123456',NULL,0,'text_email_10@gmail.com','TCHALLA','Unkown','professeur','email',1,0,1),(13,'123456',NULL,0,'text_email_11@gmail.com','TCHIOU','Unkown','professeur','email',1,0,1),(14,'123456',NULL,0,'text_email_12@gmail.com','KOUTO','Unkown','professeur','email',1,0,1),(15,'123456',NULL,0,'text_email_13@gmail.com','ADJAMAGBO','Unkown','professeur','email',1,0,1),(16,'123456',NULL,0,'text_email_14@gmail.com','DROVOU','Unkown','professeur','email',1,0,1),(17,'123456',NULL,0,'text_email_15@gmail.com','GERALDO','Unkown','professeur','email',1,0,1),(18,'123456',NULL,0,'text_email_16@gmail.com','AGBESSI','Unkown','professeur','email',1,0,1),(19,'123456',NULL,0,'text_email_17@gmail.com','AGBETOSSOU','Unkown','professeur','email',1,0,1),(20,'123456',NULL,0,'text_email_18@gmail.com','ANAKPA','Unkown','professeur','email',1,0,1),(21,'123456',NULL,0,'text_email_19@gmail.com','KPEGOUNI','Unkown','professeur','email',1,0,1),(22,'123456',NULL,0,'text_email_20@gmail.com','AYITE','Unkown','professeur','email',1,0,1),(23,'123456',NULL,0,'text_email_21@gmail.com','AFIO','Unkown','professeur','email',1,0,1),(24,'123456',NULL,0,'text_email_22@gmail.com','KPEGOUNI','Unkown','professeur','email',1,0,1),(25,'123456',NULL,0,'text_email_23@gmail.com','KPEGOUNI','Unkown','professeur','email',1,0,1),(26,'123456',NULL,0,'text_email_24@gmail.com','AMOUZOU','Unkown','professeur','email',1,0,1),(27,'123456',NULL,0,'text_email_25@gmail.com','AMOUDJI','Unkown','professeur','email',1,0,1),(28,'123456',NULL,0,'text_email_26@gmail.com','APALOO-BARA','Unkown','professeur','email',1,0,1),(29,'123456',NULL,0,'text_email_27@gmail.com','AMOUZOU','Unkown','professeur','email',1,0,1),(30,'123456',NULL,0,'text_email_28@gmail.com','SAMAH','Unkown','professeur','email',1,0,1),(31,'123456',NULL,0,'text_email_29@gmail.com','BATAZI','Unkown','professeur','email',1,0,1),(32,'123456',NULL,0,'text_email_30@gmail.com','TOSSOU AUDE','Unkown','professeur','email',1,0,1),(33,'123456',NULL,0,'text_email_31@gmail.com','LAKMON','Unkown','professeur','email',1,0,1),(34,'123456',NULL,0,'text_email_32@gmail.com','AGBOSSOU','Unkown','professeur','email',1,0,1),(35,'123456',NULL,0,'text_email_33@gmail.com','LIMAZIE','Unkown','professeur','email',1,0,1),(36,'123456',NULL,0,'text_email_34@gmail.com','ADJAMAGBO','Unkown','professeur','email',1,0,1),(37,'123456',NULL,0,'text_email_35@gmail.com','GOGOLI','Unkown','professeur','email',1,0,1),(38,'123456',NULL,0,'text_email_36@gmail.com','TEPE','Unkown','professeur','email',1,0,1),(39,'123456',NULL,0,'text_email_37@gmail.com','KALIPE','Unkown','professeur','email',1,0,1),(40,'123456',NULL,0,'text_email_38@gmail.com','KALIPE','Unkown','professeur','email',1,0,1),(41,'123456',NULL,0,'text_email_39@gmail.com','BOKOVI','Unkown','professeur','email',1,0,1),(42,'123456',NULL,0,'text_email_40@gmail.com','WOTODZO','Unkown','professeur','email',1,0,1),(43,'123456',NULL,0,'text_email_41@gmail.com','IDRISSOU','Unkown','professeur','email',1,0,1),(44,'123456',NULL,0,'text_email_42@gmail.com','AGBESSI','Unkown','professeur','email',1,0,1),(45,'123456',NULL,0,'text_email_43@gmail.com','BARATE','Unkown','professeur','email',1,0,1),(46,'123456',NULL,0,'text_email_44@gmail.com','BARATE','Unkown','professeur','email',1,0,1),(47,'123456',NULL,0,'text_email_45@gmail.com','AYELEH','Unkown','professeur','email',1,0,1),(48,'123456',NULL,0,'text_email_46@gmail.com','KOUTO','Unkown','professeur','email',1,0,1),(49,'123456',NULL,0,'text_email_47@gmail.com','KODJO','Unkown','professeur','email',1,0,1),(50,'123456',NULL,0,'text_email_48@gmail.com','ATADEGNON','Unkown','professeur','email',1,0,1),(51,'123456',NULL,0,'text_email_49@gmail.com','KUAGBENU','Unkown','professeur','email',1,0,1),(52,'123456',NULL,0,'text_email_50@gmail.com','MOUZOU','Unkown','professeur','email',1,0,1),(53,'123456',NULL,0,'text_email_51@gmail.com','KODJO','Unkown','professeur','email',1,0,1),(54,'123456',NULL,0,'text_email_52@gmail.com','KUAGBENU','Unkown','professeur','email',1,0,1),(55,'123456',NULL,0,'text_email_53@gmail.com','GUENOUKPATI','Unkown','professeur','email',1,0,1),(56,'123456',NULL,0,'text_email_54@gmail.com','MOUZOU','Unkown','professeur','email',1,0,1),(57,'123456',NULL,0,'text_email_55@gmail.com','MESSI','Unkown','professeur','email',1,0,1),(58,'123456',NULL,0,'text_email_56@gmail.com','AGBESSI','Unkown','professeur','email',1,0,1),(59,'123456',NULL,0,'text_email_57@gmail.com','AGBETOSSOU','Unkown','professeur','email',1,0,1),(60,'123456',NULL,0,'text_email_58@gmail.com','KPOGLI','Unkown','professeur','email',1,0,1),(61,'123456',NULL,0,'text_email_59@gmail.com','AKORO','Unkown','professeur','email',1,0,1),(62,'123456',NULL,0,'text_email_60@gmail.com','MOUZOU','Unkown','professeur','email',1,0,1),(63,'123456',NULL,0,'text_email_61@gmail.com','AKAKPO','Unkown','professeur','email',1,0,1),(64,'123456',NULL,0,'text_email_62@gmail.com','TCHIOU','Unkown','professeur','email',1,0,1),(65,'123456',NULL,0,'text_email_63@gmail.com','AGOUZE','Unkown','professeur','email',1,0,1),(66,'123456',NULL,0,'text_email_64@gmail.com','DAMALI','Unkown','professeur','email',1,0,1),(67,'123456',NULL,0,'text_email_65@gmail.com','AGBOSSE','Unkown','professeur','email',1,0,1),(68,'123456',NULL,0,'text_email_66@gmail.com','GUENOUKPATI','Unkown','professeur','email',1,0,1),(69,'123456',NULL,0,'text_email_67@gmail.com','AYITE','Unkown','professeur','email',1,0,1),(70,'123456',NULL,0,'text_email_68@gmail.com','ATTIPOU','Unkown','professeur','email',1,0,1),(71,'123456',NULL,0,'text_email_69@gmail.com','AYELEH','Unkown','professeur','email',1,0,1),(72,'123456',NULL,0,'text_email_70@gmail.com','AMEY','Unkown','professeur','email',1,0,1),(73,'123456',NULL,0,'text_email_71@gmail.com','GUENOUKPATI','Unkown','professeur','email',1,0,1),(74,'123456',NULL,0,'text_email_72@gmail.com','DROVOU','Unkown','professeur','email',1,0,1),(75,'123456',NULL,0,'text_email_73@gmail.com','IDRISSOU','Unkown','professeur','email',1,0,1),(76,'123456',NULL,0,'text_email_74@gmail.com','WOTODZO','Unkown','professeur','email',1,0,1),(77,'123456',NULL,0,'text_email_75@gmail.com','ADJONYO','Unkown','professeur','email',1,0,1),(78,'123456',NULL,0,'text_email_76@gmail.com','AGOSSEME','Unkown','professeur','email',1,0,1),(79,'123456',NULL,0,'text_email_77@gmail.com','AMEY','Unkown','professeur','email',1,0,1),(80,'123456',NULL,0,'text_email_78@gmail.com','DROVOU','Unkown','professeur','email',1,0,1),(81,'123456',NULL,0,'text_email_79@gmail.com','ASSIDENU','Unkown','professeur','email',1,0,1),(82,'123456',NULL,0,'text_email_80@gmail.com','TIASSOU','Unkown','professeur','email',1,0,1),(83,'123456',NULL,0,'text_email_81@gmail.com','DITONA','Unkown','professeur','email',1,0,1),(84,'123456',NULL,0,'text_email_82@gmail.com','TEPE','Unkown','professeur','email',1,0,1),(85,'123456',NULL,0,'text_email_83@gmail.com','(LF GE S6)','Unkown','professeur','email',1,0,1),(86,'123456',NULL,0,'text_email_84@gmail.com','AMEY','Unkown','professeur','email',1,0,1),(87,'123456',NULL,0,'text_email_85@gmail.com','BANAKINAO','Unkown','professeur','email',1,0,1),(88,'123456',NULL,0,'text_email_86@gmail.com','GUENOUKPATI','Unkown','professeur','email',1,0,1),(89,'123456',NULL,0,'text_email_87@gmail.com','ADJALLAH','Unkown','professeur','email',1,0,1),(90,'123456',NULL,0,'text_email_88@gmail.com','AYELEH','Unkown','professeur','email',1,0,1),(91,'123456',NULL,0,'text_email_89@gmail.com','GBAFA','Unkown','professeur','email',1,0,1),(92,'123456',NULL,0,'text_email_90@gmail.com','AYELEH','Unkown','professeur','email',1,0,1),(93,'123456',NULL,0,'text_email_91@gmail.com','HOETOWOU','Unkown','professeur','email',1,0,1),(94,'123456',NULL,0,'text_email_92@gmail.com','TAMPANGO','Unkown','professeur','email',1,0,1),(95,'123456',NULL,0,'text_email_93@gmail.com','ABOLO-SEWOVI','Unkown','professeur','email',1,0,1),(96,'123456',NULL,0,'text_email_94@gmail.com','AGBETOSSOU','Unkown','professeur','email',1,0,1),(97,'123456',NULL,0,'text_email_95@gmail.com','TCHARIE','Unkown','professeur','email',1,0,1),(98,'123456',NULL,0,'text_email_96@gmail.com','LAWSON-BODY','Unkown','professeur','email',1,0,1),(99,'123456',NULL,0,'text_email_97@gmail.com','ZOMBLEOU','Unkown','professeur','email',1,0,1),(100,'123456',NULL,0,'text_email_98@gmail.com','BANAKINAO','Unkown','professeur','email',1,0,1),(101,'123456',NULL,0,'text_email_99@gmail.com','OTTOU','Unkown','professeur','email',1,0,1),(102,'123456',NULL,0,'text_email_100@gmail.com','ASSIDENU','Unkown','professeur','email',1,0,1),(103,'123456',NULL,0,'text_email_101@gmail.com','MIHAM','Unkown','professeur','email',1,0,1),(104,'123456',NULL,0,'text_email_102@gmail.com','GUENOUKPATI','Unkown','professeur','email',1,0,1),(105,'123456',NULL,0,'text_email_103@gmail.com','ZOMBLEOU','Unkown','professeur','email',1,0,1),(106,'123456',NULL,0,'text_email_104@gmail.com','AGBOSSOU','Unkown','professeur','email',1,0,1),(107,'123456',NULL,0,'text_email_105@gmail.com','GBAFA','Unkown','professeur','email',1,0,1),(108,'123456',NULL,0,'text_email_106@gmail.com','DROVOU','Unkown','professeur','email',1,0,1),(109,'123456',NULL,0,'text_email_107@gmail.com','AGBEMADON','Unkown','professeur','email',1,0,1),(110,'123456',NULL,0,'text_email_108@gmail.com','ADJALLAH','Unkown','professeur','email',1,0,1),(111,'123456',NULL,0,'text_email_109@gmail.com','AFIO','Unkown','professeur','email',1,0,1),(112,'123456',NULL,0,'text_email_110@gmail.com','ANAKPA','Unkown','professeur','email',1,0,1),(113,'123456',NULL,0,'text_email_111@gmail.com','MOUZOU','Unkown','professeur','email',1,0,1),(117,'test_secretaire1',NULL,0,'test_secretaire_classe_1','secretaire_classe1','Unkown','secretaire_classe','email',1,0,1),(118,'test_secretaire2',NULL,0,'test_secretaire_classe_2','secretaire_classe2','Unkown','secretaire_classe','email',1,0,1),(119,'test_secretaire3',NULL,0,'test_secretaire_classe_3','secretaire_classe3','Unkown','secretaire_classe','email',1,0,1),(120,'test_secretaire4',NULL,0,'test_secretaire_classe_4','secretaire_classe4','Unkown','secretaire_classe','email',1,0,1),(121,'test_secretaire5',NULL,0,'test_secretaire_classe_5','secretaire_classe5','Unkown','secretaire_classe','email',1,0,1),(122,'test_secretaire6',NULL,0,'test_secretaire_classe_6','secretaire_classe6','Unkown','secretaire_classe','email',1,0,1),(123,'test_secretaire7',NULL,0,'test_secretaire_classe_7','secretaire_classe7','Unkown','secretaire_classe','email',1,0,1),(124,'test_secretaire8',NULL,0,'test_secretaire_classe_8','secretaire_classe8','Unkown','secretaire_classe','email',1,0,1),(125,'test_secretaire9',NULL,0,'test_secretaire_classe_9','secretaire_classe9','Unkown','secretaire_classe','email',1,0,1),(126,'test_secretaire10',NULL,0,'test_secretaire_classe_10','secretaire_classe10','Unkown','secretaire_classe','email',1,0,1),(127,'test_secretaire11',NULL,0,'test_secretaire_classe_11','secretaire_classe11','Unkown','secretaire_classe','email',1,0,1),(128,'test_secretaire12',NULL,0,'test_secretaire_classe_12','secretaire_classe12','Unkown','secretaire_classe','email',1,0,1),(129,'test_secretaire13',NULL,0,'test_secretaire_classe_13','secretaire_classe13','Unkown','secretaire_classe','email',1,0,1),(130,'test_secretaire14',NULL,0,'test_secretaire_classe_14','secretaire_classe14','Unkown','secretaire_classe','email',1,0,1),(131,'test_secretaire15',NULL,0,'test_secretaire_classe_15','secretaire_classe15','Unkown','secretaire_classe','email',1,0,1),(132,'test_secretaire16',NULL,0,'test_secretaire_classe_16','secretaire_classe16','Unkown','secretaire_classe','email',1,0,1),(133,'test_secretaire17',NULL,0,'test_secretaire_classe_17','secretaire_classe17','Unkown','secretaire_classe','email',1,0,1),(134,'test_secretaire18',NULL,0,'test_secretaire_classe_18','secretaire_classe18','Unkown','secretaire_classe','email',1,0,1),(135,'test_secretaire19',NULL,0,'test_secretaire_classe_19','secretaire_classe19','Unkown','secretaire_classe','email',1,0,1),(136,'test_secretaire20',NULL,0,'test_secretaire_classe_20','secretaire_classe20','Unkown','secretaire_classe','email',1,0,1),(137,'test_secretaire21',NULL,0,'test_secretaire_classe_21','secretaire_classe21','Unkown','secretaire_classe','email',1,0,1);
/*!40000 ALTER TABLE `utilisateur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utilisateur_groups`
--

DROP TABLE IF EXISTS `utilisateur_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `utilisateur_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `utilisateur_groups_customuser_id_group_id_0d4fc31d_uniq` (`customuser_id`,`group_id`),
  KEY `utilisateur_groups_group_id_f333a17e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `utilisateur_groups_customuser_id_5bf3c374_fk_utilisateur_id` FOREIGN KEY (`customuser_id`) REFERENCES `utilisateur` (`id`),
  CONSTRAINT `utilisateur_groups_group_id_f333a17e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilisateur_groups`
--

LOCK TABLES `utilisateur_groups` WRITE;
/*!40000 ALTER TABLE `utilisateur_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `utilisateur_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utilisateur_user_permissions`
--

DROP TABLE IF EXISTS `utilisateur_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `utilisateur_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `utilisateur_user_permiss_customuser_id_permission_e2887981_uniq` (`customuser_id`,`permission_id`),
  KEY `utilisateur_user_per_permission_id_0616051c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `utilisateur_user_per_customuser_id_57e74459_fk_utilisate` FOREIGN KEY (`customuser_id`) REFERENCES `utilisateur` (`id`),
  CONSTRAINT `utilisateur_user_per_permission_id_0616051c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilisateur_user_permissions`
--

LOCK TABLES `utilisateur_user_permissions` WRITE;
/*!40000 ALTER TABLE `utilisateur_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `utilisateur_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `validation`
--

DROP TABLE IF EXISTS `validation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `validation` (
  `id_validation` int NOT NULL AUTO_INCREMENT,
  `statut` varchar(11) NOT NULL,
  `date_validation` datetime(6) NOT NULL,
  `id_cahier` int NOT NULL,
  `id_professeur` bigint NOT NULL,
  `id_seance` int NOT NULL,
  `id_UEs` int NOT NULL,
  PRIMARY KEY (`id_validation`),
  KEY `validation_id_cahier_15d84e01_fk_Cahiertexte_id_cahier` (`id_cahier`),
  KEY `validation_id_professeur_e18706fb_fk_professeur_id` (`id_professeur`),
  KEY `validation_id_seance_fed5b2d5_fk_seance_id_seance` (`id_seance`),
  KEY `validation_id_UEs_1f082b04_fk_UEs_id_UEs` (`id_UEs`),
  KEY `validation_statut_8c6ddc5b` (`statut`),
  CONSTRAINT `validation_id_cahier_15d84e01_fk_Cahiertexte_id_cahier` FOREIGN KEY (`id_cahier`) REFERENCES `cahiertexte` (`id_cahier`),
  CONSTRAINT `validation_id_professeur_e18706fb_fk_professeur_id` FOREIGN KEY (`id_professeur`) REFERENCES `professeur` (`id`),
  CONSTRAINT `validation_id_seance_fed5b2d5_fk_seance_id_seance` FOREIGN KEY (`id_seance`) REFERENCES `seance` (`id_seance`),
  CONSTRAINT `validation_id_UEs_1f082b04_fk_UEs_id_UEs` FOREIGN KEY (`id_UEs`) REFERENCES `ues` (`id_UEs`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `validation`
--

LOCK TABLES `validation` WRITE;
/*!40000 ALTER TABLE `validation` DISABLE KEYS */;
/*!40000 ALTER TABLE `validation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-28  8:07:02
