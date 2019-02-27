/* Classifier class source code
 * Description: This file implements the main function used in the Gaussian Naive Bayes classifier
 * Author: Juan David Rios
 * Date: February 26/2019
*/

#include "classifier.h"
#include <math.h>
#include <string>
#include <vector>
#include <iostream>

//using Eigen::ArrayXd;
using std::string;
using std::vector;

// for portability of M_PI (V. Studio, MinGW, etc.)
#ifndef M_PI
const double M_PI = 3.14159265358979323846;
#endif

// Initializes GNB
GNB::GNB() {
  /**
   * Initialize GNB, if necessary. May depend on implementation.
   */
  
}

GNB::~GNB() {}

void GNB::train(const vector<vector<double>> &data, 
                const vector<string> &labels) {
  /**
   * Trains the classifier with N data points and labels.
   * @param data - array of N observations
   *   - Each observation is a tuple with 4 values: s, d, s_dot and d_dot.
   *   - Example : [[3.5, 0.1, 5.9, -0.02],
   *                [8.0, -0.3, 3.0, 2.2],
   *                 ...
   *                ]
   * @param labels - array of N labels
   *   - Each label is one of "left", "keep", or "right".
   *
   */
   
   int c;
   
   // Initializes vectors of mean, standard deviation and label probability values
   for (int i = 0; i < possible_labels.size() ; ++i ) {
       mean_values.push_back({0.0,0.0,0.0});
       std_values.push_back({0.0,0.0,0.0});
       p_label.push_back(0.0);
   }
   
   // Accumulate values of data per label per feature
   for (int i = 0; i < data.size(); ++i) {
       if (labels[i]==possible_labels[0]) c = 0;
       else if (labels[i]==possible_labels[1]) c = 1;
       else if (labels[i]==possible_labels[2]) c = 2;
       else std::cout << "Label " << i << "th is not in the list of possible labels."<<std::endl;
       
       mean_values[c][0] += data[i][1];
       mean_values[c][1] += data[i][2];
       mean_values[c][2] += data[i][3];
       //mean_values[c][3] += data[i][3];
       p_label[c] += 1;
   }
   
   // Calculate mean value per label per feature
   for (int c = 0; c < possible_labels.size(); ++c) {
       for (int j = 0; j < data[0].size()-1; ++j) {
           mean_values[c][j] /= p_label[c];
           //std::cout << " Mean value for class "<<c<< " , feature "<< j << " : " << mean_values[c][j] << std::endl;
           //std::cout << "Total labels in class " << c<<" : " << p_label[c] << std::endl;        
       }
   }
   
   // Accumulate values of data minus the mean
   for (int i = 0; i < data.size(); ++i) {
       
       if (labels[i]==possible_labels[0]) c = 0;
       else if (labels[i]==possible_labels[1]) c = 1;
       else if (labels[i]==possible_labels[2]) c = 2;
       else std::cout << "Label " << i << "th is not in the list of possible labels."<<std::endl;
       
       std_values[c][0] += (data[i][1]-mean_values[c][0])*(data[i][1]-mean_values[c][0]);
       std_values[c][1] += (data[i][2]-mean_values[c][1])*(data[i][2]-mean_values[c][1]);
       std_values[c][2] += (data[i][3]-mean_values[c][2])*(data[i][3]-mean_values[c][2]);
       //std_values[c][3] += (data[i][3]-mean_values[c][3])*(data[i][3]-mean_values[c][3]);
   }
  
  // Standard deviation per label per feature
  for (int c = 0; c < possible_labels.size(); ++c) {
      for (int j = 0; j < data[0].size()-1; ++j) {
           std_values[c][j] = sqrt(std_values[c][j]/(p_label[c]-1));
           //std::cout << " Standard deviation for class "<<c<< " , feature "<< j << " : " << std_values[c][j] << std::endl;
      }
      p_label[c] /= data.size();
      std::cout << "Probability of class " << c<< " : "<< p_label[c] << std::endl;
  }
}

string GNB::predict(const vector<double> &sample) {
  /**
   * Once trained, this method is called and expected to return 
   *   a predicted behavior for the given observation.
   * @param observation - a 4 tuple with s, d, s_dot, d_dot.
   *   - Example: [3.5, 0.1, 8.5, -0.2]
   * @output A label representing the best guess of the classifier. Can
   *   be one of "left", "keep" or "right".
   *
   * TODO: Complete this function to return your classifier's prediction
   */
   
   // Store maximum probability max_prob and the associated class index max_class
   double max_prob = 0.0;
   int max_class = 0;
   // Likelihood of the state sample to be part of a particular class
   double likelihood;
   
   for (int c = 0; c < possible_labels.size(); ++c) {
       likelihood = 1.0;
       for (int i = 0; i < sample.size()-1; ++i) {
            // Product of all probabilities of independant state features i in the class c
            likelihood *= gaussian(std_values[c][i], mean_values[c][i], sample[i+1]);   
       }
       likelihood *= p_label[c];
       
       // Store maximum probability and the respective class index
       if (likelihood > max_prob) {
           max_prob = likelihood;
           max_class = c;
       }
   }
   // Return class with maximum likelihood associated to the state provided in sample
  return this -> possible_labels[max_class];
}


/**
 * Calculates the univariate gaussian probability given the standard deviation, 
 * mean value for a given feature
 */  
inline double gaussian(double std_x, double ux, double x) {
    // Define normalization factor in multivariate gaussian distribution
    double normalization;
    normalization = 1.0/sqrt(2.0 * M_PI * std_x * std_x);

    // Define exponent of multivariate gaussian distribution
    double exponent;
    exponent = (pow(x-ux, 2)/(2*pow(std_x,2)));

    // Define probability given the normalization factor and the exponent
    double weight;
    weight = normalization * exp(-exponent);

    return weight;
}