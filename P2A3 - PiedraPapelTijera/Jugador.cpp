//Emilio Vega de Llergo Vargas
//00549955
//P2A3 Piedra Papel Tijera

#include "Jugador.h"
#include <cstdlib>
#include <ctime> 


Jugador::Jugador(string nombre) {
    this->nombre = nombre;
}

string Jugador::getNombre() {
    return nombre;
}

string Jugador::getEleccion() {
    return eleccion;
}

void Jugador::elegirJugada() {
    int random = rand() % 3;  // 0, 1 o 2

    if (random == 0) {
        eleccion = "piedra";
    } else if (random == 1) {
        eleccion = "papel";
    } else {
        eleccion = "tijera";
    }
}