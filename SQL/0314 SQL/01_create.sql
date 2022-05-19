-- SQLite
INSERT INTO classmates (name,age) VALUES ('홍길동', 23);

INSERT INTO classmates VALUES ('홍길동', 30, '서울');

SELECT * FROM classmates

SELECT rowid, * FROM classmates;

drop TABLE classmates;

CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address) VALUES ('홍길동',30,'서울');

drop TABLE classmates;

CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates VALUES 
('홍길동',30,'서울'),
('김철수',30,'대전'),
('이싸피',26,'광주'),
('박삼성',29,'구미'),
('최전자',28,'부산');
