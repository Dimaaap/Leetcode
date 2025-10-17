def find_repeated_dna_sequences(s: str) -> list[str]:
    """
    The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
    For example, "ACGAATTCCG" is a DNA sequence.
    When studying DNA, it is useful to identify repeated sequences within the DNA.
    Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings)
    that occur more than once in a DNA molecule. You may return the answer in any order
    """
    res = []
    seen = set()
    for i in range(len(s)):
        if s[i:i+10] in seen and s[i:i+10] not in res:
            res.append(s[i:i+10])
        else:
            seen.add(s[i:i+10])
    return res

print(find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(find_repeated_dna_sequences("AAAAAAAAAAAAA"))