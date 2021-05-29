#!/bin/bash

echo "================================================================================"
echo "Tellico Synchonized"
echo "================================================================================"

#Se comprueban los privilegios
if [ "$(id -u)" -ne 0 ];then
echo "Este script debe ejecutarse con privilegios root" >&2
exit 1
else

sudo apt-get  update -y && apt-get  upgrade -y
sudo apt-get  install  python3 -y
sudo apt-get  install  python3-pip -y
sudo apt-get  install  python3-pyqt5 -y
sudo apt-get  install  pyqt5-dev-tools -y
sudo apt-get  install  qttools5-dev-tools -y
sudo  pip3  install  python-crontab

chmod +x Tellico.sh
fi
