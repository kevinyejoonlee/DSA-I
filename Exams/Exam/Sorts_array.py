"""
-------------------------------------------------------
Array versions of various sorts.
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = "2022-04-06"
-------------------------------------------------------
"""


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of array-based sort operations.
    -------------------------------------------------------
    """
    k = "abcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def radix_string_sort(strings):
        """
        -------------------------------------------------------
        Performs a string radix sort.
        Use: Sorts.radix_string_sort(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns‌‌​​​‌‌​:
            None
        -------------------------------------------------------
        """

        k = "abcdefghijklmnopqrstuvwxyz"
        
        if len(strings) > 0:
            maxlen = 0
            for strng in strings:
                if len(strng) > maxlen:
                    maxlen = len(strng)
            
            index = maxlen - 1
            
            while index >= 0:
                
                buckets = []
                for _ in range(26):
                    buckets.append([])
                    
                for strng in strings:
                    if index >= len(strng):
                        bucket_index = 0
                    else:
                        bucket_index = k.index(strng.lower()[index])
                    buckets[bucket_index].append(strng)
               
                new_strings = []
                
                for bucket in buckets:
                    new_strings += bucket
                for i in range(len(strings)):
                    strings[i] = new_strings[i]
                index -= 1

        return


# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    @staticmethod
    def is_sorted_alpha(strings):
        """
        -------------------------------------------------------
        Determines whether an array is sorted or not.
        Use: srtd = Sorts.is_sorted(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns‌‌​​​‌‌​:
            srtd - True if contents of strings are sorted,
                False otherwise (boolean)
       -------------------------------------------------------
        """
        srtd = True
        n = len(strings)
        i = 0

        while srtd and i < n - 1:

            if strings[i].lower() <= strings[i + 1].lower():
                i += 1
            else:
                srtd = False
        return srtd
