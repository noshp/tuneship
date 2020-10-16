# base image
FROM postgres:10.5-alpine

# run create.sql on init
ADD 1_create.sql /docker-entrypoint-initdb.d
ADD 2_seed_data.sql /docker-entrypoint-initdb.d
