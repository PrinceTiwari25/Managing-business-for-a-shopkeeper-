#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream myfile("inventory.txt");

    if (myfile.is_open()) {
        myfile << "Date\tItem\tPurchase Price\tSelling Price\tQuantity\n";
        myfile << "2025-04-26\tPen\t5\t10\t50\n";
        myfile << "2025-04-26\tNotebook\t20\t35\t30\n";
        myfile.close();
        cout << "Inventory saved to file successfully!" << endl;
    }
    else {
        cout << "Unable to open file!" << endl;
    }

    return 0;
}
