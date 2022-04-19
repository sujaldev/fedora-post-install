git clone https://github.com/sujaldev/fedora-post-install
cd fedora-post-install || exit
pip install virtualenv psutil
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
ansible-playbook main.yml --ask-become-pass --extra-vars "$1"
