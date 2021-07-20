#include <iostream> 
using namespace std; 

int variables_test(int p);  // function declaration OR prototype 

int main () {
  cout << "In main function ... " << endl;
  variables_test(3);
}

int variables_test(int p) {
  cout << "Inside variables_test function ... " << endl;
  return 0;
}
