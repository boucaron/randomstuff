As many of us having an old NVidia GTxx card, because we do not need more for Server or Basic usage. It is a real pain to reinstall for each kernel change the proprietary driver, because the nouveau driver simply does not work.

The package akmod-nvidia-470xx is pretty useful --> rpmfusion-nonfree-nvidia

However from time to time, when installing a fresh kernel it is stuck.

I found this pretty nice little trick to cleanup and to reinstall it from scratch and really recompile the module.

1. Remove the existing stuff (be careful if you have Cuda stuff and other packages)
   sudo dnf remove *nvidia* --noautoremove --exclude=nvidia-gpu-firmware

2. Reinstall the whole thing
   sudo dnf install akmod-nvidia-470xx

Check running a 'top' that the module is compiled in the background

3. Check list of installed nvidia stuff
   sudo dnf list installed *nvidia*

4. Reboot the puppy



