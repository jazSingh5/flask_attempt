from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
  
    name = "Jaskaran"
    return '''
    <html>
    <body>
        <h1>Hello, '''  + name +'''!</h1>
        <p> <a href = "https://www.google.com" >not google</a> </p>
        <p> <ul>  <li> Paris </li> <li> London </li> <li> Rome </li> <li> Tahiti </li> </ul> </p>
                
    </body>
    </html>'''
    
    
   
if __name__ == '__main__':
    app.run()
