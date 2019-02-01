/*
 * Purpose: Implementation of Markov localization algorithm in 1D
 * Author: Juan David Rios
 * Date: January 31, 2019
 * Intructions:
 * Run "g++ -g -Wall -std=c++11 -omarkov main.cpp" in a Linux console
*/

#include <iostream>
#include <vector>

#include "helpers.h"

using std::vector;

// initialize priors assuming vehicle at landmark +/- 1.0 meters position stdev
vector<float> initialize_priors(int map_size, vector<float> landmark_positions,
                                float position_stdev);

float motion_model(float pseudo_position, float movement, vector<float> priors,
                   int map_size, int control_stdev);

int main() {

  // set standard deviation of control:
  float control_stdev = 1.0f;

  // set standard deviation of position:
  float position_stdev = 1.0f;

  // meters vehicle moves per time step
  float movement_per_timestep = 1.0f;

  // set map horizon distance in meters 
  int map_size = 25;

  // initialize landmarks
  vector<float> landmark_positions {5, 10, 20};

  // initialize priors
  vector<float> priors = initialize_priors(map_size, landmark_positions,
                                           position_stdev);

  // step through each pseudo position x (i)    
  for (float i = 0; i < map_size; ++i) {
    float pseudo_position = i;

    // get the motion model probability for each x position
    float motion_prob = motion_model(pseudo_position, movement_per_timestep,
                                     priors, map_size, control_stdev);
        
    // print to stdout
    std::cout << pseudo_position << "\t" << motion_prob << std::endl;
  }    

  return 0;
}

// motion model: calculates prob of being at 
// an estimated position at time t
float motion_model(float pseudo_position, float movement, vector<float> priors,
                   int map_size, int control_stdev) {
  // initialize probability
  float position_prob = 0.0f;
  
  for (int i = 0; i < map_size; ++i){
    float norm_value = Helpers::normpdf(pseudo_position-i, movement, control_stdev);
    position_prob += norm_value*priors[i];
  }
 
  return position_prob;
}

//initialize_priors function
vector<float> initialize_priors(int map_size, vector<float> landmark_positions,
                                float position_stdev) {

  // initialize priors assuming vehicle at landmark +/- 1.0 meters position stdev

  // set all priors to 0.0
  vector<float> priors(map_size, 0.0);
  
  float normalizer = landmark_positions.size()*(2*int(position_stdev)+1);
  float value = 1/normalizer;
  
  for (int i =0; i<landmark_positions.size(); ++i)
  {
      for (int p = int(landmark_positions[i]-position_stdev); p<= int(landmark_positions[i]+position_stdev); ++p)
      {
          priors[p] = value;
      }
  }
  return priors;
}