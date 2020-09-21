# Scraper

## Setting up the environm ent

#### Virtualenv
I use virtualenv but it is not strictly speaking necessary

```
virtualenv venv
source /venv/bin/activate
```
#### Aquire credentials
You need to create a twitter app
Credentials can be generated on the [Twitter App Dashboard](https://developer.twitter.com/en/portal/projects-and-apps)
Simply click the ```key``` icon next to the app name
There you will see ```API Key & Secret``` this will be your ```CONSUMER_KEY``` and ```CONSUMER_SECRET```
You will also see ```Access Token & Secret```, this will be your ```ACCESS_KEY``` and ```ACCESS_SECRET```
Just hit generate for both these and copy the values

#### Environment variables
```
"TWENDS_DATABASE": "mysql://user:password@host/dbname?charset=utf8",
"CONSUMER_KEY": "X",
"CONSUMER_SECRET": "Y",
"ACCESS_KEY": "U",
"ACCESS_SECRET": "W"
```

You can either export these manually each time (not reccomended) or add them to the activation script for the virtual environment (reccomended)
Simply edtit the file ```/venv/bin/activate``` and add 
```
"TWENDS_DATABASE": "mysql://user:password@host/dbname?charset=utf8",
"CONSUMER_KEY": "X",
"CONSUMER_SECRET": "Y",
"ACCESS_KEY": "U",
"ACCESS_SECRET": "W"
```
#### Python packages installation
```
pip3 install -r requirements.txt
or
pip install -r requirements.txt
```

#### Initializing the database
Just create a database called ```dbname``` as it appears in your ```TWENDS_DATABASE``` environment variable.
You must input some rows into the table ```location```. These will control what ```WOEID's``` will be queried later on.
```WOEID``` for ```Worldwide``` is 1, so it might be beneficial to run

```
insert into location (id, value) values(1, 'Worldwide');
```

Note that the ```id``` is NOT an ```autoincrementing``` value, this is the ```WOEID```

# Usage
```
python run.py --count=10
```

The default value for ```count``` is ```10```. This number controls how many hashtags will be saved per location

The program will save into ```MySQL``` into two tables, ```run``` and ```trend```

```run``` is simply bookkeeping, it has ```id```, ```location``` and ```time```, where ```location``` points to the location table.
Every entry in ```trend``` will have a pointer to ```run```, ```value``` like "#WearAMask" and an order number like ```1```, meaning that would be the no. 1 trending hashtag for that location.

