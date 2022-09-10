#include<iostream>
#include<fstream>
#include<string>
#include"Hack Assembler Source.cpp"
using namespace std;

int main(void)
{

    string filename = "test.txt";
    //cout << fileRead(filename);
    assembler(filename);
    cout << "\nSystem End, press any key to exit";
    std::cin.get();
    return 0;
}
