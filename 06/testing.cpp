#include<stdio.h>
#include<iostream>
#include<string>
#include<bitset>
using namespace std;

int main(void)
{
    int a = 16;
    bitset<16>temp(a);
    string binary = temp.to_string();
    printf("%s", binary.c_str());
    return 0;
}
