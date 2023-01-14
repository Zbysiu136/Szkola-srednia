#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    float a, b, c;
    float suma;
    float x1, x2;

    cout << "To jest program obliczajacy pierwiastki rownania kwadratowego." << endl;
    cout << "Podaj wartosc - a" << endl;
    cin >> a;
   
   if(a!=0){
        cout << "Podaj wartosc - b" << endl;
        cin >> b;
        cout << "Podaj wartosc - c" << endl;
        cin >> c;

        suma = pow(b,2) - 4*a*c;
        
        if (suma > 0){
        x1 = ((-1*b) - sqrt(suma)) / 2*a;
        x2 = ((-1*b) + sqrt(suma)) / 2*a;
        }

        if (suma == 0){
        x1 = (-1*b) / 2*a;
        x2 = 9999;  //może być źle
        }

        if (suma < 0){
            x1 = 1111; //może być źle
            x2 = 1111; //może być źle
        }

        cout << "Zadeklarowane zmienne to " << a << ", " << b << ", " << c << endl ;
        cout << "Miejscami zerowymi fukcji sa wartosci " << "x1=" << x1 << ", x2=" << x2 << endl;
        cout << "Suma to " << suma;
    }
    
    else
    cout << "Rownanie nie jest rownaniem kwadratowym";


    return 0;
}
