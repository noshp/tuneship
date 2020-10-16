--Clean the schema
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

--Create data for the music
CREATE TABLE tunes_data(
    id SERIAL,
    title VARCHAR(1024) NOT NULL,
    thumb_url VARCHAR(1024) NULL,
    media_url VARCHAR(1024) NOT NULL,
    iframe_string VARCHAR(1024),
    CONSTRAINT pk_tunes_data PRIMARY KEY
    (
        id
    ));
