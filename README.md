## How to get started with this project

### Clone the project

- Open the terminal and run the following command. 

```bash
git clone https://github.com/rohit-rajput1/django_app.git
``` 

---

### Create a virtual environment

- Create a virtual environment using the following command.

```bash
#virtualenv -p python3 <environment-name>
virtualenv -p python3 venv
```

- Activate the created environment.
```bash
#source <environment-name>/bin/activate
source venv/bin/activate
```

- Deactivating the environment.

```bash
deactivate
```

---

### Install the dependencies

- Install the dependencies using the following command.

```bash
pip install -r requirements.txt
```

---

### Run the project

- First migrate the database.

```bash
python manage.py migrate
```

- Run the server.

```bash
python manage.py runserver
```

---

### Now you are good to go.
