Samsung S3 GT-I9300

I was still running an old Android 7 on it with nearly nothing that can be installed or updated.
Thanks to the good work made by https://github.com/html6405, I can still reuse it (not my primary phone)

- Update to Android 11 (Android 12 not yet having a "stable" Google packages - aka open gapps)
https://forum.xda-developers.com/t/rom-unofficial-11-0-i9300-lineageos-18-1-beta-treblelized.4301657/
- Instructions are very clear

Backup:
1) Backup 
2) Backup 
3) Backup 


Download:
1) https://androidfilehost.com/?w=files&flid=326712: lineage-18.1-20220420-HTML6405-i9300.zip
2) open_gapps: open_gapps-arm-11.0-pico-20220215.zip 
I took the pico version for the OpenGApps due to size limitations
3) On Windows: Download Odin 3.x
4) Download the last TWRP
Copy on the sdcard if you have a running Android on the phone 
	- Activate Developper Mode: Settings/About my phone/Go on the release name really at the bottom/Tap several time (it will tell you this is activated)
	- Settings/System/Developper stuff/Default USB Mode/Transfer 
	- Disconnect/Reconnect the USB cable and TADA you will see both Internal and SDCARD

Follows instructions from here: https://www.mhs-solutions.com/instructions-s3/
1) Run Odin
2) Flash TWRP for Recovery (really important...)
3) Run TWRP: Cleanup: Wipe -> Advanced Wipe -> System (I finished by doing a Format...)
4) TWRP: Install: ROM + OpenGApps  (you can do it in sequence, which is handy)
5) TWRP: Reboot and enjoy

Experience:
- It crashes from time to time... the Android 12 beta seems a bit more stable and reactive (may be due to absence of OpenGAAPS)
- It is slow to boot 
- I will probably upgrade to Android 12 when OpenGAPPS will "release" it


