-- phpMyAdmin SQL Dump
-- version 2.8.0.1
-- http://www.phpmyadmin.net
-- 
-- Host: custsql-ipg54.eigbox.net
-- Generation Time: Jun 21, 2014 at 05:20 AM
-- Server version: 5.5.32
-- PHP Version: 4.4.9
-- 
-- Database: `kalamakom`
-- 
CREATE DATABASE `kalamakom` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `kalamakom`;

-- --------------------------------------------------------

-- 
-- Table structure for table `repositories`
-- 

CREATE TABLE `repositories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(400) NOT NULL,
  `title_en` varchar(400) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 AUTO_INCREMENT=24 ;

-- 
-- Dumping data for table `repositories`
-- 

INSERT INTO `repositories` VALUES (1, 'استثمار', 'investment');
INSERT INTO `repositories` VALUES (2, 'السعودى الهولندى', 'Saudi Holland');
INSERT INTO `repositories` VALUES (3, 'السعودى الفرنسى', 'Saudi French');
INSERT INTO `repositories` VALUES (4, 'ساب', 'Saab');
INSERT INTO `repositories` VALUES (5, 'العربى الوطنى', 'National Arabic');
INSERT INTO `repositories` VALUES (6, 'سامبا', 'Sampia');
INSERT INTO `repositories` VALUES (7, 'تاسي', 'Tassi');
INSERT INTO `repositories` VALUES (8, 'تاسي', 'Tassi');
INSERT INTO `repositories` VALUES (9, 'الرياض', 'Al Ryadh');
INSERT INTO `repositories` VALUES (10, 'الجزيرة', ' Al Gazirah  ');
INSERT INTO `repositories` VALUES (11, 'استثمار', '  Investment');
INSERT INTO `repositories` VALUES (12, 'العربي الوطني', '  National Arabian');
INSERT INTO `repositories` VALUES (13, 'الراجحي', '  Al Raghy');
INSERT INTO `repositories` VALUES (14, 'البلاد', '  Al Belad');
INSERT INTO `repositories` VALUES (15, 'الإنماء', '  Al Enmaa');
INSERT INTO `repositories` VALUES (16, 'كيمانول', '  Kemanool');
INSERT INTO `repositories` VALUES (17, 'بتروكيم ', '  Petrokim');
INSERT INTO `repositories` VALUES (18, 'سابك', '  Saabek');
INSERT INTO `repositories` VALUES (19, 'سافكو', '  Safco');
INSERT INTO `repositories` VALUES (20, 'التصنيع', '  Manufucturing');
INSERT INTO `repositories` VALUES (21, 'اللجين', '  Al Lojain');
INSERT INTO `repositories` VALUES (22, 'نماء للكيماويات', ' Namaa Chemicals ');
INSERT INTO `repositories` VALUES (23, 'المجموعة السعودية', ' Saudi Group ');

-- --------------------------------------------------------

-- 
-- Table structure for table `users`
-- 

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(200) NOT NULL,
  `firstname` text NOT NULL,
  `password` text NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `group_id` int(11) NOT NULL,
  `pic` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

-- 
-- Dumping data for table `users`
-- 

INSERT INTO `users` VALUES (1, 'amr@codumanity.com', 'Amr', '$2a$08$n9Y.yfaNtScTBfd8tXnIee2QhzNMKX6ZkmvChvIDF1rpKw.riADDu', '2014-06-12', '2014-06-12', 0, '');
INSERT INTO `users` VALUES (2, 'amr2@test.com', 'amr', '$2a$08$oE70pPq18OOHkL.XeeXczeUyC8kXbyfCLKWBUpJPUy6vXWdoiLeDK', '2014-06-12', '2014-06-12', 0, 'uploads/profilepics/pic_2');
INSERT INTO `users` VALUES (3, 'ahmad.elsallab_sds@yahoo.com', 'a', '$2a$08$6GP0utJDcM1h/enOwqzpYOSO0i7hv3XFZtNeegXasxwfXafNw4fKi', '2014-06-12', '2014-06-12', 0, '');
