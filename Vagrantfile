# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/focal64"

  # Forwarding port for jupyter
  config.vm.network "forwarded_port", guest: 8888, host: 8888
  # Forwarding port for rasa visualisation
  config.vm.network "forwarded_port", guest: 5006, host: 5006
  
  # Configure virtual machine specs. No idea if these makes much sense.
  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "4096"
    # Customize the amount of cores:
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    
    echo "Running apt-get update"
    sudo apt-get update

    echo "Virtual Environment Setup"
    sudo apt-get install python3-dev python3-pip -y
    sudo apt-get install python3-venv -y
    python3 -m venv ./venv
    source ./venv/bin/activate

    echo "First make sure pip version is up to date"
    pip3 install -U pip

    echo "Installing Rasa Open Source"
    pip3 install rasa

    echo "Rasa installed:"
    rasa --version

    echo "Installing discord.py"
    pip3 install -U discord.py

    echo "Installing jupyterlab"
    pip3 install jupyterlab

    mkdir .jupyter
    chown vagrant .jupyter
    chown :vagrant .jupyter
    echo "c.NotebookApp.ip = '*'" >> .jupyter/jupyter_notebook_config.py
    echo "c.NotebookApp.open_browser = False" >> .jupyter/jupyter_notebook_config.py
    echo "c.NotebookApp.port = 8888" >> .jupyter/jupyter_notebook_config.py
    echo "c.NotebookApp.password=''" >> .jupyter/jupyter_notebook_config.py
    echo "c.FileCheckpoints.checkpoint_dir = '/vagrant/.notebookChekpoints'" >> .jupyter/jupyter_notebook_config.py

    echo "As Virtual Environment was set up, you must first run 'source ~/venv/bin/activate'"
    echo "Then 'rasa --version' should give You installed Rasa version"
    echo "System set up for RASA chatbots workshop is complete"

  SHELL
end
