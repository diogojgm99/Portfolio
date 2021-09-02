#include "account.hpp"
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

void create(){
    std::string first_name;
    std::string last_name;
    std::string name;
    int id;
    double money;
    //Account user;

    std::cout << "Bank Management System\n";

    std::cout << "Enter your first name: \n";
    std::cin >> first_name;
    std::cout << "Enter your last name: \n";
    std::cin >> last_name;
    name = first_name + " " + last_name;

    std::cout << "Insert the value of cash that you want to save in the bank.\n";
    std::cin >> money;

    srand((unsigned) time(0));
    for (int index = 0; index < 5; index++)
        id = (rand() % 100) + 1;

    //Account user(name, id, money);
     
    // std::cout << "Name: " << user.name<<'\n';
    // std::cout << "Account ID: " << user.id<<'\n';
    // std::cout << "Money: " <<user.money<<'\n';

}

std::string create_name(){
    std::string first_name;
    std::string last_name;
    std::string name;

    std::cout << "Enter your first name: \n";
    std::cin >> first_name;
    std::cout << "Enter your last name: \n";
    std::cin >> last_name;
    name = first_name + " " + last_name;
    return name;
}

int create_money(){
    int money = 0;
    std::cout << "Insert the value of cash that you want to save in the bank.\n";
    std::cin >> money;
    return money;
}

int main(){
    std::string name="";
    int id=0;
    double money=0;
    Account user;
    int option = 0;
    bool flag = true;
    while(flag == true){
        std::cout << " BANK MANAGEMENT SYSTEM\n\n";
        std::cout << " 1- Criar conta\n";
        std::cout << " 2- Ver conta\n";
        std::cout << " 3- Adicionar dinheiro na conta\n";
        std::cout << " 4- Remover dinheiro na conta\n";
        std::cout << " 5- sair\n";
        std::cin >> option;

        switch (option)
        {
        case 1:
            name = create_name();
            money = create_money();
            srand((unsigned) time(0));
            for (int index = 0; index < 5; index++)
                id = (rand() % 100) + 1;
            
            user.create(name, id, money);
            std::cout << "Name: " << user.name<<'\n';
            std::cout << "Account ID: " << user.id<<'\n';
            std::cout << "Money: " <<user.money<<'\n';
            break;
        case 2:
            money=user.view_balance();
            std::cout << "Account Balance: " << money <<'\n';
            break;
        case 3:
            std::cout << "Insert the value of cash that you want to save in the bank.\n";
            std::cin >> money;
            money = user.add_money(money);
            std::cout << "Account Balance: " << money <<'\n';
            break;
        case 4:
            std::cout << "Insert the value of cash that you want to remove from the bank.\n";
            std::cin >> money;
            money = user.remove_money(money);
            std::cout << "Account Balance: " << money <<'\n';
            break;
        case 5:
            flag = false;
            break;
        default:
            std::cout << "Insira uma opção válida\n";
            break;
        }
    }
}