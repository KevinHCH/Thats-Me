# That's me App
> This web application let the user create and manage their content, the objetive of this application is show their work (images)

### Requirements
- Docker >= 19.03
- Python3
- PIP
### Stack 
- Python3
- PostgresQL
- Flask
- Docker
### Deploy
- Create the docker volume: `docker volume create psql`
- Build the docker image: `docker build -t psql-img -f .`
- Install requirements `pip install -r requirements.txt`
- Complete the `.env` file like the `.env.example`
- Init the database: `docker run --name psql -p 5432:5432 -v psql:/var/lib/postgresql psql-img`
- Complete the `SECRET` var running the `/app/bin/generate_secret.py`
- Run the server on local using the `dev.sh` file: `bash /app/bin/dev.sh`
