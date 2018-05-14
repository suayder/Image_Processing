#include <iostream>

#define MATRIXSIZEI 8
#define MATRIXSIZEJ 8
#define QTGRAY 8

using namespace std;

int main(){
    int matrix[MATRIXSIZEI][MATRIXSIZEJ] = {{0,0,6,4,2,1,1,0},
                                            {0,3,3,2,2,0,0,0},
                                            {5,6,1,1,3,0,0,0},
                                            {5,5,6,0,0,0,1,2},
                                            {6,6,6,0,0,1,2,2},
                                            {4,4,4,1,7,0,0,0},
                                            {3,3,0,7,2,7,7,7},
                                            {8,1,1,7,2,2,0,6}};

    int coocurrenceMatrix[QTGRAY][QTGRAY] = {0};

    for (int i=0; i<MATRIXSIZEI; i++){
        for(int j=0;j<MATRIXSIZEJ; j++){
            if((i+1)<MATRIXSIZEI && (j+1)<MATRIXSIZEJ)
                coocurrenceMatrix[matrix[i][j]][matrix[i+1][j+1]]++;
        }
    }
    for (int i=0; i<QTGRAY; i++){
        for(int j=0;j<QTGRAY; j++){
            cout<<coocurrenceMatrix[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}