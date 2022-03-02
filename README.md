# Swiggy clone
## A food ordering app clone using Python/Django on the backend, Vuejs on the frontend and PostgresQL for the database

## Stack Used
-Python
-Django
-Vuejs
-Postgres

## Setup
You will need to install Python, Django, Vuejs, VueCLI and Postgres on your local computer. The links below will bring you to the respective site to help you get started with the installation. You can use npm or yarn depending on your preference. Please select the installation options that are best suited for your local computer.

### Installation links
-[Node](https://nodejs.org/en/download/) This is if you want to use NPM. You will need to download Nodejs first
-[NPM](https://docs.npmjs.com/cli/v8/commands/npm-install)
-[Yarn](https://classic.yarnpkg.com/lang/en/docs/cli/install/)
-[Python](https://www.python.org/downloads/)
-[Django](https://docs.djangoproject.com/en/4.0/topics/install/)
-[Vue](https://vuejs.org/guide/quick-start.html) This is for version 3
-[Vue CLI](https://cli.vuejs.org/guide/installation.html)
-[Postgres](https://www.postgresql.org/download/)
-[Visual Studio](https://visualstudio.microsoft.com/downloads/)
-[PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html)

### Folder structure
This is a folder structure of how I have put this project together. This is subject to change and you can make it how you see fit depending on modifications or alterations you want to have beyond what I have done.

|--swiggy
  |--server
    |--apps
      |--discount
      |--menu
      |--restaurants
      |--userinfo
      |--utils
      __init__.py
    |--config
      .env
      __init__.py
      asgi.py
      settings.py
      urls.py
      wsgi.py
    |--venv
    .gitignore
    main.py
    manage.py
  |--client
    |--node_modules
    |--public
    |--src
    .gitignore
    babel.config.js
    package.json
    yarn.lock
    
### gitignore files
An easy way to get the needed info within the gitignore files is to use the website [Toptal](https://www.toptal.com/developers/gitignore). All you need to do is type in the stack that you are using and it will have all the files that need to be hidden. You can copy and paste it to your gitignore files as needed.

### Github initialization
When starting the project you and make the folders swiggy as the root then client and server as the subdirectories. We will get to the installation needed for the subdirectories. For the time being, go to the parent directory of swiggy and use your CLI to type in the following:

```
git init
git branch -M main
git add .
git commit -m 'Type your message here'
git remote add origin <your github repo url>
git push -u origin main
```

If you have something like zsh installed then you can look up the shortened git commands [here](https://kapeli.com/cheat_sheets/Oh-My-Zsh_Git.docset/Contents/Resources/Documents/index)

## Backend Setup
This project is being done with PyCharm as the IDE, but you are welcome to use whatever IDE or text editor you are comfortable with. 

### Make a virtual environment
Use this script to create a virtual environment. The virtual environment is used to store all the dependencies needed for the project to work.

```
python3 -m venv venv
```

### Go inside the virtual environment
Using the terminal/CLI I will open one window up specifically to write scripts or commands. There will be other windows opened for other purposes. In this terminal type the following command to enter the virtual environment. Make sure that you are in the server folder. This will be helpful when downloading any dependencies. It will be here.

```
source venv/bin/activate
```

### Start the project
In the root folder type this in the command prompt:

```
django-admin startproject config .
```

### Create env file
Go to the config folder and create an .env file that will hold the secret variables

```
touch .env
```

Open the env file and type the needed variables required for the database and key. I am using Postgres so that will be what is used in my codebase. However, this will change for another database type or other secret variables needed.

```
ENGINE=django.db.backends.postgresql_psycopg2
NAME=database_name
USER=database_user
PASSWORD=database_password
HOST=localhost or database_host
PORT=5432
SECRET_KEY=joi309g#j809ub0a9
```

### Installation of initial dependencies
You will need to use pip to download some dependencies to begin with. They are for the database and to have access to the env file. The environ package is for the env file and psycogq2 is for the postgres database. The djangorestframework is the dependency using django for rest activities. The cors headers dependency helps with allow the client and api talk to each other without problem.

```
pip install django-environ
pip install psycopg2
pip install djangorestframework
pip install django-cors-headers
```

### Settings file configuration
The settings file helps govern how the backend behaves. There are some parts of this file we will configure to begin with while subsequent editting will be needed as you continue on with the development of the backend.

#### Add imports
Since we have already downloaded the environ dependency then we will need to include this at the top of the file. You can type in the following:

```
import environ
```

#### Installed Apps
Any time you add a dependency or an internal app then you will need to include it to the list of installed apps. You can scroll down to find this. When you find it then add the dependencies that we have already downloaded. The rest of the inclusion to this list will happen in the flow of making apps.

```
INSTALLED_APPS = [
    ...
    'environ',
    'rest_framework',
    'corsheaders',
    ...
]
```

#### Configure rest framework
This configuration has to do with the permissions allowed by the users that are using this app. There are different settings on the scope and type of permissions that Django has available. The list of permissions available are [here](https://www.django-rest-framework.org/api-guide/permissions/).  This also affect the type of exceptions we can make for the project. This will be helpful when we configure the 404 and other error handling which may occur. We will cover this part more when we get to that point.

```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'EXCEPTION_HANDLER': 'apps.utils.custom_exception_handler.custom_exception_handler'
}
```

#### Configure environ
Within the file you will see an area where there is a SECRET_KEY variable. Initially it is showing the value of this variable which is not ideal. Instead we will be using the SECRET_KEY variable we made in the env file. In order to do that enter the following text:

```
env = environ.Env()
environ.Env.read_env()
```

This will allow you to now use this dependency within the settings file to refer any variables you want to source from the env file. When accessing a variable from the env file then you can just use the following usage:

```
SECRET_KEY = env('SECRET_KEY')
```

#### Configure Cors
Next is the configuration of cors for this project. You can copy and paste the following and include it in the settings file

```CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ORIGIN_ALLOW_ALL = True
```

#### Configure Middleware
The middleware is what gets triggers on a client request before and post, get, put, etc is done. Copy and paste this text for the needed middlware:

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

#### Configure database
We will be using Postgres for the database in this project. In order to configure it then you will need to have this text in your settings file. These variables are coming from the env file. Use the env file to edit or create any variables used in this portion.

```
DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'NAME': env('NAME'),
        'USER': env('USER'),
        'PASSWORD': env('PASSWORD'),
        'HOST': env('HOST'),
        'PORT': env('PORT'),
    }
}
```

further configuration will be done via the terminal. Open a new window and type <code>psql</code> to open the Postgres program. You will beed to create a new database by using the following:

```
CREATE DATABASE swiggy;
CREATE USER database_user WITH ENCRYPTED PASSWORD 'database_password';
GRANT ALL PRIVILEGES ON DATABASE blogs TO database_user;
```

The user and password will be specific to you what you have used to install Postgres. After creating the database you can use the command <code>\c swiggy</code> to navigate to the database. It will be empty now but if you wanted to see if there are any tables in the database then you can use the command <code>\d</code> to check that.

### Exception and Error handling configuration
Open the urls.py file located in the config folder. This will be the main routing for the app. This will route the user to the appropriate urls.py in the subsequent app. We will get to this when we go through the flow of the project. For now we will take care of the configuration of the exception and error handling. Below the urlspatterns array type the following.

```
def response404(request, status=200, message='Not Found'):
    response_object = {
        'timestamp': datetime.now(),
        'status': 'Data unavailable',
        'status_code': 404,
        'message': message,
        'data': []
    }
    return JsonResponse(data=response_object, status=status)


def response500(request, status=500, message='Not Found'):
    response_object = {
        'timestamp': datetime.now(),
        'status': 'Error',
        'status_code': status,
        'message': message,
        'data': []
    }
    return JsonResponse(data=response_object, status=status)


handler404 = response404
handler500 = response500
```

This will allow you to send back JSON payload when there is an error. I have made a response object that acts as a singular payload that the user would get when reading it from the client.

In addition to this to handle exceptions, there will be one more area to add some configuration. Make a folder in the apps folder called utils. Inside this folder make a python file which will be the custom exception handler. Inside the file you can include this:

```
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    response_object = {
        'timestamp': '',
        'status': '',
        'status_code': '',
        'message': '',
        'data': []
    }

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['timestamp'] = datetime.datetime.now()
        response.data['status'] = "Error"
        response.data['message'] = response.data['detail'],
        response.data['status_code'] = response.status_code
        response.data['data'] = []
        print(response.data['detail'])
    return response
```

Again I am using a standard response object so that each response to the client will be uniform. This will help on that side when using Typescript.

#### Admin configuration
In order to use the Django admin portal then you will need to have a way to access it. You will need to create a superuser to login. To do this, type this command in the terminal and answer the questions to make a username and password. This will be your credentials when logging in later on.

```
python3 manage.py create superuser
```

### Process Flow for Apps
This is the general process when you make each app. We will cover the restaurants app, but this is a repeatable process for you to follow on each app.

#### App creation
When you want to create a new app then you will need to do two things. The first thing to do is open the terminal window for any usage and navigate to the apps folder. Inside the apps folder you will create a new folder that will be the name of the app. This is needed first before any other CLI commands. After you make that folder then navigate inside the folder and create a __init__.py file. Then go back to your terminal and navigate back to the root folder or the server folder in this case. You will then type the following command to populate the folder you just created with the necessary files.

```
python manage.py startapp <appname> apps/<appname>
```

Insert the app name where I have put the brackets. This will populate the folder. Two more things you will need to do before moving to the next step. It includes navigating back to this app folder and creating two files. The first file will be for the urls of that app and the other will be a serializer file which we will cover later.

#### Configure apps file 
Go to the apps folder and open the apps.py file. Since we are using the apps folder and creating subfolders to hold all of our apps then we need to reconfigure the route in this file. Change the name to include and apps before the name of the app. Please see below:

```
name = 'apps.discount'
``` 

#### Configure main urls
Go to the urls.py file in the config folder. This holds the main urls and routing for the backend. You will need to include one path for the newly created app that you have just created. The urls for the respective app will be within the urls.py file within the app folder. Do include the new path type the following:

```
path('api/v1/<appname>/', include('apps.<appname>.urls'))
```

Insert your app name where there is the appname shown.
  
#### Model Configuration
The model will be the file that connects the backend to the database. Depending on the database you are using, the syntax might alter slightly. I am using Postgres so the syntax I will show is based on that.
  
Firstly, make a new class which has the name of the app. Normal convention is to capitalize the first letter of the app. Inside this class you will include all the fields you want to include in the table. This could be as simple or complex as the project dictates. If you want to link tables together then you will need to employ foreign keys or relationships. This will have an impact if you migrate your model throughout the project so take that into consideration. At the end of the class you will need to add a constructor and another class (Meta) to tell what you want to see if you query this table in the database using Django. Here is an example of the parts:
  
```
class Restaurant(models.Model):
    restaurant_id = models.UUIDField(null=False, blank=False, primary_key=True, default=uuid.uuid4, unique=True)
    restaurant_name = models.CharField(null=False, max_length=50, default="Food Stuff")

    def __str__(self):
        return self.restaurant_name

    class Meta:
        ordering = ['restaurant_name']
```
  
You can go more indepth for how each aspect of the model works and the attributes, etc can accomplish. 
  
#### Migrations configuration
If you want to migrate the model after it is made or after all the models are made is up to you. Again this has impacts on how the database will perform and if you end up inserting data into the database as you go along and have relationships between tables. In any case, you will need to use to commands to do the migration:
  
```
python manage.py makemigrations
python manage.py migrate
```
  
After this is done successfully then a new folder called migrations will show in your app folder. This will show all the migrations you do.
  
#### Admin configuration
Django has an admin portal that makes life a little easier. In order to see what is in the model then you will need to include this model in the admin file. Open the admin.py file within your app folder. Type the following:
  
```
@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('restaurant_id', 'restaurant_name')

```
  
The list display tuple will let you list which fields you want to see when accessing the Django admin portal. In there you can do all the CRUD functions for that table and it will work with the database.

#### Serializer Configuration
Go to the serializer file in your app folder. This file will be empty. You can be as complex as you want to be for your usage, but for this project we will keep it simple. In order for it to work we will type this in:

```
class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
```

#### Views Configuration
The views file works as a controller in the traditional MVC format. This is where you will create the logic for each url path. You can use decorators and then make the function which will be used in the urls file. The api view will tell which http activity will happen. The function will end with a Response which will be sent back to the client on the frontend. I have made a standard response object which makes life easier on the frontend especially when using Typescript. Here is an example of a route:

```
@api_view(['GET'])
def getRestaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message="Returning all restaurants",
        data=serializer.data
    )
    return Response(response_object)
```

#### Urls Configuration
The urls file connects to the main urls file in the config folder. The url file in your app folder will give more routing info for Django to use in order to get the correct path. The paths are based on the views that you have created. Here is an example of a url array and path:

```
app_name = "restaurants"

urlpatterns = [
    path("routes/", views.getRoutes, name="routes"),
    path("<uuid:pk>/", views.getRestaurant, name="restaurant"),
    path("", views.getRestaurants, name="restaurants"),
]
```



