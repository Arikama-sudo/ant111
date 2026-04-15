class Human:
    def __init__(self, name, eye_color, hair_color, profession=None):
        self.eye_color = eye_color
        self.hair_color = hair_color


        self.name = name
        self.profession = profession

class Child(Human):
    def __init__(self, name, father, mother, personal_trait):
        super().__init__(
            name=name,
            eye_color=father.eye_color,
            hair_color=mother.hair_color
        )
        self.personal_trait = personal_trait



dad = Human(name="Иван", eye_color="Голубой", hair_color="Брюнет", profession="Инженер")
mom = Human(name="Анна", eye_color="Зеленый", hair_color="Рыжий", profession="Врач")


kid = Child(name="Алексей", father=dad, mother=mom, personal_trait="Любит рисовать")


print(f"Ребенок {kid.name}:")
print(f"- Цвет глаз (от отца): {kid.eye_color}")
print(f"- Цвет волос (от матери): {kid.hair_color}")
print(f"- Личное качество: {kid.personal_trait}")
print(f"- Профессия: {kid.profession} (не унаследовано, значение None)")
