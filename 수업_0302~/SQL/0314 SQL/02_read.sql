SELECT rowid, * FROM classmates;

SELECT rowid, name FROM classmates;

SELECT rowid, name FROM classmates LIMIT 1;

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

SELECT rowid, name FROM classmates WHERE address='서울';

SELECT DISTINCT age FROM classmates;