apt update
apt innstall wget
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt update
apt-cache policy docker-ce
read -p "Enter "
sudo apt install docker-ce
sudo systemctl status docker
read -p "enter"

ngrok config add-authtoken 2VaL3LAsgw2R7Hl46qj2TbJ5fCr_2NsVnR9cxV9SQRk6dm6hR
