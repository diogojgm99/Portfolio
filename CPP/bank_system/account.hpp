#include <iostream>
#include <string>

class Account {
    public:
        std::string name;
        int id;
        double money;

        Account(std::string new_name="", int new_id=0, double new_money=0);
        void create(std::string new_name, int new_id, double new_money);
        double add_money(double cash);
        double remove_money(double cash);
        double view_balance();

};