# election-nepal
  Election Nepal is the project of  [Open Knowledge Nepal](https://np.okfn.org/). It  is a crowdsourced open portal that brings all kind of Data related to Nepal's Local Election together in Open and Visual Format. 

Code Behind http://electionnepal.org
  
# Status
In progress not completed. 

# Local Development
- Clone the repo
```
git clone https://github.com/okfnepal/election-nepal
```

- Create a virtualenv
```
virtualenv venv
```
- Activate the virtualenv
```
source venv/bin/activate
```
- Install prerequisites
```
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```

- Install the requirements using [pip](https://pip.pypa.io/en/stable/)
```
pip install -r requirements.txt
```
- Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
- Database fixture to load sample data 
```
python manage.py loaddata  election-nepal-fixture.json 
```

- Run the server
```
python manage.py runserver
```

- In a web browser, go to [localhost:8000](http://localhost:8000/), and you should see the development site! Please note that the terminal window you are running the development site in must stay open while you are using the site.

- When daily development is complete, terminate the local web server by typing ```CONTROL + C```. Also deactivate the virtual environment:
```shell
deactivate
```

# Contributing
 Election Nepal is an open source project. Repositories are hosted on  GitHub, so contributing is  easy and anyone can get involved.

You can browse the [issues](https://github.com/okfnepal/election-nepal/issues) to see where you can contribute. Issues tagged with `help wanted` are specifically open for contributions from community.
# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
