-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: company_hr
-- ------------------------------------------------------
-- Server version	8.0.45

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
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  `job_title` varchar(50) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10102 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (10001,'Andi Saputra','Male','1995-04-10','2021-03-12','Data Analyst',8000000),(10002,'Sari Lestari','Female','1993-08-22','2019-07-01','Accountant',9000000),(10003,'Budi Santoso','Male','1997-02-15','2022-01-10','HR Staff',7000000),(10004,'Rina Putri','Female','1996-11-05','2020-09-18','Marketing Specialist',8500000),(10005,'Dedi Kurniawan','Male','1992-06-30','2018-05-25','Operations Manager',12000000),(10006,'Maya Pratiwi','Female','1994-03-14','2021-06-20','UI Designer',8500000),(10007,'Agus Salim','Male','1990-09-12','2017-04-01','Finance Manager',13000000),(10008,'Lina Marlina','Female','1998-01-17','2023-02-11','Admin Staff',6000000),(10009,'Rudi Hartono','Male','1991-05-25','2019-08-10','Backend Developer',11000000),(10010,'Tina Wulandari','Female','1997-07-19','2022-03-01','HR Staff',7000000),(10011,'Fajar Nugroho','Male','1996-02-13','2020-11-12','Frontend Developer',10000000),(10012,'Nina Kartika','Female','1995-12-03','2021-05-16','Marketing Staff',7500000),(10013,'Bayu Prasetyo','Male','1994-10-22','2019-09-09','System Analyst',11500000),(10014,'Putri Ayu','Female','1998-06-01','2023-01-15','Customer Support',6000000),(10015,'Hendra Gunawan','Male','1992-04-07','2018-12-02','Network Engineer',10500000),(10016,'Lukman Hakim','Male','1993-07-21','2019-03-14','DevOps Engineer',11000000),(10017,'Sinta Dewi','Female','1996-05-18','2021-10-10','QA Engineer',9000000),(10018,'Rahmat Hidayat','Male','1991-11-30','2018-06-19','IT Support',7500000),(10019,'Yuni Astuti','Female','1997-08-09','2022-04-23','Recruiter',7200000),(10020,'Arif Setiawan','Male','1990-01-28','2017-02-17','Project Manager',14000000),(10021,'Dian Puspita','Female','1995-03-03','2020-06-10','Business Analyst',10000000),(10022,'Rizky Ramadhan','Male','1998-09-14','2023-03-05','Junior Developer',7000000),(10023,'Nadia Safitri','Female','1997-12-25','2022-02-02','Content Creator',7500000),(10024,'Ilham Maulana','Male','1994-07-11','2019-05-22','Database Admin',11000000),(10025,'Fitri Handayani','Female','1993-02-09','2018-11-01','Finance Staff',8000000),(10026,'Yoga Saputra','Male','1996-04-27','2021-08-13','Mobile Developer',10500000),(10027,'Ayu Lestari','Female','1999-01-15','2023-07-19','Admin Staff',6000000),(10028,'Wahyu Kurniawan','Male','1992-10-02','2018-03-30','Security Engineer',10000000),(10029,'Desi Anggraini','Female','1995-06-12','2020-09-05','HR Officer',8200000),(10030,'Rian Pratama','Male','1991-09-17','2017-07-21','Operations Supervisor',11500000),(10031,'Farhan Akbar','Male','1998-05-03','2023-05-11','Junior Analyst',6800000),(10032,'Nurul Aisyah','Female','1996-12-08','2021-01-25','Marketing Staff',7600000),(10033,'Aditya Prakoso','Male','1994-08-14','2019-06-18','Backend Developer',10800000),(10034,'Bella Oktavia','Female','1997-10-01','2022-06-30','Graphic Designer',8000000),(10035,'Chandra Wijaya','Male','1992-03-09','2018-04-27','IT Auditor',11200000),(10036,'Dinda Larasati','Female','1999-02-19','2024-01-08','Admin Staff',5800000),(10037,'Eko Prasetyo','Male','1993-11-11','2019-02-14','System Engineer',10400000),(10038,'Gita Permata','Female','1995-07-07','2020-12-12','HR Staff',7800000),(10039,'Hafiz Rahman','Male','1991-06-05','2017-10-19','Project Manager',13800000),(10040,'Indah Cahya','Female','1998-04-04','2023-04-17','Customer Support',6200000),(10041,'Joko Susilo','Male','1990-02-20','2016-09-01','Operations Manager',12500000),(10042,'Kartika Sari','Female','1997-09-09','2022-08-22','Marketing Specialist',8600000),(10043,'Luthfi Hakim','Male','1995-01-30','2020-05-14','Data Engineer',11200000),(10044,'Mega Oktaviani','Female','1996-03-17','2021-07-07','QA Engineer',9100000),(10045,'Naufal Rizky','Male','1994-12-12','2019-04-04','Backend Developer',10900000),(10046,'Oki Setiawan','Male','1993-05-05','2018-01-09','IT Support',7400000),(10047,'Putra Mahendra','Male','1992-08-16','2017-03-12','Network Engineer',10200000),(10048,'Qori Aulia','Female','1998-11-11','2023-06-01','Content Creator',7300000),(10049,'Riska Amelia','Female','1997-02-02','2022-09-15','HR Officer',8000000),(10050,'Samsul Bahri','Male','1991-04-13','2017-11-23','Finance Supervisor',11800000),(10051,'Tari Puspita','Female','1996-06-06','2021-03-29','Recruiter',7600000),(10052,'Umar Dani','Male','1993-09-27','2018-08-08','Security Engineer',9900000),(10053,'Vina Lestari','Female','1995-10-18','2020-02-10','Graphic Designer',8200000),(10054,'Wawan Setia','Male','1990-12-30','2016-05-05','Operations Manager',13000000),(10055,'Xenia Putri','Female','1999-07-21','2024-02-14','Admin Staff',5700000),(10056,'Yusuf Hidayat','Male','1994-01-09','2019-07-01','System Analyst',11300000),(10057,'Zahra Nabila','Female','1997-03-23','2022-10-03','Marketing Staff',7700000),(10058,'Arman Syah','Male','1992-02-02','2018-07-17','Database Admin',10800000),(10059,'Bunga Melati','Female','1998-05-25','2023-08-09','Customer Support',6100000),(10060,'Cahyo Nugroho','Male','1991-11-19','2017-06-30','Project Manager',13600000),(10071,'Ali Ababwa','male','1998-08-09','2023-12-03','IT Support',8000000),(10081,'Zahra','female','1997-02-19','2026-02-20','Accountant',6000000);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-19 13:19:04
