-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: computer_equipment_store
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.20.04.1

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
-- Table structure for table `clientlist`
--

DROP TABLE IF EXISTS `clientlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientlist` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `birthday_date` date DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientlist`
--

LOCK TABLES `clientlist` WRITE;
/*!40000 ALTER TABLE `clientlist` DISABLE KEYS */;
INSERT INTO `clientlist` VALUES (29,'John Doe','1985-07-15','123 Main St, City, Country','+380501234567','john.doe@example.com'),(30,'Jane Smith','1990-03-22','456 Elm St, City, Country','+380672345678','jane.smith@example.com'),(31,'Michael Johnson','1978-09-10','789 Oak St, City, Country','+380934567890','michael.johnson@example.com'),(32,'Sarah Davis','1982-12-05','890 Pine St, City, Country','+380997654321','sarah.davis@example.com'),(33,'Robert Clark','1989-05-18','234 Cedar St, City, Country','+380444556677','robert.clark@example.com'),(34,'Laura Lee','1995-08-29','567 Maple St, City, Country','+380667788899','laura.lee@example.com'),(35,'David Martin','1980-04-12','678 Birch St, City, Country','+380333222111','david.martin@example.com');
/*!40000 ALTER TABLE `clientlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marketlist`
--

DROP TABLE IF EXISTS `marketlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marketlist` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `producer` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `detailed_description` varchar(255) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `availability` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marketlist`
--

LOCK TABLES `marketlist` WRITE;
/*!40000 ALTER TABLE `marketlist` DISABLE KEYS */;
INSERT INTO `marketlist` VALUES (1,'Laptop Dell XPS 13','Dell','Laptop',2023,'Ultra-portable laptop','13\" 4K display, Intel i7, 16GB RAM, 512GB SSD, Windows 10',1500,1),(2,'Gaming PC Alienware Aurora R12','Alienware','Gaming PC',2023,'High-end gaming PC','Intel i9, NVIDIA RTX 3090, 32GB RAM, 1TB SSD, Windows 10',3000,1),(3,'Monitor LG UltraGear 27GN950-B','LG','Monitor',2021,'27\" Gaming Monitor','4K resolution, 144Hz refresh rate, NVIDIA G-Sync',700,1),(4,'Wireless Keyboard Logitech K780','Logitech','Accessories',NULL,'Wireless keyboard','Multi-device Bluetooth keyboard, compatible with PC and mobile devices',60,1),(5,'External Hard Drive Seagate Backup Plus 4TB','Seagate','Storage',NULL,'External hard drive','4TB capacity, USB 3.0, backup software included',100,1),(6,'Wireless Earbuds Apple AirPods Pro','Apple','Accessories',2021,'True wireless earbuds','Active noise cancellation, water and sweat resistance',249,1),(7,'Inkjet Printer HP OfficeJet Pro 9015','HP','Printer',2019,'All-in-One Inkjet Printer','Wireless, mobile printing, 2-sided duplex printing',229,1),(8,'Portable SSD Samsung T7 1TB','Samsung','Storage',2020,'Portable SSD','1TB capacity, USB 3.2, shock-resistant, password protection',129,1),(9,'Webcam Logitech C920 HD Pro','Logitech','Webcam',2012,'HD Webcam','1080p, built-in stereo microphone, automatic low-light correction',69,1),(10,'Wireless Router ASUS RT-AX86U','ASUS','Networking',2020,'Dual-Band WiFi 6 Router','Wi-Fi 6, 2.4 GHz and 5 GHz, MU-MIMO, AiProtection Pro',249,1);
/*!40000 ALTER TABLE `marketlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-26  1:18:41
