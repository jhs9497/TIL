/*
앞에 . 을 붙히는 명령어는 sql이 아니고 sqlite에서 제공하는 명령어다
뒤에 ;을 붙히는 명령어가 sql명령어다.

sql 명령어의 끝은 언제나 세미콜론(;)으로 끝난다!


1) sqlite3 tutorial.sqlite3

2) .databases  

3) csv 파일 SQL폴더에 넣고

4) .mode csv

5) .import hellodb.csv examples

6) SELECT * FROM examples;

.headers on -> 데이터 뽑을 때 제목 보여줘
.mode column -> 데이터 뽑을 때 column을 보여줘
*/


-- 한 줄 주석

/*
  여러줄 주석
*/

-- CREATE TABLE
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
);

-- TABLE 확인 명령어
.tables

-- 특정 테이블 스키마 조회
.schema classmates

-- 특정 테이블 삭제
-- (주의)
-- 이 명령어를 치기 전에는
-- 반드시 3번 이상 스스로에게 
-- 내가 이 명령어를 쳐도 되는지 되묻습니다.
DROP TABLE classmates;

-- Data 추가(INSERT)
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 30, '서울');

-- Data 추가(INSERT) ver02 - 모든 컬럼에 넣을거면 가능인데 권장은 X
INSERT INTO classmates 
VALUES ('홍길동', 30, '서울');


--CREATE TABLE with NOT NULL
CREATE TABLE classmates(
  id INTEGER PRIMARY KEY,   --프라이머리 키를 정의할 땐 not int but INTEGER 
  name TEXT NOT NULL,
  age int NOT NULL,
  address TEXT NOT NULL
);

/*
  <<SELECT 구문 순서>>

  SELECT 컬럼 목록
  FROM 테이블명
  WHERE 로우 필터링 조건
  ODER BY 정렬 조건
  LIMIT 카운트 OFFSET 카운트
  GROUP BY 컬럽
  HAVING 그룹 필터링 조건;
*/

-- SELECT (테이블 내의 모든 data 확인)
SELECT * FROM classmates;

-- data id 확인
SELECT rowid, * FROM classmates; -- 자동으로 id 생성해줌


-- 특정한 컬럼만 가져오기
SELECT rowid, name 
FROM classmates;

-- SELECT with LIMIT 몇개 가져올꺼야 ?
SELECT rowid, name 
FROM classmates
LIMIT 1;

-- classmates에서 id, name 컬럼값을 3번째있는거 한 개만 가져온다면 ?
SELECT rowid, name
FROM classmates
LIMIT 1 OFFSET 2;

--필터링해서 가져올때
SELECT rowid, name, age, address
FROM classmates
WHERE address='서울';

-- classmates에서 age 값 전체를 중복없이 가져온다면 ?
SELECT DISTINCT age
FROM classmates;

-- 필드값 삭제
DELETE FROM classmates
WHERE rowid=4;cv.cvcvv.v

-- AUTOINCREMENT (ID값이 django처럼 고유값을 갖게) 
CREATE TABE tests (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

-- 필드값 UPDATE
UPDATE classmates
SET name='현식', address='부산'
WHERE rowid=3;

-- WHERE 심화
SELECT last_name, age
FROM users
WHERE age >= 30;

--필드의 갯수 COUNT
SELECT COUNT(*)
FROM users;

-- 30살 이상인 사람들의 평균 나이는 ?
SELECT AVG(age) --as average_age 추가하면 이름짓기 가능
FROM users
WHERE age >= 30;

-- users에서 계좌 잔액(balance)이 가장 높은 사람과 액수는 ? MAX
SELECT first_name, MAX(balance)
FROM users
GROUP BY first_name;

-- WHERE column LIKE
/*
  2% : 2로 시작하는 값
  %2 : 2로 끝나는 값
  %2% : 2가 들어가는 값
  _2% : 아무값이나 들어가고 두번째가 2로 시작하는 값
  1___ : 1로 시작하고 4자리인 값
  2_%_% / 2__% : 2로 시작하고 적어도 3자리인 값
*/

-- 20대인 사람
SELECT first_name, age
FROM users
WHERE age LIKE '2_';

-- 지역 번호가 02인 사람
SELECT first_name, phone
FROM users
WHERE phone LIKE '02-____-____';

--users에서 이름이 '준'으로 끝나는 사람
SELECT first_name
FROM users
WHERE first_name LIKE '%준';

--users에서 중간 번호가 5114인 사람
SELECT first_name, phone
FROM users
WHERE phone LIKE '%-5114-%';

--ODER BY -> ASC : 오름차순, DESC : 내림차순
--users에서 나이순으로 오름차순 정렬하여 상위 10개만 뽑아보면 ?
SELECT last_name, age
FROM users
ORDER BY age, last_name
LIMIT 10;

-- 
SELECT last_name, first_name, balance
FROM users
ORDER BY balance DESC
LIMIT 10;

--GROUP BY 지정된 기준에 따라 행 세트를 그룹으로 결합한다.
-- 데이터를 요약하는 상황에서 주로 사용한다.

-- users에서 각 성(last_name)씨가 몇 명씩 있는지 조회하시오.
SELECT last_name, first_name, count(*)
FROM users
GROUP BY last_name, first_name;

-- 테이블명 변경
CREATE TABLE articles(
  title TEXT NOT NULL,
  content TEXT NOT NULL
);

INSERT INTO articles (title, content)
VALUES ('1번 제목', '1번 내용');

-- 테이블명 변경
ALTER TABLE articles
RENAME TO news;

-- 새로운 컬럼 추가
ALTER TABLE news
ADD COLUMN created_at TEXT NOT NULL DEFAULT 1;

-- JOIN
-- 커리큘럼엔 없어서 넘어가지만 반드시 알고 넘어갈 것 !
-- 프로그래머스 -> 코딩테스트프랙티스 -> SQL 고득점 KIT
-- hackerrank  SQL문제 많이 보유
 