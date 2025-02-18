# Name: میراث آدم خطی
# URL:  https://quera.org/problemset/182550

import sys
from collections import defaultdict

def parse_time(time_str):
    mm, ss, xxx = map(int, time_str.split(":"))
    return mm * 60000 + ss * 1000 + xxx

class Unit:
    def __init__(self, role, health, cost, damage, attack_interval, size):
        self.role = role
        self.health = health
        self.cost = cost
        self.damage = damage
        self.attack_interval = attack_interval
        self.size = size
        self.alive = True

class Army:
    def __init__(self):
        self.units = {}
        self.unit_count = defaultdict(int)
        self.total_size = 0
        self.unit_index = 1
        self.next_gold_time = 20000
        self.gold = 500
        self.dragon_health = 0

    def add_unit(self, role, timestamp):
        role_stats = {
            'miner': (100, 150, 0, 0, 1),
            'swordwrath': (120, 125, 20, 1000, 1),
            'archidon': (80, 300, 10, 1000, 1),
            'spearton': (250, 500, 35, 3000, 2),
            'magikill': (80, 1200, 200, 5000, 4),
            'giant': (1000, 1500, 150, 4000, 4)
        }
        health, cost, damage, attack_interval, size = role_stats[role]
        
        if self.total_size + size > 50:
            return "too many army"
        if self.gold < cost:
            return "not enough money"
        
        unit = Unit(role, health, cost, damage, attack_interval, size)
        self.units[self.unit_index] = unit
        self.unit_count[role] += 1
        self.total_size += size
        self.gold -= cost
        self.unit_index += 1
        
        return str(self.unit_index - 1)
    
    def damage_unit(self, index, damage, timestamp):
        if index not in self.units or not self.units[index].alive:
            return "no matter"
        
        unit = self.units[index]
        unit.health -= damage
        
        if unit.health <= 0:
            unit.alive = False
            self.unit_count[unit.role] -= 1
            self.total_size -= unit.size
            return "dead"
        else:
            return str(unit.health)
    
    def get_dragon_status(self, timestamp):
        return str(self.dragon_health) if self.dragon_health > 0 else "game over"
    
    def get_army_status(self, timestamp):
        if self.dragon_health <= 0:
            return "game over"
        
        roles = ['miner', 'swordwrath', 'archidon', 'spearton', 'magikill', 'giant']
        return ' '.join(str(self.unit_count[role]) for role in roles)
    
    def get_money_status(self, timestamp):
        return str(self.gold) if self.dragon_health > 0 else "game over"
    
    def update_gold(self, timestamp):
        while self.next_gold_time <= timestamp:
            self.gold += 180
            self.next_gold_time += 20000

def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    q, h = map(int, data[0].split())
    
    army = Army()
    army.dragon_health = h
    
    for i in range(1, len(data)):
        command = data[i].split()
        timestamp = parse_time(command[-1])
        
        army.update_gold(timestamp)
        
        if command[0] == "add":
            role = command[1]
            result = army.add_unit(role, timestamp)
            print(result)
        elif command[0] == "damage":
            index = int(command[1])
            damage = int(command[2])
            result = army.damage_unit(index, damage, timestamp)
            print(result)
        elif command[0] == "enemy-status":
            result = army.get_dragon_status(timestamp)
            print(result)
        elif command[0] == "army-status":
            result = army.get_army_status(timestamp)
            print(result)
        elif command[0] == "money-status":
            result = army.get_money_status(timestamp)
            print(result)

if __name__ == "__main__":
    main()