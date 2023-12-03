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
    int count = 0;
    while(getline(new_file,line)){

        // Day 1
        if(isapair2(line)) count++;
        
    }
    cout << count << endl;

    return 0;
}

