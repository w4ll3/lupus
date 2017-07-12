import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label('Hello world',
                          font_name='Times New Roman',
                          font_size=24,
                          x=window.width // 2,
                          y=window.height // 2,
                          anchor_x='center',
                          anchor_y='center')
@window.event
def on_draw():
    window.clear()
    label.draw()
    pyglet.graphics.draw(2, pyglet.graphics.gl.GL_LINES, )

pyglet.app.run()