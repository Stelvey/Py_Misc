import csv
import sys


def main():

    # TODO: Check for command-line usage
    if not len(sys.argv) == 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    databasef = open(sys.argv[1])
    database = csv.DictReader(databasef)

    # TODO: Read DNA sequence file into a variable
    sequencef = open(sys.argv[2])
    sequence = sequencef.read()

    # TODO: Find longest match of each STR in DNA sequence
    # Extract subsequences of interest ... in a very f'd up way
    subsequences = database.fieldnames.copy()
    del subsequences[0]

    # Compute STR counts, putting everything in a dict
    longest = {}
    for subsequence in subsequences:
        longest[subsequence] = longest_match(sequence, subsequence)
    sequencef.close()

    # TODO: Check database for matching profiles
    for row in database:
        match = 0
        for str in longest:
            if int(row[str]) == longest[str]:
                match += 1
            if match == len(subsequences):
                print(row["name"])
                databasef.close()
                return

    print("No match")
    databasef.close()
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
