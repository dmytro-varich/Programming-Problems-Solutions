from random import randint
import matplotlib.pyplot as plt


class Room:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.room = list()
        for w in range(self.width):
            self.room.append(list())
            for _ in range(self.length):
                self.room[-1].append(0)

    def check_room(self):
        for x in range(self.width):
            for y in range(self.length):
                print(self.room[x][y], end=" ")
            print()

    def add_dust(self, count):
        while count != 0:
            n_count = randint(1, count)
            r_w = randint(0, self.width-1)
            r_l = randint(0, self.length-1)

            self.room[r_w][r_l] += n_count
            count -= n_count
        # self.check_room()

    def has_position(self, pos):
        x_w, y_l = pos[0], pos[1]
        if (0 <= x_w < self.width) and (0 <= y_l < self.length): return True 
        return False

    def has_dust(self, pos):
        if not self.has_position(pos):
            raise ValueError("This position does not exist!")

        x, y = pos[0], pos[1]
        if self.room[x][y] > 0: return True
        return False

    def pickup_dust(self, pos):
        x, y = pos[0], pos[1]
        if self.has_dust(pos): self.room[x][y] -= 1

    def is_clean(self):
        for x in range(self.width):
            for y in range(self.length):
                if self.room[x][y] != 0:
                    return False
        return True


class VacuumCleaner:
    def __init__(self, start_pos, room):
        self.current_position = start_pos
        self.possible_directions = ['N', 'E', 'S', 'W']
        self.room = room

    def move(self, direction):
        x_vac, y_vac = self.current_position[0], self.current_position[1]

        # step 1
        self.room.pickup_dust(self.current_position)

        # step 2
        if direction not in self.possible_directions:
            raise ValueError("This direction does not exist!")

        # step 3
        pos_dir = {
            "N": (-1, 0),  
            "S": (1, 0), 
            "E": (0, 1), 
            "W": (0, -1)
        }

        for key in pos_dir.keys():
            if key == direction:
                value = pos_dir[direction]
                x_dir, y_dir = value[0], value[1]
        
                if self.room.has_position((x_vac + x_dir, y_vac + y_dir)):
                    self.current_position = (x_vac + x_dir, y_vac + y_dir)
                else: 
                    return 
                    # raise ValueError("This direction is not correct!")
        
def simulate_cleaning(room_dimensions, dust_count, simulation_no):
    width, length = room_dimensions[0], room_dimensions[1]
    all_steps = list()

    room = Room(width, length)

    for sim in range(simulation_no):
        step = 0
        room.add_dust(dust_count)
        x_vac, y_vac = randint(0, width-1), randint(0, length-1)
        iRobot = VacuumCleaner((x_vac, y_vac), room)    
        while not room.is_clean(): 
            pos_dir = iRobot.possible_directions
            direction = randint(0, len(pos_dir) - 1)
            iRobot.move(pos_dir[direction])
            step += 1
        all_steps.append(step)
    return all_steps


def main():
    width = int(input("Enter your room width: "))
    length = int(input("Enter your room lenght: "))
    dust_count = int(input("Enter the number of dust: "))
    simulation_no = int(input("Enter the number of simulation: "))

    all_steps = simulate_cleaning((width, length), dust_count, simulation_no)
    print(f"Number of steps needed to clear a room in {simulation_no} simulation: {all_steps}")

    fig = plt.figure(num="Varich Company")

    plt.hist(all_steps, edgecolor='black')

    plt.title("Robotic Vacuum Cleaner Simulation", pad=20)
    plt.xlabel("Steps", labelpad=10)
    plt.ylabel("Simulations", labelpad=10) 
    
    plt.show()

if __name__ == '__main__':
    main()
