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
        <div class="text">MLOPs</div>
    </body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return html_content
