#include <iostream>
using namespace std;



void array_test() {
  int a[5];    // fixed size, continguous memory locations!
               // a poor man's list



  a[0] = 24;   // 0-based index






  cout << "Before assignment --- " << endl;
  for (int i = 0; i < 5; i++) {
    cout << a[i] << "  ";    // notice the garbage values
  }

  cout << endl;
  // return;





  // change values
  for (int i = 0; i < 5; i++) {
    a[i] = i*i;
  }

  // let's output again:
  cout << "After assignment --- " << endl;
  for (int i = 0; i < 5; i++) {
    cout <<  a[i] << " ";    // notice the garbage values
  }

  cout << endl;
}


void array_test_2d() {
  int a[2][3];




  cout << "Before assignment --- " << endl;
  for (int i = 0; i < 2; i++) {
    // i = 0
    for (int j = 0; j < 3; j++) {
      // j = 0
      cout << a[i][j] << "  " ;
    }

    cout << endl;
  }
  // return;



  int val = 1;
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
      a[i][j] = val;
      val += 1;
    }
  }

  cout << "After assignment --- " << endl;
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
      cout << a[i][j] << " " ;
    }

    cout << endl;
  }
}

void struct_test() {

  int x = 4; 







  // a struct is a kind of template

  struct student {
    int rollno;
    float marks;
  };





  student s1;
  student s2;

  s1.rollno = 1;
  s1.marks = 19.9;

  s2.rollno = 2;
  s2.marks = 59.9;

  cout << "Student s1 has " << s1.marks << " marks" << endl;
  cout << "Student s2 has " << s2.marks << " marks" << endl;
  // return;

  int       nums[2]; 




  student   a[5];
  a[0].marks = 87.9;
  cout << "Student a[0] has " << a[0].marks << " marks" << endl;

  // future topics 
}

int main() {

  array_test();

  // array_test_2d();

  // struct_test();

  return 0;

}
