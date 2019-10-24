from math import pi, sin

import util

if __name__ == '__main__':
    print('8 squared = {}'.format(util.square(8)))

    val = util.quad(pi)
    print('pi quad = {:0.6f}'.format(val))

    print('sin(pi) = {:0.2f}'.format(sin(pi)))

    xs = [1, 2, 3, 4]
    x = 6
    if x in xs:
        print('{} is in {}'.format(x, xs))
    else:
        print('{} is not in  {}'.format(x, xs))
