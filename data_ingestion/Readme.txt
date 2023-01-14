$ The data-upload.ipynb contains the script to perform data ingestion.
$ To run everything in dev mode, run the database inside a container -- use the command_to_run.txt for reference.

$ To run the complete data ingestion pipeline inside containers, cd to 'data_ingestion_docker' folder and run `docker-compose up`.
$ This command will setup the postgres database inside a container and then create another container to run the data ingestion script, which will insert data into the database.