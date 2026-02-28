Instructions
Since we already did "Hello, World!" in the material let's do something else.

Start 3 containers from an image that does not automatically exit (such as nginx) in detached mode.

Stop two of the containers and leave one container running.

As an answer:

i) Write the commands you used to start and stop the containers.
ii) Write the output for docker ps -a which shows 2 stopped containers and one running.

i)
docker run -d nginx
docker run -d redis
docker run -d httpd

docker stop 871
docker stop 4ea

ii)
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                      PORTS     NAMES
b3905cbc2173   httpd     "httpd-foreground"       2 minutes ago   Up 2 minutes                80/tcp    interesting_sinoussi
8714ca7a77d4   redis     "docker-entrypoint.s…"   5 minutes ago   Exited (0) 16 seconds ago             lucid_einstein
4eabd55ff43f   nginx     "/docker-entrypoint.…"   6 minutes ago   Exited (0) 8 seconds ago              silly_hermann
