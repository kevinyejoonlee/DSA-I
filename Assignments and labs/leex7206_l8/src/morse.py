"""
-------------------------------------------------------
Morse Code Definitions and Functions
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = '2022-01-15'
-------------------------------------------------------
"""

# In order by letters.
DATA1 = (('A', '.-'), ('B', '-...'), ('C', '-.-.'),
         ('D', '-..'), ('E', '.'), ('F', '..-.'),
         ('G', '--.'), ('H', '....'), ('I', '..'),
         ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'),
         ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
         ('S', '...'), ('T', '-'), ('U', '..--'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..'))

# In order by splitting.
DATA2 = (('M', '--'), ('F', '..-.'), ('T', '-'),
         ('C', '-.-.'), ('J', '.---'), ('P', '.--.'),
         ('W', '.--'), ('A', '.-'), ('D', '-..'),
         ('H', '....'), ('K', '-.-'), ('N', '-.'),
         ('R', '.-.'), ('U', '..--'), ('Y', '-.--'),
         ('B', '-...'), ('E', '.'), ('I', '..'),
         ('G', '--.'), ('L', '.-..'), ('O', '---'),
         ('Q', '--.-'), ('S', '...'), ('V', '...-'),
         ('X', '-..-'), ('Z', '--..'))

# In order by popularity.
DATA3 = (('E', '.'), ('T', '-'), ('A', '.-'),
         ('O', '---'), ('I', '..'), ('N', '-.'),
         ('S', '...'), ('H', '....'), ('R', '.-.'),
         ('D', '-..'), ('L', '.-..'), ('U', '..--'),
         ('C', '-.-.'), ('M', '--'), ('P', '.--.'),
         ('F', '..-.'), ('Y', '-.--'), ('W', '.--'),
         ('G', '--.'), ('B', '-...'), ('V', '...-'),
         ('K', '-.-'), ('J', '.---'), ('X', '-..-'),
         ('Z', '--..'), ('Q', '--.-'))


class ByLetter:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by letter attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByLetter object.
        Use: var = ByLetter(letter, code)
        -------------------------------------------------------
        Parameters:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Returns:
            A ByLetter object.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares source against target for equality.
        Object are equal if their letters match.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if letters match, False otherwise (boolean)
        -------------------------------------------------------
        """
        v = False
        
        if self.letter == target.letter:
            v = True
        
        return v


    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if source comes before target.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if source precedes target,
              False otherwise (boolean)
        -------------------------------------------------------
        """

        v = False
        
        if self.letter < target.letter:
            v = True
        
        return v

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if source precedes or is or equal to target.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if source precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """

        r = False
        
        if self.letter <= target.letter:
            r = True

        return r

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByLetter data.
        Use: print(source)
        Use: string = str(source)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of ByLetter (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.letter, self.code)


class ByCode:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by code attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByCode object.
        Use: var = ByCode(letter, code)
        -------------------------------------------------------
        Parameters:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Returns:
            A ByCode object.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code
        return

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares source against target for equality.
        Object are equal if their codes match.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if codes match, False otherwise (boolean)
        -------------------------------------------------------
        """

        v = False
        
        if self.code == target.code:
            v = True
        
        return v


    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if source comes before target.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if source precedes target,
              False otherwise (boolean)
        -------------------------------------------------------
        """

        v = False
        
        if self.code < target.code:
            v = True
        
        return v

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if source precedes or is or equal to target.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if source precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """

        v = False
        
        if self.code <= target.code:
            v = True
        
        return v
        

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByCode data.
        Use: print(source)
        Use: string = str(source)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of ByCode (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.code, self.letter)


def fill_letter_bst(bst, values):
    """
    -------------------------------------------------------
    Fills a BST with ByLetter Morse code letter/code pairs
    (Function must convert contents of values to ByLetter objects)
    Use: fill_letter(bst, values)
    -------------------------------------------------------
    Parameters:
        bst - a bst (BST)
        values - set of Morse code letter/code pairs (list of tuples)
    Returns:
        None
    -------------------------------------------------------
    """
    
    for i in values:
        var = ByLetter(i[0], i[1])
        bst.insert(var)

    return


def fill_code_bst(bst, values):
    """
    -------------------------------------------------------
    Fills a BST with ByCode Morse code letter/code pairs.
    (Function must convert contents of values to ByCode objects)
    Use: fill_letter(bst, values)
    -------------------------------------------------------
    Parameters:
        bst - a bst (BST)
        values - set of Morse code letter/code pairs (list of tuples)
    Returns:
        None
    -------------------------------------------------------
    """

    for i in values:
        var = ByCode(i[0], i[1])
        bst.insert(var)

    return


def encode_morse(bst, text):
    """
    -------------------------------------------------------
    Converts English text to Morse code
    Use: code = encode_morse(bst, text)
    -------------------------------------------------------
    Parameters:
        bst - Morse code bst sorted by letter (BST)
        text - English text to convert (str)
    Returns:
        result - Morse code version of text (str)
    -------------------------------------------------------
    """
    morse = ''
    
    for i in text:
        if i.isalpha():
            if i ==' ':
                morse += '\n'
            else:
                morse += bst.retrieve(ByLetter(i,'')).code
                morse +=' '
    return morse


def decode_morse(bst, code):
    """
    -------------------------------------------------------
    Converts Morse code to English text
    Use: text = decode_morse(bst, code)
    -------------------------------------------------------
    Parameters:
        bst - Morse code bst sorted by code (BST)
        code - Morse code to convert (str)
    Returns:
        result - English version of code (str)
    -------------------------------------------------------
    """
    
    result = ''
    
    for i in code.split():
        result += bst.retrieve(ByCode('',i)).letter
    
    
    return result
 
