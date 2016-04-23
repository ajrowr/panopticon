# panopticon
Using Raspberry Pi's to build a self-organising camera network for photographing in bullet time.

## Goal

If you know me then you're probably aware of my experiments with 360° rotational imaging. The idea here is to take it to 
the next level by having multiple synchronized cameras instead of a single camera with a subject being rotated by 
a turntable.

## Abstract

By building a standard disk image which can be flashed to a bunch of SD cards and deployed across a set of Raspberry Pi 
3 units we can build a self-organising network of camera nodes (let's call them Cameroids). These nodes can then 
coordinate to take photos at the same instant, which can then be displayed on the web using Orbimg technology. Attach
batteries to these cameroids and they can go out in the field. Who knows what we might be able to do from there.

Each cameroid will search for a wi-fi network called Panopticon and join it if found. If not found, it will build the network
itself so that others can attach (this first-to-boot node is known as the co-ordinator). Each node runs a collection of 
deliberately simplistic network services which tell it (most likely via UDP broadcast) when and how to take photos. These are
stored on each local device and the co-ordinator provides various means for the outside world to access them. 

This repo will contain all my work relating to this topic, so expect to find info on setting up the OS of the Pi units; 
software; and hardware specs. 

## Hardware

I'm using Raspberry Pi 3's because they have built-in wi-fi. If you're using a 2 or earlier with a USB wi-fi dongle then 
some hacking may be required. The Pi's each have a standard Pi Camera module attached, and I'm trying out various different 
types of USB powerbank-style batteries to see which ones give the best bang for buck.

## Software

As much as possible written in Python.

