#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <vector>
#include <sstream>
#include <unistd.h>

using namespace std;

// function to update csv file - creating a account if not exists or update password
void update_database(){
    string name;
    string username;
    string password;
    string line, word;
    vector<string> row;
    int count=0;

    // reading and writing on respectives files
    fstream fin, fout;
    fin.open("data.csv", ios::in);
    fout.open("newdata.csv", ios::out);

    cout << "Enter the username: ";
    cin >> username;

    cout << "Enter the password: ";
    cin >> password;

    while(!fin.eof()){
        row.clear();
        getline(fin, line);
        stringstream s(line);
        while(getline(s, word, ',')) {
            row.push_back(word);
        }

        name = row[0];
        int row_size = row.size();
        // if there is already a account with that name, password will be updated
        if (name == username){
            count =1;
            // change the password of the username
            row[1] = password;

            if (!fin.eof()) {
                for (int i = 0; i < row_size - 1; i++) {
  
                    // write the updated data on newdata.csv
                    fout << row[i] << ",";
                }
                fout << row[row_size - 1] << "\n";
            }
        }
        // writing in the new file other usernames and passwords that already exist on data.csv
        else {
            if (!fin.eof()) {
                for (int i = 0; i < row_size - 1; i++) {
  
                    // writing other existing records
                    fout << row[i] << ",";
                }
                fout << row[row_size - 1] << "\n";
            }
        }
        //final of document
        if (fin.eof())
            break;
    }
    //if the username do not exists on csv file then will be created a new user with the given data above
    if (count == 0){
        fout << username << "," << password << '\n';
    }
    fin.close();
    fout.close();
    // removing the existing file
    remove("data.csv");
  
    // renaming the updated file with the existing file name
    rename("newdata.csv", "data.csv");
}

// menu terminal
int menu(){
    int option;

    cout << "Choose one of the options:\n";
    cout << "1- Create/Update Account\n";
    cout << "2- Log in\n";
    cout << "3- Exit\n";
    cin >> option;
    return option;
}

// login in the system 
bool log_in(){
    int count = 0;
    string name;
    string username;
    string password;
    string line, word;
    vector<string> row;

    fstream fin;
    fin.open("data.csv", ios::in);

    cout << "Enter the username: ";
    cin >> username;

    cout << "Enter the password: ";
    cin >> password;

    while(!fin.eof()){
        row.clear();
        getline(fin, line);
        stringstream s(line);
        while(getline(s, word, ',')) {
            row.push_back(word);
        }

        name = row[0];
        int row_size = row.size();
        // if the username and password are found on csv file then there is a sucessfull login 
        if(name == username && password == row[1]){
            count = 1;
            cout << "Succesfull login\n";
            cout << "Welcome "<< name<<'\n';
            return true;
        }
    }
    if(count == 0){
        cout << "Wrong password or username\n";
    }
    return false;
}

int main(){
    bool flag = true;
    bool login = false;
    while (flag == true){
        int option = menu();
        switch (option)
        {
        case 1:
            update_database();
            break;
        case 2:
            login = log_in();
            if(login == true){
                cout << "Exiting in five seconds. Goodbye\n";
                sleep(5);
                flag = false;
            }
            break;
        case 3:
            flag = false;
            break;
        default:
            break;
        }
    }
}