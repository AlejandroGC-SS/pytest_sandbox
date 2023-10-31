
# Pytest personal Sandbox



## Running the Project Locally
##### Pre-requisites
- install python3.11
- run the following command to install sub dependencies
```pip install -r requirements.txt```
##### Running the tests
To run all the tests with a generated report, run the following command
```shell
pytest -s --capture sys .\tests\ --html=pytest_report.html --self-contained-html
```


## Running with docker
##### Pre-requisites
- have docker installed
##### Building the image
- run this command: ```docker build -t pytest_sandbox --rm .```
##### Running the image
- run this command: ```docker run -it --rm pytest_sandbox```
- once you're inside your docker image, run the next command: 
```pytest -s --capture sys ./tests/ --html=pytest_report.html --self-contained-html```


### Passing the generated report to your local computer
- get your container id with
```docker ps```
- run the following command
```docker cp {container_id}:/pytest_report.html  C:\git\Public\pytest_sandbox\```