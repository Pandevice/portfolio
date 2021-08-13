#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>



int main(void)
{
    // Prompt the user for a string of Text.
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text.
    int letterCounter = 0, wordCounter = 0, sentenceCounter = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] >= 'A' && text[i] <= 'z')
        {
            letterCounter++;
        }
        else if (text[i] == ' ')
        {
            wordCounter++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentenceCounter++;
        }
    }

    // There will always be one more word that needs to be added to the count becuase a sentence always ends in punctuation, not spaces.
    wordCounter++;

    // printf("Letters: %i\n", letterCounter);
    // printf("Words: %i\n", wordCounter);
    // printf("Sentences: %i\n", sentenceCounter);

    // Print as output "Grade X" where X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer
    float L = letterCounter / (float) wordCounter * 100;
    float S = sentenceCounter / (float) wordCounter * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;

    int grade = round(index);

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }

}