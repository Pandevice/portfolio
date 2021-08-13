#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for input
    long cardNum, numCheck;
    int counter;
    long firstNum, secondNum, tempSecondNum;
    do
    {
        counter = 0;

        cardNum = get_long("Credit Card Number: ");

        numCheck = cardNum;

        while (numCheck != 0)
        {
            numCheck /= 10;
            //printf("Counter: %i\n", counter);
            //printf("%li\n", numCheck);
            counter++;
        }

        if (counter == 14)
        {
            counter -= 14;
        }

        if (counter < 13 || counter > 16)
        {
            break;
            printf("INVALID\n");
        }

    }
    while (counter < 13 || counter > 16);


    //printf("Counter: %i\n", counter);
    //printf("%li\n", numCheck);
    //printf("%li\n", cardNum);

    if (counter == 16) // when there is a credit card number entered with 16 digits;
    {
        firstNum = cardNum / 1000000000000000;
        //printf("firstNum: %li\n", firstNum);
        tempSecondNum = cardNum / 100000000000000;
        secondNum = tempSecondNum % 10;
        //printf("secondNum: %li\n", secondNum);
    }
    else if (counter == 15) // when there is a credit card number entered with 15 digits;
    {
        firstNum = cardNum / 100000000000000;
        //printf("firstNum: %li\n", firstNum);
        tempSecondNum = cardNum / 10000000000000;
        secondNum = tempSecondNum % 10;
        //printf("secondNum: %li\n", secondNum);
    }
    else if (counter == 13)
    {
        firstNum = cardNum / 1000000000000;
        //printf("firstNum: %li\n", firstNum);
        tempSecondNum = cardNum / 100000000000;
        secondNum = tempSecondNum % 10;
        //printf("secondNum: %li\n", secondNum);
    }

    // Calculate checksum (If valid continue. If invaild print invalid) - might require while loops within a if statement.
    long indivNum = cardNum;
    int evenCountCheck = counter;

    // A variable that will equal the sum of all the digits multplied by 2, a variable that will equal all the digits not divided by 2.
    int checkSumX2 = 0, checkSumNotX2 = 0;

    if (counter == 13 || counter == 15)
    {
        while (indivNum != 0)
        {

            //printf("0?: %i ", evenCountCheck);

            int digit = indivNum % 10;

            // Since the checksum starts with the second to last digit, if the counter is an odd digit, then we want
            if (evenCountCheck % 2 == 0)
            {
                int digitToAdd = digit * 2;
                // Include the digit in the initial checksum calc that is multiplied by 2.
                if (digitToAdd > 9)
                {
                    // THIS IS THE PROBLEM AREA!
                    int tempDigit = 0;
                    while (digitToAdd != 0)
                    {
                        tempDigit += digitToAdd % 10;
                        //printf("this should ultimately equal 5: %i\n ", tempDigit);
                        digitToAdd /= 10;
                    }

                    digitToAdd = tempDigit;

                }

                checkSumX2 += digitToAdd;
            }
            else
            {
                // Include the digit in the checksum that is not multiplied by 2.
                checkSumNotX2 += digit;
            }

            //printf("Checksum: %i ", checkSumX2);
            evenCountCheck--;

            //printf("Digit: %i\n", digit);

            indivNum /= 10;
        }
    }
    else //if counter == 16
    {
        while (indivNum != 0)
        {

            //printf("0?: %i ", evenCountCheck);

            int digit = indivNum % 10;

            // Since the checksum starts with the second to last digit, if the counter is an odd digit, then we want
            if (evenCountCheck % 2 != 0)
            {
                int digitToAdd = digit * 2;
                // Include the digit in the initial checksum calc that is multiplied by 2.
                if (digitToAdd > 9)
                {
                    // THIS IS THE PROBLEM AREA!
                    int tempDigit = 0;
                    while (digitToAdd != 0)
                    {
                        tempDigit += digitToAdd % 10;
                        //printf("this should ultimately equal 5: %i\n ", tempDigit);
                        digitToAdd /= 10;
                    }

                    digitToAdd = tempDigit;

                }

                checkSumX2 += digitToAdd;
            }
            else
            {
                // Include the digit in the checksum that is not multiplied by 2.
                checkSumNotX2 += digit;
            }

            //printf("Checksum: %i ", checkSumX2);
            evenCountCheck--;

            //printf("Digit: %i\n", digit);

            indivNum /= 10;
        }
    }
    //printf("Final ChecksumX2: %i \n", checkSumX2);

    int checkSum = checkSumX2 + checkSumNotX2;
    //printf("Final CheckSum: %i \n", checkSum);

    // Print AMEX, Mastercard, Visa, or Invalid
    if (checkSum % 10 != 0)
    {
        printf("INVALID\n");
    }

    else if ((checkSum % 10 == 0 && firstNum == 4 && counter == 16) || counter == 13)
    {
        printf("VISA\n");
    }
    else if ((checkSum % 10 == 0 && counter == 15 && firstNum == 3 && secondNum == 4) || secondNum == 7)
    {
        printf("AMEX\n");
    }
    else if ((checkSum % 10 == 0 && counter == 16 && firstNum == 5 && secondNum == 1) || secondNum == 2 || secondNum == 3 || secondNum == 4 || secondNum == 5)
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }
}