//Jared Johnstun
//Date created: 12/4/2024
//Purpose: Solve Diff equation and write to file

//import needed libraries and declare standards
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;
using std::cout;
using std::cin;
using std::endl;
std::ofstream dataOut;
std::stringstream name;

//declare float constants for circuit elements
const float R = 1078.;
const float C = 0.0000000004;
const float H = 0.0205;
const float Vd0 = 1.3;
const float freq = 40000;

//declare circuit-relevant constants
float t = 0.;
float i = 0.;
float q = 0.;

//declare other needed quantities
const double pi = std::acos(-1);
std::vector<float> ODEVector(3, 0);


float Vd(float t0) {
    float V = Vd0*sin(2*pi*freq*t0);
    return V;
}

float Vr(float i0) {
    float vr = R*i0;
    return vr;
}

float Vc(float q0) {
    float vc = q0/C;
    return vc;
}


float f(float t0, float q0, float i0 ) {
    float di = (Vd(t0) - (q0/C) - (R*i0)/H);
    return di;
}

void ODE2step(float t0, float q0, float i0, float dt) {
    t = t0 + dt;
    q = q0 + (dt*i0);
    i = i0 + dt*f(t0, q0, i0);
    ODEVector = {t, q, i};
}

void solveODE(float t0){
    //we need to generate the solution for 60 periods in 500 steps, find what dt should be
    float T = (1./freq);
    float dt0 = (T/100);

    //setup name for transient file and open it
    name << "freq - " << freq << " - trans.txt";
    string filename = name.str();
    dataOut.open(filename);

    //write header for transient file
    dataOut << "t" << std::setw(20) << "Vd" << std::setw(20)
            << "VR" << std::setw(20) << "VC" << std::setw(20)
            << "VL" << std::endl;

    //begin solving equation
    for(int j = 0; j<6000; j++) {
        //For the first 6 periods, write to the transient file
        if (j<=600) {
            dataOut << std::setprecision(15) << std::fixed << std::left << std::setw(20)<< t << std::setw(20) << Vd(t) << std::setw(20)
                    << Vr(i) << std::setw(20) << Vc(q) << std::setw(20) << f(t, q, i) << std::endl;
        
        } else if (j == 601) { // after 6th period close the transient file and open the steady file
            dataOut.close();
            name.str("");
            name << "freq - " << freq << " - steady.txt";
            filename = name.str();
            dataOut.open(filename);
            
            //write the header to the steady file
            dataOut << std::setw(20) << "t" << std::setw(20) << "Vd" << std::setw(20)
                    << "VR" << std::setw(20) << "VC" << std::setw(20)
                    << "VL" << std::endl;


        } else if (j>=5400) { //write to the steady file
            dataOut << std::setprecision(15) << std::fixed << std::left << std::setw(20)<< t << std::setw(20) << Vd(t) << std::setw(20)
                    << Vr(i) << std::setw(20) << Vc(q) << std::setw(20) << f(t, q, i) << std::endl;
        }
        ODE2step(t, q, i, dt0);

    }

}


int main() {
    solveODE(0.);
    return 0;
}