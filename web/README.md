# Web

## Setup on raspberry pi
1. Install maria db
`sudo apt install mariadb-server`
2. install pip and install the dependencies in requirements.txt
`pip3 install -r requirements.txt`
3. run sql/install.sql using mysql
`sudo mysql -e "source sql/install.sql"`
