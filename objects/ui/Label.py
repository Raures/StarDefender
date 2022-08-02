import pygame

from settings import FONT


class Label:
	"""
	Create a Label object.

	Attributes
	----------
	text : str
		Text of the label
	text_size : int
		Size of the text
	text_color : tuple
		RGB value for text color
	text_font : str
		Path to the *.ttf file used for text font
	text_padding : int
		Distance between the text and the label margin
	x : int
		Coordinate of position x
	y : int
		Coordinate of position y
	background : bool
		Display or hide label background
	background_color : tuple
		RGB value for background color
	border : bool
		Display or hide label border
	border_color : tuple
		RGB value for border color
	border_thickness : int
		Thickness of the border

	Methods
	-------
	set_text(new_text)
		Set the new text displayed on the label
	set_font(new_font)
		Set a new font for the text
	set_text_color(new_color)
		Set a new color for the text
	set_text_size(new_size)
		Set a new size for the text
	set_text_padding(new_padding)
		Set the padding of the text
	set_position(new_x, new_y)
		Set a new position for the label
	set_background(new_bool)
		Set the visibility of the background
	set_background_color(new_color)
		Set the color of the background
	set_border(new_bool)
		Set the visibility of the border
	set_border_color(new_color)
		Set the color of the border
	set_border_thickness(new_thickness)
		Set the thickness of the border
	show(surface)
		Display the label on the surface
	"""
    def __init__(self, text: str,
                 pos_x: int,
                 pos_y: int,
                 size=20,
                 font_type=FONT,
                 color: tuple = (255, 255, 255)):
	"""
	Parameters
	----------
	pos_x : int
		The x coordinate of the label position
	pos_y : int
		The y coordinate of the label position
	size : int
		The size of the text displayed on the label
		Default: 20
	font_type : str
		The font type of the text displayed on the label
		Default: FONT
	color : tuple
		The RGB color of the text displayed on the label
		Default: (255, 255, 255)
	"""

        self.text = text
        self.text_size = size
        self.text_color = color
        self.text_font = font_type
        self.text_padding = 15

        self.x = pos_x
        self.y = pos_y

        self.background = False
        self.background_color = (255, 255, 255)

        self.border = False
        self.border_color = (0, 255, 0)
        self.border_thickness = 2

    def set_text(self, new_text: str) -> None:
	"""
	Set the new text displayed on the label.

	Parameters
	----------
	new_text : str
		New text of the label
	"""
        self.text = new_text

    def set_font(self, new_font_type: str) -> None:
	"""
	Set a new font for the text displayed on the label.

	Parameters
	----------
	new_font_type : str
		New font of the text
	"""
        self.text_font = new_font_type

    def set_text_color(self, new_color: tuple) -> None:
	"""
	Set a new color for the text displayed on the label.
	
	Parameters
	----------
	new_color : tuple
		A tuple representing an RGB color
	"""
        self.text_color = new_color

    def set_text_size(self, new_size: int) -> None:
	"""
	Set a new size for the text displayed on the label.
	
	Parameters
	----------
	new_size : int
		New size of the text
	"""
        self.text_size = new_size

    def set_text_padding(self, new_padding: int) -> None:
	"""
	Set the padding value of the text.

	It represents the distance between the text and the margin of the label rectangle.

	Parameters
	----------
	new_padding : int
		New padding value
	"""
        self.text_padding = new_padding

    def set_position(self, new_x: int or None, new_y: int or None) -> None:
	"""
	Set a new position for the label.

	Parameters
	----------
	new_x : int, None
		New x coordinate for the label position, None leaves the value unchanged
	new_y : int, None
		New y coordinate for the label position, None leaves the value unchanged
	"""
        if new_x:
            self.x = new_x
        if new_y:
            self.y = new_y

    def set_background(self, new_bool: bool) -> None:
	"""
	Set the visibility of the label background.	

	Parameters
	----------
	new_bool : bool
		True or False
	"""
        self.background = new_bool

    def set_background_color(self, new_color: tuple) -> None:
	"""
	Set the label background color.

	Parameters
	----------
	new_color : tuple
		New RGB color for the label background
	"""
        self.background_color = new_color

    def set_border(self, new_bool: bool) -> None:
	"""
	Set the visibility of the label border.	

	Parameters
	----------
	new_bool : bool
		True or False
	"""
        self.border = new_bool

    def set_border_color(self, new_color: tuple) -> None:
	"""
	Set the color for the label border.
	
	Parameters
	----------
	new_color : tuple
		New RGB color for the label border
	"""
        self.border_color = new_color

    def set_border_thickness(self, new_thickness: int) -> None:
	"""
	Set the thickness of the label border

	Parameters
	----------
	new_thickness : int
		New thickness value for the label border
	"""
        self.border_thickness = new_thickness

    def show(self, surface) -> None:
	"""
	Display the label on the surface.

	Parameters
	----------
	surface : pygame.display.set_mode()
		The surface object created by pygame
	"""

        text_surface = pygame.font.Font(self.text_font, self.text_size).render(self.text, True, self.text_color)
        text_rectangle = text_surface.get_rect(center=(self.x, self.y))

        if self.background:
            pygame.draw.rect(surface, self.background_color, text_rectangle.inflate(self.text_padding, self.text_padding))

        if self.border:
            pygame.draw.rect(surface, self.border_color,
                             text_rectangle.inflate(self.text_padding, self.text_padding), self.border_thickness)

        surface.blit(text_surface, text_rectangle)
