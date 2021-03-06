# docker-kafka

### Download docker

``curl -fsSL https://get.docker.com | bash``

``docker --version``

### Init service docker
``sudo service docker start``

### Create the docker group
``sudo groupadd docker``

### Add your user to the docker group
``sudo usermod -aG docker $USER``

### Logout and login again
``newgrp docker``

### Download docker-compose
https://docs.docker.com/compose/install/


1- Run this command to download the current stable release of Docker Compose:

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

2 - Apply executable permissions to the binary:

``sudo chmod +x /usr/local/bin/docker-compose``

3 - create a symbolic link to /usr/bin

``sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose``

4 - Test the installation.

``$ docker-compose --version``


### Execute container
``docker-compose up``

### Installing dependencies
``pip install -r requirements.txt`` 

### Execute producer  kafka
``python example.producer.purchases``

### Execute the consumer kafka
``python example.consumer.purchases``

