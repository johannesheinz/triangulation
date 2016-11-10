
import json

def read_coordinates(filename='coordinates.json'):
    """
    Summary line.

    Parameters
    ----------
    arg1 : int
        Description of arg1

    Returns
    -------
    int
        Description of return value
    """
    with open(filename, 'r') as input:    
        # Example plot: http://www.wolframalpha.com/input/?i=plot+%5B+%5B1,+1%5D,+%5B1,+6%5D,+%5B10,+6%5D,+%5B10,+1%5D,+%5B7,+1%5D,+%5B7,+4%5D,+%5B4,+4%5D,+%5B4,+1%5D+%5D
        coordinates_json = json.loads(input.read())
        
        # Store in dictionary
        coordinates = {}
        for index, coordinate in enumerate(coordinates_json):
            coordinates[index + 1] = coordinate
        
        return(coordinates)
