# from typing import Optional

# from fastapi import FastAPI

# import uvicorn

# app = FastAPI()

# @app.get("/")

# def read_root():
#     return {"hello" :"world and my love"}

# @app.get("/items/{item_id}")

# def read_item(item_id: int, q : Optional[str] = None):
#     return {"item_id" : item_id, "q" : q   }

# if __name__ == '__main__' :
#     uvicorn.run(app)


from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
    <head>
        <title>MLOPs Demo</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #f0f0f0;
            }
            .text {
                font-size: 72px;
                color: red;
                font-family: Arial, sans-serif;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="text">Tooi yeu cac ban</div>
    </body>
</html>
"""

<<<<<<< HEAD
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return html_content
=======
def read_root():
    return {"hello" :"world"}

@app.get("/items/{item_id}")

def read_item(item_id: int, q : Optional[str] = None):
    return {"item_id" : item_id, "q" : q   }

if __name__ == '__main__' :
    uvicorn.run(app,host="0.0.0.0", port=8000)
>>>>>>> 19afad4025f23dde878e32209952e9316c5d16aa
