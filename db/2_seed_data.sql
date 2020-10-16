-- upload seed data from csv
COPY tunes_data FROM '/data/tunes_data_2020_10_15.csv' DELIMITER ',' CSV HEADER;
