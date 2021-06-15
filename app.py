from flask import Flask, request
app = Flask(__name__)

value = "1";

@app.route('/')
def home_route():
    return """
        <body>
            <script>
                async function change(){ 
                    await fetch(
                        'http://localhost/change',
                        { 
                            method: 'POST', 
                            body: Math.random()
                        }
                    ); 
                    location.reload()
                }
            </script>
            <b>""" + str(value) + """</b>
            <button onClick='change()'>change</button>
        </body>
        """

@app.route('/change', methods = ["POST"])
def change_route():
    global value
    value = request.data
    print(value)
    return value