import mapElement as mE
import map as m

mapa2D = [[mE.Wall(), mE.Floor()],
          [mE.Wall(), mE.Floor()],
          [mE.Wall(), mE.Floor()]]

mapa = m.Map(3, 2, mapa2D)

mapa.check(0,0)


