#include "AOC.h"

int main(int argc,char** argv){
    if(argc!=2){ // checks to see if there were enough arguments
        errmsg // prints error message
        return 0; // exits gracefully
    }
    
    ifstream new_file(argv[1]); // declares a new file 
    cout<<"File opened successfully"<<endl;

    if(new_file.is_open()==false){
        errmsg // prints error message
        return 0; // exits gracefully
    }

    string line; // declares a string for the line to go into
    
    map<char,prio> mymap;{
    mymap['a'] = a;
    mymap['b'] = b;   
    mymap['c'] = c;
    mymap['d'] = d;
    mymap['e'] = e;
    mymap['f'] = f;
    mymap['g'] = g;
    mymap['h'] = h;
    mymap['i'] = i;
    mymap['j'] = j;
    mymap['k'] = k;
    mymap['l'] = l;
    mymap['m'] = m;
    mymap['n'] = n;
    mymap['o'] = o;
    mymap['p'] = p;
    mymap['q'] = q;
    mymap['r'] = r;
    mymap['s'] = s;
    mymap['t'] = t;
    mymap['u'] = u;
    mymap['v'] = v;
    mymap['w'] = w;
    mymap['x'] = x;
    mymap['y'] = y;
    mymap['z'] = z;
    mymap['A'] = A;
    mymap['B'] = B;
    mymap['C'] = C;    
    mymap['D'] = D;
    mymap['E'] = E;
    mymap['F'] = F;
    mymap['G'] = G;
    mymap['H'] = H;
    mymap['I'] = I;
    mymap['J'] = J;
    mymap['K'] = K;
    mymap['L'] = L;
    mymap['M'] = M;
    mymap['N'] = N;
    mymap['O'] = O;
    mymap['P'] = P;
    mymap['Q'] = Q;
    mymap['R'] = R;
    mymap['S'] = S;
    mymap['T'] = T;
    mymap['U'] = U;
    mymap['V'] = V;
    mymap['W'] = W;
    mymap['X'] = X;
    mymap['Y'] = Y;
    mymap['Z'] = Z;
    }
    int count1 = 0;
    int count2 = 0;
    int counter=0;
    vector<string> mystrings;
    while(getline(new_file,line)){
        //part one 
        string* myline = splitstring(line);
        char dupe = FindDupes(myline[0],myline[1]);
        count1 = count1 + mymap[char(dupe)];
        
        // part two
        counter ++;
        mystrings.push_back(line);
        if(counter == 3){
            count2 = count2 + mymap[FindTrupes(mystrings[0],mystrings[1],mystrings[2])];
            mystrings.clear();
            counter = 0;
        }
        
    }
    
    cout << "Day 1 = " << count1 << endl;
    cout << "Day 2 = " << count2 << endl;

    return 0;
}

