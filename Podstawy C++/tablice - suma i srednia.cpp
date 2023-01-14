#include <iostream>

using namespace std;

int main()
{
    int suma, srednia, n;

    cout << "podaj n ";
    cin >> n;
    cout << endl;
    int tablica[n];

    for(int i=0; i!=n; i++){
        cin >> tablica[i];
    }

    for (int i=0; i!=n; i++){
        suma = suma + tablica[i];
        srednia = suma/n;
    }

    cout << suma << endl << srednia;
    return 0;
}
