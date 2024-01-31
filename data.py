import random
import actor
import item


def generate_random_level_data(enemies, items):
    selected_enemies = random.sample(enemies, 5)
    selected_items = random.sample(items, 5)
    return selected_enemies, selected_items


# Poziom 1
enemy1 = actor.Enemy(hp=10, dmg=10, name="Procrastinator", initiative=1, x=1, y=1)
enemy2 = actor.Enemy(hp=10, dmg=12, name="Crammer", initiative=2, x=2, y=2)
enemy3 = actor.Enemy(hp=10, dmg=14, name="Sleep-Deprived Student", initiative=3, x=3, y=3)
enemy4 = actor.Enemy(hp=10, dmg=16, name="Coffee Addict", initiative=2, x=4, y=4)
enemy5 = actor.Enemy(hp=10, dmg=10, name="Lecturer", initiative=3, x=5, y=5)
enemy6 = actor.Enemy(hp=10, dmg=8, name="Lecture Skipper", initiative=1, x=6, y=6)
enemy7 = actor.Enemy(hp=10, dmg=11, name="Assignment Procrastinator", initiative=2, x=7, y=7)
enemy8 = actor.Enemy(hp=10, dmg=13, name="Late Night Gamer", initiative=3, x=8, y=8)
enemy9 = actor.Enemy(hp=10, dmg=15, name="Lab Experiment Saboteur", initiative=2, x=9, y=9)
enemy10 = actor.Enemy(hp=10, dmg=14, name="Extracurricular Overachiever", initiative=3, x=10, y=10)

item1 = item.Item("Boa o woa", 10, 0, 1, "Drink")
item2 = item.Item("Highlighter", 0, 5, 1, "Weapon")
item3 = item.Item("Laptop", 10, 5, -1, "Accessory")
item4 = item.Item("Coffee Mug", 0, 1, 3, "Hat")
item5 = item.Item("Calculator", 0, 7, 1, "Weapon")
item6 = item.Item("Notebook", 4, 2, 0, "Accessory")
item7 = item.Item("Energy Drink", 0, 2, 3, "Drink")
item8 = item.Item("USB Drive", 2, 4, 0, "Weapon")
item10 = item.Item("Stinky Hoodie", 10, 3, 5, "Hoodie")

level1_enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10]
level1_items = [item1, item2, item3, item4, item5, item6, item7, item8, item10]


# Poziom 2
enemy11 = actor.Enemy(hp=120, dmg=18, name="Programming Guru", initiative=5, x=1, y=1)
enemy12 = actor.Enemy(hp=90, dmg=20, name="Exam Proctor", initiative=6, x=2, y=2)
enemy13 = actor.Enemy(hp=110, dmg=15, name="Group Project Leader", initiative=4, x=3, y=3)
enemy14 = actor.Enemy(hp=80, dmg=22, name="Pop Quiz Master", initiative=5, x=4, y=4)
enemy15 = actor.Enemy(hp=150, dmg=25, name="Thesis Supervisor", initiative=7, x=5, y=5)
enemy16 = actor.Enemy(hp=105, dmg=16, name="Library Ghost", initiative=4, x=6, y=6)
enemy17 = actor.Enemy(hp=95, dmg=14, name="Lab Assistant", initiative=3, x=7, y=7)
enemy18 = actor.Enemy(hp=115, dmg=20, name="Code Debugger", initiative=5, x=8, y=8)
enemy19 = actor.Enemy(hp=85, dmg=18, name="Research Assistant", initiative=4, x=9, y=9)
enemy20 = actor.Enemy(hp=130, dmg=22, name="Computer Lab Manager", initiative=6, x=10, y=10)

item11 = item.Item("Code Editor", 15, 8, 0, "Weapon")
item12 = item.Item("Lab Report", 8, 3, 3, "Accessory")
item13 = item.Item("Coffee Thermos", 0, 0, 5, "Hat")
item14 = item.Item("Scientific Calculator", 0, 10, 3, "Weapon")
item15 = item.Item("Research Paper", 15, 0, 6, "Accessory")
item16 = item.Item("Graphing Calculator", 5, 12, 1, "Weapon")
item17 = item.Item("Whiteboard Marker", 0, 4, 0, "Accessory")
item18 = item.Item("Projector Remote", 0, 8, 2, "Weapon")
item19 = item.Item("Group Presentation Notes", 6, 0, 5, "Accessory")
item20 = item.Item("Red-Bull", 0, 2, 5, "Drink")

level2_enemies = [enemy11, enemy12, enemy13, enemy14, enemy15, enemy16, enemy17, enemy18, enemy19, enemy20]
level2_items = [item11, item12, item13, item14, item15, item16, item17, item18, item19, item20]

# Poziom 3
enemy21 = actor.Enemy(hp=200, dmg=30, name="Final Boss", initiative=8, x=1, y=1)
enemy22 = actor.Enemy(hp=180, dmg=28, name="Graduation Supervisor", initiative=7, x=2, y=2)
enemy23 = actor.Enemy(hp=160, dmg=25, name="Postgraduate Researcher", initiative=6, x=3, y=3)
enemy24 = actor.Enemy(hp=140, dmg=22, name="Academic Dean", initiative=5, x=4, y=4)
enemy25 = actor.Enemy(hp=220, dmg=35, name="Tenure Committee Chair", initiative=9, x=5, y=5)
enemy26 = actor.Enemy(hp=185, dmg=32, name="Conference Speaker", initiative=7, x=6, y=6)
enemy27 = actor.Enemy(hp=165, dmg=28, name="Grant Reviewer", initiative=6, x=7, y=7)
enemy28 = actor.Enemy(hp=145, dmg=25, name="Peer Reviewer", initiative=5, x=8, y=8)
enemy29 = actor.Enemy(hp=225, dmg=38, name="Research Committee Chair", initiative=10, x=9, y=9)
enemy30 = actor.Enemy(hp=250, dmg=40, name="Conference Organizer", initiative=11, x=10, y=10)

item21 = item.Item("Dissertation", 20, 12, 0, "Hat")
item22 = item.Item("Research Grant", 0, 5, 10, "Drink")
item23 = item.Item("SCII MEMBERSHIP HOODIEdd", 10, 8, 5, "Hoodie")
item24 = item.Item("Library Card", 5, 5, 5, "Accessory")
item25 = item.Item("PhD Diploma", 25, 0, 20, "Hat")
item26 = item.Item("Conference Program", 8, 0, 5, "Drink")
item27 = item.Item("Grant Approval Letter", 0, 10, 0, "Hat")
item28 = item.Item("Research Journal", 10, 5, 0, "Weapon")
item29 = item.Item("Conference Badge", 5, 3, 0, "Drink")
item30 = item.Item("Tenure Certificate", 15, 0, 10, "Hat")

level3_enemies = [enemy21, enemy22, enemy23, enemy24, enemy25, enemy26, enemy27, enemy28, enemy29, enemy30]
level3_items = [item21, item22, item23, item24, item25, item26, item27, item28, item29, item30]

# Poziom 4
enemy31 = actor.Enemy(hp=270, dmg=45, name="Job Interviewer", initiative=10, x=1, y=1)
enemy32 = actor.Enemy(hp=240, dmg=42, name="Office Manager", initiative=8, x=2, y=2)
enemy33 = actor.Enemy(hp=255, dmg=48, name="Workplace Strategist", initiative=12, x=3, y=3)
enemy34 = actor.Enemy(hp=225, dmg=40, name="Business Tycoon", initiative=9, x=4, y=4)
enemy35 = actor.Enemy(hp=290, dmg=50, name="CEO", initiative=14, x=5, y=5)
enemy36 = actor.Enemy(hp=260, dmg=46, name="Entrepreneur", initiative=11, x=6, y=6)
enemy37 = actor.Enemy(hp=245, dmg=44, name="Office Party Planner", initiative=10, x=7, y=7)
enemy38 = actor.Enemy(hp=280, dmg=52, name="Productivity Guru", initiative=13, x=8, y=8)
enemy39 = actor.Enemy(hp=255, dmg=47, name="Startup Founder", initiative=12, x=9, y=9)
enemy40 = actor.Enemy(hp=300, dmg=55, name="Board Chairman", initiative=15, x=10, y=10)

item31 = item.Item("Job Offer Letter", 0, 20, 0, "Helmet")
item32 = item.Item("Executive Briefcase", 10, 15, 5, "Accessory")
item33 = item.Item("Business Suit", 15, 8, 10, "Gloves")
item34 = item.Item("Corporate Smartphone", 5, 12, 0, "Weapon")
item35 = item.Item("Power Tie", 8, 5, 0, "Accessory")
item36 = item.Item("Company Share Certificate", 20, 0, 15, "Helmet")
item37 = item.Item("Product Launch Invitation", 0, 10, 5, "Boots")
item38 = item.Item("Desk Plant", 3, 0, 8, "Boots")
item39 = item.Item("Entrepreneurship Book", 12, 5, 0, "Weapon")
item40 = item.Item("Business Card Holder", 0, 5, 3, "Accessory")

level4_enemies = [enemy31, enemy32, enemy33, enemy34, enemy35, enemy36, enemy37, enemy38, enemy39, enemy40]
level4_items = [item31, item32, item33, item34, item35, item36, item37, item38, item39, item40]


def lvl_items_and_enemies(level):
    if level == 1:
        return generate_random_level_data(level1_enemies, level1_items)
    if level == 2:
        return generate_random_level_data(level2_enemies, level2_items)
    if level == 3:
        return generate_random_level_data(level3_enemies, level3_items)
    if level == 4:
        return generate_random_level_data(level4_enemies, level4_items)

