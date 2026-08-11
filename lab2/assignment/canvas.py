import cv2


class Canvas:
    """Wraps an image loaded with OpenCV and lets you draw/write on it."""

    def __init__(self, path, color=(0, 255, 0), thickness=2):
        self.path = path
        self.color = color
        self.thickness = thickness

        # TODO: load the image at `path` with cv2.imread and store it
        # in self.image. If it failed to load (result is None), raise
        # a FileNotFoundError with a helpful message.
        self.image = None

    def draw_rectangle(self, top_left, bottom_right):
        # TODO: draw a rectangle on self.image from top_left to
        # bottom_right, using self.color and self.thickness.
        # Use cv2.rectangle.
        pass

    def draw_circle(self, center, radius):
        # TODO: draw a circle on self.image centered at `center` with
        # radius `radius`, using self.color and self.thickness.
        # Use cv2.circle.
        pass

    def put_text(self, text, position):
        # TODO: write `text` on self.image starting at `position`,
        # using cv2.putText. Use cv2.FONT_HERSHEY_SIMPLEX, a font
        # scale of 1 and self.color/self.thickness.
        pass

    def save(self, out_path):
        # TODO: write self.image to disk at `out_path` with cv2.imwrite
        pass

    def show(self, window_name="Canvas"):
        cv2.imshow(window_name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
