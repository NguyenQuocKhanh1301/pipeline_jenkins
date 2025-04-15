from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>I Love You</title>
        <style>
            h1 {
                color: red;
            }
        </style>
    </head>
    <body>
        <h1>i love you</h1>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
