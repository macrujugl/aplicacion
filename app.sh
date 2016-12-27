#!/bin/bash
LOG=/root/base-provision.log
exec > $LOG
exec 2>&1

echo "---CUSTOM empieza---"
export DEBIAN_FRONTEND=noninteractive
apt-get -y update
apt-get install -y lsscsi
apt-get install -y python-pytest python-pip python-dev nginx

echo "---CUSTOM pip y virtualenv---"
pip install virtualenv
export APP_DIR=/home/mario/aplicacion
mkdir -p $APP_DIR
cd $APP_DIR
virtualenv entorno
source entorno/bin/activate

pip install uwsgi flask

echo "---Clonando app---"
git clone https://github.com/macrujugl/aplicacion
mv ./aplicacion/* .
rmdir ./aplicacion
chown -R mario:www-data *

echo "---Arrancando servicios---"
cp aplicacion.service /etc/systemd/system
systemctl start aplicacion
systemctl enable aplicacion

cp aplicacion_web /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/aplicacion_web /etc/nginx/sites-enabled
rm /etc/nginx/sites-enabled/default

systemctl restart nginx

echo "---CUSTOM termina---"
exit 0