APPNAME="nettools"
PYTHONVERSION="3.6.9"
EXTRAS="none"

help:
	@echo "usage: make [command]"

download_bash_environment_manager:
	@if test ! -d ".tmp/bash-environment-manager-master";then \
		sudo su -m $(SUDO_USER) -c "mkdir -p .tmp"; \
		sudo su -m $(SUDO_USER) -c "cd .tmp; wget -O bash-environment-manager.zip https://github.com/terminal-labs/bash-environment-manager/archive/master.zip"; \
		sudo su -m $(SUDO_USER) -c "cd .tmp; unzip bash-environment-manager.zip"; \
	fi

conda: download_bash_environment_manager
	@sudo bash .tmp/bash-environment-manager-master/types/python/assemble.sh $(APPNAME) $(SUDO_USER) conda
	@sudo bash .tmp/bash-environment-manager-master/types/python/emit/emit_activate.sh $(APPNAME) $(SUDO_USER) conda

vagrant.conda: download_bash_environment_manager
	@if test ! -f "Vagrantfile";then \
		wget https://raw.githubusercontent.com/terminal-labs/shelf/master/vagrant/Vagrantfile; \
		chown $(SUDO_USER) Vagrantfile; \
	fi
	@sudo bash .tmp/bash-environment-manager-master/types/python/assemble.sh $(APPNAME) $(SUDO_USER) vagrant-conda
