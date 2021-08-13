#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Prompt the user for a positive value between 1 and 8 until they enter a valid input.
    int height;
    do
    {
        height = get_int("Height: ");

        //printf("%i\n", height);
    }
    while (height < 1 || height > 8);

    // Build a left-aligned pyramid
    // for (int i = 0; i < height; i++)
    // {
    //     for (int j = 0; j <= i; j++)
    //     {
    //         printf("#");
    //     }
    //     printf("\n");
    // }

    // Build a Right-aligned pyramid
    for (int i = 0; i < height; i++)
    {
        // Mario Less
        for (int x = height - 1; x > i; x--)
        {
            printf(" ");
        }

        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }

        // Mario more
        printf("  ");

        for (int a = 0; a <= i; a++)
        {
            printf("#");
        }

        printf("\n");
    }
}