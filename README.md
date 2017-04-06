# election-nepal
  Election Nepal is the project of  [Open Knowledge Nepal](https://np.okfn.org/). It  is a crowdsourced open portal that brings all kind of Data related to Nepal's Local Election together in Open and Visual Format. 
  
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
- Install the requirements using [pip](https://pip.pypa.io/en/stable/)
```
pip install -r requirements.txt
```
- Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

- Run the server
```
python manage.py runserver
```

# Contributing
 Election Nepal is an open source project. Repositories are hosted on  GitHub, so contributing is  easy and anyone can get involve.
 
  
Code Behind http://electionnepal.org

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
