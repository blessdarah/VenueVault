# Venue Vault
This is an application that is out to solve a 


## Project setup
1. clone the repository to your local setup
2. ```bash 
cd VenueVault
```
3. Source the virtual environment `source venv/bin/activate`
4. Copy the env.example file to .env by running `mv .env.example .env`
5. Edit the .env file by adding the values valid for your PostreSQL database. If you don't postres, you need to download it.
6. Install all dependencies `pip install -r requirements.txt`
7. Run migrations 
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
8. Create a superuser using `python3 manage.py createsuperuser`
9. Run the application using `python3 manage.py runserver`
10. Now visit http://localhost:8000 to see the application running.
11. Login using http://localhost:8000/admin
