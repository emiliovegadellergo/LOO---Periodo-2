#include <iostream>
#include <Aminales.h>

Mamifero::Mamifero(string n, double p) {
    this -> nombre = n;
    this -> peso = p;
}

void Mamifero::setNombre(string n) {
    this -> nombre = n; 
}
string Mamifero::getNombre() {
    return this -> nombre;
}
string Mamifero::toString() {
    return "Mamifero\n [" + nombre + "," + to_string(peso) + " kg]";
}

/************************ CLASE GATO ********************/
Gato::Gato(string , double p, int b) : Mamifero (n, p) {
    this -> bigotes = b;
}

string Gato::toString() {
    return "GATO"+Mamifero::toString() + " [Bigotes:" + to_string(nBigotes) + "]";
}

/************************ CLASE VACA ********************/
Vaca::Vaca(string n, double p, double l) : Mamifero(n,p) {
    this -> litrosDeLeche = l;
}

void Vaca::calcularCantidadComida() {
    cout << this->peso * 0.03 << " kg de comida" << endl;
}
string Vaca::toString() {
    return "VACA" + Mamifero::toString() + " [Litros de leche:" + to_string(litrosDeLeche) + "]";
}

/************************ CLASE BALLENA ********************/
Ballena::Ballena(string n, double p) : mamifero(n,p) {
}
string Ballena::toString() {
    return "BALLENA" + Mamifero::toString();
}