"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and JaeJung Hyun.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():


    two_circles()
    circle_and_rectangle()
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def two_circles():

    width = 1000
    height = 500
    window = rg.RoseWindow(width, height)

    center_point = rg.Point(300, 250)
    radius = 100
    qw = rg.Circle(center_point, radius)
    qw.fill_color = 'blue'
    qw.attach_to(window)

    center_point1 = rg.Point(600, 250)
    radius1 = 200
    wq = rg.Circle(center_point1, radius1)
    wq.attach_to(window)

    window.render()
    window.close_on_mouse_click()








    """
    
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():

    width = 1000
    height = 500
    window = rg.RoseWindow(width, height)

    center_point = rg.Point (400,250)
    radius = 150

    we = rg.Circle(center_point, radius)
    we.pen = rg.Pen('black', 5)
    we.fill_color = 'blue'
    we.attach_to(window)



    point1= rg.Point(700,300)
    point2= rg.Point(600,200)
    ew = rg.Rectangle(point1,point2)
    ew.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
