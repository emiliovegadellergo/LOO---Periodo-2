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