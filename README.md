# Getting started
A simple [Knock Full Stack Screening - Core](https://gist.github.com/marvincolgin/b348800b942d4d56e51e173b099b1e49#file-knock-screening-fullstack-md) implementation.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Tests

## Database

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```
## Postman
The provided postman collection to make calls to the messaging API. Feel free to let loose and have some fun sending messages! 

# Architectural Considerations & Design Decisions
## Database
### Why MongoDB instead of DynamoDB, Sqlite, MySQL, Redis etc? 
##### Here it is really a matter of taste. I wanted persistence that would be quick to integrate with and was decoupled from the API application. Since I already had a MongoDB cluster setup; that fit the bill.

## Framework 
### Why Flask instead of FastAPI, Django etc?
##### I chose Flask because I have used it before for simple API applications. With that said, I think that FastAPI is the preferred choice here. It is more performant than Flask. It also provides DI, data validation and documentation generation (SwaggerUI and ReDoc) out of the box. All of which Flask is lacking. If I were to continue this messaging project, I would quickly replace Flask with FastAPI. However, I was able to make use of some of Flask's features. Like serialization and modularity using Blueprints. I guess it is also worth noting that Django could handle all of my needs here, but I was preferential to a micro-framework instead.

## Configuration
### What is going on with configuration?
##### I chose to hard code configuration and secrets as setting up a Secrets Manager (AWS) or Key Vault (Azure) and including a robust configuration module at this stage of the "project" is not a good use of time and resources.

## Error Handling Concept
### What is the current state of error handling?
##### TODO: Fill out

## Logging
### What is logged and when? 
##### TODO: Consider anonymization of logs

## Pipeline (CI/CD)
##### To be added (due by 01.01.2050)