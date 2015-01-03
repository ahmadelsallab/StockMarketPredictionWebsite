-- phpMyAdmin SQL Dump

--
-- Database: `django2`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_twitte`
--

CREATE TABLE IF NOT EXISTS `app_twitte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `twitter_id` varchar(200) NOT NULL,
  `user_id` varchar(200) NOT NULL,
  `text` varchar(200) CHARACTER SET utf8 NOT NULL,
  `created_at` varchar(200) NOT NULL,
  `user_followers_count` int(11) NOT NULL,
  `user_profile_image_url` varchar(500) NOT NULL,
  `pub_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `twitter_id` (`twitter_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=351 ;

--
-- Dumping data for table `app_twitte`
--

INSERT INTO `app_twitte` (`id`, `twitter_id`, `user_id`, `text`, `created_at`, `user_followers_count`, `user_profile_image_url`, `pub_date`) VALUES
(37, '540178956234674177', '1154361139', 'RT @ebdaacenter_01: #دورة_استثمر_راتبك_و_ضاعف_ثروتك\nتعمل من سنوات وليس لديك منزل ملك او استثمار \nستجد الحل بأذن الله بالدورة\n0508331235 htt…', 'Wed Dec 03 16:21:13 +0000 2014', 99074, 'http://pbs.twimg.com/profile_images/535952576978513920/SQHnpP_5_normal.jpeg', '2014-12-03 16:21:45'),
(38, '540178936324308992', '2270351687', 'RT @dfran456: تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/hi…', 'Wed Dec 03 16:21:09 +0000 2014', 6939, 'http://pbs.twimg.com/profile_images/524866767219204097/jDXLylHM_normal.jpeg', '2014-12-03 16:21:45'),
(39, '540178753666572289', '906316400', 'RT @bent_sa3: تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/WA…', 'Wed Dec 03 16:20:25 +0000 2014', 551113, 'http://pbs.twimg.com/profile_images/378800000760671808/89d7191b9d5fc85bedba2a12bd3de868_normal.jpeg', '2014-12-03 16:21:45'),
(40, '540178699401060353', '2572241282', 'RT @dfran456: تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/hi…', 'Wed Dec 03 16:20:12 +0000 2014', 5537, 'http://pbs.twimg.com/profile_images/539435811104518145/OWE7-xOK_normal.jpeg', '2014-12-03 16:21:45'),
(41, '540178664264970240', '541597317', 'RT @dfran456: تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/hi…', 'Wed Dec 03 16:20:04 +0000 2014', 289502, 'http://pbs.twimg.com/profile_images/378800000722795709/82019a4cecff23fdc0c52c375362aaee_normal.jpeg', '2014-12-03 16:21:46'),
(42, '540178183316717568', '1354771974', 'RT @dora56789: تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/z…', 'Wed Dec 03 16:18:09 +0000 2014', 13131, 'http://pbs.twimg.com/profile_images/539483393658875904/73odc4J3_normal.jpeg', '2014-12-03 16:21:46'),
(43, '540178180112281600', '969972264', 'د. إحسان: مبيعات النفط الغير المنضبط من مؤثرات سوق #النفط #اوبك #الأحساء_واحة_استثمار', 'Wed Dec 03 16:18:08 +0000 2014', 14, 'http://pbs.twimg.com/profile_images/427343840320569344/c7kxXgFi_normal.jpeg', '2014-12-03 16:21:46'),
(44, '540177593916346368', '2661610219', 'RT @ebdaacenter_01: #دورة_استثمر_راتبك_و_ضاعف_ثروتك\nتعمل من سنوات وليس لديك منزل ملك او استثمار \nستجد الحل بأذن الله بالدورة\n0508331235 htt…', 'Wed Dec 03 16:15:49 +0000 2014', 3358, 'http://pbs.twimg.com/profile_images/504813853020917760/wgbbEgxT_normal.jpeg', '2014-12-03 16:21:46'),
(45, '540177452941590528', '2152186793', 'تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/hToyoquqIo\n٨', 'Wed Dec 03 16:15:15 +0000 2014', 40473, 'http://pbs.twimg.com/profile_images/501735436033589248/okwKrX86_normal.jpeg', '2014-12-03 16:21:46'),
(46, '540177443357618176', '2149558096', 'تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/ow6SARB8ee\n٦', 'Wed Dec 03 16:15:13 +0000 2014', 27207, 'http://pbs.twimg.com/profile_images/378800000638257165/11edbbe37efa46b6506d0101bbf9ab7f_normal.jpeg', '2014-12-03 16:21:46'),
(47, '540177442397110275', '2152174805', 'تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/oui6dFza2o\n٢', 'Wed Dec 03 16:15:12 +0000 2014', 14245, 'http://pbs.twimg.com/profile_images/501330883010232320/X39SLGfY_normal.jpeg', '2014-12-03 16:21:46'),
(48, '540177438458671105', '1914470288', 'تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/m7FjyI3bI1\n١٠', 'Wed Dec 03 16:15:11 +0000 2014', 31031, 'http://pbs.twimg.com/profile_images/499527384341557248/EQ0DYIWI_normal.jpeg', '2014-12-03 16:21:46'),
(49, '540177430837604352', '1912664406', 'تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/WwklxAiFma\n١', 'Wed Dec 03 16:15:10 +0000 2014', 12148, 'http://pbs.twimg.com/profile_images/498752245232455680/PnqMxhpv_normal.jpeg', '2014-12-03 16:21:46'),
(50, '540177426307743745', '2157079511', 'تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/JDnQYVZwJs\n٤', 'Wed Dec 03 16:15:09 +0000 2014', 40071, 'http://pbs.twimg.com/profile_images/500961333529939968/O4FluOmF_normal.jpeg', '2014-12-03 16:21:46'),
(51, '540177417537474560', '2157064420', 'تبي تزيد دخلك وانت ببيتك؟\nدورة مجانا\nاكسب ألآف آلدولآرآت في استثمار العملات\nسجل إسمك رقمك ايميلك\nالتسجيل مفتوح\nhttp://t.co/zSPfnJniDr\n١', 'Wed Dec 03 16:15:07 +0000 2014', 47961, 'http://pbs.twimg.com/profile_images/500731900030230528/2VWMbxtP_normal.jpeg', '2014-12-03 16:21:46'),
(52, '540179056533065730', '1270225987', 'RT @abu_saleh_0: أحد الحسابات متابعينه يفوق ٢٠ الف كان يقول عن س الجوف وهي على مشارف ٢٥ أنها أفضل استثمار في شركات الأسمنت وتداخلت معه ولكن…', 'Wed Dec 03 16:21:37 +0000 2014', 492, 'http://pbs.twimg.com/profile_images/509220128827797504/SvzSrDQi_normal.jpeg', '2014-12-03 16:22:02'),
(67, '540240751481720832', '496797948', '@null 0.0014469057481145032965', 'Wed Dec 03 20:26:46 +0000 2014', 82103, 'http://pbs.twimg.com/profile_images/540162061070659585/csPsic1J_normal.jpeg', '2014-12-03 20:27:08'),
(68, '540240750739750912', '2802126685', 'RT @CezarLaLv: @hm_registered https://t.co/PqWwQ1aEWu  RT!', 'Wed Dec 03 20:26:46 +0000 2014', 129, 'http://pbs.twimg.com/profile_images/509745574954803200/wE3mek62_normal.jpeg', '2014-12-03 20:27:08'),
(70, '540240750256992256', '246806484', 'RT @CescOffender: "@chelseafc: Who was our hat-trick hero when we beat Spurs 4-0 at Stamford Bridge in 2002?"\nTrick question, Chelsea didn''…', 'Wed Dec 03 20:26:46 +0000 2014', 3254, 'http://pbs.twimg.com/profile_images/536869782318878722/Hlnn9rrr_normal.jpeg', '2014-12-03 20:27:08'),
(71, '540240750210846720', '1953196135', 'RT @ChurchOfFutbol: Mourinho is right to criticize Stamford Bridge. All I hear is Spurs fans chanting, and Chelsea is winning 2-0.', 'Wed Dec 03 20:26:46 +0000 2014', 765, 'http://pbs.twimg.com/profile_images/539255136132947968/y2HMtNGa_normal.jpeg', '2014-12-03 20:27:08'),
(72, '540240749955411969', '2398203194', '40'' Arsenal 0 - 0 Soton', 'Wed Dec 03 20:26:46 +0000 2014', 150, 'http://pbs.twimg.com/profile_images/446347922163003392/g506b-H3_normal.jpeg', '2014-12-03 20:27:08'),
(73, '540240749422710785', '250331754', 'Might start calling us Hull City 0 #hcafc', 'Wed Dec 03 20:26:46 +0000 2014', 141, 'http://pbs.twimg.com/profile_images/532322221285724160/3v11zaDi_normal.jpeg', '2014-12-03 20:27:08'),
(74, '540240749397168129', '1689659264', 'RT @Arsenal: Martinez holds a Tadic corner under pressure. The young keeper looks assured again tonight. (39) 0-0 #AFCvSFC', 'Wed Dec 03 20:26:46 +0000 2014', 320, 'http://pbs.twimg.com/profile_images/523222028724469760/EcmrmPpn_normal.jpeg', '2014-12-03 20:27:08'),
(75, '540240749154299904', '944646714', 'RT @Atleti: 69''. 0-1. Gran incorporación de @Cebolla_CR11 que ensaya el disparo con la zurda ¡Balón alto! #HospitaletAtleti #CopaDelRey #Aú…', 'Wed Dec 03 20:26:46 +0000 2014', 948, 'http://pbs.twimg.com/profile_images/504982469154967552/-24Li8lL_normal.jpeg', '2014-12-03 20:27:08'),
(76, '540240748634210304', '930312529', 'RT @mxnquillo: 33: GOAL! Pelle finds a succulent ball from Wanyama and he tapped in the ball, 1-0 to the Saints', 'Wed Dec 03 20:26:46 +0000 2014', 1418, 'http://pbs.twimg.com/profile_images/539144019885162497/uPvMSo3l_normal.jpeg', '2014-12-03 20:27:08'),
(77, '540240748512563200', '1683845516', '@busrabagdogaan KULAKTAN ALDIM BE SEN NE DİYON -SDFKOŞSLDFÖ230O*0', 'Wed Dec 03 20:26:46 +0000 2014', 1369, 'http://pbs.twimg.com/profile_images/539567695667429377/BiRqynqy_normal.jpeg', '2014-12-03 20:27:08'),
(78, '540240748307021824', '2354828159', 'RT @kevans835: 6-0 pépère des Lyonnaises face à Saint-Etienne ! Bouuum #TeamOL #OLFeminin #AHOU', 'Wed Dec 03 20:26:46 +0000 2014', 201, 'http://pbs.twimg.com/profile_images/540191983571333122/ZxvOK7VZ_normal.jpeg', '2014-12-03 20:27:08'),
(79, '540240748177018880', '262607962', 'RT @CD_Atleti: GOOOOOOOOL DE ANTOOOOOINE GRIEEEEEEZMANN. Cabezazo del 7 a la red tras el centro de Gámez. Min. 68. Hospitalet 0 Atleti 1.', 'Wed Dec 03 20:26:46 +0000 2014', 650, 'http://pbs.twimg.com/profile_images/505519785455923201/onBHTqxj_normal.jpeg', '2014-12-03 20:27:08'),
(80, '540240747799121920', '769062553', 'Today''s Reminders notice is now available via our website. https://t.co/UMxYwYtpvG', 'Wed Dec 03 20:26:46 +0000 2014', 26, 'http://pbs.twimg.com/profile_images/2523785413/Screen_shot_2012-08-20_at_7.49.13_PM_normal.png', '2014-12-03 20:27:08'),
(81, '540240747153596416', '1241621737', 'RT @mrferomonas: El exito creciente deL #ViagraFemenino y de Soloparaellas en la WEB via: LUN http://t.co/RwHjEJmxCu @dondatos  RT', 'Wed Dec 03 20:26:45 +0000 2014', 1505, 'http://pbs.twimg.com/profile_images/3338254144/b98ab9fefb04c8255e39c3a909d64624_normal.jpeg', '2014-12-03 20:27:08'),
(82, '540240834688741377', '626740946', 'Nuevos seguidores: 1, unfollowers: 0 (21:27) #TuitUtil http://t.co/7X2cLT1ZPV', 'Wed Dec 03 20:27:06 +0000 2014', 478, 'http://pbs.twimg.com/profile_images/520680789072416768/hkE_oUDj_normal.jpeg', '2014-12-03 20:27:26'),
(83, '540240834638004224', '1609055809', 'Barack Obama considera "bastante serias" las reformas acometidas en España: EUROPA PRESS Sin embargo, el presi... http://t.co/MgEBcq1gJf', 'Wed Dec 03 20:27:06 +0000 2014', 13, 'http://pbs.twimg.com/profile_images/378800000162457665/df1a8d8bec8c12012dce72f1a82ac174_normal.jpeg', '2014-12-03 20:27:26'),
(84, '540240834575466496', '1163900786', 'Ainda apurando votos de vetos. Não havendo coro, cai seção e volta tudo à estaca 0. PLN36 aguardando...derrubada, esperamos.\n#SouContraPLN36', 'Wed Dec 03 20:27:06 +0000 2014', 645, 'http://pbs.twimg.com/profile_images/3231552889/4f0c4c5b8354fc701b179aa4d9166b40_normal.jpeg', '2014-12-03 20:27:26'),
(85, '540240834503770113', '1583818158', 'Barack Obama considera "bastante serias" las reformas acometidas en España: EUROPA PRESS Sin embargo, el presi... http://t.co/h8sHwjJTNP', 'Wed Dec 03 20:27:06 +0000 2014', 48, 'http://pbs.twimg.com/profile_images/378800000529979797/2d318cc585c094345c5c3b88d95f64a4_normal.jpeg', '2014-12-03 20:27:26'),
(86, '540240834378334208', '1674146502', 'счет 1-2. первый тайм. \nвторой тайм 0.5 меньше надо !!))) \nхочу точный счет угадать хаха', 'Wed Dec 03 20:27:06 +0000 2014', 53, 'http://pbs.twimg.com/profile_images/539025952458567682/EHAS_RaD_normal.jpeg', '2014-12-03 20:27:26'),
(87, '540240834281476096', '2502419388', 'هل استغفرت اليوم ؟ \n                                     \nنسيت لا بأس ، ردد الآن \nأستغفر الله ، أستغفر الله ، أستغفر الله \n  -ذكر بها غيرك ♡', 'Wed Dec 03 20:27:06 +0000 2014', 1385, 'http://pbs.twimg.com/profile_images/539723933155487744/MQzi1o-f_normal.jpeg', '2014-12-03 20:27:26'),
(88, '540240834218979328', '459846074', 'Wind 0.0 mph ---. Barometer 1014.2 mb, Falling. Temperature 76.3 °F. Rain today 0.00 in. Humidity 68%', 'Wed Dec 03 20:27:06 +0000 2014', 21, 'http://pbs.twimg.com/profile_images/1837515826/weatherstation03_l_normal.jpg', '2014-12-03 20:27:26'),
(89, '540240834214785024', '2785916781', 'RT @ZAMENZA: "A Mari não vai embora!!!!!!!!!!!!" (Jeff 1000000 X 0 Todos) #Malhação', 'Wed Dec 03 20:27:06 +0000 2014', 400, 'http://pbs.twimg.com/profile_images/538434417422004225/UYt2_4tK_normal.jpeg', '2014-12-03 20:27:26'),
(90, '540240834139271169', '1317103579', 'callate Thor 2.0 eres mas cule q undiano mallenco', 'Wed Dec 03 20:27:06 +0000 2014', 2, 'http://abs.twimg.com/sticky/default_profile_images/default_profile_1_normal.png', '2014-12-03 20:27:26'),
(91, '540240833656946688', '2813264254', '#7646 Bell &amp; Howell DNV6HD Rogue Infrared Night Vision 1080p HD Video Camera Camcorder http://t.co/qQkMUFLOUf\n\n... http://t.co/rnLLV4bNGC', 'Wed Dec 03 20:27:06 +0000 2014', 32, 'http://pbs.twimg.com/profile_images/519414060048084992/2Z8jCDg4_normal.jpeg', '2014-12-03 20:27:26'),
(92, '540240833640157184', '2359667309', 'RT @chelseafc: Chelsea 1 Tottenham 0 on 18 minutes. Hazard squeezes the ball past Lloris at the near-post after combining with Drogba. #CFC…', 'Wed Dec 03 20:27:06 +0000 2014', 28, 'http://pbs.twimg.com/profile_images/540240192817623040/h5sh2YdH_normal.jpeg', '2014-12-03 20:27:27'),
(93, '540240833312980992', '1335436776', 'Un tiburón tigre ataca a un pescador en la costa de Granada http://t.co/XDDrlBsWaw | http://t.co/LaK5iOltdQ', 'Wed Dec 03 20:27:06 +0000 2014', 10605, 'http://pbs.twimg.com/profile_images/3492097258/8c41c2503894d9c3831b9062e1e9a956_normal.png', '2014-12-03 20:27:27'),
(94, '540240832855830529', '2355222199', 'RT @cansinaymontuno: Por una Ley q logre la violencia 0 d verdad http://t.co/BFGfA1LFVb #EXISTEN3dic @MariaGilMorata @eugenioalcalde   @jua…', 'Wed Dec 03 20:27:06 +0000 2014', 1194, 'http://pbs.twimg.com/profile_images/485107798934421505/yPA3xF9x_normal.png', '2014-12-03 20:27:27'),
(96, '540240832737980416', '1538145704', 'RT @SouthamptonFC: 34: Dangerous cross from @ryanbertrand3 looks destined to find @GPelle19 but it''s headed clear. #saintsfc [0-0]', 'Wed Dec 03 20:27:06 +0000 2014', 177, 'http://pbs.twimg.com/profile_images/378800000755864059/2b2a24f75252fd5a908e62eddb83afb1_normal.jpeg', '2014-12-03 20:27:27'),
(97, '540240980335931392', '254569407', '@jeffowens_SN sounds great but who and the bang for the buck and return on investment is not what it once was', 'Wed Dec 03 20:27:41 +0000 2014', 363, 'http://pbs.twimg.com/profile_images/1255021535/app_full_proxy.php_normal.jpeg', '2014-12-03 20:28:08'),
(98, '540240955140354048', '2589777740', 'Don’t Justify Frivolous Spending by Calling It an Investment http://t.co/HVBLm0ISRl http://t.co/CcgHGtGFZP', 'Wed Dec 03 20:27:35 +0000 2014', 15, 'http://pbs.twimg.com/profile_images/482232859462090752/0AFpP8aO_normal.png', '2014-12-03 20:28:08'),
(99, '540240950304313344', '84631502', 'Don’t Justify Frivolous Spending by Calling It an Investment http://t.co/sPn7i6l5cE http://t.co/IEySnoyhrR', 'Wed Dec 03 20:27:34 +0000 2014', 439, 'http://pbs.twimg.com/profile_images/2656646455/7312e3eda90a9fd9fd80d762511e324c_normal.png', '2014-12-03 20:28:08'),
(100, '540240949868494848', '320732134', 'AthenaInvest Wins 2014 Wealth &amp; Finance Alternative Investment Award and Receives Fifth Patent ... http://t.co/RImaGGNQyK #alternativei...', 'Wed Dec 03 20:27:34 +0000 2014', 598, 'http://pbs.twimg.com/profile_images/1404445938/CapitalHedgeLogo_Final_normal.png', '2014-12-03 20:28:08'),
(101, '540240930197233665', '871247886', 'RT @REIHQ: CPE 100 Quarterly Sentiment Survey: Executives Eye 2016 as Peak Year; Multi-Family Still Rules http://t.co/ez0UVbHMtO #CRE #Real…', 'Wed Dec 03 20:27:29 +0000 2014', 227, 'http://pbs.twimg.com/profile_images/3654022098/7fc456c4dcd615232f3058318ac383ae_normal.jpeg', '2014-12-03 20:28:08'),
(102, '540240897477074944', '129379052', 'Investment Assistant I - Co... - Citizens Financial Group: (#Columbus, OH) http://t.co/kBhKgpQBXN #InvestmentBanking #cfgjobs #Job', 'Wed Dec 03 20:27:21 +0000 2014', 260, 'http://pbs.twimg.com/profile_images/2303686231/Logo_tmj_new2b_normal.png', '2014-12-03 20:28:08'),
(103, '540240895086706688', '21856757', 'RT @EMInvestment: Big changes in #Qatar, changes at sovereign fund, but also at Supreme Council for Economic Affairs and #Investment http:/…', 'Wed Dec 03 20:27:21 +0000 2014', 1686, 'http://pbs.twimg.com/profile_images/1641661558/314535_10150433331644993_667274992_10154872_1535393004_n_normal.jpg', '2014-12-03 20:28:08'),
(104, '540240892519800832', '343435968', 'RT @FibsFreitag: Winterschlussverkauf: Ukrainische Ministerposten gehen an ausländische Investmentbanker http://t.co/2bCjiw6evP', 'Wed Dec 03 20:27:20 +0000 2014', 463, 'http://pbs.twimg.com/profile_images/421985857147396096/FifKO9_t_normal.png', '2014-12-03 20:28:09'),
(105, '540240862920179712', '158059731', 'CERTNYS – Wells Fargo Real Estate Investment Corp. (0001616093) (Filer) http://t.co/j001yiWkfF', 'Wed Dec 03 20:27:13 +0000 2014', 531, 'http://pbs.twimg.com/profile_images/540238936720031745/ZV37-rDL_normal.png', '2014-12-03 20:28:09'),
(106, '540240856520081408', '186966085', 'Investment Clubs TICN: Sie selbst am Steuer Ihres Investments http://t.co/jdCUelJWoD …', 'Wed Dec 03 20:27:12 +0000 2014', 3638, 'http://pbs.twimg.com/profile_images/455474584569905153/2n-wUFuw_normal.jpeg', '2014-12-03 20:28:09'),
(107, '540240856360312832', '1337585012', 'Want to Make Great Investment Decisions? Just Look Left https://t.co/GCRxvUuVqJ', 'Wed Dec 03 20:27:12 +0000 2014', 1644, 'http://pbs.twimg.com/profile_images/473568783450120192/mUMqQ1m9_normal.png', '2014-12-03 20:28:09'),
(109, '540240843127656448', '494023726', 'RT @Jon_Proctor92: London Palestine Action shut down Barclay''s Piccadilly square over their investment in Elbit systems. #FreePalestine htt…', 'Wed Dec 03 20:27:08 +0000 2014', 427, 'http://pbs.twimg.com/profile_images/536683110776455168/1P4eujrh_normal.jpeg', '2014-12-03 20:28:09'),
(110, '540240838610018304', '2564145908', '"@WSJ: China planning to open up state-owned firms to private investment. The numbers: http://t.co/EvmrWFUscn" To get in on the party floor', 'Wed Dec 03 20:27:07 +0000 2014', 12, 'http://pbs.twimg.com/profile_images/506775562833391616/6eb9V7H1_normal.jpeg', '2014-12-03 20:28:09'),
(111, '540240829466820608', '1055932591', 'Investment bankers steal trillions from humanity and in return they indebt the masses.', 'Wed Dec 03 20:27:05 +0000 2014', 4968, 'http://pbs.twimg.com/profile_images/3631078578/f979f5925f87742f7691219c8ab52bf0_normal.jpeg', '2014-12-03 20:28:09'),
(112, '540244715950837760', '67300980', 'RT @ClydeWilliams46: #NHT How does purchasing an entity mired in debt + debt write off + never made a profit + no skill in NHT to turn arou…', 'Wed Dec 03 20:42:32 +0000 2014', 124, 'http://pbs.twimg.com/profile_images/497949615569006593/KiNLugPa_normal.jpeg', '2014-12-03 20:42:51'),
(113, '540244710737338368', '424921307', 'Only got 736 songs and still got 101gs best investment can''t have enough music on my phone', 'Wed Dec 03 20:42:30 +0000 2014', 254, 'http://pbs.twimg.com/profile_images/540230605070688257/3Jwq8_DJ_normal.jpeg', '2014-12-03 20:42:51'),
(114, '540244705431531520', '2271943398', '¿ Qué tiene este cariño que nunca muere ? By @Danigg95', 'Wed Dec 03 20:42:29 +0000 2014', 28180, 'http://pbs.twimg.com/profile_images/538821891549851649/IGE2LZx4_normal.jpeg', '2014-12-03 20:42:52'),
(115, '540244703934173186', '1123659882', 'RT @CollegeSummit: Study shows community colleges'' return on investment: http://t.co/7JewpNMzHQ', 'Wed Dec 03 20:42:29 +0000 2014', 1012, 'http://pbs.twimg.com/profile_images/3167796279/6b6792173ac9008223913a38fe778421_normal.jpeg', '2014-12-03 20:42:52'),
(116, '540244698489954304', '365686428', '@YorkshireFirst Decades of misplaced investment behind us. How many before us?', 'Wed Dec 03 20:42:28 +0000 2014', 10, 'http://pbs.twimg.com/profile_images/3310573182/2f07b44f596d13293c7628fc571bb768_normal.jpeg', '2014-12-03 20:42:52'),
(117, '540244690009096192', '17396685', '#LewesSitP Is there a scientific renaissance is Islamic countries? It seems so; increases in investment &amp; results, papers &amp; patents, ...', 'Wed Dec 03 20:42:26 +0000 2014', 489, 'http://pbs.twimg.com/profile_images/64657969/joem_normal.gif', '2014-12-03 20:42:52'),
(118, '540244676046249984', '388731865', 'RT @Chicago_Reader: Only #MayorRahm could figure out a way to make pre-K for poor kids benefit investment bankers. http://t.co/zIomqRRHam', 'Wed Dec 03 20:42:22 +0000 2014', 859, 'http://pbs.twimg.com/profile_images/477274711563317248/TLB_blEe_normal.jpeg', '2014-12-03 20:42:52'),
(119, '540244649005563905', '632443951', 'Be patient with yourself. Self-growth is tender; it’s holy ground. There’s no greater investment. Stephen Covey', 'Wed Dec 03 20:42:16 +0000 2014', 1250, 'http://pbs.twimg.com/profile_images/457608477062340608/ZA7Kk2yK_normal.jpeg', '2014-12-03 20:42:52'),
(120, '540244634937466881', '18453099', 'RT @StefanBielau: Massive investment in alternative UA by @King_Games http://t.co/eQFFSIfaAC', 'Wed Dec 03 20:42:12 +0000 2014', 4006, 'http://pbs.twimg.com/profile_images/68908629/uusi_toimisto_normal.jpg', '2014-12-03 20:42:52'),
(121, '540244618814554112', '361136609', '@UMaine trustees'' investment committee voted 4-0 to eliminate direct investments in coal-mining companies &amp; to screen future investments.', 'Wed Dec 03 20:42:09 +0000 2014', 177, 'http://pbs.twimg.com/profile_images/427897700567089152/Tf2vjhw7_normal.jpeg', '2014-12-03 20:42:52'),
(122, '540244618714296320', '1060578475', 'Qatar Investment authority moderniser removed as head of $300bn fund #Harrods  http://t.co/wbz36qLKJ3', 'Wed Dec 03 20:42:09 +0000 2014', 19671, 'http://pbs.twimg.com/profile_images/3064448154/98ee637272e2796d40f0301a6b823b7b_normal.jpeg', '2014-12-03 20:42:52'),
(123, '540244617245888512', '148473927', 'UN #Climate Chief: Investment in Fossil Fuels Becoming ''More and More Risky'' http://t.co/Ds9HrujCBs', 'Wed Dec 03 20:42:08 +0000 2014', 2383, 'http://pbs.twimg.com/profile_images/1372417123/Nirvana-nirvana-65524_1024_768fulllbig_normal.jpg', '2014-12-03 20:42:52'),
(124, '540244604423905280', '286153784', 'RT @tokaiama: 過去最悪を記録した生活保護世帯と富裕層への課税\nhttp://t.co/Cu4A19s2Oq', 'Wed Dec 03 20:42:05 +0000 2014', 90, 'http://pbs.twimg.com/profile_images/1321100460/C004_normal.jpg', '2014-12-03 20:42:52'),
(125, '540244602943733760', '87055873', 'Stronger investment of institutional dollars in research', 'Wed Dec 03 20:42:05 +0000 2014', 674, 'http://pbs.twimg.com/profile_images/3221323960/e2ea58185a9763e895eae2409a03f3d0_normal.jpeg', '2014-12-03 20:42:52'),
(126, '540244580390543360', '26188073', 'RT @BKFUniversity: your investment has the ability AND high likelihood of appreciating in price and value.', 'Wed Dec 03 20:41:59 +0000 2014', 402, 'http://pbs.twimg.com/profile_images/524233754126974976/GrPL6Rqk_normal.jpeg', '2014-12-03 20:42:52'),
(127, '540245444203659264', '30986638', 'Want an #investment house that makes you $$? Positive #cashflow search #Duck oceanfronts http://t.co/kU4rqpqCck http://t.co/Db4HWHgpiE', 'Wed Dec 03 20:45:25 +0000 2014', 127, 'http://pbs.twimg.com/profile_images/494528479510032384/KAU1RiWa_normal.jpeg', '2014-12-03 20:45:46'),
(128, '540245443016687618', '141748686', 'Learn more about #OperationHomefront, which offers free premium investment management to those who have served: http://t.co/wyA5uYXqsj', 'Wed Dec 03 20:45:25 +0000 2014', 2748, 'http://pbs.twimg.com/profile_images/533333549022060544/cWOF0Fyh_normal.jpeg', '2014-12-03 20:45:46'),
(129, '540245442664357888', '2815369204', 'How much value do home improvements add to a property? http://t.co/Ih7jXOVAmI #yorkshirehour #investment #propertylettings', 'Wed Dec 03 20:45:25 +0000 2014', 35, 'http://pbs.twimg.com/profile_images/533608273828909056/PHEQ1AAt_normal.jpeg', '2014-12-03 20:45:46'),
(130, '540245434414170112', '17527932', 'Commercial real estate investment firm is looking for a dedicated Investment Analyst to join their successful team http://t.co/46slIpC5vr', 'Wed Dec 03 20:45:23 +0000 2014', 2233, 'http://pbs.twimg.com/profile_images/67760096/I_love_McNak_sign_forTwitter_normal.jpg', '2014-12-03 20:45:46'),
(131, '540245431322542080', '2761750820', 'Business seems to be buzzing at the IoD London Pall Mall this morning. We''re busy promoting international investment in UK businesses.', 'Wed Dec 03 20:45:22 +0000 2014', 44, 'http://pbs.twimg.com/profile_images/524165457939419137/16Q7GKt4_normal.jpeg', '2014-12-03 20:45:46'),
(132, '540245430228246529', '199226402', '10 Real Estate Markets to Keep An Eye on! #Investors #Investment #RealEstate', 'Wed Dec 03 20:45:22 +0000 2014', 137, 'http://pbs.twimg.com/profile_images/471747299035459585/iDuHYIac_normal.jpeg', '2014-12-03 20:45:46'),
(133, '540245415376199680', '358227694', 'Love how Walter just asked for $70,000 as a seed investment into making 4 pounds of meth every week. #BreakingBad', 'Wed Dec 03 20:45:18 +0000 2014', 40763, 'http://pbs.twimg.com/profile_images/378800000655438109/69ac36622c27fc7e696f586d7ae02bff_normal.jpeg', '2014-12-03 20:45:46'),
(134, '540245407205310464', '2893849735', '''Post-seed'' investing is a strategy, not an investment stage, says Bullpen Capital partner - http://t.co/OTRKELxdJ0', 'Wed Dec 03 20:45:17 +0000 2014', 311, 'http://pbs.twimg.com/profile_images/531127182605561857/ZRhyTGuz_normal.jpeg', '2014-12-03 20:45:46'),
(135, '540245391971983360', '1723563360', 'RT @canativeobt: UN #Climate Chief: Investment in Fossil Fuels Becoming ''More and More Risky'' http://t.co/Ds9HrujCBs', 'Wed Dec 03 20:45:13 +0000 2014', 6315, 'http://pbs.twimg.com/profile_images/378800000402599044/3267a492bb835d3dc0d7910ce8b173bd_normal.jpeg', '2014-12-03 20:45:47'),
(136, '540245391888089088', '61661638', 'Virtus Investment Partners Upgraded at Zacks $VRTS http://t.co/5MpstpuEDq', 'Wed Dec 03 20:45:13 +0000 2014', 4892, 'http://pbs.twimg.com/profile_images/541252987/Image5_normal.jpg', '2014-12-03 20:45:47'),
(137, '540245381490425856', '526657967', 'Is good health a sound investment? http://t.co/7t10760hfQ #HealthyLiving', 'Wed Dec 03 20:45:10 +0000 2014', 1258, 'http://pbs.twimg.com/profile_images/2028965919/Stratmish_Twitter_Avatar_FNL_normal.jpg', '2014-12-03 20:45:47'),
(138, '540245377895522305', '1876179516', 'RT @EdwinaOHart: .@CHCymru call for additional investment from #autumnstatement to be spent on #supportingpeople #prevention agenda http://…', 'Wed Dec 03 20:45:10 +0000 2014', 825, 'http://pbs.twimg.com/profile_images/498187261830119424/uOSlSWiN_normal.jpeg', '2014-12-03 20:45:47'),
(139, '540245376800796672', '16068973', 'You can''t just run around saying college is an investment as if a piece of paper appreciates in value.', 'Wed Dec 03 20:45:09 +0000 2014', 10663, 'http://pbs.twimg.com/profile_images/428027887527022592/ukoAU4Xt_normal.jpeg', '2014-12-03 20:45:47'),
(140, '540245376649801728', '94128075', '#International #CRE investment has been picking up. Take a look at our list of top locations. http://t.co/p3tGWXHmvp http://t.co/9BwkxXKTSU', 'Wed Dec 03 20:45:09 +0000 2014', 6392, 'http://pbs.twimg.com/profile_images/378800000539037859/3ea942fa6492dd01e5469e781481a4e5_normal.jpeg', '2014-12-03 20:45:47'),
(141, '540245358941458432', '517735964', 'What Buyers Should Look for When Purchasing an #Investment Property - http://t.co/dtF3zl80bS', 'Wed Dec 03 20:45:05 +0000 2014', 67, 'http://pbs.twimg.com/profile_images/2190149677/Waddell_Building_sign_normal.jpg', '2014-12-03 20:45:47'),
(142, '539150440688939008', '28737726', 'Worldwide School new students this week are from: Switzerland, Brazil, Russia, Holland, Colombia, Belgium, France, Korea and Saudi Arabia.', 'Sun Nov 30 20:14:16 +0000 2014', 227, 'http://pbs.twimg.com/profile_images/489228211138490368/Q0n-cPgV_normal.jpeg', '2014-12-03 20:45:49'),
(143, '537606649616535552', '265145204', 'Best wishes dear friend today its your,never give up your dreams,Hugs #UK #Holland#Canada#Saudi Arabia #France #Egypt http://t.co/xXlojnqXGN', 'Wed Nov 26 13:59:48 +0000 2014', 830, 'http://pbs.twimg.com/profile_images/534920319287693312/4Z10cdHD_normal.jpeg', '2014-12-03 20:45:49'),
(144, '540110772341207040', '2647548872', '#Politics Saudi- Hollande Alwaleed discuss investment bilateral ties: …  Company (KHC) met French President Fr...  http://t.co/IPWqKauezW', 'Wed Dec 03 11:50:17 +0000 2014', 120, 'http://pbs.twimg.com/profile_images/489027088137986048/7_FNVYd7_normal.jpeg', '2014-12-03 20:45:52'),
(145, '540084203572850688', '495328347', 'RT @rebelready: Judge denied #GlenBeck #Blaze dismissal motion.  The Saudi dude LOL is a French Model &amp; #ItWorks distributor http://t.co/e3…', 'Wed Dec 03 10:04:43 +0000 2014', 1075, 'http://pbs.twimg.com/profile_images/514742945279246336/OA-fBsIN_normal.jpeg', '2014-12-03 20:45:52'),
(146, '540067803982999552', '372694280', 'RT @3WhitehallPlace: Hinkley Point C update. We are delighted Saudi Arabia wants to rebuild Britain''s nuclear industry by investing in Fren…', 'Wed Dec 03 08:59:33 +0000 2014', 142, 'http://pbs.twimg.com/profile_images/1540842181/Tbilisi_2007_normal.jpg', '2014-12-03 20:45:52'),
(147, '540058995348611072', '507078507', 'Saudi Press 2 Riyadh: Alsharq newspaper highlighted the adoption by the French House of Representatives overwh... http://t.co/v7bsGMENkx', 'Wed Dec 03 08:24:32 +0000 2014', 6127, 'http://pbs.twimg.com/profile_images/1864073751/185245_102730193164109_100002813866928_15260_221115_n_normal.jpg', '2014-12-03 20:45:52'),
(148, '540057902783160320', '2788032008', 'Do you want to be informed of the french cultural activities in Saudi Arabia ? Like the fan page of the Cooperation and Cultural action...', 'Wed Dec 03 08:20:12 +0000 2014', 45, 'http://pbs.twimg.com/profile_images/510070458117394433/Jo8FeoPf_normal.jpeg', '2014-12-03 20:45:52'),
(149, '539971184327393282', '2758249526', 'RT @TurkeyPulse: G20 leaders Nov15 w/French Pres. Hollande, Turkish PM Davutoglu, Japanese PM Abe and Saudi Crown Prince Al Saud http://t.c…', 'Wed Dec 03 02:35:37 +0000 2014', 327, 'http://pbs.twimg.com/profile_images/539374743585976320/Ced-BQbw_normal.jpeg', '2014-12-03 20:45:52'),
(150, '539959793268830208', '521458643', 'RT @rebelready: Judge denied #GlenBeck #Blaze dismissal motion.  The Saudi dude LOL is a French Model &amp; #ItWorks distributor http://t.co/e3…', 'Wed Dec 03 01:50:21 +0000 2014', 783, 'http://pbs.twimg.com/profile_images/486576057357590529/Spyuo-o3_normal.jpeg', '2014-12-03 20:45:52'),
(151, '539872994097917952', '2159472672', 'http://t.co/EpMm62QNo0 #ريتويت_للمزيد #Saudi #jobs #وظيفة Sales Assistant - Company OverviewA Luxury French Pa... http://t.co/DuJjJtISB5', 'Tue Dec 02 20:05:26 +0000 2014', 1701, 'http://pbs.twimg.com/profile_images/521876803619532800/06bTIUuP_normal.jpeg', '2014-12-03 20:45:52'),
(152, '539870131611250688', '270806514', '#Saudi #jobs #وظيفة Sales Assistant - Company OverviewA Luxury French Pastry brand is looking for  http://t.co/ZEO7uxTqW7', 'Tue Dec 02 19:54:04 +0000 2014', 697, 'http://pbs.twimg.com/profile_images/462906076866674688/HR84XHgt_normal.jpeg', '2014-12-03 20:45:52'),
(153, '539865636449423360', '885445418', 'ISIS=pure blowback frm western corruption in Mideast.Formed+armed=  CIA,British,French,Turkey+funded by Saudi Arabia. http://t.co/2iH2mqs2Dm', 'Tue Dec 02 19:36:12 +0000 2014', 375, 'http://pbs.twimg.com/profile_images/2731896119/cf8a088a6bef1c760a0bf6b104428bd3_normal.png', '2014-12-03 20:45:53'),
(154, '539841097816489984', '483395237', 'So if one supports UKIP Or French-Le Pen your an extremists-but its okay to be friends with Nazi Ukraine or anti-christian Saudi Arabia-sick', 'Tue Dec 02 17:58:42 +0000 2014', 187, 'http://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', '2014-12-03 20:45:53'),
(155, '539838339579273216', '398067695', 'Sales Assistant: Company Overview A Luxury French Pastry brand is looking for Sales… http://t.co/HzAnEYNdWC', 'Tue Dec 02 17:47:44 +0000 2014', 1973, 'http://pbs.twimg.com/profile_images/1606113330/PSP_jobs-FB-Icon_normal.jpg', '2014-12-03 20:45:53'),
(156, '539824538775592960', '1526559252', 'Sales Assistant: Company OverviewA Luxury French Pastry brand is looking for Sales Assistants for its branch i... http://t.co/UTc0RroJ2A', 'Tue Dec 02 16:52:54 +0000 2014', 4831, 'http://pbs.twimg.com/profile_images/378800000009019884/3ea1b8110bcd5be062c5e59e85cc5d89_normal.jpeg', '2014-12-03 20:45:53'),
(157, '539824537286623232', '2657507840', 'Sales Assistant: Company OverviewA Luxury French Pastry brand is looking for Sales Assistants for its branch i... http://t.co/2I5zUM0ALt', 'Tue Dec 02 16:52:53 +0000 2014', 419, 'http://pbs.twimg.com/profile_images/494311672236892161/ItYYmtnJ_normal.jpeg', '2014-12-03 20:45:53'),
(158, '539824535126552576', '373687084', 'Sales Assistant: Company OverviewA Luxury French Pastry brand is looking for Sales Assistants for its branch i... http://t.co/GqSoqlVVM2', 'Tue Dec 02 16:52:53 +0000 2014', 79508, 'http://pbs.twimg.com/profile_images/1712869077/jobs2saudi_normal.jpg', '2014-12-03 20:45:53'),
(159, '540245932550656000', '2864354778', 'Kentucky Pension Investments: State Says Retirees Have No Right to Know Details of Fees And Investment Risks http://t.co/qL2Beco51i', 'Wed Dec 03 20:47:22 +0000 2014', 89, 'http://pbs.twimg.com/profile_images/523755794186391552/O-boHJcl_normal.jpeg', '2014-12-03 20:47:48'),
(160, '540245920726921216', '17190269', '@saragoldrickrab AGREED!  Needs to be more than wonk photo op! #CollegeOpportunity needs investment for student success...', 'Wed Dec 03 20:47:19 +0000 2014', 713, 'http://pbs.twimg.com/profile_images/1122985325/TWITTER__Large__normal.jpg', '2014-12-03 20:47:48'),
(161, '540245920491646976', '625711123', 'Hyipvictory N°1 Hyip Investment Guide - Niche Market: A 150 Page Absolutely Complete Hyip Investment Handbook ... http://t.co/rKgvbUfjIg', 'Wed Dec 03 20:47:19 +0000 2014', 87762, 'http://pbs.twimg.com/profile_images/531935366865899520/Ojo0QbFf_normal.jpeg', '2014-12-03 20:47:48'),
(162, '540245917375676416', '1451891695', '#Realtors! Do you know how to achieve your investment goals? Best ways to achieve them. #RealtorInvest http://t.co/Hzf2Wf7EA3', 'Wed Dec 03 20:47:18 +0000 2014', 2622, 'http://pbs.twimg.com/profile_images/531916046249103360/DJHUtlAi_normal.jpeg', '2014-12-03 20:47:48'),
(163, '540245906193653761', '260469188', 'RT @StudentsNCL: In today''s #AS2014 @George_Osborne praised our "brilliant" work on ageing research &amp; pledged £20 million investment http:/…', 'Wed Dec 03 20:47:15 +0000 2014', 296, 'http://pbs.twimg.com/profile_images/467551550014251009/SkJVJBQd_normal.jpeg', '2014-12-03 20:47:48'),
(164, '540245905338015744', '55905893', 'RT @AfricapInst: .@_AfricanUnion explains a new resource: African Investment Promotion Network (http://t.co/jQpu5jcxhg) @AfricapInst http:/…', 'Wed Dec 03 20:47:15 +0000 2014', 105, 'http://pbs.twimg.com/profile_images/2578926355/ll_normal.jpg', '2014-12-03 20:47:48'),
(165, '540245895090933761', '2557592562', 'Return on investment and cost-effectiveness of harm reduction program in Malaysia http://t.co/rHXU9eu80n', 'Wed Dec 03 20:47:13 +0000 2014', 13, 'http://pbs.twimg.com/profile_images/476121344115892225/nBtYtuuJ_normal.jpeg', '2014-12-03 20:47:48'),
(166, '540245880771973121', '139508677', 'RT @BKFUniversity: An investment has the ability to appreciate in value without your direct involvement.', 'Wed Dec 03 20:47:09 +0000 2014', 642, 'http://pbs.twimg.com/profile_images/540172117430767617/zA8EnR_8_normal.jpeg', '2014-12-03 20:47:48'),
(167, '540245854486269952', '2211759480', 'RT @Conservatives: We''re backing businesses with the biggest investment in roads for a generation: https://t.co/VkADQpsati http://t.co/HyMK…', 'Wed Dec 03 20:47:03 +0000 2014', 27, 'http://pbs.twimg.com/profile_images/378800000838108482/617941331673d75ad11bd938d46b3553_normal.jpeg', '2014-12-03 20:47:48'),
(168, '540245852611018752', '976626354', 'UN calls fossil fuels high risk investment - https://t.co/lMly4qQRxK via @YahooIndia #marketforces #divestment #safeclimate #actonclimate', 'Wed Dec 03 20:47:03 +0000 2014', 247, 'http://pbs.twimg.com/profile_images/2907633026/c00a5b0143a354a86a02ba9c67daf495_normal.jpeg', '2014-12-03 20:47:48'),
(169, '540245850224877568', '13737', 'Not sure how any investor would fund people who lie... How AdPushup Closed $632K in Angel Investment  http://t.co/mqZiBDvygn', 'Wed Dec 03 20:47:02 +0000 2014', 31969, 'http://pbs.twimg.com/profile_images/14964642/Photo_21_normal.jpg', '2014-12-03 20:47:48'),
(170, '540245840804454400', '373026496', 'Immediate Need:  Senior Analyst – Investment Operations in Montreal, QC Canada http://t.co/od1JYS51dq #job', 'Wed Dec 03 20:47:00 +0000 2014', 205, 'http://pbs.twimg.com/profile_images/1894060070/3290_89565538452_531183452_2445838_5614012_n_normal.jpg', '2014-12-03 20:47:48'),
(171, '540245837830307840', '1854558348', 'RT @rechargenews: Brazil''s National Development Bank pegs wind and solar generation investment at R$42.1bn ($16.1bn) through 2018. http://t…', 'Wed Dec 03 20:46:59 +0000 2014', 952, 'http://pbs.twimg.com/profile_images/378800000443366194/d29d0ce601c153f824b90d38e8519a98_normal.png', '2014-12-03 20:47:48'),
(172, '540245808554471424', '381089924', 'RT @smckenzie21: Glidden, Reich introducing ordinance setting minimum standard for city''s investment in public art http://t.co/PxbF2NHxDz #…', 'Wed Dec 03 20:46:52 +0000 2014', 109, 'http://pbs.twimg.com/profile_images/491252401047740416/vUPfxWmi_normal.png', '2014-12-03 20:47:48'),
(173, '540245792871956481', '501600628', 'Dog fouling can be a significant deterrent to inward investment and tourism http://t.co/2G2CI7RSeK @CllrTerryJermy http://t.co/IamusG3KgA', 'Wed Dec 03 20:46:48 +0000 2014', 13223, 'http://pbs.twimg.com/profile_images/453865821404540928/N8C2KWdM_normal.png', '2014-12-03 20:47:48'),
(174, '540246605648392193', '906434047', 'BLOGPOST: Climate Change Journalism Training Shows Results | Climate Investment Funds http://t.co/dl6MObMBmB', 'Wed Dec 03 20:50:02 +0000 2014', 5318, 'http://pbs.twimg.com/profile_images/2767667441/3e4275823b8b9bdc1bdcdbeaf3c7b6aa_normal.jpeg', '2014-12-03 20:50:22'),
(175, '540246574451146752', '2771144935', 'dlc announces investment in Semafone’s technology for telephone payment security @Semafone #cctr #ccexpo http://t.co/SpqVt9Q9PL', 'Wed Dec 03 20:49:55 +0000 2014', 271, 'http://pbs.twimg.com/profile_images/504366237166477312/ttqIwt_k_normal.jpeg', '2014-12-03 20:50:22'),
(176, '540246565739560961', '34362372', '@bmiddlemas free as in money, but an investment in time? #LTHEchat', 'Wed Dec 03 20:49:53 +0000 2014', 1270, 'http://pbs.twimg.com/profile_images/441666885491253248/n0aUJv_7_normal.jpeg', '2014-12-03 20:50:22'),
(178, '540246554012307456', '53698849', 'RT @NASA_SLS: NASA''s David Miller: Technology drives exploration. Sustained investment in technology is essential to keep this journey goin…', 'Wed Dec 03 20:49:50 +0000 2014', 77, 'http://pbs.twimg.com/profile_images/1309952587/6555th_patch_normal.jpg', '2014-12-03 20:50:22'),
(179, '540246547355955200', '2585644124', 'RT @RichardatKF: @1adass warns that investing more in NHS but cutting social care is " a nonsense" http://t.co/vBkytqZxwK #autumnstatement …', 'Wed Dec 03 20:49:48 +0000 2014', 101, 'http://pbs.twimg.com/profile_images/481424318325194755/40tOsfcY_normal.jpeg', '2014-12-03 20:50:22'),
(181, '540246475633352704', '2305280647', '#Crowdnetic Feed: Central Plaza received investment commitment(s) of $250,000 on @EarlyShares  http://t.co/8dHAoi4E8D', 'Wed Dec 03 20:49:31 +0000 2014', 212, 'http://pbs.twimg.com/profile_images/426058955480002561/6r01z6PW_normal.png', '2014-12-03 20:50:22'),
(182, '540246475482341376', '2305280647', '#Crowdnetic Feed: Classwallet received investment commitment(s) of $230,000 on @EarlyShares  http://t.co/FeHjb8HEW8', 'Wed Dec 03 20:49:31 +0000 2014', 212, 'http://pbs.twimg.com/profile_images/426058955480002561/6r01z6PW_normal.png', '2014-12-03 20:50:22'),
(183, '540246464476090368', '2542136006', 'The imminent failure of Lanco Infratech’s investment in Griffin Coal : Renew Economy http://t.co/d8wZ9yHV1O', 'Wed Dec 03 20:49:29 +0000 2014', 158, 'http://pbs.twimg.com/profile_images/475759822906724352/tx36o8D5_normal.png', '2014-12-03 20:50:22'),
(184, '540246452270669825', '2311009890', '簡単なことをやれ。難しい状態にあるビジネスを立て直す方法は学ぶことができませんでした。代わりに、そういうビジネスは避けるべきと学びました。', 'Wed Dec 03 20:49:26 +0000 2014', 222, 'http://pbs.twimg.com/profile_images/427259398809858048/lBLOUbyZ_normal.jpeg', '2014-12-03 20:50:22'),
(185, '540246449875738624', '2889214302', 'RT @McNak: Commercial real estate investment firm is looking for a dedicated Investment Analyst to join their successful team http://t.co/4…', 'Wed Dec 03 20:49:25 +0000 2014', 53, 'http://pbs.twimg.com/profile_images/529458731692466176/zAC-mXHY_normal.jpeg', '2014-12-03 20:50:22'),
(186, '540246448714313729', '2396552338', 'New SNS to earn money with no investment, grow your family tree - https://t.co/rJfgeY4stH December 03, 2014 at 09:49PM', 'Wed Dec 03 20:49:25 +0000 2014', 44, 'http://pbs.twimg.com/profile_images/531837515649404928/VC9PWVew_normal.jpeg', '2014-12-03 20:50:22'),
(187, '540246439033847810', '40355815', 'RT @Anti_Intellect: You should always question your investment in white supremacy, but you really should during times like this.', 'Wed Dec 03 20:49:23 +0000 2014', 360, 'http://pbs.twimg.com/profile_images/527480153489018880/Ii5w-mb4_normal.jpeg', '2014-12-03 20:50:22'),
(188, '540246429273296896', '1000311642', 'Payments Startup Stripe Lands $80 Million Investment Ahead of Twitter Partnership http://t.co/NJQxO1MqHa via @DelRey @HarvardBusLaw #VCMath', 'Wed Dec 03 20:49:20 +0000 2014', 831, 'http://pbs.twimg.com/profile_images/378800000146939919/6efaf5aa39547af221cb0e12d53886d6_normal.png', '2014-12-03 20:50:22'),
(189, '540246782333431809', '191138656', 'RT @ginakel2008: A former BT Young Scientist winner''s company has been valued at €2.8bn http://t.co/n9v23CYlca via @Independent_ie @btyste …', 'Wed Dec 03 20:50:44 +0000 2014', 792, 'http://pbs.twimg.com/profile_images/532943840752443392/h7Hxvf-f_normal.jpeg', '2014-12-03 20:51:07'),
(190, '540246778700763137', '14761348', 'RT @TaurangaBC: $250,000 investment for Tauranga Startup Weekend team Clevercare  http://t.co/9gtzzSy5wn #tgabc @swnz http://t.co/vEYfQtBoIc', 'Wed Dec 03 20:50:43 +0000 2014', 1005, 'http://pbs.twimg.com/profile_images/418541481167577088/QsZ_4Bf3_normal.png', '2014-12-03 20:51:07'),
(191, '540246772225163264', '126586159', 'That''s the end of a short period of question time tonight. Now an item about investment in an improved council website.', 'Wed Dec 03 20:50:42 +0000 2014', 3236, 'http://pbs.twimg.com/profile_images/1605708766/AVDC_logo_normal.JPG', '2014-12-03 20:51:07'),
(192, '540246767204564992', '474359398', 'RT @lionelbarber: Qatar Investment authority moderniser removed as head of $300bn fund #Harrods  http://t.co/wbz36qLKJ3', 'Wed Dec 03 20:50:41 +0000 2014', 9771, 'http://pbs.twimg.com/profile_images/537113753050169345/9yEtUTZo_normal.jpeg', '2014-12-03 20:51:07'),
(193, '540246748120109057', '469670578', 'Goldman Sachs: Investment Banking ‘Momentum Remains Positive’ But No Upgrade Yet http://t.co/tgGERTESVw via @barronsonline', 'Wed Dec 03 20:50:36 +0000 2014', 7, 'http://pbs.twimg.com/profile_images/538338061038673920/P6_--_V-_normal.jpeg', '2014-12-03 20:51:07'),
(194, '540246740440322048', '2529686690', 'UKRAINE: US-Investment-Banksterin ist neuer Finanzminister http://t.co/bOQ3iCW50W', 'Wed Dec 03 20:50:34 +0000 2014', 6, 'http://pbs.twimg.com/profile_images/471603488246341633/-dSuXtdi_normal.jpeg', '2014-12-03 20:51:07'),
(195, '540246724951150592', '2573551328', 'RT @otcaddict: Goldman Sachs: Investment Banking ‘Momentum Remains Positive ’ But No Upgrade Yet  http://t.co/TIJNpYykgE', 'Wed Dec 03 20:50:31 +0000 2014', 841, 'http://pbs.twimg.com/profile_images/479006424282828800/ziHPb0Mq_normal.jpeg', '2014-12-03 20:51:07'),
(196, '540246718038966272', '2850638668', 'A brief look at Apollo Investment Corp.''s oil exposure and what it means for the company''s income and book value.... http://t.co/LRcA1hKB3V', 'Wed Dec 03 20:50:29 +0000 2014', 93, 'http://pbs.twimg.com/profile_images/527591030921515008/AtjDw6VO_normal.png', '2014-12-03 20:51:07'),
(197, '540246709205757952', '2590581757', 'RT @ginakel2008: A former BT Young Scientist winner''s company has been valued at €2.8bn http://t.co/n9v23CYlca via @Independent_ie @btyste …', 'Wed Dec 03 20:50:27 +0000 2014', 255, 'http://pbs.twimg.com/profile_images/482352447327703041/ez_HX_R-_normal.jpeg', '2014-12-03 20:51:07'),
(198, '540246703891574784', '15749585', 'Nice push towards creating better supply chains @GAPinc &amp; @TAU_Investment http://t.co/HojQqv4Sc2  \n@cnnfreedom #goodbusiness #letsdomore', 'Wed Dec 03 20:50:26 +0000 2014', 319, 'http://pbs.twimg.com/profile_images/412027502685470721/1uyEUhsY_normal.jpeg', '2014-12-03 20:51:07'),
(199, '540246702050258944', '543231788', 'INVESTMENT NEWS Actelion Submits Marketing Application for Uptravi in EU - Analyst Blog http://t.co/KbEp3VLfsD... http://t.co/1r1xo2Uh4B', 'Wed Dec 03 20:50:25 +0000 2014', 261, 'http://pbs.twimg.com/profile_images/2016616308/socmedia_normal.jpeg', '2014-12-03 20:51:07'),
(200, '540246700536102912', '543231788', 'INVESTMENT NEWS Cable MSOs Maintain Dominance Over the SMB Segment - Analyst Blog http://t.co/8UKxSWcBvw ... http://t.co/1r1xo2Uh4B', 'Wed Dec 03 20:50:25 +0000 2014', 261, 'http://pbs.twimg.com/profile_images/2016616308/socmedia_normal.jpeg', '2014-12-03 20:51:07'),
(201, '540246699038748672', '543231788', 'INVESTMENT NEWS MasterCard''s Xmas Gift: 45% Dividend Hike &amp; $3.75B Buyback - Analyst Blog ... http://t.co/1r1xo2Uh4B', 'Wed Dec 03 20:50:25 +0000 2014', 261, 'http://pbs.twimg.com/profile_images/2016616308/socmedia_normal.jpeg', '2014-12-03 20:51:07'),
(202, '540246696996126720', '543231788', 'INVESTMENT NEWS IBM Inks $1.25B Cloud Deal with Advertising Firm WPP - Analyst Blog http://t.co/ed4BYmXjuj ... http://t.co/1r1xo2Uh4B', 'Wed Dec 03 20:50:24 +0000 2014', 261, 'http://pbs.twimg.com/profile_images/2016616308/socmedia_normal.jpeg', '2014-12-03 20:51:08'),
(203, '540246695523520512', '997783818', 'Fort Lauderdale Hotel''s For Sale #fortlauderdale #realestate #investment #boutique #hotel - http://t.co/XYDtHGJssJ via @Shareaholic', 'Wed Dec 03 20:50:24 +0000 2014', 137, 'http://pbs.twimg.com/profile_images/378800000597080756/da5f5ba2717bd65d9a3519328f8282c7_normal.jpeg', '2014-12-03 20:51:08'),
(204, '540247324153618432', '535465446', 'TREND TRANSFER Asia, Market Expansion, Market Entry Incubator, Executive Search - Investment -  http://t.co/rKuMhsKmAW Exklusive Anlagem...', 'Wed Dec 03 20:52:54 +0000 2014', 166, 'http://pbs.twimg.com/profile_images/1960039926/CAKVHKFQ_2_normal.jpg', '2014-12-03 20:53:14'),
(205, '540247297700155394', '538981873', 'Newsday: Paul Greenwood, former Islanders co-owner, sentenced to 10 years for investment fraud http://t.co/TPbdXMymLK', 'Wed Dec 03 20:52:47 +0000 2014', 1186, 'http://pbs.twimg.com/profile_images/1977281412/taxi_cab_normal.jpg', '2014-12-03 20:53:14'),
(206, '540247288074219520', '194031207', 'Marketing is an investment in your business not an expense but spend wisely on marketing that is effective.', 'Wed Dec 03 20:52:45 +0000 2014', 2086, 'http://pbs.twimg.com/profile_images/2827350477/80710cddaec453c2edb7355384f6870e_normal.png', '2014-12-03 20:53:14'),
(207, '540247284861399040', '65316869', 'RT @ginakel2008: A former BT Young Scientist winner''s company has been valued at €2.8bn http://t.co/n9v23CYlca via @Independent_ie @btyste …', 'Wed Dec 03 20:52:44 +0000 2014', 1413, 'http://pbs.twimg.com/profile_images/539733082308620288/WR-45VYU_normal.jpeg', '2014-12-03 20:53:14'),
(208, '540247269203648512', '300616933', 'Real Estate Executives Eye 2016 as Peak Year | Commercial Property Executive http://t.co/M9EaGBniPc', 'Wed Dec 03 20:52:40 +0000 2014', 222, 'http://pbs.twimg.com/profile_images/2911676376/b32b1f333fdc685b9103b4147209060a_normal.jpeg', '2014-12-03 20:53:14'),
(209, '540247262534701056', '935433810', 'RT @mheschmeyer: PE firm @Blackstone hoping to repeat success with its 2007 #CRE investment strategy\nhttp://t.co/quVknERBSL http://t.co/Ff9…', 'Wed Dec 03 20:52:39 +0000 2014', 1249, 'http://pbs.twimg.com/profile_images/483664708671533056/8Y_wqSlY_normal.jpeg', '2014-12-03 20:53:14'),
(210, '540247257812312064', '453932208', '@Namurian1 also what about this angle? Likely big investment funds will dump fossil fuels? http://t.co/MjWvJ7to6K', 'Wed Dec 03 20:52:38 +0000 2014', 2167, 'http://pbs.twimg.com/profile_images/1848043035/lowvelo_normal.jpg', '2014-12-03 20:53:14');
INSERT INTO `app_twitte` (`id`, `twitter_id`, `user_id`, `text`, `created_at`, `user_followers_count`, `user_profile_image_url`, `pub_date`) VALUES
(211, '540247255618695168', '1229877270', 'RT @Joe_Meyer1: @BillTufts Pension Study..funded ratios rose modestly, but remain near 70% despite strong years of investment returns http:…', 'Wed Dec 03 20:52:37 +0000 2014', 359, 'http://pbs.twimg.com/profile_images/442696667922321409/OQvt0Fv0_normal.jpeg', '2014-12-03 20:53:14'),
(212, '540247253797986304', '2840441986', 'Sometimes a poor past turns out to be the best investment in a promising future. -Susan Gale', 'Wed Dec 03 20:52:37 +0000 2014', 32, 'http://pbs.twimg.com/profile_images/537842643221225472/quMvCAcZ_normal.jpeg', '2014-12-03 20:53:14'),
(213, '540247252540076032', '1390321334', 'RT @SeasonalWisdom: #gardeningtip @TwinPinesLandsc: Never underestimate the value of healthy soil. It''s the most important investment.  #Tw…', 'Wed Dec 03 20:52:36 +0000 2014', 492, 'http://pbs.twimg.com/profile_images/3603858128/4294e3dfc10c7ab77bb948d950160085_normal.jpeg', '2014-12-03 20:53:14'),
(214, '540247240309501953', '72861070', 'New #job: Senior Analyst – Investment Operations Location: Toronto .. http://t.co/UPdhulCd6Z #experis', 'Wed Dec 03 20:52:34 +0000 2014', 680, 'http://pbs.twimg.com/profile_images/408331669/Manpower_Colour_Logo_300_pixels_normal.jpg', '2014-12-03 20:53:14'),
(215, '540247217974816768', '62907861', 'RT @PRECIOUS_Awards: Be patient with yourself. Self-growth is tender; it’s holy ground. There’s no greater investment. Stephen Covey', 'Wed Dec 03 20:52:28 +0000 2014', 1626, 'http://pbs.twimg.com/profile_images/461013802851782656/Gp0kusd5_normal.jpeg', '2014-12-03 20:53:14'),
(216, '540247215826948096', '111940539', 'Why hiring actors for your next video production is a sound investment. http://t.co/EgSOTdWTot', 'Wed Dec 03 20:52:28 +0000 2014', 63, 'http://pbs.twimg.com/profile_images/533022340615897088/E04PIJ7Y_normal.jpeg', '2014-12-03 20:53:14'),
(217, '540247212765503488', '1642106527', 'RT @Streetkleen: Dog fouling can be a significant deterrent to inward investment and tourism http://t.co/2G2CI7RSeK @CllrTerryJermy http://…', 'Wed Dec 03 20:52:27 +0000 2014', 1602, 'http://pbs.twimg.com/profile_images/378800000233599954/a3afa5be35f2fd293bdae824806e0f60_normal.png', '2014-12-03 20:53:14'),
(218, '540247194301763585', '15447692', 'North Capital Investment Technology (NTCI) has closed its seed funding round of $1 million http://t.co/x98q8qTYAX', 'Wed Dec 03 20:52:23 +0000 2014', 158, 'http://pbs.twimg.com/profile_images/1825088500/12-0112-neotrope_72dpi_normal.jpg', '2014-12-03 20:53:14'),
(219, '540248972074307584', '17595745', 'RT @WalkableDFW: StreetSmart - Creating value by investing in neighborhoods; learning from Greenville and Bishop - http://t.co/xe1i90qbuq', 'Wed Dec 03 20:59:26 +0000 2014', 82232, 'http://pbs.twimg.com/profile_images/469557441349156864/8ssZLYnn_normal.jpeg', '2014-12-03 20:59:50'),
(220, '540248966835609600', '70342801', 'RT @PresReed: Boston gets $1b transit investment. More reason to believe in @NorthSouthMetro. http://t.co/1UFO3CvZEN #NSMetro #Transit #STL', 'Wed Dec 03 20:59:25 +0000 2014', 1151, 'http://pbs.twimg.com/profile_images/477807926409576448/24aO1WWT_normal.jpeg', '2014-12-03 20:59:50'),
(221, '540248945251713024', '364261383', 'Echo Park landmark Jensen''s Recreation Center sold: Vista Investment Group, a Los Angeles real estate investme... http://t.co/OsItLP4l7c', 'Wed Dec 03 20:59:20 +0000 2014', 481, 'http://pbs.twimg.com/profile_images/520469632642449408/a_KwQDWs_normal.jpeg', '2014-12-03 20:59:50'),
(222, '540248924292800513', '584097578', 'Think Investment Realty-The Hottest Areas for QLD Property Investment: Think Investment Realty explore the hot... http://t.co/TQDag5VujV', 'Wed Dec 03 20:59:15 +0000 2014', 419, 'http://pbs.twimg.com/profile_images/2684349081/d4654c9da3bb6125a6df92c86bc8ee35_normal.png', '2014-12-03 20:59:50'),
(223, '540248892164427776', '2269163545', 'Escrow is a deposit of funds or a deed  by one party for the delivery to another party upon completion of a particular condition or event.', 'Wed Dec 03 20:59:07 +0000 2014', 1229, 'http://pbs.twimg.com/profile_images/417714850094010368/rxGDdXP9_normal.jpeg', '2014-12-03 20:59:50'),
(224, '540248882379517952', '261466941', 'RT @TheEconomist: The European Commission’s grand investment plan to kick-start growth is laughably inadequate http://t.co/WuRuBdzDR7 http:…', 'Wed Dec 03 20:59:05 +0000 2014', 112, 'http://pbs.twimg.com/profile_images/1314897910/jd_normal.jpg', '2014-12-03 20:59:50'),
(225, '540248871289782272', '30270036', 'The 2008 Crisis was a stock and investment bank crisis. But it was not THE Crisis.', 'Wed Dec 03 20:59:02 +0000 2014', 1218, 'http://pbs.twimg.com/profile_images/479624760/twitterProfilePhoto_normal.jpg', '2014-12-03 20:59:50'),
(226, '540248861231816705', '944677303', '.@BenM_IM Government certainly seem focused on policies that equate #ukhousing with ownership/asset value rather than social investment/glue', 'Wed Dec 03 20:59:00 +0000 2014', 296, 'http://pbs.twimg.com/profile_images/478932599138570240/cYURgZ6g_normal.png', '2014-12-03 20:59:50'),
(227, '540248854571282432', '17460118', '2014 SEC and FINRA Enforcement Actions Against Broker-Dealers and Investment Advisers http://t.co/aSNIKBBxYr | by @KLGates #mergers', 'Wed Dec 03 20:58:58 +0000 2014', 2232, 'http://pbs.twimg.com/profile_images/83495106/Picture_4_normal.png', '2014-12-03 20:59:50'),
(228, '540248843284398080', '584812227', 'RT @BKFUniversity: An investment has the ability to appreciate in value without your direct involvement.', 'Wed Dec 03 20:58:56 +0000 2014', 764, 'http://pbs.twimg.com/profile_images/531570235732922371/mgeIANTW_normal.jpeg', '2014-12-03 20:59:50'),
(229, '540248839504924672', '20374262', '“I joined @BankToTheFuture and got a free investment in a business StartUp, http://t.co/x7las5orR2, @StartJOIN.... http://t.co/VprIGl9ZiT', 'Wed Dec 03 20:58:55 +0000 2014', 120877, 'http://pbs.twimg.com/profile_images/513673436590116865/fMX02-YO_normal.png', '2014-12-03 20:59:50'),
(230, '540248822027268096', '259696452', 'RT @BKFUniversity: You can''t just run around saying college is an investment as if a piece of paper appreciates in value.', 'Wed Dec 03 20:58:51 +0000 2014', 218, 'http://pbs.twimg.com/profile_images/535544655677362176/lxTo-byd_normal.jpeg', '2014-12-03 20:59:51'),
(231, '540248806973915136', '245423471', '.@GAPinc &amp; @TAU_Investment to innovate the factories of the future. via @FastCompany @jeffchu http://t.co/xNqrdJyx10  #letsdomore', 'Wed Dec 03 20:58:47 +0000 2014', 568, 'http://pbs.twimg.com/profile_images/418647215582613504/zx7WTXEQ_normal.jpeg', '2014-12-03 20:59:51'),
(232, '540248799420366848', '2858108355', 'RT @EveryChildFed: Our Pres/CEO @RachaelsJourney recently attended an interview w/Radio Phoenix on the Zambia Investment Conf. that she''ll …', 'Wed Dec 03 20:58:45 +0000 2014', 12, 'http://pbs.twimg.com/profile_images/532629654067089408/QpV-UyjM_normal.jpeg', '2014-12-03 20:59:51'),
(233, '540248776825651200', '21330040', 'RT @Inc: Peter Thiel''s investment red flags? Too many other investors &amp; trendy buzzwords @jeffbercovici http://t.co/MkZLCC4ihw http://t.co/…', 'Wed Dec 03 20:58:40 +0000 2014', 4639, 'http://pbs.twimg.com/profile_images/423918619228401664/2dmPSX7j_normal.jpeg', '2014-12-03 20:59:51'),
(234, '540254502495215617', '2814326650', 'RT @MSHLA: @mediaLIESalways @Ale66x66 Kaffir from Holland killed today in Saudi Arabia. #IS', 'Wed Dec 03 21:21:25 +0000 2014', 7075, 'http://pbs.twimg.com/profile_images/537556429985828864/MksKZsgn_normal.jpeg', '2014-12-03 21:38:17'),
(235, '540254425005453312', '93342234', '@mediaLIESalways @Ale66x66 Kaffir from Holland killed today in Saudi Arabia. #IS', 'Wed Dec 03 21:21:07 +0000 2014', 810, 'http://pbs.twimg.com/profile_images/540017264461099009/2x_64XYs_normal.jpeg', '2014-12-03 21:38:17'),
(242, '540260387304660992', '2414595968', 'GW’S Losses Widen Following Cannabis-Based Drug Investment http://t.co/FEIRXikRAc', 'Wed Dec 03 21:44:48 +0000 2014', 837, 'http://pbs.twimg.com/profile_images/475437437255041025/ZoeQPd-__normal.png', '2014-12-03 21:45:10'),
(243, '540260386084098048', '1468949456', '@billshortenmp Missed the negative gearing opportunity again, Bill. Who do you look after? The 50% of pollies who own investment property?', 'Wed Dec 03 21:44:48 +0000 2014', 8, 'http://abs.twimg.com/sticky/default_profile_images/default_profile_2_normal.png', '2014-12-03 21:45:10'),
(244, '540260384616112128', '2213348533', 'http://t.co/mCx7wUNtdC - REHAB/INVESTMENT PROPERTY ASKING 20,000 http://t.co/ZDwQ5SK2cZ', 'Wed Dec 03 21:44:47 +0000 2014', 191, 'http://pbs.twimg.com/profile_images/485292170799099905/JmPghGZV_normal.png', '2014-12-03 21:45:10'),
(245, '540260365406175233', '268094901', 'You don''t need investment to create a successful startup @wadhwa #LSASummit14', 'Wed Dec 03 21:44:43 +0000 2014', 3786, 'http://pbs.twimg.com/profile_images/378800000698879889/cb82923d8c4ee647b902759d84bdb95a_normal.png', '2014-12-03 21:45:10'),
(246, '540260319084679169', '248132844', 'RT @JamratGLA: This #stampduty change http://t.co/Sw4FVzmNyS could be key to unlocking institutional investment and massively expanding sha…', 'Wed Dec 03 21:44:32 +0000 2014', 69, 'http://pbs.twimg.com/profile_images/378800000589037176/97e3eefac038c7728038e26c2e9557e4_normal.jpeg', '2014-12-03 21:45:10'),
(247, '540260294409195520', '2757428814', 'RT @forexinvestm: Earn 250%-900% Daily On Your Investment For 4 Days.forex education. "http://t.co/dAXDR1hVQJ"', 'Wed Dec 03 21:44:26 +0000 2014', 1742, 'http://pbs.twimg.com/profile_images/503010566936346624/o__aVTWg_normal.jpeg', '2014-12-03 21:45:10'),
(248, '540260282850115585', '289883555', 'Well, the general consensus in our family, is tell Alan Sugar to stick his investment #TheApprentice', 'Wed Dec 03 21:44:23 +0000 2014', 1376, 'http://pbs.twimg.com/profile_images/378800000469745834/cce9f13deb82e9104c3ee6845f9f65c2_normal.jpeg', '2014-12-03 21:45:10'),
(249, '540260276470554624', '423642052', 'Big wine investment http://t.co/6sySp09Psx', 'Wed Dec 03 21:44:22 +0000 2014', 629, 'http://pbs.twimg.com/profile_images/523573998635208705/4r4LOYPc_normal.jpeg', '2014-12-03 21:45:10'),
(250, '540260275078053891', '800409601', 'See How Long It Takes To Triple an Investment with the Rule of 115 http://t.co/13x8BqAUmj', 'Wed Dec 03 21:44:21 +0000 2014', 60, 'http://pbs.twimg.com/profile_images/495899599723180032/jk3CFBgX_normal.png', '2014-12-03 21:45:10'),
(251, '540260274180456449', '226178902', 'RT @cabinetofficeuk: Food waste charity @FareShareSW has used the #SocInv tax relief to attract £70K of investment. Find out about #SITR: h…', 'Wed Dec 03 21:44:21 +0000 2014', 231, 'http://pbs.twimg.com/profile_images/378800000190239726/6afc65318d16282ff6980547952c12bb_normal.jpeg', '2014-12-03 21:45:10'),
(252, '540260259273932800', '359877319', 'RT @Mae_Carson1: So Lord Smith of Kelvin has backed fracking while holding office as chairman of Green Investment Bank? No conflicts of int…', 'Wed Dec 03 21:44:18 +0000 2014', 1743, 'http://pbs.twimg.com/profile_images/527798116368777216/RPI_jRL8_normal.jpeg', '2014-12-03 21:45:10'),
(253, '540260257873027072', '2548528430', 'RT @BombardierR_UK: Noel Travers on BBC News: "Delighted to hear about continuing #investment in #infrastructure &amp; hope we can build new tr…', 'Wed Dec 03 21:44:17 +0000 2014', 142, 'http://pbs.twimg.com/profile_images/517684161516023808/clk-OGiC_normal.jpeg', '2014-12-03 21:45:10'),
(254, '540260254425292800', '2846486337', 'See How Long It Takes To Triple an Investment with the Rule of 115 http://t.co/7gRGFrAjCY #SaveTime #Lifehacker', 'Wed Dec 03 21:44:16 +0000 2014', 9, 'http://pbs.twimg.com/profile_images/527157396997558272/_D3fIhqy_normal.jpeg', '2014-12-03 21:45:10'),
(255, '540260252927930370', '22150874', 'RT @globeinvestor: Dividend cut fears grow as yields surge among Canadian oil producers http://t.co/IH8KonZKOs', 'Wed Dec 03 21:44:16 +0000 2014', 48801, 'http://pbs.twimg.com/profile_images/3508069940/d60662ddb2802901b6bea02fea910137_normal.jpeg', '2014-12-03 21:45:10'),
(256, '540260221201833984', '501341520', '@RealJoelRowan But a SuperCity will allow for projects like the Airport Runway+2nd MtVic tunnel which are important and need the investment', 'Wed Dec 03 21:44:08 +0000 2014', 147, 'http://pbs.twimg.com/profile_images/2660849881/81d74e65c08bdb7f60899259f599a8b1_normal.jpeg', '2014-12-03 21:45:11'),
(257, '540268714541588480', '2311009890', '投資とは、消費を延期することです。いまお金を出して、あとでもっと大きなお金になって戻ってくるわけです。ほんとうに大事な問題はふたつだけです。ひとつは、どれだけ戻ってくるか、もうひとつは、いつ戻ってくるか', 'Wed Dec 03 22:17:53 +0000 2014', 222, 'http://pbs.twimg.com/profile_images/427259398809858048/lBLOUbyZ_normal.jpeg', '2014-12-03 22:18:16'),
(258, '540268686469115904', '167330533', 'Dubai-based company purchasing Springfield hotel: A United Arab Emirates-based global investment company is pu... http://t.co/6vnJjwMYFf', 'Wed Dec 03 22:17:47 +0000 2014', 856, 'http://pbs.twimg.com/profile_images/1929866655/Dubai_TW_normal.jpg', '2014-12-03 22:18:16'),
(259, '540268681817649152', '41488578', 'Jack Z: As far as investments go, this is a sound investment. #SeagerBeliever', 'Wed Dec 03 22:17:46 +0000 2014', 232096, 'http://pbs.twimg.com/profile_images/522990137081208832/42xh-uW2_normal.jpeg', '2014-12-03 22:18:16'),
(260, '540268671923277824', '396224478', 'RT @danielbowen: Very sad to hear of Lynne Kosky''s passing. It was under her that serious PT investment (especially train fleet expansion) …', 'Wed Dec 03 22:17:43 +0000 2014', 439, 'http://pbs.twimg.com/profile_images/2142094938/me1_normal.JPG', '2014-12-03 22:18:16'),
(261, '540268665888051201', '337133670', '20 million pound investment is needed in r defence and goalkeeper, and another cm with that!', 'Wed Dec 03 22:17:42 +0000 2014', 382, 'http://pbs.twimg.com/profile_images/533769078784421888/5he1bv3O_normal.jpeg', '2014-12-03 22:18:16'),
(262, '540268648888545280', '421473004', 'Best 14$ investment I''ve ever made', 'Wed Dec 03 22:17:38 +0000 2014', 3900, 'http://pbs.twimg.com/profile_images/539646005327970304/_NmOgpI8_normal.jpeg', '2014-12-03 22:18:16'),
(263, '540268648812666881', '1240871894', 'Teaching hospital rentals tucson,land tucson,rentals tucson,office title tucson,investment plot tucson,etc.: uYlKZqw', 'Wed Dec 03 22:17:38 +0000 2014', 22, 'http://pbs.twimg.com/profile_images/3510504215/97e7b8bea58ed231e27263feeb0cf4c9_normal.jpeg', '2014-12-03 22:18:16'),
(264, '540268639971078144', '30224973', 'U.S. Investment Heroes of 2014: Investing at Home: AT&amp;T #1.  Progressive Policy Institute #attemployee http://t.co/ghPtyZNOPf', 'Wed Dec 03 22:17:36 +0000 2014', 194, 'http://pbs.twimg.com/profile_images/444438553301241856/BKfVSNmR_normal.jpeg', '2014-12-03 22:18:16'),
(265, '540268634652692481', '322028243', 'The value of (truly) active investment http://t.co/HMmhf9FFJa', 'Wed Dec 03 22:17:34 +0000 2014', 2347, 'http://pbs.twimg.com/profile_images/1417334169/CapCity_Twitter_Large_Thumb_normal.gif', '2014-12-03 22:18:16'),
(266, '540268619045683201', '1326471859', 'RT @CFMEU_National: Under the "infrastructure Prime Minister" there has been less, not more infrastructure investment. #auspol http://t.co/…', 'Wed Dec 03 22:17:31 +0000 2014', 630, 'http://pbs.twimg.com/profile_images/3737689052/44845a462a251f1688f8c3c933bd511a_normal.jpeg', '2014-12-03 22:18:16'),
(267, '540268610363879425', '405942433', 'RT @joravben: Just in time for Xmas--Rahm gives more school money to bankers: http://t.co/ClFfjBJyOY', 'Wed Dec 03 22:17:29 +0000 2014', 160, 'http://pbs.twimg.com/profile_images/457649636103041024/JawJ02sF_normal.jpeg', '2014-12-03 22:18:16'),
(268, '540268598225547266', '1443401936', 'http://t.co/SBv4COlQDC #ebay #auctions #rare #investment #art #fineart #design #fashion #shopping #interiordesign #rt #love #oscars #gifts #', 'Wed Dec 03 22:17:26 +0000 2014', 34, 'http://pbs.twimg.com/profile_images/378800000095287733/d6e557b76f89e5532eca17f9b3d9a13b_normal.jpeg', '2014-12-03 22:18:16'),
(269, '540268591598145536', '63138229', 'RT @TechCrunch: Flipkart founders’ interest in Ather comes at a promising time for the scooter market in India http://t.co/Bz8hZkiNrM http:…', 'Wed Dec 03 22:17:24 +0000 2014', 320, 'http://pbs.twimg.com/profile_images/1098687639/d803f890-4311-47b0-aec1-f6f9e7c93f22_normal.png', '2014-12-03 22:18:17'),
(270, '540268589278699520', '2888363514', 'お金を持っている人は、凡人よりもお金儲けに目ざといので、365日情報収集をしています。', 'Wed Dec 03 22:17:24 +0000 2014', 38, 'http://pbs.twimg.com/profile_images/529241288537669632/etTKbI2B_normal.png', '2014-12-03 22:18:17'),
(271, '540268577207902209', '345319405', 'RT @yamitsi: We''re starting to look sharper and look so much better with Nabil in midfield, but we''re still soft! That won''t change without…', 'Wed Dec 03 22:17:21 +0000 2014', 1251, 'http://pbs.twimg.com/profile_images/531737140401799168/mZDS-iBR_normal.jpeg', '2014-12-03 22:18:17'),
(272, '540268837313077249', '359792950', 'RT @Mariners: Jack Z: As far as investments go, this is a sound investment. #SeagerBeliever', 'Wed Dec 03 22:18:23 +0000 2014', 211, 'http://pbs.twimg.com/profile_images/378800000418610823/3a1b9f1c8d07b93220447822f2118b6f_normal.jpeg', '2014-12-03 22:18:44'),
(273, '540268824583741442', '2843181100', 'All this talk of foreign direct investment is making me hungry. Better avoid getting stuck in Somalia', 'Wed Dec 03 22:18:20 +0000 2014', 3150, 'http://pbs.twimg.com/profile_images/539987165157928960/xPa027GG_normal.jpeg', '2014-12-03 22:18:44'),
(274, '540268804287127552', '354539810', 'RT @1petermartin: So far under the infrastructure Prime Minister there is not more infrastructure investment but less: http://t.co/6nd4mZDW…', 'Wed Dec 03 22:18:15 +0000 2014', 972, 'http://pbs.twimg.com/profile_images/2220779211/capt_larry_dart-char_normal.jpg', '2014-12-03 22:18:44'),
(275, '540268780669005827', '1150444830', 'RT @Mariners: Jack Z: As far as investments go, this is a sound investment. #SeagerBeliever', 'Wed Dec 03 22:18:09 +0000 2014', 21, 'http://pbs.twimg.com/profile_images/3210753991/18bc996e8bb6116bc013da14de6419ac_normal.jpeg', '2014-12-03 22:18:44'),
(276, '540268780400570368', '2888363514', 'RT @Kanja_lover: 同窓会にオシャレしようと・・・・　　\nビリ・・ヒップラインヤバだったｗｗｗ　　　　\nこれはまずいとこれつかっててみたｗｗｗ\n⇒ http://t.co/llvQe6ciHe\n\nマジモテまくりｗｗｗ 逆ハーレム状態ｗｗｗ http://t.co/…', 'Wed Dec 03 22:18:09 +0000 2014', 38, 'http://pbs.twimg.com/profile_images/529241288537669632/etTKbI2B_normal.png', '2014-12-03 22:18:44'),
(277, '540268761660420096', '2288221220', 'Different points in real estate investment to Hokkaido and Okinawa http://t.co/y8bqdCMAo2　#realestate #Japan #Okinawa #Hokkaido #investment', 'Wed Dec 03 22:18:05 +0000 2014', 1389, 'http://pbs.twimg.com/profile_images/422371829626306560/CdyxpZ5x_normal.png', '2014-12-03 22:18:44'),
(278, '540268758728982530', '2590914981', 'Make Smart Investment Decisions With These Handy Tips - http://t.co/xrgmSeoOT7', 'Wed Dec 03 22:18:04 +0000 2014', 363, 'http://pbs.twimg.com/profile_images/475977607154892801/VKaWP-iB_normal.jpeg', '2014-12-03 22:18:44'),
(279, '540268754773364736', '509568090', 'Bought a bed, probably best investment I''ve ever made', 'Wed Dec 03 22:18:03 +0000 2014', 207, 'http://pbs.twimg.com/profile_images/476617499790684160/ZAXX_cY3_normal.jpeg', '2014-12-03 22:18:44'),
(280, '540268730316750848', '1510030513', 'RT @EnglishHeritage: Government announce investment in 2.9km tunnel to remove A303 from @EH_Stonehenge landscape http://t.co/QnuIEZweIe htt…', 'Wed Dec 03 22:17:57 +0000 2014', 42, 'http://pbs.twimg.com/profile_images/532879090517172225/Yun8XJNT_normal.jpeg', '2014-12-03 22:18:45'),
(306, '540249671739121664', '61859021', '@Zaphesheya of course Afrikan countries aren''t free when English, French &amp; Arabic are most of Afrikan countries national languages. WTF', 'Wed Dec 03 21:02:13 +0000 2014', 817, 'http://pbs.twimg.com/profile_images/533606015808573440/o78blM8e_normal.jpeg', '2014-12-03 22:18:56'),
(307, '540047727480946688', '13619352', 'The National Library of Israel sounds like a real treasure. http://t.co/3mgfd1XFS4 #israel #dialogue', 'Wed Dec 03 07:39:46 +0000 2014', 209, 'http://pbs.twimg.com/profile_images/49753562/totorox_normal.gif', '2014-12-03 22:18:56'),
(308, '540046451477184513', '2277495895', 'RT @MentorsLinguist: Learning the Arabic language will have a positive impact for many a budding career in both national &amp; international fi…', 'Wed Dec 03 07:34:42 +0000 2014', 40, 'http://pbs.twimg.com/profile_images/465124956901081088/dkG3ggWn_normal.jpeg', '2014-12-03 22:18:56'),
(309, '540034133833965568', '2856630150', 'Learning the Arabic language will have a positive impact for many a budding career in both national &amp; international firms in the Arab world.', 'Wed Dec 03 06:45:45 +0000 2014', 4, 'http://pbs.twimg.com/profile_images/522354649756487680/b1qfzMxD_normal.jpeg', '2014-12-03 22:18:56'),
(310, '539949753593643008', '29962235', '@Chaouia_xx @ahmedGKMazari Somalia is in the Arab world, ''Arab league'' and national language is ARABIC/somali. Is it arab? Lol logic', 'Wed Dec 03 01:10:27 +0000 2014', 880, 'http://pbs.twimg.com/profile_images/539973190223921153/QUwTCeGB_normal.jpeg', '2014-12-03 22:18:56'),
(311, '539908409697382400', '405164716', '#ليبيا محلل "The National Interest".. من السابق لأوانه "دفن" أوبك http://t.co/kQ6Nbx0f0P', 'Tue Dec 02 22:26:10 +0000 2014', 6755, 'http://pbs.twimg.com/profile_images/3642021404/be5221b8f6d032b5750d4783a80ad42f_normal.png', '2014-12-03 22:18:56'),
(312, '539908401824690176', '1451203958', '#ليبيا محلل "The National Interest".. من السابق لأوانه "دفن" أوبك http://t.co/gupgPi0hsX', 'Tue Dec 02 22:26:08 +0000 2014', 1459, 'http://pbs.twimg.com/profile_images/3698430267/8ed911fcc96b8d10158c9536334d9311_normal.jpeg', '2014-12-03 22:18:56'),
(313, '539907753981280257', '1550020933', 'محلل "The National Interest".. من السابق لأوانه "دفن" أوبك\n\nhttp://t.co/j36hqkymAr\n\nذكرت صحيفة "The National Interest " أن الحديث بدأ ح...', 'Tue Dec 02 22:23:34 +0000 2014', 2441, 'http://pbs.twimg.com/profile_images/378800000052535500/12cb1cad315f9455e25ec6bfada010d5_normal.png', '2014-12-03 22:18:56'),
(314, '539901974724886528', '1896607982', 'RT @SultanAlQassemi: Following Gulf states agreement in Riyadh - Qatar officials attend UAE National Day celebrations in Doha http://t.co/Z…', 'Tue Dec 02 22:00:36 +0000 2014', 309, 'http://pbs.twimg.com/profile_images/519894043052883968/60-naANy_normal.jpeg', '2014-12-03 22:18:56'),
(315, '539901619958460416', '19758502', 'RT @SultanAlQassemi: Following Gulf states agreement in Riyadh - Qatar officials attend UAE National Day celebrations in Doha http://t.co/Z…', 'Tue Dec 02 21:59:11 +0000 2014', 2060, 'http://pbs.twimg.com/profile_images/413646279906828288/uvM8s5nl_normal.jpeg', '2014-12-03 22:18:56'),
(316, '539901571048296448', '134230908', 'RT @SultanAlQassemi: Following Gulf states agreement in Riyadh - Qatar officials attend UAE National Day celebrations in Doha http://t.co/Z…', 'Tue Dec 02 21:59:00 +0000 2014', 1375, 'http://pbs.twimg.com/profile_images/519465804312502272/wkRAcbbK_normal.jpeg', '2014-12-03 22:18:57'),
(317, '539901131946598400', '1597512912', 'RT @SultanAlQassemi: Following Gulf states agreement in Riyadh - Qatar officials attend UAE National Day celebrations in Doha http://t.co/Z…', 'Tue Dec 02 21:57:15 +0000 2014', 417, 'http://pbs.twimg.com/profile_images/378800000140988685/9b6d8a55b12d58692cada501d101d534_normal.jpeg', '2014-12-03 22:18:57'),
(318, '539900503170093056', '46744791', 'Following Gulf states agreement in Riyadh - Qatar officials attend UAE National Day celebrations in Doha http://t.co/ZiXJ01AL61 Wam Arabic', 'Tue Dec 02 21:54:45 +0000 2014', 309023, 'http://pbs.twimg.com/profile_images/499665029017649152/H-SPRCEI_normal.jpeg', '2014-12-03 22:18:57'),
(319, '539876118858584065', '2532487766', 'RT @LowlandsSN: LSN attended the United #Arabic #Emirates National Day celebrations in The Hague with thanks to the ambassador H.E. Abdalla…', 'Tue Dec 02 20:17:51 +0000 2014', 125, 'http://pbs.twimg.com/profile_images/530085226827878401/2UnQRMBK_normal.jpeg', '2014-12-03 22:18:57'),
(320, '539876039623987202', '2235614311', 'The National Library of #Israel opens its doors to dialogue, in #Arabic and #Hebrew http://t.co/N0ljw9apg2 #peace #Coexist #Palestine', 'Tue Dec 02 20:17:32 +0000 2014', 70, 'http://pbs.twimg.com/profile_images/378800000844278921/e735f77a17757958884990b16250737c_normal.jpeg', '2014-12-03 22:18:57'),
(321, '540268295166119937', '479582242', 'Le spese aumentarono,si procurava il credito a tassi impossibili, aumentarono tasse e benzina,aumentarono  le spese sanitarie...', 'Wed Dec 03 22:16:13 +0000 2014', 33, 'http://pbs.twimg.com/profile_images/530485407272931328/5A5_E2iR_normal.jpeg', '2014-12-03 22:19:00'),
(322, '540257000530395136', '1544125128', 'RT @munnops: "Söögiga klassi tulek on rangelt keelatud!" \n*Tuleb iga päev tassi kohviga tundi.*', 'Wed Dec 03 21:31:21 +0000 2014', 32, 'http://pbs.twimg.com/profile_images/540256559432237058/PU5TKrcT_normal.jpeg', '2014-12-03 22:19:00'),
(323, '540255507114909696', '708773624', 'Si può far chiedere ai 3 giornalai .... se i tassi a Sant Moritz', 'Wed Dec 03 21:25:25 +0000 2014', 4887, 'http://pbs.twimg.com/profile_images/530233211608391680/DVZi5inb_normal.jpeg', '2014-12-03 22:19:00'),
(324, '540255414374641666', '1219888831', '@braveheartmmt @JerryPolemica1 @Chri_Oo ma strutturalmente abbiamo tassi di inflazione diversi, come non può essere temporaneo senza trasf?', 'Wed Dec 03 21:25:02 +0000 2014', 320, 'http://pbs.twimg.com/profile_images/470896671246008320/pz97Sj-1_normal.jpeg', '2014-12-03 22:19:00'),
(325, '540254928586166272', '449714985', 'Ma ei tohi kohvi vererõhu pärast juua ja täna juba üle 10 tassi kohvi joonud.. Tubli olen! #Kohvihoolik', 'Wed Dec 03 21:23:07 +0000 2014', 232, 'http://pbs.twimg.com/profile_images/538756510680371200/4fWgALNJ_normal.jpeg', '2014-12-03 22:19:00'),
(326, '540254023744757760', '2599925622', 'RT @PencilsOfPromis: Retweet for a good cause. Each RT sends $1 to build a school for children in Ghana. Thank you, @livelokai! #SharePromi…', 'Wed Dec 03 21:19:31 +0000 2014', 66, 'http://pbs.twimg.com/profile_images/531505355784994816/7UlNjjDY_normal.jpeg', '2014-12-03 22:19:00'),
(328, '540252694376501248', '856814010', 'Giusto per saperne qualcosa in più...chi può inizi a pensarci...un suggerimento per il vostro futuro http://t.co/xlzb5YSUnh', 'Wed Dec 03 21:14:14 +0000 2014', 363, 'http://pbs.twimg.com/profile_images/3566359269/a3fb7216fb99a0b0d24c68edcf97ff8f_normal.jpeg', '2014-12-03 22:19:00'),
(329, '540250626354319360', '83584668', 'RT @thebenjimusic: so my dad tells me he''s sitting next to some rapper whose super high on his plane to Miami and then sends me this http:/…', 'Wed Dec 03 21:06:01 +0000 2014', 195, 'http://pbs.twimg.com/profile_images/378800000066213330/099bb07dbf11e8a9cfb580e4a8ff4b2f_normal.jpeg', '2014-12-03 22:19:00'),
(330, '540247785220874240', '83584668', 'RT @PencilsOfPromis: Retweet for a good cause. Each RT sends $1 to build a school for children in Ghana. Thank you, @livelokai! #SharePromi…', 'Wed Dec 03 20:54:43 +0000 2014', 195, 'http://pbs.twimg.com/profile_images/378800000066213330/099bb07dbf11e8a9cfb580e4a8ff4b2f_normal.jpeg', '2014-12-03 22:19:00'),
(331, '540246298109431808', '2689089643', 'pretty much sums up the squad http://t.co/VOT01Oy5GI', 'Wed Dec 03 20:48:49 +0000 2014', 92, 'http://pbs.twimg.com/profile_images/539276743899901952/28V9JwC1_normal.jpeg', '2014-12-03 22:19:00'),
(332, '540246173450522625', '423179771', 'RT @WarnerBrosIta: Lotteremo con Bilbo fino alla fine. Sarete dei nostri per l''#UltimoViaggio? Al cinema dal 17 dicembre http://t.co/2rvCjG…', 'Wed Dec 03 20:48:19 +0000 2014', 155, 'http://pbs.twimg.com/profile_images/451888503874670592/i99dz2rv_normal.jpeg', '2014-12-03 22:19:00'),
(333, '540245556099284994', '2217943762', 'RT @monctonwildcats: Alex Dubeau, Dominic Talbot-Tassi &amp; Jason Rioux visited with Wildcats Fan and Goalie, 13 year old… http://t.co/BREyX2Y…', 'Wed Dec 03 20:45:52 +0000 2014', 117, 'http://pbs.twimg.com/profile_images/540260616997728256/TtUqi2eh_normal.jpeg', '2014-12-03 22:19:00'),
(334, '540242958591614976', '39556047', '@ADTstaysafe Oh and also, just a tip, trying to blame the customer is never a good strategy.', 'Wed Dec 03 20:35:33 +0000 2014', 963, 'http://pbs.twimg.com/profile_images/497929394548396033/3x9HoDfF_normal.jpeg', '2014-12-03 22:19:00'),
(335, '540242679271923712', '39556047', '@ADTstaysafe is the absolute WORST company I have ever dealt with. 3 months without service, no refunds and an hour call with no progress?!?', 'Wed Dec 03 20:34:26 +0000 2014', 963, 'http://pbs.twimg.com/profile_images/497929394548396033/3x9HoDfF_normal.jpeg', '2014-12-03 22:19:01'),
(336, '540243040674136064', '2552541264', '“دروب ” برنامج وطني يستهدف الطلاب والباحثين عن عمل والموظفين:   ( الريادة ) – محليات :: يكشف صندوق تنمية الموا... http://t.co/zam8SRWnn5', 'Wed Dec 03 20:35:52 +0000 2014', 31, 'http://pbs.twimg.com/profile_images/496696596621299714/YoP8MFwk_normal.jpeg', '2014-12-03 22:19:09'),
(337, '540211761979211777', '2552541264', 'مدير شرطة منطقة الباحة: يقلد “المالح و العتيبي” رتبتي “عميد”:   ( الريادة ) – الباحة :: قلد اللواء / مسفر بن س... http://t.co/hzAnJpyBYD', 'Wed Dec 03 18:31:35 +0000 2014', 31, 'http://pbs.twimg.com/profile_images/496696596621299714/YoP8MFwk_normal.jpeg', '2014-12-03 22:19:09'),
(338, '540206910301941760', '462208882', '“الإسكان” تعمل على 13.6 ألف وحدة سكنية شمال #جدة :   ( ) – جدة :: كشف مصدر مسؤول أن #وزارة_لإسكان #السعودية تعم ... http://t.co/OGrlxCvRLv', 'Wed Dec 03 18:12:18 +0000 2014', 6420, 'http://pbs.twimg.com/profile_images/442318441765429248/_jGhVzEM_normal.jpeg', '2014-12-03 22:19:09'),
(339, '540201345752375298', '2552541264', '“الإسكان” تعمل على 13.6 ألف وحدة سكنية شمال جدة:   ( الريادة ) – جدة :: كشف مصدر مسؤول أن وزارة الإسكان تعمل ح... http://t.co/YKV0o4bt4a', 'Wed Dec 03 17:50:11 +0000 2014', 31, 'http://pbs.twimg.com/profile_images/496696596621299714/YoP8MFwk_normal.jpeg', '2014-12-03 22:19:10'),
(340, '540198442350297088', '251720979', 'RT @dar_alsalaf: تلاوة طيبة «يا أيها الذين آمنوا اتقوا الله»  http://t.co/M3S3h2ESZN', 'Wed Dec 03 17:38:39 +0000 2014', 498, 'http://pbs.twimg.com/profile_images/444921086291894272/sPk7soRc_normal.jpeg', '2014-12-03 22:19:10'),
(341, '540082873726824451', '498260555', 'RT @dar_alsalaf: تلاوة طيبة «يا أيها الذين آمنوا اتقوا الله»  http://t.co/M3S3h2ESZN', 'Wed Dec 03 09:59:26 +0000 2014', 363, 'http://pbs.twimg.com/profile_images/2249950806/image_normal.jpg', '2014-12-03 22:19:10'),
(342, '540057582182744064', '274287440', 'تَدبّــروا ..\n\nhttp://t.co/880dGWEvEk', 'Wed Dec 03 08:18:56 +0000 2014', 271, 'http://pbs.twimg.com/profile_images/535348461671944192/GjsrUG7b_normal.jpeg', '2014-12-03 22:19:10'),
(343, '540026984038821889', '2708171078', 'RT @dar_alsalaf: تلاوة طيبة «يا أيها الذين آمنوا اتقوا الله»  http://t.co/M3S3h2ESZN', 'Wed Dec 03 06:17:20 +0000 2014', 173, 'http://pbs.twimg.com/profile_images/539243922250153985/voI4CBUg_normal.jpeg', '2014-12-03 22:19:10'),
(344, '540003478689423360', '297317876', 'RT @dar_alsalaf: تلاوة طيبة «يا أيها الذين آمنوا اتقوا الله»  http://t.co/M3S3h2ESZN', 'Wed Dec 03 04:43:56 +0000 2014', 3606, 'http://pbs.twimg.com/profile_images/526099984614047744/LhvggcgK_normal.jpeg', '2014-12-03 22:19:10'),
(345, '539984960153600001', '297894871', 'تلاوة طيبة «يا أيها الذين آمنوا اتقوا الله»  http://t.co/M3S3h2ESZN', 'Wed Dec 03 03:30:21 +0000 2014', 10082, 'http://pbs.twimg.com/profile_images/2440182562/8196_normal.png', '2014-12-03 22:19:10'),
(346, '539969124571426816', '2552541264', 'خلال 16 ساعة تعرض “6 أشخاص لإصابات خطيرة أثر حوادث مرورية بمنطقة الباحة:   ( الريادة ) – الباحة :: تعرض “6 أشخ... http://t.co/lRkf94Z4CY', 'Wed Dec 03 02:27:26 +0000 2014', 31, 'http://pbs.twimg.com/profile_images/496696596621299714/YoP8MFwk_normal.jpeg', '2014-12-03 22:19:10'),
(347, '539870923068022784', '2612027790', 'RT @AsSalafiyaa: Invoquez pour Sheikh Salih Al Fawzan qui est malade et n''a pu donner cours depuis presque une semaine à Ryadh . Qu''Allah l…', 'Tue Dec 02 19:57:13 +0000 2014', 326, 'http://pbs.twimg.com/profile_images/517708473472004096/dBj9A25D_normal.jpeg', '2014-12-03 22:19:10'),
(348, '539858629092847616', '2552541264', '” بالصور”: الأمير مشارى يتفقد سير العمل في جهات حكومية ببلجرشي: ( الريادة ) – بالجرشي :: اطلع أمير منطقة الباح... http://t.co/Qlm44YiEWQ', 'Tue Dec 02 19:08:21 +0000 2014', 31, 'http://pbs.twimg.com/profile_images/496696596621299714/YoP8MFwk_normal.jpeg', '2014-12-03 22:19:10'),
(349, '539815968659103744', '2552541264', 'إنقلاب دورية “لأمن الطرق” بعقيق الباحه وإصابة قائدها:   ( الريادة ) – العقيق :: أُصيب رجل امن في حادثة انقلاب ... http://t.co/IyFBY90srM', 'Tue Dec 02 16:18:50 +0000 2014', 31, 'http://pbs.twimg.com/profile_images/496696596621299714/YoP8MFwk_normal.jpeg', '2014-12-03 22:19:10'),
(350, '539793991835717633', '2552541264', 'بالفيديو.. “داعش” يتبنى إطلاق النار على المقيم الدنماركي بالرياض:   ( الريادة ) – الرياض :: أظهر مقطع فيديو تد... http://t.co/YLLA8FAgWl', 'Tue Dec 02 14:51:31 +0000 2014', 31, 'http://pbs.twimg.com/profile_images/496696596621299714/YoP8MFwk_normal.jpeg', '2014-12-03 22:19:10');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=22 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add site', 6, 'add_site'),
(17, 'Can change site', 6, 'change_site'),
(18, 'Can delete site', 6, 'delete_site'),
(19, 'Can add twitte', 7, 'add_twitte'),
(20, 'Can change twitte', 7, 'change_twitte'),
(21, 'Can delete twitte', 7, 'delete_twitte');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$12000$QJY2H0hb4hty$bgasYG35oazoSiBx5o56hLbNddhAOkW/ZZMvXm92XOs=', '2014-12-03 18:38:41', 1, 'mahmoud', '', '', 'test@mail.com', 1, 1, '2014-11-30 14:40:10'),
(2, 'pbkdf2_sha256$12000$6GEOG52WH4V9$V3X1CPdW3DDrifTgBXPB7kN75hmWudn1eU4MWumFhA0=', '2014-12-01 02:02:32', 0, 'asd', '', '', 'asd@asd.co', 0, 1, '2014-12-01 02:02:32'),
(3, 'pbkdf2_sha256$12000$Z0hXcPP6jRpQ$nEPYC25p754+PtfOrVf6RWvM/2QuLzqpfHai7OBvZmI=', '2014-12-01 02:29:26', 0, 'asddd', '', '', 'asdaa@asd.co', 0, 1, '2014-12-01 02:29:26'),
(4, 'pbkdf2_sha256$12000$8d85nlHdkPE5$v2G6H9hMQrHcN9odrssKIRzPb0dnos3aF75y+qJxFLo=', '2014-12-01 02:32:51', 0, 'sad', '', '', 'sdaaaa@aa.vv', 0, 1, '2014-12-01 02:32:51'),
(5, 'pbkdf2_sha256$12000$aPt0cH30NsDN$QpRvmIGhLXRA/fAN9FfjH8YnHDElgHe6etBF7cnExQ0=', '2014-12-01 02:36:31', 0, 'ad', '', '', 'asdas@ads.aaa', 0, 1, '2014-12-01 02:36:31'),
(6, 'pbkdf2_sha256$12000$HNGtrMyxOalP$GQbf1Spy4z2I6cUVMgaf7dRssYUKClkS5NgZQlJcyOY=', '2014-12-01 02:54:18', 0, 'sadaaaaaa', '', '', 'aaaa@a.zzzz', 0, 1, '2014-12-01 02:54:18'),
(7, 'pbkdf2_sha256$12000$ien1CGmeXon0$almPmA7bIdZdl4agVCkxGaBnmDqFwOsxRWZd1ZsFTw4=', '2014-12-01 04:32:48', 0, 's', '', '', 'asd@asd.co', 0, 1, '2014-12-01 04:32:48'),
(8, 'pbkdf2_sha256$12000$hwkQxJTlRWZq$jqjdBA+bFBDXHSKtnMvPPE1P3pS8NgrMBw97YTvNeCI=', '2014-12-01 04:41:56', 0, 'ee', '', '', 'ee@rr.co', 0, 1, '2014-12-01 04:41:50');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_239d946_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'content type', 'contenttypes', 'contenttype'),
(5, 'session', 'sessions', 'session'),
(6, 'site', 'sites', 'site'),
(7, 'twitte', 'app', 'twitte');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2014-11-30 14:39:12'),
(2, 'auth', '0001_initial', '2014-11-30 14:39:28'),
(3, 'sessions', '0001_initial', '2014-11-30 14:39:30'),
(4, 'sites', '0001_initial', '2014-11-30 14:39:30');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1pw4nuhdva4t6j8jhiofqg1tdwguzn1n', 'ZWZiNjQxYTI1ZWQ3OThiZTAxMjc4MmNhYTYwMjJlZDQ5YzlmZjNkYTp7fQ==', '2014-12-15 04:46:28'),
('3oibo5j8upb6e9ylsqp4kwg95uxjx906', 'ZWZiNjQxYTI1ZWQ3OThiZTAxMjc4MmNhYTYwMjJlZDQ5YzlmZjNkYTp7fQ==', '2014-12-14 14:41:27'),
('3z07k5b2o8mawjf7dfimqu38svdb1zbw', 'ZWZiNjQxYTI1ZWQ3OThiZTAxMjc4MmNhYTYwMjJlZDQ5YzlmZjNkYTp7fQ==', '2014-12-15 03:36:00'),
('5g2szhy6fp62rfgr3ll13vwn6m2y7aak', 'ODMyNjczNjg0ODExMDMwNjY3ZjJhNmY2MGU1OGJiM2YxMDI3ZmNjYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImFwcC5iYWNrZW5kcy5FbWFpbEF1dGhCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MSwiX2F1dGhfdXNlcl9oYXNoIjoiNzNiYzdjMmEyOTI2N2I0ZDUyZTRhZWMyOWYzY2U0ZmQzMjFkYTgxMiJ9', '2014-12-15 05:19:08'),
('7chhyvsl55hi1thwjw7e6q58hmhvx3rt', 'ZWZiNjQxYTI1ZWQ3OThiZTAxMjc4MmNhYTYwMjJlZDQ5YzlmZjNkYTp7fQ==', '2014-12-15 03:33:10'),
('ep3u3wzh66oaj0hs1l4h21l3d95drd6x', 'ZWZiNjQxYTI1ZWQ3OThiZTAxMjc4MmNhYTYwMjJlZDQ5YzlmZjNkYTp7fQ==', '2014-12-15 03:49:28'),
('f1xusnf9vsksjbi1j08eyrrfcvny5140', 'NzRiZTE0NWViZTI4MDZiMDkwNDRkNGUwN2IyZTkxNWZjMGRlMzJhZjp7Il9hdXRoX3VzZXJfaGFzaCI6IjczYmM3YzJhMjkyNjdiNGQ1MmU0YWVjMjlmM2NlNGZkMzIxZGE4MTIiLCJfYXV0aF91c2VyX2lkIjoxLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhcHAuYmFja2VuZHMuRW1haWxBdXRoQmFja2VuZCJ9', '2014-12-17 18:38:41'),
('lt1gb1yneupq0ogxbt6u872v2uczxdh7', 'ZWZiNjQxYTI1ZWQ3OThiZTAxMjc4MmNhYTYwMjJlZDQ5YzlmZjNkYTp7fQ==', '2014-12-15 03:44:19'),
('m0nmyvn35kfdxr7fjtobxaju213xx9b3', 'ZWZiNjQxYTI1ZWQ3OThiZTAxMjc4MmNhYTYwMjJlZDQ5YzlmZjNkYTp7fQ==', '2014-12-15 03:35:29'),
('ps3izeutwl5fevkrdht4o39voy1fztq6', 'ZWZiNjQxYTI1ZWQ3OThiZTAxMjc4MmNhYTYwMjJlZDQ5YzlmZjNkYTp7fQ==', '2014-12-15 03:39:09');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_2a2598e9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissi_permission_id_1ab4addf_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permissi_content_type_id_129dcafd_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_642891bc_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6478c946_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_382cc4d6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_perm_permission_id_47ce9908_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

