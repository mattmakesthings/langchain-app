# langchain-app

setup:
- rename '.env.example' -> '.env'
- place your OpenApiKey in the .env file
  
## Local development
create project level virtual environment, activate, and install dependencies:

```bash
 python -m venv involv && \
 source ./involv/bin/activate &&\
 pip install -r requirements.txt
```

activate your venv then install packages
`pip install -r requirements.txt`

Run on local machine:
`flask --app main run`

Run in Docker:

``` bash
docker build -t langchain_app . # build
docker run -p 3000:3000 langchain_app # run
```

## Deployment via Serverless

Serverless [install instructions](https://www.serverless.com/framework/docs/getting-started/)

``` bash
serverless deploy
```