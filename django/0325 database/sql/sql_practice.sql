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


-- SELECT (테이블 내의 data 확인)
SELECT * FROM examples;

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

-- data id 확인
SELECT rowid, * FROM classmates; -- 자동으로 id 생성해줌

--CREATE TABLE with NOT NULL
CREATE TABLE classmates(
  id INTEGER PRIMARY KEY,   --프라이머리 키를 정의할 땐 not int but INTEGER 근데 이렇게 하면 id 수동으로 넣어줘야함
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
WHERE address='광주';