# X11 Server on WSL2

This is kind of annoying when you want to display something in the VM, or you do not have an equivalent software on Windows

This tip is taken from : 
https://askubuntu.com/questions/1252007/opening-ubuntu-20-04-desktop-on-wsl2/1365455#1365455

sudo apt install xrdp xfce4

You will be asked to set the keyboard layout, put the same as in Windows


# Optionally, back up the default config
sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak

# Windows are often already running RDP on 3389
# Prevent conflicts:
sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini

# Prevent Wayland from being used in Xrdp
echo "export WAYLAND_DISPLAY=" > ~/.xsessionrc

# Optional, if you only have one desktop environment installed
echo startxfce4 > ~/.xsession 

sudo service xrdp start
# Or, if running Systemd
sudo systemctl restart xrdp

If you cannot login with your user, set a password
sudo passwd myLogin

After under the windows host, you launch the 'remote desktop' 
on 'localhost:3390' and enjoy ;)
