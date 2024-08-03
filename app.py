# First we have to build a new folder as "weather_app" inside the "WORKSPACE", never inside the ".vscode"
# inside this folder create new folder as "templates"
# Inside the templates create "index.html", Inside the "weather_app" create "app.py"
# "app.py" is the python file where we write the code
# The indentation should be maintained, otherwise it would create the issues
# The system as local remains blank,
# when i go for deployment,I will keep all the dependencies and all the libraries in the "requirements.txt" file, 
# "html" is kind of EY File,created inside the "weather_app", This is the basic folder structure/scleton
# when my code will be creasing, my folder structure will increase going forward
# from outside the main directory when we want to go to it, we just have to print "clear"
# Then print the "ls", check the directory path, we should stay inside the main directory as "weather_app" directory
# by using "cd weather_app/", we can change the directory, then we are inside the "weather_app"
# where we are getting the "app.py  requirements.txt  templates"
# "abc@993940e75d5a:~/workspace/weather_app$" m,eans we are inside the project directory of "weather_app"
# We can get the result of the html page, by download it and open by google browser
# if any library is not even installed, then we have to install it to the Terminal portion
# by as  "pip install requests"
# we can execute the code by click the Right hand side "Run or Debug" section, then Run Python File
# when only execute with "@app.route('/')", then getting the form as result
# If we are going to press the search button, then we will get the "weatherapp" ulr
# as "https://mango-receptionist-oqkee.pwskills.app:5002/weatherapp", this is api
# but we don't have anything in this route, if we dont have anything in this route,so can't execute

from flask import Flask , render_template, request
import requests 


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route("/weatherapp",methods = ['POST' , "GET"]) # By this route, we bind the function
 # when we work with url and body both then, should mention "['POST' , "GET"]", though "post" method is always more secure
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"

    param = {
        'q':request.form.get("city"),
        'appid':request.form.get('appid'),
        'units':request.form.get('units')
        }
    response = requests.get(url,params=param)
    data = response.json()
    return f"data : {data}"










if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5002)


# In our lap each and every thing is preinstalled
# so, when we going to deploy to cloud
# cloud is completely blank system, we have to install the library over there
# cloud is gives a system, On the other hand Project to project our library are differents
# here as we have to install flask , request over here
# unless we not going to install everything, the system is not going to work
# "requirements.txt" is being used to keep all the dependency, whatever we would like to install
# For the local system, we can ready our system in one short during the bulk installation
# "gunicorn==20.0.4" is needed to deploy inside cloud
# we should not over burden our cloud environment
# we should always take the latest version from the pip repositery
# we can know which library have to ltake from the first lines of rhe code
# we can search the version as "flask pip", the recent version is "Flask 3.0.3"
# we have to write as "Flask==3.0.3", we can write as only "Flask" also
# Itv would be always take "pip install Flask"
# Then I have to push my code to git and from git push to the cloud
# # First we have to build the repositary inside the github (git_2:30)
#  This is the entire code, whatever inside the directory, i have to push those things 
# After clearing the terminal when i print"ls", then getting as 
# "app.py  requirements.txt  templates"
# The folder structure would be "abc@c834d2d9ce49:~/workspace/weather_app$"