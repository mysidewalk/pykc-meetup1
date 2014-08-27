**Deployment Setup**
1. Install Vagrant: http://www.vagrantup.com/download-archive/v1.5.4.html
3. Install VirtualBox: https://www.virtualbox.org/wiki/Downloads
4. Install git and clone the repository
5. From the COMMAND LINE in the directory you just downloaded, type:
  vagrant plugin install vagrant-vbguest
  vagrant up
6. To create a super user:
  vagrant ssh
  cd /vagrant/demo
  python manage.py createsuperuser
After it finishes, you should now be able to see the site by browsing to http://localhost:8080
