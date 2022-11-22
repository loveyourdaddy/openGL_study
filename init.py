import OpenGL
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU
# print("Imports successful!") 

def iterate():
    gl.glViewport(0, 0, 500, 500)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    gl.glMatrixMode (gl.GL_MODELVIEW)
    gl.glLoadIdentity()

def square():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    gl.glBegin(gl.GL_QUADS) # Begin the sketch
    gl.glVertex2f(100, 100) # Coordinates for the bottom left point
    gl.glVertex2f(200, 100) # Coordinates for the bottom right point
    gl.glVertex2f(200, 200) # Coordinates for the top right point
    gl.glVertex2f(100, 200) # Coordinates for the top left point
    gl.glEnd() # Mark the end of drawing

def showScreen():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    gl.glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    gl.glColor3f(1.0, 0.0, 3.0) # Set the color to pink
    square() # Draw a square using our function
    glut.glutSwapBuffers()

glut.glutInit() # Initialize a glut instance which will allow us to customize our window
glut.glutInitDisplayMode(glut.GLUT_RGBA) # Set the display mode to be colored
glut.glutInitWindowSize(500, 500)   # Set the width and height of your window
glut.glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glut.glutCreateWindow("OpenGL Coding Practice") # Give your window a title
glut.glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
glut.glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times
glut.glutMainLoop()  # Keeps the window created above displaying/running in a loop