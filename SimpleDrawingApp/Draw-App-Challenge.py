import cv2

screenCapCounter = 0

cap = cv2.VideoCapture(0)
left_mouse_down = False
start = (0,0)
end = (0,0)
color = [False, False, False]

lines = []


class Tiny_Line:
    def __init__ (self, start, end, color):
        self.start = start
        self.end = end
        self.color = [0,0,0]
        for i in range(3):
            if color[i]:
                self.color[i] += 250

        self.color = tuple(self.color)


def click(event, x, y, flags, param) :
    global left_mouse_down, start, end
    if event == cv2.EVENT_LBUTTONDOWN:
        left_mouse_down = True
        start = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        left_mouse_down = False
    elif event == cv2.EVENT_MOUSEMOVE and left_mouse_down:
        end = (x, y)
        lines.append(Tiny_Line(start,end,color))
        start = end
        # print("button lifted")


cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)


while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    for l in lines:
        cv2.line(frame, l.start, l.end, l.color, thickness=5)
    cv2.imshow("Frame", frame)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('c'):
        lines = []
        print("lines cleared")
    elif ch & 0xFF == ord('p'):
        temp = "screenCap%d.png" % screenCapCounter
        cv2.imwrite(temp, frame)
        screenCapCounter += 1
    elif ch & 0xFF == ord('r'):
        color[0] = not color[0]
        print("Red =",color[0])
    elif ch & 0xFF == ord('g'):
        color[1] = not color[1]
        print("Green =", color[1])
    elif ch & 0xFF == ord('b'):
        color[2] = not color[2]
        print("Blue =", color[2])

    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()