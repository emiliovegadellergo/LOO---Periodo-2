#include <iostream>
#include "Animales.h"
using namespace std;

int main()
{
    Gato mitch("Mitch", 6.7, 20);
    Vaca nani("Nani", 350, 20);
    Ballena titi("Titi", 200000);

    cout << mitch.toString() << endl;

    cout << nani.toString() << endl;
    nani.calcularCantidadComida();

    cout << titi.toString() << endl;
}