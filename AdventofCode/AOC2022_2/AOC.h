#include<fstream>
#include<iostream>
#include<vector>
#include<string.h>
#include<cstring>
#include<map>
using namespace std;
#define default_file .\data.txt
#define defname "Bob"
#define errmsg cout<<"Error, please use program as: ./AOC2022_2.exe [filename.txt]"<<endl;
enum cases{AX = 3, AY = 4, AZ = 8, BX = 1, BY = 5, BZ = 9, CX = 2, CY = 6, CZ = 7,def = 0}; // settings cases using values in ADOC 2022 Day 2 Part 2

class elves{
    
private:
    vector<int> items;
    int elfnum;
    elves* left = nullptr;
    elves* right = nullptr;
    elves* up = nullptr;
public:
        
    void add_item(int input){ //
        items.push_back(input);
    }

    elves(int in){ // default constructor
        elfnum = in; // setting the elfnum
    }

    int total_calories(){
        int count = 0;
        for(int i = 0; i < items.size() ; i++){
            count+=items[i];
        }
        return count;
    }

    elves* get_left(){
        return left;
    }
    elves* get_right(){
        return right;
    }
    elves* get_up(){
        return up;
    }
    void insert_left(elves* in){
        left = in;
    }
    void insert_right(elves* in){
        right = in;
    }
    void set_up(elves* parent){
        up = parent;
    }

};

class elftree{
private:
    elves* head;
    int numofelves = 0;
public:
    void add_node(elves* input){ // maybe works
        elves* tmp = head;
        bool cycle = true;
        while(cycle == true){
            if(numofelves == 0){
                head = input;
                numofelves++;
                cycle = false;
            }
            // If less than tmp
            else if((input->total_calories() < tmp->total_calories())){
                if(tmp->get_left() == nullptr){
                    input->set_up(tmp);
                    tmp->insert_left(input);
                    numofelves++;
                    cycle = false;
                }
                else if(tmp->get_left()!=nullptr){
                    tmp = tmp->get_left();
                }
            }

            // If greater than tmp
            else if((input->total_calories() >= tmp->total_calories())){
                if(tmp->get_right() == nullptr){
                    input->set_up(tmp);
                    tmp->insert_right(input);
                    numofelves++;
                    cycle = false;
                }
                else if(tmp->get_right()!=nullptr){
                    tmp = tmp->get_right();
                }

            }
        }
    }

    elves* get_head(){
        return head;
    }

    elves* least(){
        elves* tmp2 = head;
        while(tmp2->get_left()!=nullptr){
            tmp2 = tmp2->get_left();
        }
        return tmp2;
    }

    elves* most(elves* tmp){
        elves* tmp2 = tmp;
        while(tmp2->get_right()!=nullptr){
            tmp2 = tmp2->get_right();
        }
        return tmp2;
    }

    int most3(){
        elves* tmp2 = most(head);
        int sum = 0;
        sum+=tmp2->total_calories();
        tmp2 = tmp2->get_up();
        sum+=tmp2->total_calories();
        if(tmp2->get_left()!=nullptr){
            tmp2 = most(tmp2->get_left());
        }
        else{
            tmp2 = tmp2->get_up();
        }
        sum+=tmp2->total_calories();
        return sum;
    }


};

vector <char> tokenize(string in){ //Tokenizing Strings By Spaces
    string s = in;
    string delimiter = " ";
    vector<char> ret;
    ret.push_back(in[0]);
    ret.push_back(in[2]);
    return ret;
}

cases get_case(string in){
    if     (in == "AX") return AX; // Elf Rock Me Scissor       L 0+3 = 3
    else if(in == "AY") return AY; // Elf Rock Me Rock          D 3+1 = 4
    else if(in == "AZ") return AZ; // Elf rock Me Paper         W 6+2 = 8
    else if(in == "BX") return BX; // Elf paper Me rock         L 0+1 = 1
    else if(in == "BY") return BY; // Elf paper Me Paper        D 3+2 = 5
    else if(in == "BZ") return BZ; // Elf paper Me Scissor      W 6+3 = 9
    else if(in == "CX") return CX; // Elf scissor Me Paper      L 0+2 = 2
    else if(in == "CY") return CY; // Elf scissor Me Scissor    D 3+3 = 6
    else if(in == "CZ") return CZ; // Elf scissor Me Rock       W 6+1 = 7
    else{
        errmsg
        return def;
    }

}

int get_score(vector<char> in){
    string s; // Putting the tokenized characters into a string
    s.push_back(in[0]);
    s.push_back(in[1]);

    cases mycase = get_case(s); // gives the string to return the case
    return mycase;
}

