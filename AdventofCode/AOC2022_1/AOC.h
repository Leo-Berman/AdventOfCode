#include<fstream>
#include<iostream>
#include<vector>
using namespace std;
#define default_file .\data.txt
#define defname "Bob"
#define errmsg cout<<"Error, please use program as: ./AOC2022_1.exe [filename.txt]"<<endl;
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

        elves* enthmost(elves* rightmost,int count){
        elves* tmp=rightmost;
        if(count == 1) return rightmost;
        if(rightmost == head){
            while(tmp->get_left()!=nullptr){
                count --;
                tmp = tmp->get_left();
                if(count == 1) return tmp;
            }
        }
        else{
            while(tmp->get_left()!= nullptr){
                count--;
                tmp = tmp->get_left();
                if(count == 1) return tmp;
            }
            return enthmost(rightmost->get_up(),count-1);
        }
        
    }


};