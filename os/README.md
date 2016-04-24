
## Overview

Here's how to build an image for use across a bunch of imaging nodes. Approach we're using here is to get a bunch 
of homogenous MicroSD cards, build image for one, and then duplicate it to others. Making an image available for 
download would be pretty challenging at this point so I won't just now.

## CAVEAT

__This is incomplete and to a large extent is me collecting my thoughts as I get this up and running - so this document is very much a work in progress. Don't expect great things from this process just yet!__

## Unpacking the Raspbian image

The Raspbian image can be obtained at [...]

I'm using a Mac to write the image to a MicroSD card. So these instructions are Mac specific but all Unixes have the DD
command so you should be able to adapt these if you're on Linux. On Windows? Sorry I have no idea. If you figure it out
feel free to let me know.

Go to the terminal:
```
diskutil list                         # See which disk has the SD media and use that for the next step
sudo diskutil unmountDisk /dev/disk1  # Replace disk1 with the target disk - unmount disk rather than partition
sudo dd bs=1m if=<path_to>/raspbian-jessie.img of=/dev/rdisk1   # Rdisk is raw disk, again, use the right one for your system
sudo diskutil unmountDisk /dev/disk1  # Just in case
```

This overwrites the contents of the entire media with Raspbian.

Remove the media (shouldn't have to eject since it's not mounted), put it in the Pi and boot it. Pi needs to be
connected to the internet, preferably via an ethernet cable as we'll be messing with the wireless. On the initial 
boot it will go straight to the GUI.

Launch the console and type
```
sudo raspi-config
```

Choose option 3 - "Boot Options" and select option B1.
You may wish to set your keyboard type via 5 - "Internationalisation Options" if you're not in the UK.
Choose option 1 - "Expand Filesystem" to expand the partition to fill the card. 
Choose "Finish" and reboot when asked.

Once rebooted into the console, log back in as `pi` and execute these commands:

```
sudo apt-get update
sudo apt-get install hostapd dnsmasq
```

Now would be a good time to clone this repo to your local system if you haven't already.

## Apply the files in this repo

For each of the files in the `os/etc` and `os/boot` folders, either:
* If the repo filename starts with __APPEND__, then append its contents to the matching file in the Raspbian's system files. `cat <infile> >> <outfile>` is a good way to do this.
* If the repo filename starts with __EDIT__, then find the appropriate part of the file and update it accordingly. You'll probably have to do this by hand.
* Otherwise, just copy the file to the correct location.

## A bunch of stuff that isn't exactly figured out yet

__Here's where you install the software that I haven't written yet in the places I haven't determined yet and configure it in ways I can't yet articulate.__ Watch this space.

## Duplicate the image N times.

Where N is the number of camera-equipped Raspberry Pi's you want to run as imaging nodes.

Start by shutting down the Pi (with `shutdown`) and removing the media.

If you have 2 separate means of accessing MicroSD cards on your computer this will be easier because you can use `dd` to dump straight from the one we just made to a fresh one. Otherwise, you'll have to extract an image from the card we just configured and use that; so make sure you have enough free space for the entire size of the media (even thought it's mostly empty!)

[...more to come...]

## In the interim...

As nice as it would be to have homogenous images, it's probably going to take some work.
Quickest way to get this up and running is to bite the bullet and have a specific image for the coordinator.

The coordinator will need to have its access point manually started:

```
sudo hostapd /etc/hostapd/hostapd.conf
```

## TODO 

Lots and lots!
