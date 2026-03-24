//Emilio Vega de Llergo Vargas
//00549955
//P2A3 Piedra Papel Tijera

#include "Juego.h"
#include <iostream>
using namespace std;

Juego::Juego(Jugador jugador1, Jugador jugador2)
    : jugador1(jugador1), jugador2(jugador2) {
}

void Juego::iniciar() {
    jugador1.elegirJugada();
    jugador2.elegirJugada();
}

void Juego::imprimirResultado() {
    cout << "Bienvenido al juego de piedra papel o tijera" << endl;
    cout << "El jugador 1 ha usado: " << jugador1.getEleccion() << endl;
    cout << "El jugador 2 ha usado: " << jugador2.getEleccion() << endl;
}

void Juego::definirGanador() {
    string e1 = jugador1.getEleccion();
    string e2 = jugador2.getEleccion();

    if (e1 == e2) {
        cout << "Empate" << endl;
    } else if (
        (e1 == "piedra"  && e2 == "tijera") ||
        (e1 == "tijera"  && e2 == "papel")  ||
        (e1 == "papel"   && e2 == "piedra")
    ) {
        cout << "El ganador es: Jugador 1" << endl;
    } else {
        cout << "El ganador es: Jugador 2" << endl;
    }
}