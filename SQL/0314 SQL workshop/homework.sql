CREATE TABLE classmates (
  name TEXT,
  age INT,
  address TEXT
);

INSERT INTO classmates (name,age,address)
VALUES('홍길동',20,'seoul');

INSERT into classmates VALUES('홍길동',20,'서울');

INSERT into classmates values(adderes='seoul',age=20,name='홍길동');

insert into classmates (address,age,name) VALUES('seoul',20,'홍길동');