Instructions

Stop all your containers.

Now you have containers and some images that are no longer in use and are taking up space. Running docker ps -a and docker image ls will confirm this.

Clean the Docker daemon by removing all images and containers.

As an answer:
i) Give the commands you used to remove the images and containers.
ii) Give the output for docker ps -a and docker image ls.

jawaban aku :

i)
docker ps -a
docker rm b39 871 4ea
docker rmi httpd nginx redis

ii)
docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS     NAMES
b3905cbc2173   httpd     "httpd-foreground"       23 minutes ago   Exited (0) 3 minutes ago              interesting_sinoussi
8714ca7a77d4   redis     "docker-entrypoint.s…"   26 minutes ago   Exited (0) 20 minutes ago             lucid_einstein
4eabd55ff43f   nginx     "/docker-entrypoint.…"   26 minutes ago   Exited (0) 20 minutes ago             silly_hermann

docker images 
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
httpd:latest   96b1e8f69ee3        177MB         47.6MB
nginx:latest   0236ee02dcbc        240MB         65.8MB
redis:latest   5cb00b0f236e        204MB         55.3MB
