-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: gestion_stock_EPL
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
INSERT INTO `auth_permission` VALUES (1,'Can add classe',1,'add_classe'),(2,'Can change classe',1,'change_classe'),(3,'Can delete classe',1,'delete_classe'),(4,'Can view classe',1,'view_classe'),(5,'Can add Cahiertexte',2,'add_cahiertexte'),(6,'Can change Cahiertexte',2,'change_cahiertexte'),(7,'Can delete Cahiertexte',2,'delete_cahiertexte'),(8,'Can view Cahiertexte',2,'view_cahiertexte'),(9,'Can add seance',3,'add_seance'),(10,'Can change seance',3,'change_seance'),(11,'Can delete seance',3,'delete_seance'),(12,'Can view seance',3,'view_seance'),(13,'Can add validation',4,'add_validation'),(14,'Can change validation',4,'change_validation'),(15,'Can delete validation',4,'delete_validation'),(16,'Can view validation',4,'view_validation'),(17,'Can add custom user',5,'add_customuser'),(18,'Can change custom user',5,'change_customuser'),(19,'Can delete custom user',5,'delete_customuser'),(20,'Can view custom user',5,'view_customuser'),(21,'Can add professeur',6,'add_professeur'),(22,'Can change professeur',6,'change_professeur'),(23,'Can delete professeur',6,'delete_professeur'),(24,'Can view professeur',6,'view_professeur'),(25,'Can add secretaire classe',7,'add_secretaireclasse'),(26,'Can change secretaire classe',7,'change_secretaireclasse'),(27,'Can delete secretaire classe',7,'delete_secretaireclasse'),(28,'Can view secretaire classe',7,'view_secretaireclasse'),(29,'Can add secretaire general',8,'add_secretairegeneral'),(30,'Can change secretaire general',8,'change_secretairegeneral'),(31,'Can delete secretaire general',8,'delete_secretairegeneral'),(32,'Can view secretaire general',8,'view_secretairegeneral'),(33,'Can add log entry',9,'add_logentry'),(34,'Can change log entry',9,'change_logentry'),(35,'Can delete log entry',9,'delete_logentry'),(36,'Can view log entry',9,'view_logentry'),(37,'Can add permission',10,'add_permission'),(38,'Can change permission',10,'change_permission'),(39,'Can delete permission',10,'delete_permission'),(40,'Can view permission',10,'view_permission'),(41,'Can add group',11,'add_group'),(42,'Can change group',11,'change_group'),(43,'Can delete group',11,'delete_group'),(44,'Can view group',11,'view_group'),(45,'Can add content type',12,'add_contenttype'),(46,'Can change content type',12,'change_contenttype'),(47,'Can delete content type',12,'delete_contenttype'),(48,'Can view content type',12,'view_contenttype'),(49,'Can add session',13,'add_session'),(50,'Can change session',13,'change_session'),(51,'Can delete session',13,'delete_session'),(52,'Can view session',13,'view_session'),(53,'Can add ue',14,'add_ue'),(54,'Can change ue',14,'change_ue'),(55,'Can delete ue',14,'delete_ue'),(56,'Can view ue',14,'view_ue'),(57,'Can add fichier_ ue',15,'add_fichier_ue'),(58,'Can change fichier_ ue',15,'change_fichier_ue'),(59,'Can delete fichier_ ue',15,'delete_fichier_ue'),(60,'Can view fichier_ ue',15,'view_fichier_ue'),(61,'Can add blacklisted token',16,'add_blacklistedtoken'),(62,'Can change blacklisted token',16,'change_blacklistedtoken'),(63,'Can delete blacklisted token',16,'delete_blacklistedtoken'),(64,'Can view blacklisted token',16,'view_blacklistedtoken'),(65,'Can add outstanding token',17,'add_outstandingtoken'),(66,'Can change outstanding token',17,'change_outstandingtoken'),(67,'Can delete outstanding token',17,'delete_outstandingtoken'),(68,'Can view outstanding token',17,'view_outstandingtoken');
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
  `id_secretaire` bigint NOT NULL,
  `id_classe` int NOT NULL,
  PRIMARY KEY (`id_cahier`),
  KEY `Cahiertexte_id_secretaire_70133660_fk_secretaireclasse_id` (`id_secretaire`),
  KEY `Cahiertexte_id_classe_a1c5f806_fk_classe_id_classe` (`id_classe`),
  CONSTRAINT `Cahiertexte_id_classe_a1c5f806_fk_classe_id_classe` FOREIGN KEY (`id_classe`) REFERENCES `classe` (`id_classe`),
  CONSTRAINT `Cahiertexte_id_secretaire_70133660_fk_secretaireclasse_id` FOREIGN KEY (`id_secretaire`) REFERENCES `secretaireclasse` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cahiertexte`
--

LOCK TABLES `cahiertexte` WRITE;
/*!40000 ALTER TABLE `cahiertexte` DISABLE KEYS */;
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
  PRIMARY KEY (`id_classe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classe`
--

LOCK TABLES `classe` WRITE;
/*!40000 ALTER TABLE `classe` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
INSERT INTO `django_content_type` VALUES (5,'accounts','customuser'),(6,'accounts','professeur'),(7,'accounts','secretaireclasse'),(8,'accounts','secretairegeneral'),(9,'admin','logentry'),(11,'auth','group'),(10,'auth','permission'),(2,'CahierDeTexte','cahiertexte'),(1,'CahierDeTexte','classe'),(3,'CahierDeTexte','seance'),(4,'CahierDeTexte','validation'),(12,'contenttypes','contenttype'),(13,'sessions','session'),(16,'token_blacklist','blacklistedtoken'),(17,'token_blacklist','outstandingtoken'),(15,'ues','fichier_ue'),(14,'ues','ue');
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
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-04-13 11:21:31.476673'),(2,'contenttypes','0002_remove_content_type_name','2025-04-13 11:21:31.610271'),(3,'auth','0001_initial','2025-04-13 11:21:32.039600'),(4,'auth','0002_alter_permission_name_max_length','2025-04-13 11:21:32.118546'),(5,'auth','0003_alter_user_email_max_length','2025-04-13 11:21:32.137210'),(6,'auth','0004_alter_user_username_opts','2025-04-13 11:21:32.142617'),(7,'auth','0005_alter_user_last_login_null','2025-04-13 11:21:32.150023'),(8,'auth','0006_require_contenttypes_0002','2025-04-13 11:21:32.153746'),(9,'auth','0007_alter_validators_add_error_messages','2025-04-13 11:21:32.156696'),(10,'auth','0008_alter_user_username_max_length','2025-04-13 11:21:32.166019'),(11,'auth','0009_alter_user_last_name_max_length','2025-04-13 11:21:32.171510'),(12,'auth','0010_alter_group_name_max_length','2025-04-13 11:21:32.198788'),(13,'auth','0011_update_proxy_permissions','2025-04-13 11:21:32.205143'),(14,'auth','0012_alter_user_first_name_max_length','2025-04-13 11:21:32.209486'),(15,'accounts','0001_initial','2025-04-13 11:21:33.112929'),(16,'ues','0001_initial','2025-04-13 11:21:33.421662'),(17,'CahierDeTexte','0001_initial','2025-04-13 11:21:34.132613'),(18,'CahierDeTexte','0002_seance_id_ues_validation_id_ues','2025-04-13 11:21:34.376239'),(19,'accounts','0002_secretaireclasse_id_classe','2025-04-13 11:21:34.493624'),(20,'admin','0001_initial','2025-04-13 11:21:34.733742'),(21,'admin','0002_logentry_remove_auto_add','2025-04-13 11:21:34.752454'),(22,'admin','0003_logentry_add_action_flag_choices','2025-04-13 11:21:34.764041'),(23,'sessions','0001_initial','2025-04-13 11:21:34.827106'),(24,'token_blacklist','0001_initial','2025-04-13 13:41:45.795306'),(25,'token_blacklist','0002_outstandingtoken_jti_hex','2025-04-13 13:41:45.905101'),(26,'token_blacklist','0003_auto_20171017_2007','2025-04-13 13:41:45.936356'),(27,'token_blacklist','0004_auto_20171017_2013','2025-04-13 13:41:46.093446'),(28,'token_blacklist','0005_remove_outstandingtoken_jti','2025-04-13 13:41:46.203242'),(29,'token_blacklist','0006_auto_20171017_2113','2025-04-13 13:41:46.250118'),(30,'token_blacklist','0007_auto_20171017_2214','2025-04-13 13:41:46.642548'),(31,'token_blacklist','0008_migrate_to_bigautofield','2025-04-13 13:41:47.192379'),(32,'token_blacklist','0010_fix_migrate_to_bigautofield','2025-04-13 13:41:47.223627'),(33,'token_blacklist','0011_linearizes_history','2025-04-13 13:41:47.239254'),(34,'token_blacklist','0012_alter_outstandingtoken_user','2025-04-13 13:41:47.270502');
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
INSERT INTO `django_session` VALUES ('avgxf5ptgctbb0m68flpd45mpodysydw','.eJxVjEEOgjAQRe_StWlmhpaCS_eegcxMi6CmTSisjHdXEha6_e-9_zIDb-s0bDUtwxzN2aA5_W7C-kh5B_HO-Vaslrwus9hdsQet9lpiel4O9-9g4jp9a9-NGJGoAx-4cb5x6lwLPZDrWgQhcj6xgI4ihIkBKGAc-wBBBdWb9wekija3:1u3wbh:Ih0WRLbERT3v6ylPvH0CWd_RqJ62J3_NpxPklbB7kss','2025-04-27 12:38:41.270707');
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
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `professeur_user_id_8fb382c4_fk_utilisateur_id` FOREIGN KEY (`user_id`) REFERENCES `utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professeur`
--

LOCK TABLES `professeur` WRITE;
/*!40000 ALTER TABLE `professeur` DISABLE KEYS */;
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
  `date_heure` datetime(6) NOT NULL,
  `id_classe` int DEFAULT NULL,
  `id_professeur` bigint DEFAULT NULL,
  `id_UEs` int DEFAULT NULL,
  PRIMARY KEY (`id_seance`),
  KEY `seance_id_classe_78366382_fk_classe_id_classe` (`id_classe`),
  KEY `seance_id_professeur_98b9fe6d_fk_professeur_id` (`id_professeur`),
  KEY `seance_id_UEs_5c578ed4_fk_UEs_id_UEs` (`id_UEs`),
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
  `user_id` bigint NOT NULL,
  `id_classe` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `secretaireclasse_id_classe_d602df8e_fk_classe_id_classe` (`id_classe`),
  CONSTRAINT `secretaireclasse_id_classe_d602df8e_fk_classe_id_classe` FOREIGN KEY (`id_classe`) REFERENCES `classe` (`id_classe`),
  CONSTRAINT `secretaireclasse_user_id_48f3a23d_fk_utilisateur_id` FOREIGN KEY (`user_id`) REFERENCES `utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `secretaireclasse`
--

LOCK TABLES `secretaireclasse` WRITE;
/*!40000 ALTER TABLE `secretaireclasse` DISABLE KEYS */;
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
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `secretairegeneral_user_id_937b6624_fk_utilisateur_id` FOREIGN KEY (`user_id`) REFERENCES `utilisateur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `secretairegeneral`
--

LOCK TABLES `secretairegeneral` WRITE;
/*!40000 ALTER TABLE `secretairegeneral` DISABLE KEYS */;
INSERT INTO `secretairegeneral` VALUES (1,'string',2);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_blacklistedtoken`
--

LOCK TABLES `token_blacklist_blacklistedtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` DISABLE KEYS */;
INSERT INTO `token_blacklist_blacklistedtoken` VALUES (1,'2025-04-13 13:42:42.176820',1);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_outstandingtoken`
--

LOCK TABLES `token_blacklist_outstandingtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` DISABLE KEYS */;
INSERT INTO `token_blacklist_outstandingtoken` VALUES (1,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTE1Mjg1NiwiaWF0IjoxNzQ0NTQ4MDU2LCJqdGkiOiIxMDUzMGVjMTFjNWM0NTIzOTU1ZDVmYTIwYzgyNTI3ZiIsInVzZXJfaWQiOjJ9.5lby6QWDlOWHEf63_aNSYExaYWgq_XOPYtpJSQvYVuU','2025-04-13 13:42:42.145551','2025-04-20 12:40:56.000000',2,'10530ec11c5c4523955d5fa20c82527f'),(2,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTE1NjU2MiwiaWF0IjoxNzQ0NTUxNzYyLCJqdGkiOiI1OGY5ODY3YTRkNTU0MDQwYmUxNDUzY2M1YmRlYWY4ZCIsInVzZXJfaWQiOjJ9.YUCJR4BKYhERvDexDpT0bR43o91iT_63CKnkftn1Azg','2025-04-13 13:42:42.145551','2025-04-20 13:42:42.000000',2,'58f9867a4d554040be1453cc5bdeaf8d');
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
  `id_prof` bigint NOT NULL,
  PRIMARY KEY (`id_UEs`),
  UNIQUE KEY `code_UEs` (`code_UEs`),
  KEY `UEs_id_prof_819a95d2_fk_professeur_id` (`id_prof`),
  CONSTRAINT `UEs_id_prof_819a95d2_fk_professeur_id` FOREIGN KEY (`id_prof`) REFERENCES `professeur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ues`
--

LOCK TABLES `ues` WRITE;
/*!40000 ALTER TABLE `ues` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilisateur`
--

LOCK TABLES `utilisateur` WRITE;
/*!40000 ALTER TABLE `utilisateur` DISABLE KEYS */;
INSERT INTO `utilisateur` VALUES (1,'pbkdf2_sha256$870000$rA7SqmL5f4ebrIWROWqqek$usgS/NZhjUAb8YnatDk/+Fb+Xif0ffRBkBGcdZ1PZJs=','2025-04-13 12:38:41.254671',1,'r@gmail.com','','','','email',1,1,0),(2,'pbkdf2_sha256$870000$QwcqYdyycPsRlSY6E84m2K$FAyqjIGwDMKEmOZ8T1pp1p6TPo/Gc5x1xeFhYA5rteg=',NULL,0,'rustpaul80@gmail.com','string','string','secretaire_general','email',1,0,1);
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
  `signature` varchar(100) DEFAULT NULL,
  `id_cahier` int DEFAULT NULL,
  `id_professeur` bigint DEFAULT NULL,
  `id_seance` int DEFAULT NULL,
  `id_UEs` int DEFAULT NULL,
  PRIMARY KEY (`id_validation`),
  KEY `validation_id_cahier_15d84e01_fk_Cahiertexte_id_cahier` (`id_cahier`),
  KEY `validation_id_professeur_e18706fb_fk_professeur_id` (`id_professeur`),
  KEY `validation_id_seance_fed5b2d5_fk_seance_id_seance` (`id_seance`),
  KEY `validation_id_UEs_1f082b04_fk_UEs_id_UEs` (`id_UEs`),
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

-- Dump completed on 2025-04-13 17:51:34
