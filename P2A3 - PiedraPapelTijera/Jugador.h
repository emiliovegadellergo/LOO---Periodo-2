//Emilio Vega de Llergo Vargas
//00549955
//P2A3 Piedra Papel Tijera

#ifndef JUGADOR_H
#define JUGADOR_H

#include <string>
using namespace std;

class Jugador {

    private:
        string nombre;
        string eleccion;
    
    public:
        Jugador(string nombre);

        string getNombre();
        string getEleccion();

        void elegirJugada();
};

#endif