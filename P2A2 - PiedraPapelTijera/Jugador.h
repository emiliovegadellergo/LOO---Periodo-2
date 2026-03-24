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