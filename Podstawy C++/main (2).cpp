#include <iostream>

using namespace std;

string imie, nazwisko, szkola;
float odleglosc, czas;
char PLI, PLN;
int wiek;

int main()
{
    cout << "podaj imie: ";
    cin >> imie;
    cout << "podaj nazwisko: ";
    cin >> nazwisko;
    cout << "podaj inicjaly: ";
    cin >> PLI;
    cin >> PLN;
    cout << "podaj wiek: ";
    cin >> wiek ;
    cout << "podaj nazwe szkoly: ";
    cin >> szkola ;
    cout << "podaj odleglosc od szkoly (w km): ";
    cin >> odleglosc ;
    cout << "podaj czas w ktory docierasz do szkoly (w minutach): ";
    cin >> czas;
    cout << endl;
    cout << "Mam na imie " << imie << " Na nazwisko  " << nazwisko << " moje inicjaly to " << PLI << PLN << endl;
    cout << " obecnie mam " << wiek << " lat. Wtym roku chodze do " << szkola << " moja szkola jest " << odleglosc << " od domu zwykle dojazd zajmuje mi "<< czas;
    cout << endl;

    return 0;
}
