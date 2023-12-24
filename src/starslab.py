box = cq.Workplane("XY").box(20, 10, 1)

points = [
    ((-8.5, 0),.25),
    ((2, 0),.5),
    ((2.25, 0),.75),
    ((2.5, 0),1),
    ((2.75, 0),1.25),
    ((3, 0),1.5),
    ((3.25,0),1.75)
]

for point, size in points:
    box = box.faces(">Z").workplane().center(*point).hole(size)
