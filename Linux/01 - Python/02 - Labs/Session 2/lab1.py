operation = input(
    '''
To understand split function press \'1\'\n\
To understand splitlines function press \'2\' 
''')

if operation == '1':
    print(
        '''
        Syntax:
            string.split(separator, maxsplit)

        Parameter	Description:
        separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
        maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
        
        Example:
        Split the string, using comma, followed by a space, as a separator:

        
        '''
    )

    txt = "hello, my name is Peter, I am 26 years old"

    x = txt.split(", ")

    print(x)

elif operation == '2':
    print(
        '''
        Definition and Usage
        The splitlines() method splits a string into a list. The splitting is done at line breaks.

        Syntax
        string.splitlines(keeplinebreaks)

        Split a string into a list where each line is a list item:

        
        '''
    )
    txt = "Thank you for the music\nWelcome to the jungle"

    x = txt.splitlines()

    print(x)
