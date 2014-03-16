CREATE DATABASE IF NOT EXISTS Twitter;

-- Tweets table
DROP TABLE IF EXISTS Tweets;

CREATE TABLE IF NOT EXISTS Tweets (tweets_count char(10),
									  entities_id char(50),
									  text char (100),
									  place char(20),
									  place_id char(50),
									  favorite_count char(10),
									  id char(100),
							          in_reply_to_status_id char(50),
									  in_reply_to_screen_name char(100),
									  contributors char(10),
									  contributors_id char(50),
									  metadata_id char(50),
									  in_reply_to_status_id_str char(50),
									  retweeted_status_id char(50),
									  lang char(10),
									  in_reply_to_user_id char(50),
									  retweeted boolean,
									  coordinates char(10),
									  coordinates_id char(50),
									  geo char(10),
									  retweet_count char(10),
									  truncated boolean,
									  created_at char(50),
									  user_id char(50),
									  favorited boolean,
									  possibly_sensitive boolean);

LOAD XML LOCAL INFILE 'e:\\documents and settings\\ASALLAB\\Desktop\\Flash\\Guru_Kalam\\Code\\TwitterCrawler\\feeds_empty_q.xml' INTO TABLE Tweets ROWS IDENTIFIED BY '<Tweet>';

SELECT * FROM Tweets;


-- Users table
DROP TABLE IF EXISTS Users;

CREATE TABLE IF NOT EXISTS Users ( entities_id char(10),
									  default_profile_image boolean,
									  profile_background_image_url_https char (100),
									  profile_image_url_https char(20),
									  description char(100),
									  id char(10),
									  geo_enabled boolean,
							          is_translator boolean,
									  profile_text_color char(10),
									  profile_link_color char(10),
									  profile_background_tile boolean,
									  time_zone char(20),
									  default_profile boolean,
									  contributors_enabled boolean,
									  following boolean,
									  favourites_count char(10),
									  lang char(5),
									  listed_count char(10),
									  profile_background_image_url char(50),
									  id_str char(50),
									  notifications boolean,
									  friends_count char(10),
									  profile_sidebar_border_color char(10),
									  url char(50),
									  location char(20),
									  follow_request_sent boolean,
									  profile_image_url char(50),
									  profile_use_background_image boolean,
							          utc_offset char(20),
									  protected boolean,
									  screen_name char(50),
									  profile_banner_url char(50),
									  verified boolean,
                                      profile_sidebar_fill_color char(10),
								      followers_count char(10),
									  created_at char(50),
									  name char(50),
									  statuses_count char(10),
									  profile_background_color char(20),
									  withheld_copyright boolean);

LOAD XML LOCAL INFILE 'e:\\documents and settings\\ASALLAB\\Desktop\\Flash\\Guru_Kalam\\Code\\TwitterCrawler\\feeds_empty_q.xml' INTO TABLE Users ROWS IDENTIFIED BY '<user>';

SELECT * FROM Users;

-- Users table
DROP TABLE IF EXISTS Entities;

CREATE TABLE IF NOT EXISTS Entities ( id char(10),
									     hashtags_id char(10),
										 urls_id char(10),
										 user_mentions char(10),
										 media_id char(10));
LOAD XML LOCAL INFILE 'e:\\documents and settings\\ASALLAB\\Desktop\\Flash\\Guru_Kalam\\Code\\TwitterCrawler\\feeds_empty_q.xml' INTO TABLE Entities ROWS IDENTIFIED BY '<entities>';

SELECT * FROM Entities;

	-- hashtags table
	DROP TABLE IF EXISTS Hashtags;

	CREATE TABLE IF NOT EXISTS Hashtags ( id char(10),
											 text char(50));

	LOAD XML LOCAL INFILE 'e:\\documents and settings\\ASALLAB\\Desktop\\Flash\\Guru_Kalam\\Code\\TwitterCrawler\\feeds_empty_q.xml' INTO TABLE Hashtags ROWS IDENTIFIED BY '<hashtags>';

	SELECT * FROM Hashtags;

	-- media table
	DROP TABLE IF EXISTS Media;

	CREATE TABLE IF NOT EXISTS Media (id char(10),
										display_url char(50),
										extended_url char(50),
								        media_url char(50),
										media_url_https char(50),
										source_status_id char(50),
										type char(10),
										url char(50));

	LOAD XML LOCAL INFILE 'e:\\documents and settings\\ASALLAB\\Desktop\\Flash\\Guru_Kalam\\Code\\TwitterCrawler\\feeds_empty_q.xml' INTO TABLE Media ROWS IDENTIFIED BY '<media>';

	SELECT * FROM Media;

	-- urls table
	DROP TABLE IF EXISTS URL;

	CREATE TABLE IF NOT EXISTS URL (id char(10),
										display_url char(50),
										extended_url char(50),
										url char(50));

	LOAD XML LOCAL INFILE 'e:\\documents and settings\\ASALLAB\\Desktop\\Flash\\Guru_Kalam\\Code\\TwitterCrawler\\feeds_empty_q.xml' INTO TABLE URL ROWS IDENTIFIED BY '<urls>';

	SELECT * FROM URL;

	-- user_mentions table
	DROP TABLE IF EXISTS UserMentions;

	CREATE TABLE IF NOT EXISTS UserMentions  (id char(10),
												 name char(50),
												 screen_name char(50));

	LOAD XML LOCAL INFILE 'e:\\documents and settings\\ASALLAB\\Desktop\\Flash\\Guru_Kalam\\Code\\TwitterCrawler\\feeds_empty_q.xml' INTO TABLE UserMentions ROWS IDENTIFIED BY '<user_mentions>';

	SELECT * FROM UserMentions ;

-- Places table
DROP TABLE IF EXISTS Places;

CREATE TABLE IF NOT EXISTS Places (id char(10),
									  country char(10),
							          country_code char(5),
									  full_name char(10),
									  name char(10),
									  place_type char(10),
									  url char(50));

LOAD XML LOCAL INFILE 'e:\\documents and settings\\ASALLAB\\Desktop\\Flash\\Guru_Kalam\\Code\\TwitterCrawler\\feeds_empty_q.xml' INTO TABLE Places ROWS IDENTIFIED BY '<place>';

SELECT * FROM Places;

-- ReTweets table
DROP TABLE IF EXISTS ReTweets;

CREATE TABLE IF NOT EXISTS ReTweets (tweets_count char(10),
									  entities_id char(50),
									  text char (100),
									  place char(20),
									  place_id char(50),
									  favorite_count char(10),
									  id char(100),
							          in_reply_to_status_id char(50),
									  in_reply_to_screen_name char(100),
									  contributors char(10),
									  contributors_id char(50),
									  metadata_id char(50),
									  in_reply_to_status_id_str char(50),
									  retweeted_status_id char(50),
									  lang char(10),
									  in_reply_to_user_id char(50),
									  retweeted boolean,
									  coordinates char(10),
									  coordinates_id char(50),
									  geo char(10),
									  retweet_count char(10),
									  truncated boolean,
									  created_at char(50),
									  user_id char(50),
									  favorited boolean,
									  possibly_sensitive boolean);

LOAD XML LOCAL INFILE 'e:\\documents and settings\\ASALLAB\\Desktop\\Flash\\Guru_Kalam\\Code\\TwitterCrawler\\feeds_empty_q.xml' INTO TABLE ReTweets ROWS IDENTIFIED BY '<retweeted_status>';

SELECT * FROM ReTweets;
