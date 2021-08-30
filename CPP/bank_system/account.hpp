#include <iostream>
#include <string>

class Account {
    std::string name;
    int id;
    double money;

    public:
        Account(std::string new_name, int new_id, double new_money=0);
        double add_money(double cash);
        double remove_money(double cash);
        double view_balance();

};