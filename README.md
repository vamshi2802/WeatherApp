WEATHER API using Django

This Weather API is built using Django, which serves weather data to its users. The documentation provides step-by-step instructions on creating a virtual environment, installing necessary dependencies, migrating data, and processing data ingestion. Moreover, it furnishes users with information on accessing and utilizing the API.

The API endpoints allow users to access the following functionalities:

/api/weather - gives the weather data

/api/weather/stats - obtains the statistics about the data

/api/schema/swagger-ui/ - provides a description of the functionalities available in the API.


Prerequisites

Python (3.7 or higher)
Virtualenv
SQLite 

Installation and Usage
To create a virtual environment:
pip install virtualenv
virtualenv env


To activate the virtual environment:
env/Scripts/activate (Windows)
source env/bin/activate (Mac/Linux)


Install the required dependencies:
pip install -r requirements.txt


Run migrations:
python3 src/manage.py makemigrations
python3 src/manage.py migrate


Ingest the data:
python3 ingest.py


Run the server:
python3 src/manage.py runserver



Access the API endpoints, use the following links:

http://127.0.0.1:8000/api/weather
http://127.0.0.1:8000/api/weather/stats
http://127.0.0.1:8000/api/schema/swagger-ui/


To run tests:
cd src
python manage.py test


To deploy the API on AWS, follow these three steps:

1.Deploy the Django API using AWS EC2 and the database with Amazon Relational Database Service (RDS).
2.Utilize AWS S3 to store data.
3.Schedule data ingestion with AWS EC2 by creating a cron job and store the ingested data in the RDS database.
