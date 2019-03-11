#ifndef HYBRID_A_STAR_
#define HYBRID_A_STAR_H_

#include <vector>

using std::vector;

class HAS {
 public:
  // Constructor
  HAS();

  // Destructor
  virtual ~HAS();

  // HAS structs
  struct maze_s {
    int g;  // iteration
    double x;
    double y;
    double theta;
    double f;
  };

  struct maze_path {
    vector<vector<vector<int>>> closed;
    vector<vector<vector<maze_s>>> came_from;
    maze_s final;
  };
  
  // HAS functions
  double heuristic(double x, double y, vector<int> &goal);

  static bool compare_maze(const HAS::maze_s &lhs, const HAS::maze_s &rhs);
  
  int theta_to_stack_number(double theta);

  int idx(double float_num);

  vector<maze_s> expand(maze_s &state, vector<int> &goal);

  vector<maze_s> reconstruct_path(vector<vector<vector<maze_s>>> &came_from, 
                                  vector<double> &start, HAS::maze_s &final);

  maze_path search(vector<vector<int>> &grid, vector<double> &start, 
                   vector<int> &goal);

 private:
  const int NUM_THETA_CELLS = 90;
  const double SPEED = 1.45;
  const double LENGTH = 0.5;
};

#endif  // HYBRID_A_STAR_H_