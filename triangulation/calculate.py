def check_intersection(coordinates, triangle):
    """Summary line.

    Extended description of function.
    The determinant of a square matrix is the same as the determinant of its transpose. That's why row orientation or column orientation is irrelevant concerning the parameters.

    Args:
        coordinates (int): Description of arg1
        triangle (str): Description of arg2

    Returns:
        bool: Description of return value

    """
    
    if (len(coordinates) == 2) and (len(coordinates[0]) == 2) and (len(coordinates[1]) == 2):
        p = coordinates[0]
        q = coordinates[1]
        v1 = __connection_vector(p)
        v2 = __connection_vector(q)
        
        # A: Koeffizientendeterminanten != 0
        det1 = __determinant([[ q[0][0] - p[0][0], v2[0] ], [ q[0][1] - p[0][1], v2[1] ]])
        det2 = __determinant([[ v1[0], q[0][0] - p[0][0] ], [ v1[1], q[0][1] - p[0][1] ]])  
        
        # Normalisieren
        try:
            normalized1 = __normalize(det1, v1, v2)
            normalized2 = __normalize(det1, v1, v2)
        except ZeroDivisionError as err:
            print("Error during normalization".format(err))
            return False
        
        print("[det1, det2, normalized1, normalized2]", [det1, det2, normalized1, normalized2])
        
        # B: Beide Parameter e [0,1]
        if (0 <= normalized1 <= 1) and (0 <= normalized2 <= 1):
            return True
        else:
            return False
        
    else:
        raise ValueError("The parameter must be a 2x2 matrix!")


def check_orientation(coordinates, triangle):
    """Summary line.

    Extended description of function.

    Args:
        coordinates: Description of arg1
        triangle: Description of arg2

    Returns:
        Description of return value
    
    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    return True;


def __connection_vector(matrix):
    if (len(matrix) == 2) and (len(matrix[0]) == 2) and (len(matrix[1]) == 2):
        return [matrix[0][0]-matrix[1][0], matrix[0][1]-matrix[1][1]]
    else:
        raise ValueError("The parameter must be a 2x2 matrix!")

def __determinant(matrix):
    if (len(matrix) == 2) and (len(matrix[0]) == 2) and (len(matrix[1]) == 2):
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        raise ValueError("The parameter must be a 2x2 matrix!")

def __normalize(determinant, v1, v2):
    if (len(v1) == 2) and (len(v2) == 2):
        factor = __determinant([[ v1[0], v2[0] ], [ v1[1], v2[1] ]])
        return determinant / factor
    else:
        raise ValueError("The parameters must contain two elements!")
