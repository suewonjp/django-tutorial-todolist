### :coffee: Motivation

This project is a simple tutorial web application managing personal todo list.

It's written on top of [Django framework](https://docs.djangoproject.com/) and it's main purpose is educating myself and other people who are not familiar with many things in Django. Notice that this project is far from an web application with some serious quality.

### :coffee: A Starting Point

This project is based on [this excellent tutorial video](https://www.youtube.com/watch?v=2yXfUPwlZTw&t=218s). (You can find the tutorial project associated with the video [here](https://github.com/bradtraversy/django-todolist))

### :coffee: Demonstrated Features

The original todo list application from the video was concise, but too simple, so I started to add a few extras to educate myself as follows:

- Support for Django 2.0
- Complete CRUD functions for models
- Adding another model called Category to demonstrate many-to-many relations among models
- Basic styling and frontend scripting
- Adding extra shell scripts to help minor issues
    - Making Django shell a little more convenient
    - Quickly adding test data to the DB 

### :coffee: How To Run It By Yourself

1. Install or set up prerequisites (Mentioning installation steps for these prerequisites is out of scope of this readme)  
    - Python 3 **(Notice that Python 2.7 won't work for Django 2.0)**
    - Django - [Refer to the official installation guide](https://docs.djangoproject.com/en/2.0/intro/install/)
    - Database backend software such as Sqlite3, or MySQL, etc.
        - This project uses Sqlite3, but also has been tested with MySQL.
1. Clone the project to your local system  
    - `git clone https://github.com/suewonjp/django-tutorial-todolist.git` 
    - `cd django-tutorial-todolist` 
1. Run the DB migrations  
    - `./manage.py migrate`
1. Add test data into the DB  
    - python [tools/populate-test-models.py](tools/populate-test-models.py)
1. Confirm it works  
    - `./manage.py runserver`
    - Access the application in your browser (The url is `localhost:8000` by default)


> **TIP**
>
> You can invoke Django shell by executing [tools/shell.sh](tools/shell.sh). The shell script will import model classess and others for you.  
> It's much more convenient rather than using `./manage.py shell`

### :coffee: Todo

- Adding unit test
- Demonstration of how to use Django's Form class when dealing with HTML forms

### :copyright: COPYRIGHT/LICENSE/DISCLAIMER

    Copyright (c) 2018 Suewon Bahng, suewonjp@gmail.com
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

### :busts_in_silhouette: CONTRIBUTORS
Suewon Bahng  

* * *
Updated by Suewon Bahng ( Jan 2018 )

