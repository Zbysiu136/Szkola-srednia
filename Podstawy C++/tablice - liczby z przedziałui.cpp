#include <iostream>

using namespace std;

int main()
{
    int x;
    int y;
    int tablica[5];


    y=0;
    for(int i=0; i<5; i++){
           cin>>x;
           tablica[i]=x;
    }
    for(int i=0; i<5; i++){
        if(tablica[i]>0 && tablica[i]<=4){
            cout << tablica[i] << " ";
            y=1;
        }

    }
            if(y==0)
            cout<< "zadna liczba nie spelnia warunku";
            else if(y==1)
            cout<< "te liczby nalezaly od przedzialu 0<x<5";


    return 0;
}

