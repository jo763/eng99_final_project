# MVC | Model View Controller

Model-view-controller (Usually known as MVC) is a software design pattern commonly used for developed user interfaces that divides the related program logic into three interconnected element.

Popular programming languages like JavaScript, Python, Ruby, PHP, Java, C#, and Swift have MVC frameworks that are used for web or mobile application development straight out of the box.

## Flask

In my case I used the **Flask Micro web framework** to create a web app with Python. It is categorised as a micro-framework as it does not require particular tools or libraries to function. Although categorised as `micro` it has just as much functionality and power as any other MVC framework.

Applications that use the Flask framework include **Pinterest** and **LinkedIn**.

The power of flask comes with its wide array of third-party extensions which provide common functionalities, such as form validation, database abstraction and templating. These extensions add application features as if they were already a part of flask itself, and are updated more frequently than the core flask program.

### Model 1

>The central component of the pattern. It is the applications dynamic data structure, independent of the user interface. It directly manages the data, logic and rules of the application.

>The model is responsible for managing the data of the application. It receives user input from the controller. 

### View 2

>Any representation of information such as a chart, diagram or table. Multiple views of the same information are possible, such as a bar chart for management and a tabular view for accountants.

>The view means presentation of the model in a particular format.

### Controller 3

>Accepts input and converts it to commands for the model or view.

>The controller responds to the user input and performs interactions on the data model objects. The controller receives the input, optionally validates it and then passes the input to the model.


_In addition to dividing the application into these components, the model–view–controller design defines the interactions between them._




# The App

The Program Created has three main pages.

1. The Home Page
2. The Team Page
3. The Top30 Page

_**This is how the file structure should look. All inside a main folder called Flask**_
```
├── app.py
├── static
└── templates
```

 A **static** folder to store stylesheets, javascript files and images. 
 
 A **templates** folder to store our visual representation such as template _HTML_ files.
 
 Finally an **app.py** file which will function as the controller with Flask framework. The app will utilize the **Mode-View-Controller** design pattern in the back-end to handle requests and dish out responses to the end user. This controller will handle our apps business logic and further decide how to handle it.
 
 With this set up I can scale up the app with more resources and pages as there is already a logical separation between the front and back-end.
 
 The default port of Flask is **5000**.

```python
from flask import Flask, render_template, redirect, url_for, request, session, flash, g

import csv

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("new_homepage.html")

if __name__ == '__main__':
    app.run(debug=True)
```

* This is a base setup for the app.py file, it imports the flask framework.
* Create an application object with the app using `app = Flask(__name__)`
* Uses the `@app.route` decorator to link the function to a url in this case `/` which is the first page you see on the page. Essentially to map the movement around the site.
* The last part uses the run method to run the app object we created at the start, its that simple!

**Important** - Make sure you have Flask installed

```python
pip3 install Flask
```

When I run this on my local machine I can view it in the local browser at [https://localhost:5000/](http://127.0.0.1:5000/).

Also make sure if you want to view the HTML in the browser and make changes whilst its still visible, you need to set the environment to production to enable debugging mode.

```bash
# Change variable to development
# Windows
set FLASK_ENV=development

# Mac
export FLASK_ENV=development

# Whilst inside the flask folder run the app
Flask run
```

## Template Inheritance

A very powerful aspect of Flask is its extension with **Jinja**; a web template engine. One of the most powerful parts of this engine is **Template inheritance**, this allows you to build a base "skeleton" template that contains all the common elements of your site and define blocks that child templates can override.

This is extremely useful as you do not need to create a brand new HTML page for every template, instead you can inherit the entire base page and then override parts that need to be different on this page. A good example of this would be a navigation bar, instead of constantly writing it out, you could inherit it in every page.

_Example of Inheritance_

```html
{% extends "master.html" %}

{% block CSS %}
    <link href="CustomCSSPage" rel="stylesheet">
{% endblock %}


{% block title %}
<title>Sparta Global | Custom Title</title>
{% endblock %}

{% block content %}

<p> Custom Body </p>

{% endblock %}

{% footer content %}

<footer>
Custom Footer
</footer>

{% endfooter %}
```