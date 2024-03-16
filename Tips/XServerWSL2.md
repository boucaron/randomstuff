# Setting Up X11 Server on WSL2

Encountering difficulties when attempting to display content in the virtual machine or lacking equivalent software on Windows can be frustrating.

This helpful tip is sourced from: [askubuntu.com](https://askubuntu.com/questions/1252007/opening-ubuntu-20-04-desktop-on-wsl2/1365455#1365455)

```bash
sudo apt install xrdp xfce4
During installation, ensure to match the keyboard layout with that of Windows.

Optionally, Backup Default Configuration
```bash
sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak
To prevent conflicts, especially with Windows often utilizing RDP on port 3389, adjust the port:

```bash
sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini
Prevent Wayland from being utilized in Xrdp:

```bash
echo "export WAYLAND_DISPLAY=" > ~/.xsessionrc
If only one desktop environment is installed, set it as the default:

```bash
echo startxfce4 > ~/.xsession 
Start the xrdp service:

```bash
sudo service xrdp start
Alternatively, if using Systemd:

```bash
sudo systemctl restart xrdp
If encountering login issues, set a password for your user:

```bash
sudo passwd myLogin
Finally, on the Windows host, launch 'Remote Desktop' and connect to 'localhost:3390' to begin using the setup.

Enjoy the seamless experience!
