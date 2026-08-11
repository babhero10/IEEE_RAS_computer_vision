from canvas import Canvas


def main():
    canvas = Canvas("assets/sample.png", color=(0, 0, 255), thickness=2)

    canvas.draw_rectangle((50, 50), (200, 200))
    canvas.draw_circle((300, 150), 60)
    canvas.put_text("OpenCV!", (50, 250))

    canvas.save("output.png")
    canvas.show()


if __name__ == "__main__":
    main()
