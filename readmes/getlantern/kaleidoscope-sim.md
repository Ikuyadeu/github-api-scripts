Kaleidoscope Simulator
======================

This is a quick and dirty simulator for the [Kaleidoscope
library](https://github.com/getlantern/kaleidoscope).

![screenshot](http://i.imgur.com/xe3wv.png)


Quick Explanation
-----------------

The sim will generate a small random social-network-like graph using the 
method outlined in: 

A model for social networks
R. Toivonen, J.-P. Onnela, J. Saramäki, J. Hyvönen, K. Kaski
http://arxiv.org/abs/physics/0601114

Click the nodes to change their type.

Colors indicate the following:

* Black - censored
* White - uncensored
* Red   - adversary
* Gray  - uncensored + blocked
* Green - censored + access

Numbers: 

* Uncensored nodes (m/n) indicates unique/total nodes reached by advertisements
* Censored nodes m - indicates the number of nodes discovered via advertisements


Status
------

This simulator is mainly experimental and rough on all edges.

Quickstart
----------

You will likely need to install the kaleidoscope library by hand and run this from your favorite IDE for the time being.  

The kaleidoscope library can be found at https://github.com/getlantern/kaleidoscope

Try the following:

    git clone git://github.com/getlantern/kaleidoscope.git
    git clone git://github.com/getlantern/kaleidoscope-sim.git
    cd kaleidoscope
    mvn install
    cd ../kaleidoscope-sim
    mvn package && java -jar target/sim-1.0-SNAPSHOT-jar-with-dependencies.jar

License
-------

This library is licensed under an MIT style license. 
Complete license details can be found in the included LICENSE document.
