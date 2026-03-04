difference() {
	union() {
		translate(v = [0, 0, 20]) {
			difference() {
				sphere(r = 20);
				translate(v = [0, 0, 10]) {
					cube(center = true, size = [40, 50, 20]);
				}
				sphere(r = 19);
			}
		}
		translate(v = [0, 0, -8]) {
			cylinder(center = true, h = 20, r = 5);
		}
		translate(v = [0, 0, -20]) {
			cylinder(h = 5, r1 = 15, r2 = 5);
		}
	}
	mirror(v = [0, 1, 0]) {
		translate(v = [-8, -3, -20]) {
			text(size = 5, text = "Lukas");
		}
	}
}
