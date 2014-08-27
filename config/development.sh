#!/bin/bash

# update apt
apt-get update

# apache
apt-get install -y apache2 libapache2-mod-wsgi libapache2-mod-proxy-html
a2enmod proxy proxy_ajp proxy_http rewrite deflate headers proxy_balancer proxy_connect proxy_html

# python
apt-get install -y build-essential python python-dev

# get most up to date pip
apt-get install -y curl
curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python

# install pip requirements
pip install -r /vagrant/demo/requirements.pip

# create directories
if [ ! -d "/var/www/static" ]; then
  mkdir /var/www/static
  chown vagrant:vagrant /var/www/static
fi
if [ ! -d "/var/www/media" ]; then
  mkdir /var/www/media
  chown vagrant:vagrant /var/www/media
fi

#!/bin/bash
cp /vagrant/config/cherrypy-server.conf /etc/init/
cp -v /vagrant/config/apache.conf /etc/apache2/sites-enabled/000-default
/etc/init.d/apache2 restart

# Need to copy rest framework swagger assets to the static root
cp -r /usr/local/lib/python2.7/dist-packages/rest_framework_swagger/static/rest_framework_swagger/ /var/www/static/

chmod -R 777 /var/www/static
su - vagrant -c 'python /vagrant/demo/manage.py syncdb --noinput'
su - vagrant -c 'python /vagrant/demo/manage.py collectstatic --noinput'
