-- 데이터베이스 생성
create database sehiDB;
-- 데이터베이스 확인
show databases;
-- sehiDB 사용
use sehiDB;
-- User sehi 생성
create user 'sehi'@'localhost' identified by '1234';
-- User localhost로 접속한 sehi에게 sehiDB에 대한 권한 부여
grant all privileges on sehiDB.* to 'sehi'@'localhost';
-- User sehi의 권한 확인
SHOW GRANTS FOR 'sehi'@localhost; 



-- 데이터베이스 사용 설정
use sehiDB;

-- 테이블 삭제
drop table ITEM;

-- 테이블 생성
create table item(
	itemid int,
	itemname varchar(30),
	price int, 
	description varchar(50),
	prictureurl varchar(100),
	primary key(itemid)
);

-- 샘플 데이터 생성
insert into item values(
	1,'레몬', 500, 'Vitamin-A', 'lemon.jpg');
insert into item values(
	2,'오렌지', 1500, 'Vitamin-B', 'orange.jpg');
insert into item values(
	3,'키위', 2000, 'Vitamin-C', 'kiwi.jpg');
insert into item values(
	4,'포도', 100, 'Vitamin-D', 'grape.jpg');
insert into item values(
	5,'딸기', 2000, 'Vitamin-E', 'strawberry.jpg');
insert into item values(
	6,'감귤', 300, 'Vitamin-F', 'mandarin.jpg');

-- 작업 내용을 데이터베이스 원본에 반영
commit;

-- 데이터 확인
select * from item;
