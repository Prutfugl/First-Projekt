translate(v = [0, 0, 20]) {
	difference() {
		sphere(r = 20);
		translate(v = [0, 0, 10]) {
			cube(center = true, size = [40, 50, 20]);
		}
		sphere(r = 19);
	}
}
