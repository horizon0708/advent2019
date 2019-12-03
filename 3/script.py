
a1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')
a2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(',')
a_res = 159

b1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',')
b2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',')
b_res = 135

def main():
    
    print(a_res == calculate(a1,a2))
    print(b_res == calculate(b1,b2))


def calculate(p1, p2):
    p1s = travel(p1)
    p2s = travel(p2)
    hits = []
    
    for one in p1s:
        for two in p2s:
            if(one == two):
                hits.append(one)
    
    sorted = [ a.distance() for a in hits if a.distance() != 0 ]
    print(sorted)
    return sorted[0]

def travel(commands):
    positions = [ Vector(0,0) ]
    for c in commands:
        positions += parse_command(c, positions)
    return positions


def parse_command(command, positions):
    dir = command[0]
    mag = int(command[1:])
    if(dir == "U"):
       return list_of_vectors(positions[-1], 0, mag, 1)
    elif(dir == "D"):
       return list_of_vectors(positions[-1], 0, mag, -1)
    elif(dir == "L"):
       return list_of_vectors(positions[-1], mag, 0, -1)
    elif(dir == "R"):
       return list_of_vectors(positions[-1], mag, 0, 1)
    else:
        return []


def list_of_vectors(last_pos, dx, dy, step): 
    vectors = []
    
    for x in range(0, dx * step, step):
        vectors.append(Vector(last_pos.x + x, last_pos.y))

    for y in range(0, dy * step, step):
        vectors.append(Vector(last_pos.x, last_pos.y + y))
    return vectors
        


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def distance(self):
        return abs(self.x) + abs(self.y)


main()