#include "account.hpp"
#include <iostream>
#include <string>


Account::Account(std::string new_name, int new_id, double new_money){

    name = new_name;
    id = new_id;
    money = new_money;
}

double Account::add_money(double cash){
    money += cash;
    return money;
}

double Account::remove_money(double cash){
    money -= cash;
    return money;
}