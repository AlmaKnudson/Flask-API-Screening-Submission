

# Flask API Screening - Core

## Deliverable
A simple messaging application, built in Python using Flask/Python (no Django please). This application must be able to send and store simple textual messages that can then be retrieved via a RESTful API. This project should take between 2 - 4 hours.

## MVP Requirements

- This application must be unit tested. Please use PyTest for Python
- The data that is stored must be accessible via a RESTful API. You can store in memory or a DB
- A README file with documentation on: how to build it, how to use it, how to run the tests

### Create thread
Creates a thread on behalf of a user.

#### Request
```
POST /thread 
{
    "users": [
        "quinn",
        "jeff_goldblum"
    ]
}
```

#### Response
```
{
    "thread_id": 123
}
```

### Send message
Creates a message on behalf of a user on a thread.

#### Request
```
POST /thread/:thread_id/:username
{
    "message": "This is a message!"
}
```

#### Response
```
204
```

### Get thread
Returns a list of messages by thread ID

#### Request
```
GET /thread/:thread_id
```

#### Response
```
{
    "messages": [
        {"username": "jeff_goldblum", "message": "This is a message!"},
        ...
    ]
}
```

### Bonus
- Include a database for storage instead of in memory
- Include a functioning React user interface on top of the RESTful API (even more bonus for tests!)
- Make it function in real-time using sockets



Flow chart demonstrating how to handle Thread creation:
![alt text](https://github.com/AlmaKnudson/flaskProject/blob/master/app/resources/flow_charts/create_thread_flow.PNG?raw=true)


Flow chart demonstrating how to handle Message creation:
![alt text](https://github.com/AlmaKnudson/flaskProject/blob/master/app/resources/flow_charts/create_message_flow.PNG?raw=true)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.
Pip 20.3.1, Python 3.9 and virtualenv on MacOS was used for the development. Please make sure that the pip version is correct before running the commands below:

MacOS/Linux (Terminal)
```bash
git clone https://github.com/AlmaKnudson/flaskProject.git
cd flaskProject
virtualenv knock
source knock/bin/activate
pip install -r requirements.txt
python run-app.py
```

Windows (CMD) -- Please keep in mind that I only checked that it ran once on windows and this is not thoroughly tested
```bash
git clone https://github.com/AlmaKnudson/flaskProject.git
cd flaskProject
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
python run-app.py
```

## Tests
Navigate to the project directory "flaskProject" and run pytest
```bash
pytest 
```

## Database
Currently, configured to point to an instance of MongoDb running on MS Azure. The temporary username and password will expire in a week, but should be sufficient to play around with a bit.

## Postman
Provided is a postman collection to make calls to the messaging API. Feel free to let loose and have some fun sending messages! 

## Limitations & Potential enhancements
Threads are restricted to contain between [2-100] users and messages in the thread are restricted to be as long as a Tweet (280 characters).
FYI, a thread can currently contain duplicate usernames in a given thread. This is a clear area for improvement.

# Architectural Considerations & Design Decisions
## Database
### Why MongoDB instead of DynamoDB, Sqlite, MySQL, Redis etc? 
##### Here it is really a matter of taste. I wanted persistence that would be quick to integrate with and was decoupled from the API application. Since I already had a MongoDB cluster setup; that fit the bill.

## Framework 
### Why Flask instead of FastAPI, Django etc?
##### I chose Flask because I have used it before for simple API applications. With that said, I think that FastAPI is the preferred choice here. It is more performant than Flask. It also provides DI, data validation and documentation generation (SwaggerUI and ReDoc) out of the box. All of which Flask is lacking. If I were to continue this messaging project, I would quickly replace Flask with FastAPI. However, I was able to make use of some of Flask's features. Like serialization and modularity using Blueprints. I guess it is also worth noting that Django could handle all of my needs here, but I was preferential to a micro-framework instead.

## Configuration
### What is going on with configuration?
##### I chose to hard code configuration and secrets in the .env file. The correct approach would be to leverage Secrets Manager (AWS) or Key Vault (Azure) paired with a more robust configuration module.

## Error Handling Concept
### What is the current state of error handling?
##### Honestly, I did not really get around to defining a robust error handling strategy even though this is a must-have in a production level application.

## Logging
### What is logged and when? 
##### I have logs that rotate after 10mb. While the logging is not really useful with such a tiny application, it provides a great foundation for a production level application. It would also be important to consider anonymization of logs since they contain usernames.

## Automated Builds
### Where can I manage them?
##### I configured an automated build for this repo using [GitHub Actions](https://github.com/AlmaKnudson/flaskProject/actions/runs/413861131). You can manually trigger a build from GitHub or it will be triggered when you push to the repo. I included a linter (flake8) in the build job to help keep code smells to a minimum. There is a [Knock Task](https://github.com/AlmaKnudson/flaskProject/projects/1#card-51028315) to take a peek at what the linter picked up.

## Pipeline (CI/CD) 
### This would be nice to finish setuping with more time...
##### To be added (due by 01.01.2050)
