from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
    city_names = ["Paris","London","Rome", "Tahiti"]
    name = "Jaskaran"
    return '''
    <html>
    <body>
        <h1>Hello, '''  + name +'''</h1>
        <p> <a href = "https://www.google.com" >not google</a> </p>
        
       <ul>
{% for things in '''city_names''' %}
  <li>{{ things}}</li>
{% endfor %}
</ul>
                
    </body>
    </html>'''
    
    
   
if __name__ == '__main__
