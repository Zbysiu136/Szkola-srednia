#include <iostream>

using namespace std;

int main()
{
    int tab[] = {58, 94, 8, 62, 52, 8, 52, 36, 68, 79, 80};
    int n = sizeof(tab) / 4; //tablice c++ są 4 bitowe, a sizeof określa ilość bitów

    int suma = 0;
    int x = 20;
    int y = 1;

    if (x > y)
    {
        int xq = x;
        x = y;
        y = xq;
    }

    cout << "liczby spelniajace warunek to: ";

    for (int i = 0; i < n; i++)
    {
        if (tab[i] > x && tab[i] < y)
        {
            cout << tab[i] << ", ";
            suma = suma + 1;
        }
    }
    cout << " bylo ich " << suma;

    if (x < y)
        cout << endl
             << "Przedział liczbowy to " << x << " " << y;

    if (x > y)
        cout << endl
             << "Przedzial liczbowy to " << y << "-" << x;
	return 0;
}