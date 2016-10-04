/**
Alexis Valois-Adamowicz
#####VALA10049105#####
**/
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

void CoinSupGauche(int i, int j)
{
	int x = 288;
	int y = 288;

	x = x + (i * 32);
	y = y - (i * 16);

	x = x - (j * 32);
	y = y - (j * 16);

	printf("Position du point : (%d , %d)\n\n", x, y);
}

int main (int argc, char const *argv[])
{
	CoinSupGauche(4,2);
}