create table youtube_comment(
   id INT NOT NULL AUTO_INCREMENT,
   target_link VARCHAR(256),
   title VARCHAR(256),
   user_id VARCHAR(256),
   user_name VARCHAR(256),
   comments Text,
   PRIMARY KEY ( id )
);