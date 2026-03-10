# =========== RegEx ============= #

# to work with regular expression we need import re

import re

txt = "the sun is a start"

# and use some methods 
# search - to ask for something

# findall => Returns a list containing all matches
# search =>	Returns a Match object if there is a match anywhere in the string
# split => Returns a list where the string has been split at each match
# sub => Replaces one or many matches with a string

x = re.search("^the.*sun$", txt)
print(x)

# Match Object is an object containing information about the search and the result

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# REGEX TO SEARCH
# []    A set of characters	                                                        "[a-m]"	
# \	    Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	    Any character (except newline character)	                                "he..o"	
# ^	    Starts with	                                                                "^hello"	
# $	    Ends with	                                                                "planet$"	
# *	    Zero or more occurrences	                                                "he.*o"	
# +	    One or more occurrences	                                                    "he.+o"	
# ?	    Zero or one occurrences	                                                    "he.?o"	
# {}	Exactly the specified number of occurrences	                                "he.{2}o"	
# |	    Either or	                                                                "falls|stays"	
# ()	Capture and group

# Flag	            Shorthand	Description	Try it
# re.ASCII	        re.A	    Returns only ASCII matches	
# re.DEBUG		                Returns debug information	
# re.DOTALL	        re.S	    Makes the . character match all characters (including newline character)	
# re.IGNORECASE	    re.I	    Case-insensitive matching	
# re.MULTILINE	    re.M	    Returns only matches at the beginning of each line	
# re.NOFLAG		                Specifies that no flag is set for this pattern	
# re.UNICODE	    re.U	    Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
# re.VERBOSE	    re.X	    Allows whitespaces and comments inside patterns. Makes the pattern more readable

# Character	   Description	                                                                                                                             Example
# \A	       Returns a match if the specified characters are at the beginning of the string	                                                         "\AThe"	
# \b	       Returns a match where the specified characters are at the beginning or at the end of a word                                                r"\bain"
#              (the "r" in the beginning is making sure that the string is being treated as a "raw string")	                                              r"ain\b"	
# \B	       Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word                             r"\Bain"
#              (the "r" in the beginning is making sure that the string is being treated as a "raw string")	                                              r"ain\B"
# \d	       Returns a match where the string contains digits (numbers from 0-9)	                                                                     "\d"	
# \D	       Returns a match where the string DOES NOT contain digits	                                                                                 "\D"	
# \s	       Returns a match where the string contains a white space character	                                                                     "\s"	
# \S	       Returns a match where the string DOES NOT contain a white space character	                                                             "\S"	
# \w	       Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	 "\w"	
# \W	       Returns a match where the string DOES NOT contain any word characters	                                                                 "\W"	
# \Z	       Returns a match if the specified characters are at the end of the string	                                                                 "Spain\Z"

# Set	               Description	
# [arn]	               Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n]	               Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	           Returns a match for any character EXCEPT a, r, and n	
# [0123]	           Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	               Returns a match for any digit between 0 and 9	
# [0-5][0-9]	       Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	           Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	               Return a match for any + character in the string