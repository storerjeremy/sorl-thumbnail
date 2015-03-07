# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.vm.hostname = "thumbnail"

  config.vm.provider "virtualbox" do |virtualbox|
    virtualbox.memory = 600
    virtualbox.cpus = 2
  end

  config.vm.define "web" do |web|
    web.vm.network :forwarded_port, guest: 80, host: 8000

    web.vm.provision "ansible" do |ansible|
      ansible.inventory_path = "provision/inventory/vagrant.inv"
      ansible.playbook = "provision/development.yml"
      ansible.verbose = "v"
    end
  end

end
