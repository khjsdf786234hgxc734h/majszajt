use `cicamica$db_everything`;

alter database `cicamica$db_everything` character set utf8 collate utf8_unicode_ci;

drop table if exists `tb_bookmark`;

create table if not exists `tb_bookmark`
(
     `id`                int(11) not null primary key AUTO_INCREMENT
    ,`url`               varchar(400)
    ,`title`             varchar(400)
    ,`category`          varchar(400)
    ,`tag`               varchar(400)        
    ,`date_created`      datetime
    ,`date_last_changed` datetime
);


--drop            index `idx_title` on `tb_bookmark`;
--create fulltext index `idx_title` on `tb_bookmark`(`title`);
--drop            index `idx_url`   on `tb_bookmark`;
--create fulltext index `idx_url`   on `tb_bookmark`(`url`);



SELECT T.table_name, CCSA.character_set_name
FROM   information_schema.`TABLES` T,
       information_schema.`COLLATION_CHARACTER_SET_APPLICABILITY` CCSA
WHERE CCSA.collation_name = T.table_collation
  AND T.table_schema = 'cicamica$db_everything'
--  AND T.table_name = 'trips'
;


SELECT table_name, column_name, character_set_name, collation_name
FROM information_schema.`COLUMNS`
WHERE table_schema = 'cicamica$db_everything'
--  AND table_name = "tablename"
--  AND column_name = "columnname"
;