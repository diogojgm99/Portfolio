#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

void update_database(){
    string name;
    string username;
    string password;
    string line, word;
    vector<string> row;
    int count=0;

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
        if (name == username){
            count =1;
            row[1] = password;

            if (!fin.eof()) {
                for (int i = 0; i < row_size - 1; i++) {
  
                    // write the updated data
                    // into a new file 'reportcardnew.csv'
                    // using fout
                    fout << row[i] << ",";
                }
  
                fout << row[row_size - 1] << "\n";
            }
        }
        else {
            if (!fin.eof()) {
                for (int i = 0; i < row_size - 1; i++) {
  
                    // writing other existing records
                    // into the new file using fout.
                    fout << row[i] << ",";
                }
  
                // the last column data ends with a '\n'
                fout << row[row_size - 1] << "\n";
            }
        }
        if (fin.eof())
            break;
    }

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

int main(){
    // testing writing on csv
    ofstream myfile;
    myfile.open("data.csv");
    myfile << "adm,123,\n";
    myfile << "admin2,1233,\n";
    myfile << "admin4,1235,\n";
    myfile << "diogo,123,\n";
    myfile.close();
    update_database();
}