#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void exit(int status);

int main(int argc, string argv[1])
{
    // Check if the user typed only argument at the comamand-line
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        exit(1);
    }
    // else
    // {
    //     printf("Success\n");
    // }

    // Verify the user provided a string
    // printf("%s\n", argv[0]);
    // printf("%s\n", argv[1]);


    // Convert user's string integer
    int letterCounter = 0;
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (isdigit((char) argv[1][i]) == 0)
        {
            letterCounter++;
        }
    }

    int key = 0;
    if (letterCounter > 0)
    {
        printf("Usage: ./caesar key\n");
        exit(1);
    }
    else
    {
        //printf("Success\n");
        key = atoi(argv[1]);
        //printf("%i\n", key);
    }

    string plaintext = get_string("plaintext: ");
    // printf("%i\n", plaintext[0]);

    printf("ciphertext: ");

    string ciphertext = plaintext;

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {

        if (isalpha(plaintext[i]) != 0)
        {
            if (isupper(plaintext[i]) != 0)
            {
                // Covert to Alphanumeric Index
                ciphertext[i] = (plaintext[i] - 'A');

                // Convert to cipher text
                ciphertext[i] = (ciphertext[i] + key) % 26;

                // Covert back to Alphanumeric Index
                ciphertext[i] = ciphertext[i] + 'A';

                // Print Cipher character
                printf("%c", ciphertext[i]);
            }
            else
            {
                // Covert to Alphanumeric Index
                ciphertext[i] = (plaintext[i] - 'a');

                // Convert to cipher text
                ciphertext[i] = (ciphertext[i] + key) % 26;

                // Covert back to Alphanumeric Index
                ciphertext[i] = ciphertext[i] + 'a';

                // Print Cipher character
                printf("%c", ciphertext[i]);
            }
        }
        else
        {
            printf("%c", ciphertext[i]);
        }

    }

    printf("\n");

}