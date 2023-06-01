CREATE TABLE DOCUMENT_TEMPLATE(
   ID INTEGER NOT NULL,
   NAME TEXT,
   DESCRIPTION TEXT
);

INSERT INTO DOCUMENT_TEMPLATE(id, name, description)
SELECT id, md5(random()::text), md5(random()::text)
FROM generate_series(1,5) id;



