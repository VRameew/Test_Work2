# Test_Work2
## This is API APP.

For start app need install Docker, Python > 3.9.
## Deploying APP
After cloning repository, go in it.

`cd c:\\code_directory\`

`cd /code_directory/`

Use **Docker-Compose** for creating *container*.

`docker-compose build`

After building container, will start it.

`docker-compose up`

# EXAMPLE
For requesting data, use POST request in
`{host}/users?{params}` example `http://localhost:8000/users?name=Vlad`

Request response looks like `[8,"ede4481b-3768-435b-b169-dcf3f5a5c774"]`
