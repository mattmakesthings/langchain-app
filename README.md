# langchain-app

setup:
- rename '.env.example' -> '.env'
- place your OpenApiKey in the .env file

to run:
`flask --app main run`

Docker commands:

``` bash
docker build -t langchain_app . 
docker run -p 3000:3000 langchain_app 
```
