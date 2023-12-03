#include "MyFuncts.h"
#include<fstream>
#include<iostream>
#include<vector>
#include<string.h>
#include<cstring>
#include<map>
using namespace std;
#define default_file .\data.txt
#define defname "Bob"
#define errmsg cout<<"Error, please use program as: ./AOC2022_3.exe [filename.txt]"<<endl;

// Day 1 Function
bool isapair(string in){
    int i =0;
    string workin;
    while(in[i]!='-'){
        workin+=in[i];
        i++;
    }
    int a = stoi(workin);
    workin.clear();
    i++;
    while(in[i]!=','){
        workin+=in[i];
        i++;
    }
    i++;
    int b = stoi(workin);
    workin.clear();
    while(in[i]!='-'){
        workin+=in[i];
        i++;
    }
    i++;
    int c = stoi(workin);
    workin.clear();
    while(in[i]){
        workin+=in[i];
        i++;
    }
    int d = stoi(workin);
    if(((a<=c)&(b>=d))|((c<=a)&(d>=b))) return true;
    else return false;

    return false;
}

// Day 2 function
bool isapair2(string in){
    int i =0;
    string workin;
    while(in[i]!='-'){
        workin+=in[i];
        i++;
    }
    int a = stoi(workin);
    workin.clear();
    i++;
    while(in[i]!=','){
        workin+=in[i];
        i++;
    }
    i++;
    int b = stoi(workin);
    workin.clear();
    while(in[i]!='-'){
        workin+=in[i];
        i++;
    }
    i++;
    int c = stoi(workin);
    workin.clear();
    while(in[i]){
        workin+=in[i];
        i++;
    }
    int d = stoi(workin);
    vector<int> indexes1;
    vector<int> indexes2;
    for(int i = a; i<= b; i++){
        indexes1.push_back(i);
    }
    for(int i = c; i<= d; i++){
        indexes2.push_back(i);
    }
if(indexes1.size()>=indexes2.size()){
    for(int i = 0; i<indexes1.size();i++){
        for(int j = 0; j<indexes2.size();j++){
            if(indexes1[i]==indexes2[j]) return true;
        }
    }
}
if(indexes1.size()<indexes2.size()){
    for(int i = 0; i<indexes2.size();i++){
        for(int j = 0; j<indexes1.size();j++){
            if(indexes2[i]==indexes1[j]) return true;
        }
    }
}

return false;


}