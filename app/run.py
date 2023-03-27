from app import app , db 
from posts.blueprint import posts
import  routes


app.register_blueprint(posts, url_prefix='/blog') 
if __name__ =="__main__":
    app.run (debug = True)
    
SECRET_KEY = 'THIs12345678999'