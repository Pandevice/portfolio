#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Defining population variables and counter variable i (for number of years).
    int startPop, endPop, i;

    // TODO: Prompt for start size
    do
    {
        startPop = get_int("Please enter a start population greater than 9: ");

        printf("%i\n", startPop);
    }
    while (startPop < 9);

    // TODO: Prompt for end size
    do
    {
        endPop = get_int("Please enter an ending population size greater than your desired starting population: ");

        printf("%i\n", endPop);
    }
    while (endPop < startPop);

    // TODO: Calculate number of years until we reach threshold
    for (i = 0; startPop < endPop; i++)
    {
        startPop = startPop + (startPop / 3) - (startPop / 4);
    }

    // TODO: Print number of years
    printf("Years: %i\n", i);
}