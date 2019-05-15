# two_files.py
d_path = 'plan.txt'
d_r_path = 'sort_plan.txt'

with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    planets = reader.readlines()
    writer.writelines(sorted(planets))