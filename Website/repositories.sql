-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Sep 06, 2014 at 10:07 AM
-- Server version: 5.5.36
-- PHP Version: 5.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `kalamakom_new_1`
--

-- --------------------------------------------------------

--
-- Table structure for table `repositories`
--

CREATE TABLE IF NOT EXISTS `repositories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(400) NOT NULL,
  `title_en` varchar(400) NOT NULL,
  `syn_ar` varchar(400) NOT NULL,
  `syn_en` varchar(400) NOT NULL,
  `used_name_ar` varchar(400) NOT NULL,
  `used_name_en` varchar(400) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=162 ;

--
-- Dumping data for table `repositories`
--

INSERT INTO `repositories` (`id`, `title`, `title_en`, `syn_ar`, `syn_en`, `used_name_ar`, `used_name_en`) VALUES
(1, 'استثمار', 'investment', '', '', 'البنك السعودي للاستثمار', 'The Saudi Investment Bank'),
(2, 'السعودى الهولندى', 'Saudi Holland', '', '', 'البنك السعودي الهولندي', 'Saudi Hollandi Bank'),
(3, 'السعودى الفرنسى', 'Saudi French', '', '', 'البنك السعودي الفرنسي', 'Banque Saudi Fransi'),
(4, 'ساب', 'Saab', '', '', 'ساب للتكافل', 'SABB Takaful'),
(5, 'العربى الوطنى', 'National Arabic', '', '', 'البنك العربي الوطني', 'Arab National Bank'),
(6, 'سامبا', 'Sampia', '', '', 'مجموعة سامبا المالية', 'Samba Financial Group'),
(7, 'تاسي', 'Tassi', 'تداول-السوق السعودي-توصيات', '', 'تاسى', 'Tassi'),
(9, 'الرياض', 'Al Ryadh', '', '', 'بنك الرياض', 'Riyad Bank'),
(10, 'الجزيرة', ' Al Gazirah  ', '', '', 'شركة الجزيرة تكافل تعاوني', 'Aljazira Takaful Taawuni Company'),
(12, 'العربي الوطني', '  National Arabian', '', '', 'البنك العربي الوطني', 'Arab National Bank'),
(13, 'الراجحي', '  Al Raghy', '', '', 'مصرف الراجحي', 'Al Rajhi Bank'),
(14, 'البلاد', '  Al Belad', '', '', 'بنك البلاد', 'BANK ALBILAD'),
(15, 'الإنماء', '  Al Enmaa', '', '', 'مصرف الإنماء', 'Alinma Bank'),
(16, 'كيمانول', '  Kemanool', '', '', 'شركة تكوين المتطورة للصناعات', 'Takween Advanced Industries'),
(17, 'بتروكيم ', '  Petrokim', '', '', 'شركة الصناعات الكيميائية الأساسية', 'Basic Chemical Industries Co'),
(18, 'سابك', '  Saabek', '', '', 'شركة التعدين العربية السعودية', 'Saudi Arabian Mining Company'),
(19, 'سافكو', '  Safco', '', '', 'مجموعة أسترا الصناعية', 'Astra Industrial Group'),
(20, 'التصنيع', '  Manufucturing', '', '', 'شركة مجموعة السريع التجارية الصناعية', 'Al Sorayai Trading And Industrial Group Company'),
(21, 'اللجين', '  Al Lojain', '', '', 'شركة الحسن غازي إبراهيم شاكر', 'Al Hassan Ghazi Ibrahim Shaker'),
(22, 'نماء للكيماويات', ' Namaa Chemicals ', '', '', 'شركة نماء للكيماويات', 'Nama Chemicals Co.'),
(23, 'المجموعة السعودية', ' Saudi Group ', '', '', 'المجموعة السعودية للإستثمار الصناعي', 'Saudi Industrial Investment Group'),
(25, 'الصحراء للبتروكيماويات', 'Saharaa petrochemicals', '', '', 'شركة الصحراء للبتروكيماويات', 'Sahara Petrochemical Co.'),
(26, 'ينساب ', 'Yansab', '', '', '', ''),
(27, 'أسمنت حائل', 'Haael sement', '', '', 'شركة أسمنت حائل', 'Hail Cement Company'),
(28, 'أسمنت نجران ', 'Nagran sement', '', '', 'شركة أسمنت نجران', 'Najran Cement Company'),
(29, 'اسمنت المدينة ', 'City sement', '', '', 'شركة اسمنت المدينة', 'City Cement Co'),
(30, 'اسمنت الشمالية ', 'Alshamaleya sement', '', '', 'شركة أسمنت المنطقة الشمالية', 'Northern Region Cement Company'),
(31, 'الاسمنت العربية ', 'Arabic sement', '', '', 'شركة الاسمنت العربية', 'Arabian Cement Co'),
(32, 'اسمنت اليمامة ', 'Yamama sement', '', '', 'شركة اسمنت اليمامة', 'Yamama Cement Company'),
(33, 'اسمنت السعوديه ', 'Saudia sement', '', '', 'شركة الأسمنت السعودية', 'Saudi Cement Company'),
(34, 'اسمنت القصيم ', 'Qasem sement', '', '', 'شركة اسمنت القصيم', 'The Qassim Cement Co'),
(35, 'اسمنت الجنوبيه ', 'Ganobeya sement', '', '', 'شركة اسمنت المنطقة الجنوبيه', 'Southern Province Cement Co'),
(36, 'اسمنت ينبع', 'Yanbo sement', '', '', 'شركة اسمنت ينبع', 'Yanbu Cement Co'),
(37, 'اسمنت الشرقية ', 'Sharqeyya sement', '', '', 'شركة اسمنت المنطقة الشرقية', 'Eastern Province Cement Co'),
(38, 'اسمنت تبوك ', 'Tabook sement', '', '', 'شركة اسمنت تبوك', 'Tabuk Cement Co'),
(39, 'اسمنت الجوف ', 'Gawf sement', '', '', 'شركة اسمنت الجوف', 'AL JOUF CEMENT COMPANY'),
(40, 'أسواق ع العثيم ', 'Othaim markets', '', '', 'شركة أسواق عبدالله العثيم', 'Abdullah Al Othaim Markets Company'),
(41, 'المواساة', 'Mowasah', '', '', 'شركة المواساة للخدمات الطبية', 'Mouwasat Medical Services Company'),
(42, 'إكسترا', 'Xtra', '', '', '', ''),
(43, 'دله الصحية', 'Dallah health', '', '', 'شركة دله للخدمات الصحية القابضة', 'Dallah Healthcare Holding Company'),
(44, 'رعاية', 'Reaya', '', '', 'الشركة الوطنية للرعاية الطبية', 'National Medical Care Company'),
(45, 'ساسكو', 'Sasco', '', '', '', ''),
(46, 'ثمار', 'Themar', '', '', '', ''),
(47, 'مجموعة فتيحي ', 'Fitaihi group', '', '', 'مجموعة فتيحي القابضة', 'Fitaihi Holding Group'),
(48, 'جرير', 'Jarir', '', '', 'شركة جرير للتسويق', 'Jarir Marketing Co'),
(49, 'الدريس', 'Aldrees', '', '', 'شركة الدريس للخدمات البترولية و النقليات', 'Aldrees Petroleum & Transport Services Co.'),
(50, 'الحكير', 'Alhaker', '', '', 'شركة فواز عبدالعزيز الحكير وشركاه', 'Fawaz Abdulaziz AlHokair Company'),
(51, 'الخليج للتدريب ', 'Alkhaleej', '', '', 'شركة الخليج للتدريب و التعليم', 'Alkhaleej Training and Education Company'),
(52, 'الغاز والتصنيع ', 'Gasco', '', '', 'شركة الغاز والتصنيع الاهلية', 'National Gas & Industrialization Co.'),
(53, 'كهرباء السعودية ', 'Saudi electricity ', '', '', 'الشركة السعودية للكهرباء', 'Saudi Electricity Company'),
(54, 'مجموعة صافولا', 'Savola group', '', '', 'مجموعة صافولا', 'Savola Group'),
(55, 'الغذائية', '', '', '', '', ''),
(56, 'سدافكو', 'Sadafco', '', '', 'الشركة السعودية لمنتجات الألبان والأغذية (سدافكو)', 'Saudia Dairy and Foodstuff .Co'),
(57, 'المراعي', 'Maraii', '', '', 'شركة المراعي', 'Almarai Company'),
(58, 'أنعام القابضة ', 'Anaam group', '', '', 'شركة مجموعة أنعام الدولية القابضة', 'Anaam International Holding Group CO'),
(59, 'حلواني إخوان', 'Halwani brothers', '', '', 'حلواني إخوان', 'Halwani Bros'),
(60, 'هرفي للأغذية', 'Herfy food', '', '', 'شركة هرفي للخدمات الغذائية', 'Herfy Food Services Co'),
(61, 'التموين', 'Saudia catering', '', '', 'شركة الخطوط السعودية للتموين', 'Saudi Airlines Catering Company'),
(62, 'نادك', 'Nadec', '', '', 'الشركة الوطنية للتنمية الزراعية', 'National Agriculture Development Co.'),
(63, 'القصيم الزراعيه', 'Qassim-agricultur ', '', '', 'شركة القصيم الزراعية', 'Qassim Agriculture Co'),
(64, 'تبوك الزراعيه ', 'Tabuk', '', '', 'شركة تبوك للتنمية الزراعية', 'Tabuk Agriculture Development Co'),
(65, 'الأسماك', 'Asmak', '', '', 'الشركة السعودية للأسماك', 'Saudi Fisheries Co'),
(66, 'الشرقية للتنمية ', '', '', '', 'الشركة الشرقية للتنمية', 'Ash-Sharqiyah Development Company'),
(67, 'الجوف الزراعيه', '', '', '', 'شركة الجوف الزراعية', 'Al-Jouf Agriculture Development Co'),
(68, 'بيشة الزراعيه', '', '', '', 'شركة بيشة للتنمية الزراعية', 'Bishah Agriculture Development Co'),
(69, 'جازان للتنمية', '', '', '', 'شركة جازان للتنمية', 'Jazan Development Co'),
(70, 'الاتصالات', '', '', '', 'شركة الاتصالات السعودية', 'Saudi Telecom'),
(71, 'اتحاد اتصالات', '', '', '', 'شركة إتحاد إتصالات', 'Etihad Etisalat Co'),
(72, 'زين السعودية', '', '', '', 'شركة الاتصالات المتنقلة السعودية', 'Mobile Telecommunications Company Saudi Arabia'),
(73, 'عذيب للاتصالات', '', '', '', 'شركة إتحاد عذيب للاتصالات', 'Etihad Atheeb Telecommunication Company'),
(74, 'المتكاملة', '', '', '', 'الشركة السعودية للإتصالات المتكاملة', 'Saudi Integrated Telecom Company'),
(75, 'التعاونية ', '', '', '', 'شركة التعاونية للتأمين', 'The Company for Cooperative Insurance'),
(76, 'ملاذ للتأمين', '', '', '', '', ''),
(77, 'ميدغلف للتأمين', '', '', '', '', ''),
(78, 'أليانز إس إف ', '', '', '', '', ''),
(79, 'سلامة', '', '', '', 'شركة سلامة للتأمين التعاوني', 'Salama Cooperative Insurance Co'),
(80, 'ولاء للتأمين', '', '', '', '', ''),
(81, 'الدرع العربي ', '', '', '', 'شركة الدرع العربي للتأمين التعاوني', 'Arabian Shield Cooperative Insurance Company'),
(82, 'ساب تكافل', '', '', '', 'ساب للتكافل', 'SABB Takaful'),
(83, 'سند', '', '', '', 'شركة سند للتأمين و إعادة التأمين التعاوني', 'Sanad Insurance and Reinsurance Cooperative Company'),
(84, 'سايكو', '', '', '', 'الشركة العربية السعودية للتأمين التعاوني', 'Saudi Arabian Cooperative Insurance Company'),
(85, 'وفا للتأمين', '', '', '', '', ''),
(86, 'إتحاد الخليج', '', '', '', 'شركة إتحاد الخليج للتأمين التعاوني', 'Gulf Union Cooperative Insurance Company'),
(87, 'الأهلي للتكافل', '', '', '', 'شركة الأهلي للتكافل', 'ALAHLI TAKAFUL COMPANY'),
(88, 'الأهلية', '', '', '', 'الشركة الأهلية للتأمين التعاوني', 'Al-Ahlia Insurance Company'),
(89, 'أسيج', '', '', '', 'المجموعة المتحدة للتأمين التعاوني', 'Allied Cooperative Insurance Group'),
(90, 'التأمين العربية ', '', '', '', 'شركة التأمين العربية التعاونية', 'Arabia Insurance Cooperative Company'),
(91, 'الاتحاد التجاري ', '', '', '', 'شركة الاتحاد التجاري للتأمين التعاوني', 'Trade Union Cooperative Insurance Company'),
(92, 'الصقر للتأمين ', '', '', '', 'شركة الصقر للتأمين التعاوني', 'Al Sagr Co-operative Insurance Co'),
(93, 'المتحدة للتأمين ', '', '', '', 'المجموعة المتحدة للتأمين التعاوني', 'Allied Cooperative Insurance Group'),
(94, 'الإعادة السعودية ', '', '', '', 'الشركة السعودية لإعادة التأمين(إعادة) التعاونية', 'Saudi Re for Cooperative Reinsurance Company'),
(95, 'بوبا العربية ', '', '', '', 'بوبا العربية للتأمين التعاوني', 'Bupa Arabia for Cooperative Insurance'),
(96, 'وقاية للتكافل', '', '', '', 'شركة وقاية للتأمين و إعادة التأمين التكافلي', 'Weqaya Takaful insurance and reinsurance company'),
(97, 'تكافل الراجحي ', '', '', '', 'شركة الراجحي للتأمين التعاوني', 'Al-Rajhi Company for Cooperative Insurance'),
(98, 'ايس', '', '', '', 'شركة أيس العربية للتأمين التعاوني', 'ACE ARABIA COOPERATIVE INSURANCE COMPANY'),
(99, 'اكسا- التعاونية', '', '', '', 'شركة اكسا للتأمين التعاوني', 'AXA Cooperative Insurance Company'),
(100, 'الخليجية العامة', '', '', '', 'الشركة الخليجية العامة للتأمين التعاوني', 'Gulf General Cooperative Insurance Company'),
(101, ' بروج للتأمين', '', '', '', 'شركة بروج للتأمين التعاوني', 'BURUJ COOPERATIVE INSURANCE COMPANY'),
(102, 'العالمية', '', '', '', 'شركة العالمية للتأمين التعاوني', 'Al Alamiya for Cooperative Insurance Company'),
(103, 'سوليدرتي تكافل', '', '', '', 'شركة سوليدرتي السعودية للتكافل', 'Solidarity Saudi Takaful Co'),
(104, 'الوطنية', '', '', '', 'الشركة الوطنية للتأمين', 'Wataniya Insurance Company'),
(105, 'أمانة للتأمين', '', '', '', 'شركة أمانة للتأمين التعاوني', 'Amana Cooperative Insurance Co'),
(106, 'عناية', '', '', '', 'شركة عناية السعودية للتأمين التعاوني', 'Saudi Enaya Cooperative Insurance Company'),
(107, 'الإنماء طوكيو مارين', '', '', '', 'شركة الإنماء طوكيو مارين', 'Alinma Tokio Marine Co'),
(108, 'المصافي', '', '', '', 'شركة المصافي العربية السعودية', 'Saudi Arabia Refineries Co'),
(109, 'المتطورة', '', '', '', 'الشركة السعودية للصناعات المتطورة', 'Saudi Advanced Industries Co'),
(110, 'الاحساء للتنميه', '', '', '', 'شركة الاحساء للتنمية', 'Al-Ahsa Development Co'),
(111, 'سيسكو', '', '', '', '', ''),
(112, 'عسير', '', '', '', 'شركة عسير للتجارة والسياحة والصناعة', 'Aseer Trading, Tourism & Manufacturing Co.'),
(113, 'الباحة', '', '', '', 'شركة الباحة للإستثمار والتنمية', 'Al-Baha Investment and Development co'),
(114, 'المملكة', '', '', '', 'شركة المملكة القابضة', 'Kingdom Holding Company'),
(115, 'تكوين', '', '', '', 'شركة تكوين المتطورة للصناعات', 'Takween Advanced Industries'),
(116, 'بى سى آى', '', '', '', '', ''),
(117, 'معادن', '', '', '', 'شركة التعدين العربية السعودية', 'Saudi Arabian Mining Company'),
(118, 'أسترا الصناعية', '', '', '', 'مجموعة أسترا الصناعية', 'Astra Industrial Group'),
(119, 'مجموعة السريع', '', '', '', 'شركة مجموعة السريع التجارية الصناعية', 'Al Sorayai Trading And Industrial Group Company'),
(120, 'شاكر', '', '', '', 'شركة الحسن غازي إبراهيم شاكر', 'Al Hassan Ghazi Ibrahim Shaker'),
(121, 'الدوائية', '', '', '', 'الشركة السعودية للصناعات الدوائية والمستلزمات الطبية', 'Saudi Pharmaceutical Indust.& Med. Appliances Corp.'),
(122, 'زجاج', '', '', '', 'شركة الصناعات الزجاجية الوطنية', 'The National Co. for Glass Industries'),
(123, 'فيبكو', '', '', '', '', ''),
(124, 'معدنية', '', '', '', '', ''),
(125, 'الكيميائيه السعوديه', '', '', '', 'الشركة الكيميائية السعودية', 'Saudi Chemical Company'),
(126, 'صناعة الورق', '', '', '', 'الشركة السعودية لصناعة الورق', 'Saudi Paper Manufacturing Co'),
(127, 'العبداللطيف', '', '', '', 'شركة العبداللطيف للاستثمار الصناعي', 'ALABDULLATIF INDUSTRIAL INVESTMENT CO.'),
(128, 'الصادرات', '', '', '', 'الشركة السعودية للصادرات الصناعية', 'Saudi Industrial Export Co'),
(129, 'أسلاك', '', '', '', 'شركة إتحاد مصانع الأسلاك', 'United Wire Factories Company'),
(130, 'مجموعة المعجل', '', '', '', 'شركة مجموعة محمد المعجل', 'Mohammad Al Mojil Group Company'),
(131, 'الأنابيب السعودية', '', '', '', 'الشركة السعودية لأنابيب الصلب', 'Saudi Steel Pipe Company'),
(132, 'الخضري', '', '', '', 'شركة أبناء عبدالله عبدالمحسن الخضري', 'Abdullah A. M. Al-Khodari Sons Company'),
(133, 'الخزف', '', '', '', 'شركة الخزف السعودي', 'Saudi Ceramic Co'),
(134, 'الجبس', '', '', '', 'شركة الجبس الأهلية', 'National Gypsum Company'),
(135, 'الكابلات', '', '', '', 'شركة الكابلات السعودية', 'Saudi Cable Company'),
(136, 'صدق', '', '', '', '', ''),
(137, 'اميانتيت', '', '', '', 'شركة اميانتيت العربية السعودية', 'Saudi Arabian Amiantit Co'),
(138, 'أنابيب', '', '', '', '', ''),
(139, 'الزامل للصناعة', '', '', '', 'شركة الزامل للاستثمار الصناعي', 'Zamil Industrial Investment Co'),
(140, 'البابطين', '', '', '', 'شركة البابطين للطاقة و الاتصالات', ''),
(141, 'الفخارية', '', '', '', 'الشركة السعودية لإنتاج الأنابيب الفخارية', 'Saudi vitrified clay pipes co'),
(142, 'مسك', '', '', '', '', ''),
(143, 'البحر الأحمر ', '', '', '', '', ''),
(144, 'العقارية', '', '', '', '', ''),
(145, 'طيبة للاستثمار ', '', '', '', '', ''),
(146, 'مكة للانشاء ', '', '', '', '', ''),
(147, 'التعمير', '', '', '', '', ''),
(148, 'إعمار', '', '', '', '', ''),
(149, 'جبل عمر ', '', '', '', '', ''),
(150, 'دار الأركان', '', '', '', '', ''),
(151, 'مدينة المعرفة ', '', '', '', '', ''),
(152, 'البحري', '', '', '', '', ''),
(153, 'النقل الجماعي ', '', '', '', '', ''),
(154, 'مبرد', '', '', '', '', ''),
(155, 'بدجت السعودية ', '', '', '', '', ''),
(156, 'تهامه للاعلان', '', '', '', '', ''),
(157, 'الأبحاث و التسويق', '', '', '', '', ''),
(158, 'طباعة وتغليف', '', '', '', '', ''),
(159, 'الطيار', '', '', '', '', ''),
(160, 'الفنادق', '', '', '', '', ''),
(161, 'شمس', '', '', '', '', '');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
