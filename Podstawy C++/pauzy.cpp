#include <iostream>

using namespace std;

int main() {

cout<<"Program prezentuje działanie instrukcji break.";
int i=0;
for (i-0; i<10; i++) {
cout<<"\nNumer powtorzenia petli i="<<i; 
cout<<"\nCzy chcesz juz zakonczyc petle (t/n)? ";
char czy;
cin >> czy;
if (czy=='t') break;}
if (i==10)
cout<<"\n\nWykonales 10 powtorzen!";
else
cout<<"\n\nPrzerwales petle przez break";
return 0;
}