import OpenGL
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU
print("Imports successful!") 
def showScreen():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)

glut.glutInit() # Initialize a glut instance which will allow us to customize our window
glut.glutInitDisplayMode(glut.GLUT_RGBA) # Set the display mode to be colored
glut.glutInitWindowSize(500, 500)   # Set the width and height of your window
glut.glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glut.glutCreateWindow("OpenGL Coding Practice") # Give your window a title
glut.glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
glut.glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times
glut.glutMainLoop()  # Keeps the window created above displaying/running in a loop