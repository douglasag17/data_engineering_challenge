# Data Engineering technical challenge @Flink by Douglas Ardila


## Architecture
To make everything easier to deploy, the solution was dockerized. This involves a PostgreSQL database and a Python environment.

![alt text](/images/postgresql_docker_python.png)

## UML Diagram
For the implementation of the Python module, I decided to design a solution using object-oriented programming, hence the solution could be easier to maintain and extend with new features and functionalities and also, use the same solution for different problems that might be similar.

To make monitoring easier is important to keep track of every execution that is done. To do so, the python module will log everything that happens using the logging module.

![alt text](/images/uml.jpg)

### ETL Class
The main object is an ETL Class, which runs the entire data pipeline and uses other classes to leverage its implementations, such as reading any file, running schema and data validations over that file, loading that data into a proper database, and monitoring the whole flow of the pipeline.

### Reader Class
This object is in charge of extracting the data from any file received. The correct formatting of the file is checked here, for instance: if a JSON file is received the code will check and validate that the file is a valid JSON. Finally, if everything goes well, it will read it successfully and will be stored in a Pandas DataFrame, otherwise, the execution will fail and the pipeline will stop. Remember that everything will be logged using the Logger object.
### SchemaValidator Class
This object is in charge of validating the schema of the file received with the expected schema. Given the requirement that the schema may change over time, proper checks were implemented with a certain level of flexibility. 

First, the Python module will check if the schema matches with the expected one if it's successful it will check the data types expected for each attribute, if something goes wrong at this stage the execution will stop and will notify.

If the schema does not match, it will stop the execution and will not run until a proper expected schema is passed that matches with the data received (this assumes that the schema may change, but it will not change that often).
### DataValidator Class
This object is in charge of validating the data received. Here, with the help of the Great Expectations module, several tests (expectations) will run. For instance: the number of rows, number of unique rows, number of unique rows based on a primary key, expected values over columns, nulls columns check, etc. 
### Loader Class
This object is in charge of inserting the data into a staging area of the desired database. It manages the data schema changes by creating new columns over the tables when needed. It's is important to note that this will only insert data that passed all the previous checks and it will not update nor delete any data already stored in the target database. 
### Logger Class
This object is in charge of logging everything that happens when this module runs. Given that Python already has a pretty good module for this purpose (logging), this object will inherit its functionalities.

The importance of these logs is pretty high since could be used to keep track of everything that happens when the module is executed. This data could be analyzed later on to understand the behavior of the system.

##