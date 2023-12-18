def create_hero():
    hp = 100

    def get_hp():
        return hp

    def change_hp(delta):
        nonlocal hp
        new_hp = hp + delta
        if new_hp > 100:
            hp = 100
        elif new_hp < 0:
            hp = 0
        else:
            hp = new_hp

    def heal(amount):
        nonlocal hp
        change_hp(amount)

    def take_damage(amount):
        nonlocal hp
        change_hp(-amount)

    return get_hp, heal, take_damage

# Создаем экземпляр героя
hero_hp, hero_damage, hero_heal = create_hero()

# Пример использования
print(hero_hp())  # Выведет 100

hero_heal(50)  # Герой лечится на 50 HP
print(hero_hp())  # Выведет 100

hero_damage(75)  # Герой получает урон на 75 HP
print(hero_hp())  # Выведет 25

hero_damage(50)  # Герой получает урон на 50 HP
print(hero_hp())  # Выведет 0

hero_heal(30)  # Попытка вылечить героя на 30 HP, но его значение уже достигло минимума 0
print(hero_hp())  # Выведет 0