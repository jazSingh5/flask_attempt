from flask import Flask
app = Flask(__name__)

city_names = ["Paris","London","Rome", "Tahiti"]
name = "Jaskaran"

@app.route('/')
def home():
    
    return '''
    <html>
    <body>
        <h1>Hello, '''  + name +'''</h1>
        <p> <a href = "www.google.com" >not google</a> </p>
        
    <ul>  <li> ''' + (city_names[0]) + ''' </li> 
    <li> ''' + (city_names[1]) + '''</li>
    <li> ''' + (city_names[2]) + '''</li>
     <li> ''' + (city_names[3]) + '''</li> </ul> 
                
    </body>
    </html>'''
    
    
   
