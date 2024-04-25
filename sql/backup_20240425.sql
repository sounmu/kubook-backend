-- 백업용 sql 파일입니다.
-- 해당 sql 파일에는 민감한 정보가 포함되어 있지 않습니다.
-- 개발 환경에서 사용하면 편하게 개발을 진행할 수 있습니다.
-- made by @mjkweon17, created at 2024-04-25 19:27

-- 다음과 같이 view 생성 쿼리 주변에 DEFINER 정보가 있다면 삭제해주세요!
-- /*!50013 DEFINER=`kubook`@`%` SQL SECURITY DEFINER */



CREATE DATABASE  IF NOT EXISTS `kubook_db` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `kubook_db`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: kubook_db
-- ------------------------------------------------------
-- Server version	8.0.34

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `admin_status` tinyint(1) NOT NULL,
  `expiration_date` date NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_valid` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,1,1,'2024-05-28','2024-04-22 09:38:33','2024-04-25 18:48:34',1),(2,2,0,'2024-05-28','2024-04-22 09:38:47','2024-04-25 18:48:34',1),(3,3,0,'2024-05-28','2024-04-22 09:39:05','2024-04-25 18:48:34',0);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `book_info_id` int NOT NULL,
  `book_status` tinyint NOT NULL DEFAULT '0',
  `note` varchar(255) DEFAULT NULL,
  `donor_name` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_valid` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `book_info_id` (`book_info_id`),
  CONSTRAINT `book_ibfk_1` FOREIGN KEY (`book_info_id`) REFERENCES `book_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,1,1,NULL,'민재','2024-04-22 09:48:47','2024-04-22 10:50:10',1),(2,1,1,NULL,'수빈','2024-04-22 09:48:47','2024-04-22 10:50:10',1),(3,2,1,NULL,'민짜이','2024-04-22 09:48:47','2024-04-22 10:50:10',0),(4,2,0,NULL,NULL,'2024-04-22 09:48:47','2024-04-22 10:50:10',1),(5,3,1,NULL,'민재','2024-04-22 09:48:47','2024-04-22 10:50:10',1),(6,3,0,NULL,'수빈','2024-04-22 09:48:47','2024-04-22 10:50:10',1),(7,4,1,NULL,NULL,'2024-04-22 09:48:47','2024-04-22 10:50:10',1);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_category`
--

DROP TABLE IF EXISTS `book_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_valid` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_category`
--

LOCK TABLES `book_category` WRITE;
/*!40000 ALTER TABLE `book_category` DISABLE KEYS */;
INSERT INTO `book_category` VALUES (1,'1','언어','2024-04-25 18:50:42','2024-04-25 18:50:42',1),(2,'2','인공지능','2024-04-25 18:50:42','2024-04-25 18:50:42',1),(3,'3','PHP','2024-04-25 18:50:42','2024-04-25 18:50:42',0);
/*!40000 ALTER TABLE `book_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_info`
--

DROP TABLE IF EXISTS `book_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `subtitle` varchar(255) DEFAULT NULL,
  `author` varchar(100) NOT NULL,
  `publisher` varchar(45) NOT NULL,
  `publication_year` year NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `category_id` int NOT NULL,
  `version` varchar(45) DEFAULT NULL,
  `major` tinyint(1) DEFAULT '0',
  `language` tinyint(1) DEFAULT '1',
  `is_valid` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `book_info_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `book_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_info`
--

LOCK TABLES `book_info` WRITE;
/*!40000 ALTER TABLE `book_info` DISABLE KEYS */;
INSERT INTO `book_info` VALUES (1,'파이썬 공부',NULL,'민재','KUCC 출판사',2024,NULL,1,NULL,0,NULL,1,'2024-04-22 09:46:59','2024-04-25 20:09:33'),(2,'인공지능 공부',NULL,'민재','KUCC 출판사',2023,NULL,2,NULL,0,NULL,1,'2024-04-22 09:46:59','2024-04-25 20:09:33'),(3,'PHP 공부',NULL,'민재','KUCC 출판사',2024,NULL,3,NULL,0,NULL,1,'2024-04-22 09:46:59','2024-04-25 20:09:33'),(4,'C++ 공부',NULL,'민재','KUCC 출판사',2021,NULL,1,NULL,0,NULL,0,'2024-04-22 09:46:59','2024-04-25 20:09:33');
/*!40000 ALTER TABLE `book_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_review`
--

DROP TABLE IF EXISTS `book_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_review` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `book_info_id` int NOT NULL,
  `review_content` text NOT NULL,
  `is_valid` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `book_info_id` (`book_info_id`),
  CONSTRAINT `book_review_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `book_review_ibfk_2` FOREIGN KEY (`book_info_id`) REFERENCES `book_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_review`
--

LOCK TABLES `book_review` WRITE;
/*!40000 ALTER TABLE `book_review` DISABLE KEYS */;
INSERT INTO `book_review` VALUES (1,1,1,'최고의 책입니다',1,'2024-04-22 10:48:34','2024-04-22 10:48:34'),(2,4,1,'권민재 저자가 만든 책은 못 참치마요,,,',1,'2024-04-22 10:48:34','2024-04-22 10:48:34'),(3,3,1,'ㅇㅅㅇ',0,'2024-04-22 10:48:34','2024-04-22 10:48:34'),(4,3,2,'추천합니다!',1,'2024-04-22 10:48:34','2024-04-22 10:48:34'),(5,1,2,'따봉',1,'2024-04-22 20:25:36','2024-04-22 20:25:36');
/*!40000 ALTER TABLE `book_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `book_stat`
--

DROP TABLE IF EXISTS `book_stat`;
/*!50001 DROP VIEW IF EXISTS `book_stat`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `book_stat` AS SELECT 
 1 AS `book_info_id`,
 1 AS `review_count`,
 1 AS `loan_count`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `library_setting`
--

DROP TABLE IF EXISTS `library_setting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library_setting` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `value` varchar(50) NOT NULL,
  `data_type` varchar(50) NOT NULL,
  `description` text,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_valid` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library_setting`
--

LOCK TABLES `library_setting` WRITE;
/*!40000 ALTER TABLE `library_setting` DISABLE KEYS */;
INSERT INTO `library_setting` VALUES (1,'backend_development_start_date','2024-04-07','DATETIME','도서관 서비스 백엔드 개발 시작일','2024-04-25 19:56:21','2024-04-25 19:56:21',1),(2,'backend devlopers','권민재, 한수빈','TEXT','개발자 목록','2024-04-25 19:56:21','2024-04-25 19:56:21',1),(3,'backend_development_end_date','','DATETIME','도서관 서비스 백엔드 개발 종료일','2024-04-25 19:56:21','2024-04-25 19:56:21',1),(4,'service_start_date','2023-06-01','DATETIME','도서관 서비스 시작일','2024-04-25 19:56:21','2024-04-25 19:56:21',1),(5,'service_termination_date','','DATETIME','도서관 서비스 종료일','2024-04-25 19:56:21','2024-04-25 19:56:21',0),(6,'max_books_per_loan','5','INT','최대 대출 가능 권수','2024-04-25 19:56:21','2024-04-25 21:56:34',1),(7,'loan_duration_days','14','INT','대출 기간 (일)','2024-04-25 19:56:21','2024-04-25 21:56:34',1),(8,'loan_extension_days','7','INT','대출 연장 기간 (일)','2024-04-25 19:56:21','2024-04-25 21:56:34',1),(9,'max_books_per_request','3','INT','최대 예약 가능 권수','2024-04-25 19:56:21','2024-04-25 21:56:34',1),(10,'max_request_value','30000','INT','최대 예약 가능 금액','2024-04-25 19:56:21','2024-04-25 21:56:34',1),(11,'reservation_limit_per_user','2','INT','사용자 당 최대 예약 가능 권수','2024-04-25 19:56:21','2024-04-25 21:56:34',1),(12,'reservation_limit_per_book','3','INT','도서 당 최대 예약 가능 사용자 수','2024-04-25 19:56:21','2024-04-25 21:56:34',1);
/*!40000 ALTER TABLE `library_setting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan`
--

DROP TABLE IF EXISTS `loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `user_id` int NOT NULL,
  `loan_date` date NOT NULL,
  `due_date` date NOT NULL,
  `extend_status` tinyint(1) NOT NULL DEFAULT '0',
  `return_status` tinyint(1) NOT NULL DEFAULT '0',
  `return_date` date DEFAULT NULL,
  `overdue_days` int NOT NULL DEFAULT '0',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_valid` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `book_id` (`book_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `loan_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`),
  CONSTRAINT `loan_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan`
--

LOCK TABLES `loan` WRITE;
/*!40000 ALTER TABLE `loan` DISABLE KEYS */;
INSERT INTO `loan` VALUES (1,1,1,'2024-04-22','2024-04-28',0,0,NULL,0,'2024-04-22 10:57:58','2024-04-22 10:57:58',1),(2,2,2,'2024-04-22','2024-04-27',0,0,NULL,0,'2024-04-22 10:57:58','2024-04-22 10:57:58',1);
/*!40000 ALTER TABLE `loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notice`
--

DROP TABLE IF EXISTS `notice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `admin_id` int NOT NULL,
  `user_id` int DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `notice_content` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_valid` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `admin_id` (`admin_id`),
  CONSTRAINT `notice_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notice`
--

LOCK TABLES `notice` WRITE;
/*!40000 ALTER TABLE `notice` DISABLE KEYS */;
INSERT INTO `notice` VALUES (1,1,1,'첫 공지','테스트 공지사항입니다.','2024-04-22 09:39:29','2024-04-22 09:39:29',1),(2,1,1,'테스트 공지','유효하지 않은 공지입니다.','2024-04-22 09:39:50','2024-04-22 09:39:50',0);
/*!40000 ALTER TABLE `notice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requested_book`
--

DROP TABLE IF EXISTS `requested_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requested_book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `book_title` varchar(255) NOT NULL,
  `publication_year` year DEFAULT NULL,
  `reject_reason` text,
  `request_link` varchar(100) NOT NULL,
  `reason` text NOT NULL,
  `processing_status` tinyint NOT NULL DEFAULT '0',
  `request_date` date NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_valid` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `requested_book_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requested_book`
--

LOCK TABLES `requested_book` WRITE;
/*!40000 ALTER TABLE `requested_book` DISABLE KEYS */;
INSERT INTO `requested_book` VALUES (1,2,'파이썬 개론',NULL,NULL,'naver.com','ㅇㅅㅇ',0,'2024-04-22','2024-04-22 09:43:42','2024-04-22 10:41:12',1),(2,3,'C++ 개론',NULL,NULL,'naver.com','ㅇㅅㅇ',0,'2024-04-22','2024-04-22 09:43:42','2024-04-22 10:41:12',1),(3,4,'인공지능 개록',NULL,NULL,'naver.com','ㅇㅅㅇ',2,'2024-04-22','2024-04-22 09:43:42','2024-04-22 20:38:21',0);
/*!40000 ALTER TABLE `requested_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `user_id` int NOT NULL,
  `reservation_date` date NOT NULL,
  `reservation_status` tinyint NOT NULL DEFAULT '0',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_valid` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `book_id` (`book_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`),
  CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
INSERT INTO `reservation` VALUES (1,1,1,'2024-04-22',1,'2024-04-22 10:55:53','2024-04-22 10:55:53',1),(2,1,2,'2024-04-22',0,'2024-04-22 10:56:12','2024-04-22 10:56:12',1),(3,3,1,'2024-04-22',1,'2024-04-22 10:56:12','2024-04-22 10:56:12',1);
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `auth_id` varchar(50) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `email` varchar(100) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_valid` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_id` (`auth_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'1','(테스트)어드민',1,'test@gmail.com','2024-04-22 09:20:29','2024-04-22 09:37:21',1),(2,'2','(테스트)일반',1,'test1@gmail.com','2024-04-22 09:37:21','2024-04-22 09:37:21',1),(3,'3','(테스트)비활',0,'test2@gmail.com','2024-04-22 09:38:02','2024-04-22 09:38:02',1),(4,'4','(테스트)무효',0,'test3@gmail.com','2024-04-22 09:38:02','2024-04-24 23:08:26',0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `book_stat`
--

/*!50001 DROP VIEW IF EXISTS `book_stat`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50001 VIEW `book_stat` AS select `bi`.`id` AS `book_info_id`,count(distinct `br`.`id`) AS `review_count`,count(distinct `l`.`id`) AS `loan_count` from (((`book_info` `bi` left join `book_review` `br` on(((`bi`.`id` = `br`.`book_info_id`) and (`br`.`is_valid` = true)))) left join `book` `b` on((`bi`.`id` = `b`.`book_info_id`))) left join `loan` `l` on(((`b`.`id` = `l`.`book_id`) and (`l`.`is_valid` = true)))) group by `bi`.`id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-25 21:58:47
