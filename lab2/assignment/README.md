# Assignment 2 — Drawing with OpenCV

A small intro-to-classes exercise using OpenCV. You'll build a `Canvas`
class that loads an image and lets you draw shapes and text on it, using
what we covered in the session (functions, conditions) plus two new ideas:
**classes with attributes/methods** and the **OpenCV** library.

## Files

- `canvas.py` — the `Canvas` class. It wraps an image loaded with
  `cv2.imread` and has attributes (`image`, `color`, `thickness`) and
  methods to draw on it.
- `main.py` — loads `assets/sample.png` through a `Canvas`, draws a
  rectangle, a circle and some text, then saves and shows the result.
- `assets/sample.png` — the image to work with.

## Task

Complete the `TODO`s in `canvas.py`:

1. `__init__` — load the image at `self.path` with `cv2.imread` into
   `self.image`. If loading fails (`cv2.imread` returns `None`), raise
   a `FileNotFoundError`.
2. `draw_rectangle(top_left, bottom_right)` — draw a rectangle on
   `self.image` using `cv2.rectangle`, with `self.color` and
   `self.thickness`.
3. `draw_circle(center, radius)` — draw a circle using `cv2.circle`.
4. `put_text(text, position)` — write text on the image using
   `cv2.putText` (font: `cv2.FONT_HERSHEY_SIMPLEX`, scale `1`).
5. `save(out_path)` — write `self.image` to disk with `cv2.imwrite`.

Then run `python main.py` from inside `lab2/assignment/` — it should pop
up a window showing the sample image with a red rectangle, circle and
text on it, and also save it as `output.png`.

## Bonus (optional)

- Add a `line(start, end)` method.
- Add a `reset()` method that reloads the original image, so you can
  undo all your drawings.
- Track how many shapes have been drawn in a `self.shape_count`
  attribute and print it after running `main.py`.

Solutions live in `../soluations/` (not part of the repo — for your own
reference after you've had a try).
