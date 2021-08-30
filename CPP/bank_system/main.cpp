#include "account.hpp"
#include <iostream>
#include <string>

std::string creating(){
    std::string first_name;
    std::string last_name;
    std::string name;

    std::cout << "Enter your first name: \n";
    std::cin >> first_name;
    std::cout << "Enter your last name: \n";
    std::cin >> last_name;
    name = first_name + " " + last_name;
    std::cout << name << "\n";
    return name;
}

int creating_id(){
    int id=0;
    return id;
}


int main(){
    std::string name;
    int id;
    double money;

    std::cout << "Bank Management System\n";

    name = creating();
    id = creating_id();

    std::cout << "Insert the value of cash that you want to save in the bank.\n";
    std::cin >> money;
    std::cout << name;

    Account user(name, id, money);
    

}