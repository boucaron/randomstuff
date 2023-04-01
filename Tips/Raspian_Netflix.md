I finally found an easy way to get Netflix running on Raspbian for my daughter! The trick is to enable DRM, but the catch is that it only works on 32-bit Chromium.

Here's what you need to do:

-  Install 32-bit Chromium by typing this command: 'sudo apt install chromium-browser:armhf'
-  Install DRM by typing this command: 'sudo apt install libwidevinecdm0'
-  Launch Chromium and enjoy streaming on Netflix!

Just remember that you need to have DRM enabled, and that Chromium only works in 32 bits for this to work.


