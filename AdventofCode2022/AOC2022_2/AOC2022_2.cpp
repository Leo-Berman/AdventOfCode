#include "AOC.h"
int main(int argc,char** argv){
    if(argc!=2){ // checks to see if there were enough arguments
        errmsg // prints error message
        return 0; // exits gracefully
    }
    
    ifstream new_file(argv[1]); // declares a new file 
    cout<<"File opened successfully"<<endl;
    elftree mytree;

    if(new_file.is_open()==false){
        errmsg // prints error message
        return 0; // exits gracefully
    }

    string line; // declares a string for the line to go into
    vector<char> tokens;
    int sum;

    while(getline(new_file,line)){
        tokens = tokenize(line);
        sum+=get_score(tokens);
    }
    cout << sum << endl;
return 0;
}