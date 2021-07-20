#include <iostream>
using namespace std;

void third_function(int *v){ 
  cout << " - value of v in third_function:  " << v << endl;
  cout << " - third function changed *v to:  " << v << endl;
  *v = *v + 10; 
}

void second_function(int &v) {
  v = v + 10;
  cout << " - second function changed v to: " << v << endl;
  cout << " - address of v : " << &v << endl;
}
// ^-- BAD idea! Do not do this!

void first_function(int v) {
  v = v + 10;
  cout << " - first function changed v to:  " << v << endl;
  cout << " - address of v : " << &v << endl;
}



void runner() {
  int x;
  x = 0;

  cout << "Address of x = " << &x << endl << endl;
  cout << "Step 1: x = " << x << endl;

  // cout << "Calling first_function ...  " <<endl; 
  // first_function(x);
  // cout << "Step 2: After first_function...  x = " << x << endl;

  cout << "Calling second_function ...  " <<endl; 
  second_function(x);
  cout << "Step 3: After second_function..  x = " << x << endl;

  cout << "Calling third_function" << endl; 
  third_function(&x);
  cout << "Step 4: After third_function..  x = " << x << endl;
}





void test_array(int b[], int size) {
    cout << "Inner function ... " << endl;
    cout << "Address of b: " << b << endl;
    
    b[0] = 24; 
    for (int i=0; i < size; i++)
      cout << b[i] << " ";
    cout << endl;
}



void array_as_args() {
  int a[] = {0, 1, 2, 3, 4};

  test_array(a, 5);
  cout << "Address of a: " << a << endl;

  cout << "Outer function ...  " << endl;
  for (int i=0; i < 5; i++)
    cout << a[i] << " ";
  cout << endl;
}


int main() {
  runner();

  // array_as_args();
  return 0;
}
