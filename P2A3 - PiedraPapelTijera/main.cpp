//Emilio Vega de Llergo Vargas
//00549955
//P2A3 Piedra Papel Tijera

#include "Juego.h"
#include <cstdlib>
#include <ctime>

int main()
{

    srand(time(0));

    Jugador jugador1("Jugador 1");
    Jugador jugador2("Jugador 2");

    Juego juego(jugador1, jugador2);

    juego.iniciar();
    juego.imprimirResultado();
    juego.definirGanador();

    return 0;
}