#include <iostream>
using namespace std;


int out(int x) {
  cout << "  - called with value: "<< x << endl;
  return x;
}






void if_test() {
  int x = 29;

  if ( x < 25 ) {
    cout << "x is less than 25" << endl;
  } else {
    cout << "x is NOT less than 25" << endl;
  }

  return;

  // booleans
  int v = 0;

  if (v)
    cout << "v is true! " << endl;
  else
    cout << "v is false" << endl;


  // 0 is 'false', all other values are 'true'
  return;

  // boolean operators
  cout << "Checking and: " << (false && false) << endl;    // python and
  cout << "Checking or : " << (true || false) << endl;     // python or
  cout << "Checking not: " << (!true) << endl;             // python not

  return;



  // short circuiting
  cout << "Checking short circuiting ... " << endl;
  
  int final_val; 
  final_val =  out(0) && out(0) ;

  cout << "Final value: " << final_val << endl;

  return;

  // ternary operator
  int marks = 49; 
  int pass =  (marks >= 50)  ?  1  :  0   ;

  cout << "pass = " << pass << endl;

}




void while_test() {
  int i = 0;
  while (i < 5) {
    cout << i << endl;
    i++;   // (almost) the same as:  i += 1;
           // which is the same as:  i = i + 1;
  }
}

void for_test() {
  for (   int i = 0  ;    i < 5   ;    i++   )  {
    cout << i << endl;
  }
}





int main() {

  if_test();

  // while_test();

  // for_test();

  return 0;
}
