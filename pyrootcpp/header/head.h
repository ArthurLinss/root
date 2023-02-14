#ifndef HEAD_H    // To make sure you don't declare the function more than once by including the header multiple times.
#define HEAD_H


// toy function
int playerSprite();

// toy class
class A2DD { 
    int gx; 
    int gy;
public:
    // constructtor
    A2DD(int x, int y);
    // member function
    int getSum();
};

#endif