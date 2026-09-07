#include<iostream>
using namespace std;
class student{
    public:
    int a;
    student(){
        a=20;
        cout<<"contructor is applied";
    }
};
    int main(){
        student  s;
        s.a;
        return 0;
    }
