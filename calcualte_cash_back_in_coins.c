#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // Promting Cashier for a change amount.
    float cash;
    do
    {
        cash = get_float("Change owed: ");
    }
    while (cash < 0);

    //printf("Change owed: %2.2f\n", cash);

    int cents = round(cash * 100);

    //printf("Amount in cents: %i\n", cents);

    // Tracking the number of coins the Cashier should use.
    int coin = 0;
    while (cents >= 25)
    {
        cents = cents - 25;
        coin++;
    }

    //printf("cash after .25--> %f\n", cash);
    //printf("coin after .25--> %i\n", coin);

    while (cents >= 10)
    {
        cents = cents - 10;
        coin++;
    }

    while (cents >= 5)
    {
        cents = cents - 5;
        coin++;
    }

    while (cents >= 1)
    {
        cents = cents - 1;
        coin++;
    }

    printf("Total coins: %i\n", coin);

}