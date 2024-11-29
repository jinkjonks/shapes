from vispy.io import write_png
from vispy.scene import Node, SceneCanvas
from vispy.scene.cameras import TurntableCamera


IMAGE_SHAPE = (600, 800)  # (height, width)
CANVAS_SIZE = (800, 600)  # (width, height)
NUM_LINE_POINTS = 500


class Shape(SceneCanvas):
    def __init__(self, plot: type[Node]) -> None:
        super().__init__(size=CANVAS_SIZE, vsync=True)
        view = self.central_widget.add_view()
        camera = TurntableCamera(fov=60, elevation=30, azimuth=50, parent=view.scene)
        camera.set_range((-4, 4), (-4, 4), (-4, 4))

        view.camera = camera
        # self.view.add(XYZAxis())
        view.add(plot)

    def on_close(self, event):
        img = self.canvas.render()
        write_png(f"./out/{__module__}.png", img)
