def check_two_chessboards(coordinate1: str, coordinate2: str) -> bool:
    nums = tuple(i for i in range(1, 9))
    letters = "abcdefgh"
    black_squares = []
    white_squares = []
    for i in range(len(nums)):
        for letter_i in range(len(letters)):
            if nums[i] % 2 != 0 and letter_i % 2 == 0:
                black_squares.append(str(f'{letters[letter_i]}{nums[i]}'))
            elif nums[i] % 2 != 0 and letter_i % 2 != 0:
                white_squares.append(str(f'{letters[letter_i]}{nums[i]}'))
            elif nums[i] % 2 == 0:
                if letter_i % 2 == 0:
                    white_squares.append(str(f'{letters[letter_i]}{nums[i]}'))
                elif letter_i % 2 != 0:
                    black_squares.append(str(f'{letters[letter_i]}{nums[i]}'))
    if coordinate1 in white_squares and coordinate2 in white_squares:
        return True
    elif coordinate1 in black_squares and coordinate2 in black_squares:
        return True
    return False

print(check_two_chessboards("a1", "c3"))
print(check_two_chessboards("a1", "h3"))