from enum import Enum
from random import randint

class Roles(Enum):
    EMPEROR = 'e'
    LOYALIST = 'l'
    REBEL = 'r'
    SPY = 's'
    
    @staticmethod
    def get_roles(num_players: int) -> list["Roles"]:
        result = []
        rand = randint(0,1)
        match num_players:
            case 4:
                result = [Roles.EMPEROR, Roles.LOYALIST, Roles.REBEL, Roles.SPY]
            case 5:
                result = Roles.get_roles(4)
                result.append(Roles.REBEL)
            case 6:
                result = Roles.get_roles(5)
                result.append(Roles.REBEL) if rand == 0 else result.append(Roles.SPY)
            case 7:
                result = [Roles.EMPEROR, Roles.LOYALIST, Roles.REBEL, Roles.SPY, Roles.REBEL, Roles.REBEL, Roles.LOYALIST]
            case 8:
                result = Roles.get_roles(7)
                result.append(Roles.REBEL) if rand == 0 else result.append(Roles.SPY)
            case 9:
                result = [Roles.EMPEROR, Roles.LOYALIST, Roles.REBEL, Roles.SPY, Roles.REBEL, Roles.REBEL, Roles.LOYALIST, Roles.REBEL, Roles.LOYALIST]
            case 10:
                result = Roles.get_roles(9)
                result.append(Roles.SPY)
        return result

print(Roles.get_roles(6))