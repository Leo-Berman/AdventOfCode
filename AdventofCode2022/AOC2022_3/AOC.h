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
enum prio {
    a = 1,
    b = 2,
    c = 3,
    d = 4,
    e = 5,
    f = 6,
    g = 7,
    h = 8,
    i = 9,
    j = 10,
    k = 11,
    l = 12,
    m = 13,
    n = 14,
    o = 15,
    p = 16,
    q = 17,
    r = 18,
    s = 19,
    t = 20,
    u = 21,
    v = 22,
    w = 23,
    x = 24,
    y = 25,
    z = 26,
    A = 27,
    B = 28,
    C = 29,
    D = 30,
    E = 31,
    F = 32,
    G = 33,
    H = 34,
    I = 35,
    J = 36,
    K = 37,
    L = 38,
    M = 39,
    N = 40,
    O = 41,
    P = 42,
    Q = 43,
    R = 44,
    S = 45,
    T = 46,
    U = 47,
    V = 48,
    W = 49,
    X = 50,
    Y = 51,
    Z = 52,
};

// Part one
char FindDupes(string in1, string in2){
    char working;
    for(int i = 0; i<in1.size(); i++){
        for(int j = 0; j<in2.size();j++){
            if(in1[i] == in2[j]) working = in1[i];
        }
    }
    return working;
}
string*  splitstring(string in){
    string* ret = new string[2];
    if((in.size() % 2) == 1) {
        cout << "Odd Number of Elemnts In Line" << endl;
        return ret;
    }
    else{
        ret[0].append(in,0,in.size()/2);
        ret[1].append(in,in.size()/2,in.size());
    }
    return ret;
}
char FindTrupes(string in1, string in2,string in3){
    char working = '\0';
    for(int i = 0; i<in1.size(); i++){
        for(int j = 0; j<in2.size();j++){
            for(int k = 0; k<in3.size();k++){
                if((in1[i]==in2[j]) && (in1[i]==in3[k])) return(in1[i]); 
            }
        }
    }
    if(working = '\0'){
        cout << "No Trupes Found" << endl;
    }
    return working;
}