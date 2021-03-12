#include <stdio.h>
#include <>
using namespace std;

int main()
{
    int arr[5];
    arr[3] = 3;
    for(int i: arr) cout << i << ", ";
}