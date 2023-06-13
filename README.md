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

# №1

For requesting data, use POST request in
`{host}/users?{params}` example `http://localhost:8000/users?name=Vlad`

Request response looks like `[8,"ede4481b-3768-435b-b169-dcf3f5a5c774"]`

# №2

In params file `http://localhost:8000/records?user_id=1&token=a06dc828-c3d3-4066-b9d7-db198a7b62cd&data`
![image](https://github.com/VRameew/Test_Work2/assets/87801168/02499041-488d-4381-9499-27b6a1762956)


# №3

`http://localhost:8000/record?id=13&user=1`
![image](https://github.com/VRameew/Test_Work2/assets/87801168/6d4bca4f-50b0-47b2-a48a-16d50bde1669)
