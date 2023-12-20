import cadquery as cq

cylinder1_mm = 27
cylinder1_hole_mm = 21
cylinder1_r = cylinder1_mm / 2
cylinder1_hole_r = cylinder1_hole_mm / 2

cylinder2_mm = 22
cylinder2_hole_mm = 21
cylinder2_r = cylinder2_mm / 2
cylinder2_hole_r = cylinder2_hole_mm / 2

cylinder1 = cq.Workplane("front")\
    .circle(cylinder1_r)\
    .extrude(3)\
    .faces(">Z")\
    .workplane()\
    .hole(cylinder1_hole_r*2)

cylinder2 = cq.Workplane("front")\
    .circle(cylinder2_r)\
    .extrude(-4.5)\
    .faces(">Z")\
    .workplane()\
    .hole(cylinder2_hole_r*2)\
    .translate((0,0,.5))

big = 7.424621202458749
little = 3.71231060123
z = -1
z2 = -1
grid_thickness = .15
g = grid_thickness

pos = (0,0,z)
grid1 = cq.Workplane("front")\
    .box(21.5,g,g)\
        .translate(pos)

pos = (0,0,z2)
grid6 = cq.Workplane("front")\
    .box(g,21.5,g)\
        .translate(pos)

pos = (0,big,z)
grid2 = cq.Workplane("front")\
    .box(15.5,g,g)\
        .translate(pos)

pos = (big,0,z2)
grid7 = cq.Workplane("front")\
    .box(g,15.5,g)\
        .translate(pos)

pos = (0,little,z)
grid3 = cq.Workplane("front")\
    .box(20,g,g)\
        .translate(pos)

pos = (little,0,z2)
grid8 = cq.Workplane("front")\
    .box(g,20,g)\
        .translate(pos)

pos = (0,-little,z)
grid4 = cq.Workplane("front")\
    .box(20,g,g)\
        .translate(pos)

pos = (-little,0,z2)
grid9 = cq.Workplane("front")\
    .box(g,20,g)\
        .translate(pos)

pos = (0,-big,z)
grid5 = cq.Workplane("front")\
    .box(15.5,g,g)\
        .translate(pos)

pos = (-big,0,z2)
grid10 = cq.Workplane("front")\
    .box(g,15.5,g)\
        .translate(pos)

result =\
    cylinder1\
    .union(cylinder2)\
    .union(grid1)\
    .union(grid2)\
    .union(grid3)\
    .union(grid4)\
    .union(grid5)\
    .union(grid6)\
    .union(grid7)\
    .union(grid8)\
    .union(grid9)\
    .union(grid10)