import pygame

# Import the default text font
from settings import FONT


class Button:
    """
    Create a Button object.

    Attributes
    ----------
    text : str
        Text of the button
    text_size : int
        Size of the text
    text_font : str
        Font of the text
    text_color : tuple
        RGB value of text color
    x : int
        Position by x coordinate
    y : int
        Position by y coordinate
    width : int
        Width of the button
    height : int
        Height of the button
    background_color : tuple
        RGB value for background color
    background_surface : pygame.Surface()
        The surface object of the background
    background_rectangle : pygame.Surface().get_rect()
        The rectangle of the background, drawn on background_surface
    border : bool
        True/False, draw a border around the button
    border_color : tuple
        RGB value for border color
    border_thickness : int
        Thickness of the border
    already_clicked : bool
        True/False, prevents multiple reads of one click of the button
    click_reaction : func
        Calls func() when the button is clicked

    Methods
    -------
    set_text(new_text)
        Set the new text displayed on the button
    set_text_size(new_size)
        Set the size of the text
    set_text_font(new_font)
        Set the font of the text
    set_text_color(new_color)
        Set the color of the text
    set_position(new_x, new_y)
        Set the position of the button
    set_size(new_width, new_height)
        Set the size of the button
    set_background_color(new_color)
        Set the color of the background
    set_border_color(new_color)
        Set the color of the border
    set_border_thickness(new_thickness)
        Set the thickness of the border
    hover()
        Check if the cursor collides with the button
    clicked()
        Check if the button is clicked and call click_reaction()
    connect(func)
        Connect a function to be called when the button is clicked
    show(surface)
        Display the button on the surface
    """
    def __init__(self, text, pos_x, pos_y, width, height):
        """
        Parameters
        ----------
        text : str
            Text of the button
        pos_x : int
            The position of the button on the x-axis
        pos_y : int
            The position of the button on the y-axis
        width : int
            The width of the button
        height : int
            The height of the button
        """
        self.text = text
        self.text_size = 15
        self.text_font = FONT
        self.text_color = (0, 0, 0)

        self.x = pos_x
        self.y = pos_y

        self.width = width
        self.height = height

        self.background_color = (0, 255, 255)
        self.background_surface = None
        self.background_rectangle = None

        self.border = True
        self.border_color = (0, 255, 0)
        self.border_thickness = 5

        # mouse events
        self.already_clicked = False
        self.click_reaction = None

    def set_text(self, new_text: str) -> None:
        """
        Set the text of the button.

        Parameters
        ----------
        new_text : str
            New text of the button
        """
        self.text = new_text

    def set_text_size(self, new_size: int) -> None:
        """
        Set the size of the text.

        Parameters
        ----------
        new_size : int
            New size for text
        """
        self.text_size = new_size

    def set_text_font(self, new_font: str) -> None:
        """
        Set the font of the text.

        Parameters
        ----------
        new_font : str
            Path to a *.ttf file
        """
        self.text_font = new_font

    def set_text_color(self, new_color: tuple) -> None:
        """
        Set the color of the text.

        Parameters
        ----------
        new_color : tuple
            RGB value for color
        """
        self.text_color = new_color

    def set_position(self, new_x: int or None, new_y: int or None) -> None:
        """
        Set the position of the button.

        Parameters
        ----------
        new_x : int or None
            New x coordinate for the button, None leaves the value unchanged
        new_y : int or None
            New y coordinate for the button, None leaves the value unchanged
        """
        if new_x:
            self.x = new_x
        if new_y:
            self.y = new_y

    def set_size(self, new_width, new_height: int) -> None:
        """
        Set the size of the button.

        Parameters
        ----------
        new_width : int or None
            New width of the button, None leaves the value unchanged
        new_height : int or None
            New height of the button, None leaves the value unchanged
        """
        if new_width:
            self.width = new_width
        if new_height:
            self.height = new_height

    def set_background_color(self, new_color: int) -> None:
        """
        Set the color of the background.

        Parameters
        ----------
        new_color : tuple
            RGB value for color
        """
        self.background_color = new_color

    def set_border_color(self, new_color: tuple) -> None:
        """
        Set the color of the border.

        Parameters
        ----------
        new_color : tuple
            RGB value for color
        """
        self.border_color = new_color

    def set_border_thickness(self, new_thickness: int) -> None:
        """
        Set the thickness of the border.

        Parameters
        ----------
        new_thickness : int
            New border thickness
        """
        self.border_thickness = new_thickness

    def hover(self) -> bool:
        """
        Check if the cursor collides with the button.
        """
        if self.background_rectangle.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False

    def clicked(self) -> None:
        """
        Check if the button is clicked.

        Sets already_clicked to True until the mouse button is released,
        then it sets already_clicked to False.
        If click_reaction is not None, call it.
        """
        if self.hover() and pygame.mouse.get_pressed()[0] and not self.already_clicked:
            if self.click_reaction is not None:
                self.click_reaction()

            self.already_clicked = True

        elif not pygame.mouse.get_pressed()[0]:
            self.already_clicked = False

    def connect(self, func) -> None:
        """
        Connects a function to the button.

        Parameters
        ----------
        func : function
            A new function
        """
        self.click_reaction = func

    def show(self, surface) -> None:
        """
        Display the button on the surface.

        Parameters
        ----------
        surface : pygame.display.set_mode()
            The surface object created by pygame
        """

        # Create the surface of the text and get its rectangle to be displayed on the surface
        text_surface = pygame.font.Font(self.text_font, self.text_size).render(self.text, True, self.text_color)
        text_rectangle = text_surface.get_rect(center=(self.x, self.y))

        # Create the surface of the background depending on the values of width and height
        self.background_surface = pygame.Surface((self.width, self.height))
        # Fill the surface with the color of background_color
        self.background_surface.fill(self.background_color)
        # Get the rectangle of the surface so it can be drawn on the screen
        self.background_rectangle = self.background_surface.get_rect(center=(self.x, self.y))
        # Check if the mouse is clicked
        self.clicked()
        # Draw the background of the button on surface
        surface.blit(self.background_surface, self.background_rectangle)
        # Check if the cursor collides with the button
        if self.hover():
            # If so, draw the border
            pygame.draw.rect(surface,
                             self.border_color,
                             pygame.Rect(pygame.Surface((self.width, self.height)).get_rect(center=(self.x, self.y))),
                             self.border_thickness)
        # Draw the button on the surface
        surface.blit(text_surface, text_rectangle)
