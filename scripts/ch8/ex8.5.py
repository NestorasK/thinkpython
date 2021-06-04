def rotate_letter(let, n):
    """Rotate a letter
    let: letter
    n: int

    Return the rotated letter
    """

    if let.isupper():
        anchor = ord('A')
    elif let.islower():
        anchor = ord('a')

    dist_from_anchor = ord(let) - anchor
    dist_rotate = (dist_from_anchor + n) % 26 + anchor
    rot_letter = chr(dist_rotate)
    return(rot_letter)


def rotate_word(string, int):
    """Rotate a word by int number of characters
    string: word to rotate
    n: int to rotate

    """

    rotated_str = ''
    for letter in string:
        rot_letter = rotate_letter(let=letter, n=int)
        rotated_str = rotated_str + rot_letter
    return rotated_str


print(rotate_word(string='melon', int=-10))

print(rotate_word(string='cheer', int=7))
