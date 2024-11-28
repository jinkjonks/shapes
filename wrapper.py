from vispy.scene import Node, SceneCanvas
from vispy.scene.cameras import TurntableCamera


IMAGE_SHAPE = (600, 800)  # (height, width)
CANVAS_SIZE = (800, 600)  # (width, height)
NUM_LINE_POINTS = 500


class Shape:
    def __init__(self, plot: type[Node]) -> None:
        self.canvas = SceneCanvas(
            size=CANVAS_SIZE,
            vsync=True,
        )

        self.view = self.canvas.central_widget.add_view()
        camera = TurntableCamera(
            fov=60, elevation=30, azimuth=50, parent=self.view.scene
        )
        camera.set_range((-4, 4), (-4, 4), (-4, 4))

        self.view.camera = camera
        # self.view.add(XYZAxis())
        self.view.add(plot)
