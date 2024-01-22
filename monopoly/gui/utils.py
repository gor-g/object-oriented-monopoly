import random

class TerminalColor:
  RESET = '\033[0m' # default color of the terminal

  def __new__(cls, *args, **kwargs):
    instance = super(TerminalColor, cls).__new__(cls, *args, **kwargs)
    return instance

  @classmethod
  def reset(cls):
    return cls(cls.RESET)

  @staticmethod
  def rgb_to_ansi(r, g, b, is_background=False):
    """
    Convert RGB values to the corresponding ANSI escape code for 24-bit color.
    :param r: Red channel value (0-255).
    :param g: Green channel value (0-255).
    :param b: Blue channel value (0-255).
    :param is_background: Boolean flag to determine whether it's a background color.
    :return: ANSI escape code for the specified color.
    """
    color_format = '\033[48;2;{};{};{}m' if is_background else '\033[38;2;{};{};{}m'
    return color_format.format(r, g, b)

  @staticmethod
  def random_color(m = 0, M = 255, is_background = False):
    assert M-m > 30, "allowed intensity intervall is too small, random generation may take too much time"
    assert 0 < m < M < 255, "invalid arguments"
    r,g,b = -1, -1, -1
    while not m< (r+g*1.25+b)/3 <M:
      r = random.randint(0,255)
      g = random.randint(0,255)
      b = random.randint(0,255)

    return TerminalColor.rgb_to_ansi(r, g, b, is_background)

  @staticmethod
  def RED(s=None):
    if s is None:
      return TerminalColor.rgb_to_ansi(255,0,0)
    else:
      return TerminalColor.rgb_to_ansi(255,0,0)+s+TerminalColor.RESET

  @staticmethod
  def ORANGE(s=None):
    if s is None:
      return TerminalColor.rgb_to_ansi(150,100,0)
    else:
      return TerminalColor.rgb_to_ansi(150,100,0)+s+TerminalColor.RESET

  @staticmethod
  def GREEN(s=None):
    if s is None:
      return TerminalColor.rgb_to_ansi(30,200,30)
    else:
      return TerminalColor.rgb_to_ansi(30,200,30)+s+TerminalColor.RESET

  @staticmethod
  def BLUE(s=None):
    if s is None:
      return TerminalColor.rgb_to_ansi(70,70,255)
    else:
      return TerminalColor.rgb_to_ansi(70,70,255)+s+TerminalColor.RESET




