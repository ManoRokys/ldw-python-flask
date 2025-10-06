CREATE DATABASE  IF NOT EXISTS `santos_fc` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `santos_fc`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: santos_fc
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `jogador`
--

DROP TABLE IF EXISTS `jogador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jogador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `posicao` varchar(50) DEFAULT NULL,
  `numero` int(11) DEFAULT NULL,
  `time_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `time_id` (`time_id`),
  CONSTRAINT `jogador_ibfk_1` FOREIGN KEY (`time_id`) REFERENCES `time` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jogador`
--

LOCK TABLES `jogador` WRITE;
/*!40000 ALTER TABLE `jogador` DISABLE KEYS */;
INSERT INTO `jogador` VALUES (1,'Gabriel Brazão','Goleiro',77,1),(2,'Igor Vinícius','Defensor',18,1),(3,'Alexis Duarte','Defensor',23,1),(4,'Adonis Frías','Defensor',98,1),(5,'Gonzalo Escobar','Meio-campo',31,1),(6,'João Schmidt','Meio-campo',5,1),(7,'Tomás Rincón','Meio-campo',8,1),(8,'Zé Rafael','Meio-campo/Atacante',6,1),(9,'Benjamin Rollheiser','Meio-campo/Atacante',32,1),(10,'Guilherme','Atacante',11,1),(11,'Laurato Díaz','Atacante',19,1),(12,'Germán Cano','Atacante',14,7),(13,'Patrick','Meio-campo',88,6);
/*!40000 ALTER TABLE `jogador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partida`
--

DROP TABLE IF EXISTS `partida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partida` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` date NOT NULL,
  `competicao` varchar(150) DEFAULT NULL,
  `time_mandante_id` int(11) NOT NULL,
  `time_visitante_id` int(11) NOT NULL,
  `gols_mandante` int(11) DEFAULT NULL,
  `gols_visitante` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `time_mandante_id` (`time_mandante_id`),
  KEY `time_visitante_id` (`time_visitante_id`),
  CONSTRAINT `partida_ibfk_1` FOREIGN KEY (`time_mandante_id`) REFERENCES `time` (`id`),
  CONSTRAINT `partida_ibfk_2` FOREIGN KEY (`time_visitante_id`) REFERENCES `time` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partida`
--

LOCK TABLES `partida` WRITE;
/*!40000 ALTER TABLE `partida` DISABLE KEYS */;
INSERT INTO `partida` VALUES (1,'2025-10-05','Brasileirão Série A',2,1,3,0),(2,'2025-10-01','Brasileirão Série A',1,3,1,1),(3,'2025-09-28','Brasileirão Série A',4,1,2,2),(4,'2025-09-21','Brasileirão Série A',1,5,1,0),(5,'2025-09-14','Brasileirão Série A',6,1,1,1),(6,'2025-08-31','Brasileirão Série A',1,7,0,0);
/*!40000 ALTER TABLE `partida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `time`
--

DROP TABLE IF EXISTS `time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `cidade` varchar(150) DEFAULT NULL,
  `estado` varchar(2) DEFAULT NULL,
  `fundacao` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `time`
--

LOCK TABLES `time` WRITE;
/*!40000 ALTER TABLE `time` DISABLE KEYS */;
INSERT INTO `time` VALUES (1,'Santos FC','Santos','SP',1912),(2,'Ceará SC','Fortaleza','CE',1914),(3,'Grêmio','Porto Alegre','RS',1903),(4,'Red Bull Bragantino','Bragança Paulista','SP',1928),(5,'São Paulo FC','São Paulo','SP',1930),(6,'Patético-MG',' Belo Horizonte','MG',1908),(7,'Fluminense','Rio de Janeiro','RJ',1902);
/*!40000 ALTER TABLE `time` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-06 15:27:25
