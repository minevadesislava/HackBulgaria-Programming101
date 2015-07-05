class Enemy:

     def _init__(health,mana,damage):
        if type(health) is not int or type(mana) is not int or type(mana_regeneration_rate) is not int:
            raise TypeError("Bad values for health, mana or mana regeneration rate")
        if not isinstance(mana, int):
            raise TypeError("Mana must be integer")
        self.__health = health
        self.__mana = mana
        self.damage = damage
        self._max_mana = mana
        self.__initial_health = health
        self.weapon = None
        self.spell = None

    def get_damage(self):
        return self.damage

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health > 0

    def heal_hero(healing_points):
        new_health = self.__health + healing_points
        if new_health <= 100:
            return new_health
        else:
            return self.__health

    def take_healing(healing_points):
        if type(healing_points) not in (int, float):
            raise TypeError("The healing points should be integer or float number")
        if self.is_alive:
            return heal_hero(healing_points)
        return False

    def take_mana(self, mana):
        if self.mana + mana > self.__max_mana:
            self.mana = self.__max_mana
        else:
            self.mana += mana

    def set_health(self, points):
        self.__health = self.__health + points

        if self.__health < 0:
            self.__health = 0

        elif self.__health > self.__initial_health:
            self.__health = self.__initial_health

        return self.__health

    def take_damage(self, damage_points):
        if type(damage_points) not in (int, float):
            raise TypeError("The damage points should be integer or float number")

        self.set_health(-damage_points)

    def attack(self, by=""):
        if by not in ["weapon", "magic"]:
            raise ValueError("Enter valid attack method (weapon or magic)")
        if by == "weapon":
            if self.weapon is not None:
                return self.weapon.get_damage()
        elif by == "magic":
            if self.spell is not None:
                if self.can_cast():
                    self.mana -= self.spell.get_mana_cost()
                    return self.spell.get_damage()
                raise Exception("Not enough mana.")
        return self.damage









