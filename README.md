# pythonmicroservices
code to insert RAW data coming as json and pushing to oracle db hosted locally. Docker is also used to containerize the microservices. also fetching back the data from database in tsv format.

Assumption made :
1. The RAW data is in from of multiple entries (JSON) of employee data :id and name.
2. The database is already setup locally with a table available for adding/fethching entries.
3. The data fetched is in format .tsv which is present in file where the docker run command is executed.

######
CODE EXPLANATION
######
The code is divided into two microservices
insert and fetch microservice. each are independently connecting with the database.
the docker run command is executed on each of the separated microservice

I have used flask module for python to access api locally, where the get and post calls are made to the code to insert and fetch the data from oracle database.
the oracledb module is used to connect with oracle db.
The fetch microservice collects the data from the database and store it in file named employee_details.tsv locally
docker volume is mounted to run the and fetch the file.

commands to be run on folder :
docker commands to run on insert data microservice:
1. docker build -t <imagenameasrequired> .
2. docker run -p 5001:5001 -d --name <asrequiredcontainername> -e db_user='<username>' -e db_pass='<dbpassword>' -e db_host='<inserthostip>' -e db_service='<dbservicename' <imagenamecreatedfromstep1>
3. pass the data to the microservice via postman ( sample data mentioned below ).


1. docker build -t <imagenameasrequired> .
2. docker run -p 5001:5001 -d --name <asrequiredcontainername> -e db_user='<username>' -e db_pass='<dbpassword>' -e db_host='<inserthostip>' -e db_service='<dbservicename' -v <localabsolutepathtogetthetsvfile>:/app/tsv <imagenamecreatedfromstep1>

For scheduling the code to run exact at particular time of day (00.00) we can use cron.
commands and steps to used :
1.install cron inside the host
2.run command: 
0 0 * * * <docker run command to start insert db data microservice> && <docker run command to start fetch data from db microservice>
3. The above will the container at 00.00 local time sequentially, meaning second docker run command will run only if the first is successful.


sample json data to be passed via postman to insert data into database:
{
  "entries": [
    {
      "id": 1,
      "name": "John Doe"
    },
    {
      "id": 2,
      "name": "Jane Smith"
    },
    {
      "id": 3,
      "name": "Mark Johnson"
    }
  ]
}
