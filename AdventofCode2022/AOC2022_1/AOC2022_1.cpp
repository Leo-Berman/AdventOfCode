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
    int elfnum = 0;
    bool newelf = true;
    elves* tmp;
    
    while(getline(new_file,line)){
        if(newelf == true){ // checks to see if its a new elf
            elfnum++; // increments the elf number
            tmp = new elves(elfnum); // creates a  new elf
            tmp->add_item(stoi(line)); // adds a new item to the elf
            newelf = false; // says that it is no longer a new left
        }
        else if(line.empty()){ // checks if line is empty
            newelf = true; // sets newelft = true
            mytree.add_node(tmp);

        }
        else{
            tmp->add_item(stoi(line)); // adds a new item in
        }
            
    }
    mytree.add_node(tmp);
    elves* right = mytree.most(mytree.get_head());
    cout << right->total_calories() << endl;
    elves* two = mytree.enthmost(right,2);
    cout << two->total_calories() << endl;
    elves* three = mytree.enthmost(right,6);
    cout << three->total_calories() << endl;
    return 0;
}

