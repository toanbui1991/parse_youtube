CREATE TABLE `youtube_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `target_link` varchar(256) DEFAULT NULL,
  `title` varchar(256) DEFAULT NULL,
  `user_id` varchar(256) DEFAULT NULL,
  `user_name` varchar(256) DEFAULT NULL,
  `comment` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='demo table to store youtube comments';
