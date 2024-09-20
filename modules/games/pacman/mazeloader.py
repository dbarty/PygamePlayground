from games.pacman.entity.pill import Pill
from games.pacman.entity.wall import Wall

class MazeLoader:
    

    def load(self, filename):
        print(filename)

        ew = 32  # entity width
        eh = 32  # entity height
        x = 0
        y = 0

        entities = []

        with open(filename) as file:
            for line in file.readlines():
                el = []  # entity line

                x = 0
                for char in line:
                    
                    if char == "#":
                        entity = Wall()
                        entity.position.x = x
                        entity.position.y = y
                    elif char == ".":
                        entity = Pill()
                        entity.position.x = x + 50
                        entity.position.y = y + 32

                    # set entity position
                    entity.position.x = x
                    entity.position.y = y

                    # add entity to line
                    el.append(entity)

                    x += ew

                # add entity line to entities
                entities.append(el)
                y += eh

                    #print(char, sep=" ", end="")

            #print(entities, entities[5][5].position)  

        return entities







        #print("lines", len(lines), "maxCol", max(map(len, lines)))

        #pill = Pill()
        #print(pill)