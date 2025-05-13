from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html_content = '''
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>I Love You</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #f0f0f0;
            }
            #text {
                font-size: 72px;
                color: red;
                font-family: Arial, sans-serif;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1 class = text >Thầy Tiến rất đẹp trai!</h1>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True,host = "0.0.0.0" ,port = 5006 )
