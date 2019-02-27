# Implementation of Gaussian Naive Bayes

This folder contains the implementation of a Gaussian Naive Bayes classifier to predict the behavior of vehicles on a highway. The image below shows the vehicle behaviors on a 3 lane highway (with lanes of 4 meter width). The dots represent the d (y axis) and s (x axis) coordinates of vehicles as they either:

- change lanes left (shown in blue)
- keep lane (shown in black)
- or change lanes right (shown in red)

![Vehicle behaviors on a highway](images/naive_bayes.png)

The main job here is to write a classifier that can predict which of these three maneuvers a vehicle is engaged in given a single coordinate (sampled from the trajectories shown below).

Each coordinate contains 4 features:

- s (Tangential distance in a given lane)
- d (Ortogonal distance in a given lane)
- d(s)/dt (Rate of change of tangential distance in time) 
- d(d)/dt (Rate of change of ortogonal distance in time)

The lane width is 4 meters (this might be helpful in engineering additional features in the algorithm).