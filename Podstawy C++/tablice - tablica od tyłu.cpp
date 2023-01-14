#include <iostream>

using namespace std;

int main()
{
    char tablica[8];

    for(int i=0; i!=8; i++){
        cin >> tablica[i];
    }

    for(int i=8; i==0; i--){
        cout << tablica[i];
    }
    return 0;
}
