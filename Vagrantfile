# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version.
VAGRANTFILE_API_VERSION = "2"
Vagrant.require_version ">= 1.6.0"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.define "web", primary: true do |web|
        web.vm.box = "precise64"
        web.vm.box_url = "http://files.vagrantup.com/precise64.box"
        
        web.vm.provision :shell, :path => "config/development.sh"
        
        web.vm.synced_folder "config", "/vagrant/config"
        web.vm.synced_folder "demo", "/vagrant/demo"
        web.vm.synced_folder ".", "/vagrant", disabled: true
        
        # accessing "localhost:8080" will access port 80 on the guest machine.
        web.vm.network :forwarded_port, guest: 80, host: 8080
    end
end
