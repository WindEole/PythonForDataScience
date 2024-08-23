from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey

array = ft_load("landscape.jpg")

print(ft_invert.__doc__)
ft_invert(array)

print(ft_red.__doc__)
ft_red(array)

print(ft_green.__doc__)
ft_green(array)

print(ft_blue.__doc__)
ft_blue(array)

print(ft_grey.__doc__)
ft_grey(array)
