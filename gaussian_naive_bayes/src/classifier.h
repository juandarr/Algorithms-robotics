/* Classifier class template
 * Description: This file creates the template for the classifier class
 * Author: Juan David Rios
 * Date: February 26/2019
*/

#ifndef CLASSIFIER_H
#define CLASSIFIER_H

#include <string>
#include <vector>
//#include "Dense"

//using Eigen::ArrayXd;
using std::string;
using std::vector;

// Unimodal gaussian distribution
inline double gaussian(double std_x, double ux, double x);

// Gaussian naive bayes class

class GNB {
 public:
  /**
   * Constructor
   */
  GNB();

  /**
   * Destructor
   */
  virtual ~GNB();

  /**
   * Train classifier
   */
  void train(const vector<vector<double>> &data, 
             const vector<string> &labels);

  /**
   * Predict with trained classifier
   */
  string predict(const vector<double> &sample);

  vector<string> possible_labels = {"left","keep","right"};
  
  // Mean values for state variables s, d , s_dot and d_dot in a given class C
   vector<vector<double>> mean_values;
   // Standard deviation for state variables s, d, s_dot and d_dot in a given class C
   vector<vector<double>> std_values; 
   // Class probabilities 
   vector<double> p_label;
  
};

#endif  // CLASSIFIER_H