from enum import Enum
from random import randint

class Role(Enum):
    EMPEROR = 'e'
    LOYALIST = 'l'
    REBEL = 'r'
    SPY = 's'
    
    @staticmethod
    def get_roles(num_players: int) -> list["Role"]:
        result = []
        rand = randint(0,1)
        match num_players:
            case 4:
                result = [Role.EMPEROR, Role.LOYALIST, Role.REBEL, Role.SPY]
            case 5:
                result = Role.get_roles(4)
                result.append(Role.REBEL)
            case 6:
                result = Role.get_roles(5)
                result.append(Role.REBEL) if rand == 0 else result.append(Role.SPY)
            case 7:
                result = [Role.EMPEROR, Role.LOYALIST, Role.REBEL, Role.SPY, Role.REBEL, Role.REBEL, Role.LOYALIST]
            case 8:
                result = Role.get_roles(7)
                result.append(Role.REBEL) if rand == 0 else result.append(Role.SPY)
            case 9:
                result = [Role.EMPEROR, Role.LOYALIST, Role.REBEL, Role.SPY, Role.REBEL, Role.REBEL, Role.LOYALIST, Role.REBEL, Role.LOYALIST]
            case 10:
                result = Role.get_roles(9)
                result.append(Role.SPY)
        return result

print(Role.get_roles(6))