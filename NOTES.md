# Satellite Computation Notes

## TODO:

- speed
- Kugelkoordinatensysteme (räumliche Polarkoordinaten)
  * helferklasese

## Notes:

# Umrechnung kartesian - polar

koordinatentripel (r, theta, phi)

- r -> alle positiven Reellen Werte
- theta -> Intervall [0, pi] bzw. [0, 180°]
- phi -> Intervall [-pi, pi] bzw. [-180°, 180°] oder [0, 2pi] bzw. [0, 360°]

Umrechnung polar ->  kartesian:

- x = r * sin(theta) * cos(phi)
- y = r * sin(theta) * sin(phi)
- z = r * sin(theta)

Umrechnung kartesian -> polar:

- r = sqrt(x^2 + y^2 + z^2)
- theta = arccos({z}over{sqrt(x^2 + y^2 + z^2)})
- phi =
  - wenn x > 0, arctan({y}over{x})
  - wenn x = 0, sgn(y){pi}over{2}
  - wenn x < 0 And y >= 0, arctan({y}over{x})+pi
  - wenn x < 0 And y < 0, arctan({y}over{x})-pi
