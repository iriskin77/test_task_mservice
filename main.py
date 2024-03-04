from fastapi import FastAPI
from routes import routes
import uvicorn

app = FastAPI()


app.include_router(routes)



if __name__ == '__main__':
    uvicorn.run(app, port=8090, host="0.0.0.0")
