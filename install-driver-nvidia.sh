sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update -y
sudo apt install ubuntu-drivers-common -y

# sudo apt install nvidia-driver-<version> -y
# sudo apt install nvidia-driver-560 -y

sudo reboot

####################
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update -y
sudo apt-get install -y nvidia-container-toolkit -y
