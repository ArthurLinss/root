#include "header/head.h"            //Here. Again player.h must be in the current directory. or use relative or absolute path to it.
using namespace std;
#include <iostream>

int main()
{
	// call ty function
    int p = playerSprite();  

    // call toy class
    A2DD classm = A2DD(2,2);
    int summo = classm.getSum();
    std::cout << "summo: " << summo << std::endl;
}