-- upload seed data from csv
COPY tunes_data FROM '/data/tunes-data-2020-10-15.csv' DELIMITER ',' CSV HEADER;
