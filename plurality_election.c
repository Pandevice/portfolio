#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // printf("%i\n", argc);
    // printf("%s\n", argv[1]);
    //printf("%c\n", strlen(argv));

    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        // this takes in the 2nd string the user types in at the commandline.
        // Becuase argv[0] would be ./plurality (i.e. the name of this program.)
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            //printf("%s\n", name);
            candidates[i].votes += 1;
            // print statement to help keep track of the votes
            // int n = 0;
            // do
            // {
            //     printf("%s %i\n", candidates[n].name, candidates[n].votes);
            //     n += 1;
            // }
            // while (n < candidate_count);
            return true;
        }
    }

    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    int n = 0;

    //
    for (int i = 0; i < candidate_count; i++)
    {
        // *Troubleshoot*
        if (n < candidates[i].votes)
        {
            n = candidates[i].votes;
        }
    }

    int highestVoteCount = n;

    // printf("The highest Vote count is: %i\n", highestVoteCount);

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == highestVoteCount)
        {
            printf("%s\n", candidates[i].name);
        }
    }

    return;
}

