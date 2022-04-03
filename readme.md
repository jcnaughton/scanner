# Raspi scanner printer

### Install CUPS
[see Tom's hardware guide](https://www.tomshardware.com/how-to/raspberry-pi-print-server)


### Install sane
[Directions to install SANE](https://pimylifeup.com/raspberry-pi-scanner-server/)

### Find your device name
$ scanimage -L
device `hpaio:/usb/Deskjet_3050_J610_series?serial=CN123456RT07HX' is a Hewlett-Packard Deskjet_3050_J610_series all-in-one
- substitute the device name in line 21 of scan.cgi
- install apache2
- configure the default directory to be a cgi [how to](https://forums.raspberrypi.com/viewtopic.php?t=148254)
- install samba and create a directory /scans and share that directory.

 ```
 [scans]
   path = /scans
   comment = my scans
   browseable = yes
   read only = no
   create mask = 0700
   directory mask = 0700
   ```

