//Emilio Vega de Llergo Vargas
//00549955
//P2A3 Piedra Papel Tijera

#ifndef JUEGO_H
#define JUEGO_H

#include "Jugador.h" 

class Juego {
private:
    Jugador jugador1;
    Jugador jugador2;

public:
    Juego(Jugador jugador1, Jugador jugador2);

    void iniciar();

    void definirGanador();

    void imprimirResultado();
};

#endif