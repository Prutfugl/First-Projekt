import solid2
minModel1 = solid2.sphere(20)

minModel2 = solid2.cube([40,50,20], center=True)
minModel2 = solid2.translate([0,0,10])(minModel2)

minModel3 = solid2.sphere(19)

minModel = minModel1 - minModel2- minModel3
minModel = solid2.translate([0,0,20])(minModel)

minModel4 = solid2.cylinder(h=20, r=5,center=True)
minModel4 = solid2.translate([0,0,-8])(minModel4)

minModel5 = solid2.cylinder(h=5,r1=15,r2=5)
minModel5 = solid2.translate([0,0,-20])(minModel5)

Text = solid2.text(text="Lukas", size=5)
Text = solid2.translate([-8,-3,-20])(Text)
Text = solid2.mirror([0,1,0])(Text)
#Text = solid2.linear_extrude(height=5)(Text)

finalModel = minModel + minModel4 + minModel5 - Text
solid2.scad_render_to_file(finalModel, 'finalModel.scad')