CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL
);

INSERT INTO articles
VALUES ('1번제목', '1번내용');

-- 테이블 이름 변경
ALTER TABLE articles
RENAME TO news;

-- 새로운 컬럼 추가
ALTER TABLE news
ADD COLUMN created_at TEXT NOT null;

-- 오류 해결
-- 1. not null 설정 없이 추가
ALTER TABLE news
ADD COLUMN created_at TEXT;

INSERT INTO news
VALUES ('제목','내용',datetime('now'));

-- 2. 기본 값(DEFAULT) 설정하기
ALTER table news
ADD COLUMN subtitle TEXT not NULL
DEFAULT '소제목';

-- 컬럼 이름 바꾸기
ALTER TABLE news
RENAME COLUMN title TO main_title;

ALTER TABLE news
DROP COLUMN subtitle;

--SQL
SELECT * FROM articles_article;
SELECT * FROM articles_article WHERE rowid=1;
DELETE FROM articles_artile WHERE id=1;
--ORM
Article.objects.all()
Article.objects.get(pk=1)
Article.objects.get(pk=1).delete()
-- print(ORM.query())하면 SQL문 뜸