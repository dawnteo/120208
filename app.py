#!/usr/bin/env python
# coding: utf-8

# In[26]:


from flask import Flask 
#Flask is a lightweight WSGI web application framework.


# In[27]:


app = Flask(__name__)
#will have app.route when run dir(app)


# In[28]:


from flask import request, render_template
import joblib 
#use Flask’s render_template() helper function to serve an HTML template as the response

@app.route("/",methods=["GET","POST"]) #methods - 2 methods; more than 1 method 
#App Routing means mapping the URLs to a specific function that will handle the logic for that URL
#In our application, the URL (“/”) is associated with the root URL.
#So if our site’s domain was www.example.org and we want to add routing to “www.example.org/hello”, 
#we would use “/hello”.

def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBS")
        pred = model.predict([[float(rates)]]) #change to float datatype
        print(pred)
        s = "The predicted DBS share price is " + str(pred[0][0]) # remove [] from [[19.38726492]]
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="2"))

#get - get HTML from front end (VScode) to back end
#post - can post from back end to front end (DBS share price)


# In[ ]:


if __name__ == "__main__":
    #to authenticate this program is mine. when on cloud/Heroku if never define wont be able to output 
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




