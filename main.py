import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Manga
from schema import Manga as MangaSchema

import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URI'])

@app.get('/')
def index():
    return {'message': 'Hello World'}

@app.get('/mangas')
async def get_mangas():
    mangas = db.session.query(Manga).all()
    return mangas

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)


