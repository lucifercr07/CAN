#!/bin/sh

if [ `whoami` != 'root' ]
then
    echo "Please proceed as root!!"
    exit
fi

if [ `lsb_release -rs` = "14.04" ]
then
	add-apt-repository -y ppa:fkrull/deadsnakes-python2.7
	apt-get -y update
	apt-get -y install python2.7
fi

version=$(python -V 2>&1)
echo "Python upgraded to '$version'"

add-apt-repository -y ppa:webupd8team/sublime-text-3
apt-get update
apt-get install -y sublime-text-installer

if [ -e /usr/share/applications/sublime_text.desktop ] 
then
	sed -i -e 's/gedit/sublime_text/g' /usr/share/applications/defaults.list
	echo "Sublime Text set as default!!"
elif [ -e /usr/share/applications/sublime-text.desktop ] 
then	
	sed -i -e 's/gedit/sublime-text/g' /usr/share/applications/defaults.list
	echo "Sublime Text set as default!!"
else
	echo "Please check sublime installation /usr/share/applications/sublime-text.desktop file missing."
fi

read -p "Want to install liota? Press y/n: " choice

if [ $choice = "y" ]
then
	pip install liota
	echo "Liota Setup complete!!"
fi

read -p "Want to install docker -ce? Press y/n: " choice

if [ $choice = "y" ]
then
	if [ `lsb_release -rs` = "14.04" ]	
	then
		apt-get -y remove docker docker-engine docker.io
		apt-get -y update
		apt-get -y install linux-image-extra-$(uname -r) linux-image-extra-virtual
		apt-get -y update
		apt-get -y install apt-transport-https ca-certificates curl software-properties-common
		curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
		add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
		apt-get -y update
		apt-get -y install docker-ce
			echo "Setup complete!! Enjoy!!"
	else
		echo "Docker installation for UBUNTU 14.04 only. Please contact Docker docs for other versions."
	fi
fi

