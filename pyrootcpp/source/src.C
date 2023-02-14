#include "../header/head.h"  // player.h must be in the current directory. or use relative or absolute path to it. e.g #include "include/player.h"
#include <iostream>
using namespace std;

#include "TH1F.h"

int playerSprite(){
	std::cout << "hello it works" << std::endl;

	TH1F* histo = new TH1F("histo","histo",100,10,10);
	int entries = histo->GetEntries();
	std::cout << "entries: " << entries << std::endl;

	return 1;
}

// add body to toy class
A2DD::A2DD(int x, int y) {
	gx = x;
	gy = y;
}
// declare member function
int A2DD::getSum(){
	return gx + gy;
}


