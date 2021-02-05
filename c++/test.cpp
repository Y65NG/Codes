#include <iostream>
using namespace std;

#define L 10
int g;



int main()
{
    int i;
    cin >> i;
    int a = 3;
    int *ip = &a;
    cout << &ip << endl;
    cout << ip << endl;
    cout << *ip << endl;
    cout << a << endl;
    return 0;
}