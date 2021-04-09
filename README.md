# RASA chatbots workshop
This is RASA chatbots workshop repo. It contains files needed for the workshop. During workshop atendees will create and train chatbot with RASA framework, use Python programming language to enable it to make API calls and integrate it with Discord chat app. 

## Setting up system for workshop with Vagrantfile (recommended)
Easiest (and recommended) way to configure system for a workshop is by using [vagrant](https://www.vagrantup.com/) with [virtualbox](https://www.virtualbox.org/) and provided Vagrantfile - it will create and set up virtual environment with all tools needed for workshop.  

Vagrantfile has configuration to use 2 cores and 4GB RAM, that can be altered if needed with simple text editor like notepad.  

To check that vagrant works as expected in terminal cd to main rasa-bots folder and use
```bash
vagrant up
```
When this command is complete (can take more than few minutes) You should see something like "default: System set up for RASA chatbots workshop is complete". If that is the case everything worked as expected and You can use
```bash
vagrant halt
```
to stop the virtual machine till the workshop.

In case something doesnt run correctly in first try - e.g. it got stuck for a long time - You can retry by first destroying curent virtual machine with
```bash
vagrant destroy
```
Then you can try to bring machine up one more time with
```bash
vagrant up
```

## Setting up system for workshop by installing required tools
In case for any reason setting up with Vagrantfile didn't work, You can also just install needed tools
  * install RASA, more info [https://rasa.com/docs/rasa/installation](https://rasa.com/docs/rasa/installation)
  * install discord.py, more info [https://pypi.org/project/discord.py/](https://pypi.org/project/discord.py/)
  * install JupyterLab, more info [https://jupyter.org/install](https://jupyter.org/install)  
      For JupyterLab, please configure specific checkpoint directory (otherwise it will create new subfolder in every place we will work and that will confuse RASA):
        c.FileCheckpoints.checkpoint_dir = '/vagrant/.notebookChekpoints'

