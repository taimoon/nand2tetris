#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
#include<stdio.h>
#include<unordered_map> //hash map
using namespace std;
const int SP = 0;
const int LCL = 1;
const int ARG = 2;
const int THIS = 3;
const int THAT = 4;
enum R{R0, R1, R2, R3, R4, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15};
const int SCREEN = 16384;
const int KBD = 24576;
//A is A-register, C is C-instruction, L is pseudo command
enum COMMAND_TYPE{A_COMMAND, C_COMMAND, L_COMMAND, INDETERMINATE};
string fileRead(string filename);
string getCodeLine(string line);
bool hasMoreCommands(string line);
unordered_map<string, int> constructor();
unordered_map<string, int> addEntry(string symbol, int address, unordered_map<string, int> symbolTable);
bool contains(string symbol, unordered_map<string, int> symbolTable);
int getAddress(string symbol, unordered_map<string, int> symbolTable);

string fileRead(string filename)
{
    ifstream inFile;
    inFile.open(filename);
    if(!inFile.is_open())
    {
        cout << "Could not open the file\t:" << filename << endl;
        cout << "Program terminating.\n";
        exit(EXIT_FAILURE);
    }
    string codeText, temp;
    while(!inFile.eof())
    {
        std::getline(inFile, temp);
        if(hasMoreCommands(temp))
            codeText += "\n" + getCodeLine(temp);
    }
    if(codeText[0]=='\n')
        codeText.erase(0,1);
    if(*(codeText.end())!= '\n')
        codeText += '\n';
    inFile.close();
    return codeText;
}
string getCodeLine(string line)
{
    string codeLine;
    string::iterator ptr;
    for(ptr = line.begin(); ptr < line.end(); ++ptr)
    {
        if(*ptr == '\n')
            break;
        else if(*ptr == ' '|| *ptr == '\t')
            continue;
        else
        {
            codeLine += *ptr;
            if(codeLine[0] == '(' && *ptr == ')')
                break;
        }
    }
    return codeLine;
}
bool hasMoreCommands(string line)
{
    string::iterator ptr;
    char temp = '\0';
    for(ptr = line.begin(); ptr < line.end(); ++ptr)
    {
        if(*ptr == '/' && *ptr == '/')
            return 0;
        else if(*ptr == 'A' ||
                *ptr == 'D' ||
                *ptr == 'M' ||
                *ptr == '@'
                )
            return 1;
        else if(*ptr == '0' && *(ptr+1) == ';')
            return 1;
        else if(*ptr == '(')
                    temp = *ptr;
        else if(*ptr == ')'&&temp=='(')
            return 1;
    }
    return 0;
}
int commandType(string line)
{
    string::iterator ptr;
    char temp = '\0';
    for(ptr = line.begin(); ptr < line.end(); ++ptr)
    {
        if(*ptr == '@')
            return A_COMMAND;
        else if(*ptr == 'A' ||
                *ptr == 'D' ||
                *ptr == 'M' ||
                *ptr == 'J'
                )
            return C_COMMAND;
        else if(*ptr == '(')
                    temp = *ptr;
        else if(*ptr == ')'&&temp=='(')
            return L_COMMAND; //pseudo-command
    }
    return INDETERMINATE;
}
string symbol(string line) //return the name without @
{
    string::iterator ptr;
    string varName;
    varName.clear();
    char temp = '\0';
    for(ptr = line.begin(); ptr < line.end(); ++ptr)
    {
        if(*ptr == '@' || *ptr == '(')
                temp = *ptr;
        else if((temp == '@' && *ptr == ' ' ) ||
                (temp == '(' && *ptr == ')')  ||
                *ptr == '\\'
                )
            break;
        else if(temp != '\0')
        {
            if(temp == *ptr)
                exit(EXIT_FAILURE);
            varName += *ptr;
        }
    }
    if(varName.back()=='\n')varName.back() = '\0';
    return varName;
}
string dest(string line)
{
    string::iterator ptr;
    string destSymbol;
    ptr = line.begin();
    while(*ptr != '=' && *ptr != ';' && ptr < line.end())
    {
        destSymbol += *ptr;
        ++ptr;
    }
    return destSymbol;
}
string comp(string line)
{
    string::iterator ptr;
    string compSymbol ="";
    ptr = line.begin();
    while(*ptr != '=' && *ptr != ';'&& ptr < line.end())
        ++ptr;
    if(*ptr == ';')
        return compSymbol;
    ++ptr;
    while(*ptr != '\n' && ptr < line.end())
    {
        compSymbol += *ptr;
        ++ptr;
    }
    return compSymbol;
}
string jump(string line)
{
    string::iterator ptr;
    string jumpSymbol="";
    ptr = line.begin();
    while(*ptr != ';' && *ptr != '=' && ptr < line.end())
        ++ptr;
    if(*ptr == '=')
        return jumpSymbol;
    ++ptr;
    while(jumpSymbol.length() < 3 && *ptr != '\n')
    {
        jumpSymbol += *ptr;
        ++ptr;
    }cout<<endl<<jumpSymbol<<endl;
    return jumpSymbol;
}
void binaryStringToBoolArr(string str, bool arr[], int len)
{
    char temp;
    for(int i = 0; i < len; ++i)
    {
        temp = str[i]-'0';
        arr[i] += (bool)temp;
    }
}
string get_destBinary(string mnemonic)
{
    string::iterator ptr;
    char temp[4] ={'0', '0', '0', '\0'};
    for(ptr = mnemonic.begin(); ptr < mnemonic.end(); ++ptr)
    {
        if(*ptr == 'A')
            temp[0] = '1';
        else if(*ptr == 'D')
            temp[1] = '1';
        else if(*ptr == 'M')
            temp[2] = '1';
    }
    string bitString(temp);
    return bitString;
}
string get_jumpBinary(string mnemonic)
{
    //Note: You can directly do the if else according to table covers 8 cases
    //No improvement compare to current implementation

    char temp[4] = {'0','0','0','\0'};
    if(mnemonic.length() == 0)
    {
        temp[0] = '0';
        temp[1] = '0';
        temp[2] = '0';
    }
    else
    {
        switch(mnemonic[1])
        {
        case 'E':
            temp[1] = '1';
            break;
        case 'N':
            temp[0] = '1';
            temp[2] = '1';
            break;
        case 'M':
            temp[0] = temp[1] = temp[2] = 1;
            break;
        case 'G':
            temp[2] = '1';
            break;
        case 'L':
            temp[0] = '1';
            break;
        }
        if(mnemonic[2] == 'E')
            temp[1] = '1';
    }

    string bitString(temp);
    return bitString;
}
string get_compBinary(string mnemonic)
{
    char temp;
    string binaryString;
    size_t found = mnemonic.find("M");
    bool isM = found != string::npos;
    if(isM)
        temp = '1';
    else
        temp = '0';
    found = mnemonic.find("D");
    bool isD = found != string::npos;
    found = mnemonic.find("1");
    bool isOne = found != string::npos;
    if(mnemonic.length() == 1)
    {
        switch(mnemonic[0])
        {
        case '0' :
            binaryString = "101010";
            break;
        case '1' :
            binaryString = "111111";
            break;
        case 'D' :
            binaryString = "001100";
            break;
        case 'A':
        case 'M':
            binaryString = "110000";
            break;
        }
    }
    else if(mnemonic.length() == 2)
    {
        if(isOne)
            binaryString ="111010";
        if(mnemonic[0] == '!')
        {
            if(isD)
                binaryString = "001100";
            else
                binaryString = "110000";
        }
        else if(mnemonic[0] == '-')
        {
            if(isD)
                binaryString = "001111";
            else
                binaryString = "110011";
        }
    }
    else if(mnemonic.length() == 3)
    {
        if(mnemonic[1] == '+')
            if(isOne)
                if(isD)
                    binaryString = "011111";
                else
                    binaryString = "110111";
            else
                binaryString = "000010";
        else if(mnemonic[1] == '&')
            binaryString = "000000";
        else if(mnemonic[1] == '|')
            binaryString = "010101";
        else if(mnemonic[1] == '-')
        {
            if(isOne)
                if(isD)
                        binaryString = "001110";
                    else
                        binaryString = "110010";
            if(mnemonic[0] == 'D')
                binaryString = "010011";
            else
                binaryString = "000111";
        }
    }
    binaryString = temp + binaryString;
    return binaryString;
}
void assembler(string filename, string targetFileName = "out.txt")
{
    FILE *outFile;
    outFile = fopen(targetFileName.c_str(), "w");
    string codeText = fileRead(filename);
    string::iterator ptr;
    string line;
    string binary;
    unordered_map<string, int> symbolTable = constructor();
    int romAddress = 0;
    int varAddress = 16;
    ptr = codeText.begin();
    while(ptr < codeText.end()) //first pass to handle pseudocommand
    {
        line.clear();
        while(*ptr != '\n')
        {
            line += *ptr;
            ++ptr;
        }
        line += *ptr;
        if(commandType(line) == A_COMMAND)
        {
            ++romAddress;
            if(!(contains(symbol(line), symbolTable))){
                symbolTable = addEntry(symbol(line), varAddress, symbolTable);
            }
            ++varAddress;
        }
        else if(commandType(line) == L_COMMAND)
        {
            if(!(contains(symbol(line), symbolTable)))
                symbolTable = addEntry(symbol(line), romAddress, symbolTable);
        }
        else if(commandType(line) == C_COMMAND)
            ++romAddress;
        ++ptr;
    }
    ptr = codeText.begin();
    while(ptr < codeText.end()) //second pass
    {
        line.clear();
        while(*ptr != '\n')
        {
            line += *ptr;
            ++ptr;
        }
        line += *ptr;
        if(commandType(line) == A_COMMAND)
        {
            if(!(contains(symbol(line), symbolTable)))
            {
                symbolTable = addEntry(symbol(line), varAddress, symbolTable);
                ++varAddress;
            }
            else
            {
                int address = getAddress(symbol(line), symbolTable);
            }

        }
        else if(commandType(line) == C_COMMAND)
        {
            cout << "111" << get_compBinary(comp(line))<<get_destBinary(dest(line))<<get_jumpBinary(jump(line))<<endl;
            fprintf(outFile, "111%s%s%s\n",
                    get_compBinary(comp(line)).c_str(),
                    get_destBinary(dest(line)).c_str(),
                    get_jumpBinary(jump(line)).c_str());
        }
        ++ptr;
    }
    fclose(outFile);
}
unordered_map<string, int> constructor()
{
    unordered_map <string, int> symbolTable;
    symbolTable.emplace("SP", SP);
    symbolTable.emplace("LCL", LCL);
    symbolTable.emplace("ARG", ARG);
    symbolTable.emplace("THIS", THIS);
    symbolTable.emplace("THAT", THAT);
    for(int i = 0; i < 16; ++i)
    {
        string temp = "R"+to_string(i);
        symbolTable.emplace(temp, i);
    }
    symbolTable.emplace("SCREEN", SCREEN);
    symbolTable.emplace("KBD", KBD);
    return symbolTable;
}
unordered_map<string, int> addEntry(string symbol, int address, unordered_map<string, int> symbolTable)
{
    pair <string, int>temp(symbol, address);
    symbolTable.insert(temp);
    return symbolTable;
};
bool contains(string symbol, unordered_map<string, int> symbolTable)
{
    unordered_map<string, int>::iterator got = symbolTable.find(symbol);
    return (got != symbolTable.end());
}
int getAddress(string symbol, unordered_map<string, int> symbolTable)
{
    unordered_map<string, int>::iterator temp = symbolTable.find(symbol);
    return temp->second;
}
