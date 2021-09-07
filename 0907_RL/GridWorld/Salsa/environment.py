# environment.py : 강화 학습을 수행할 환경, 룰
# 여기를 공부할 때 environment를 읽어보는 것은 중요한 작업이 아닙니다.
# 실제 구현할 모델이 있을 때 초기상태, 동작, 동작에 따른 다음 상태를 가지고 직접 만들어야 합니다.

import time
import numpy as np
# python이 내장하고 있는 GUI 패키지입니다.
# mac에서 pycharm 을 실행하면 이 패키지의 이미지를 제대로 불러오지 못하는 경우가 있습니다.
import tkinter as tk
from PIL import ImageTk, Image

np.random.seed(1)
PhotoImage = ImageTk.PhotoImage
UNIT = 100  # 필셀 수
HEIGHT = 5  # 그리드 월드 가로
WIDTH = 5  # 그리드 월드 세로


class Env(tk.Tk):
    # 초기값 설정
    def __init__(self):
        super(Env, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('SARSA')
        self.geometry('{0}x{1}'.format(HEIGHT * UNIT, HEIGHT * UNIT))
        self.shapes = self.load_images()
        self.canvas = self._build_canvas()
        self.texts = []

    # 그래픽 출력을 위한 함수
    # 그래픽을 메모리에 출력합니다.
    def _build_canvas(self):
        canvas = tk.Canvas(self, bg='white',
                           height=HEIGHT * UNIT,
                           width=WIDTH * UNIT)
        # 그리드 생성
        for c in range(0, WIDTH * UNIT, UNIT):  # 0~400 by 80
            x0, y0, x1, y1 = c, 0, c, HEIGHT * UNIT
            canvas.create_line(x0, y0, x1, y1)
        for r in range(0, HEIGHT * UNIT, UNIT):  # 0~400 by 80
            x0, y0, x1, y1 = 0, r, HEIGHT * UNIT, r
            canvas.create_line(x0, y0, x1, y1)

        # 캔버스에 이미지 추가
        self.rectangle = canvas.create_image(50, 50, image=self.shapes[0])
        self.triangle1 = canvas.create_image(250, 150, image=self.shapes[1])
        self.triangle2 = canvas.create_image(150, 250, image=self.shapes[1])
        self.circle = canvas.create_image(250, 250, image=self.shapes[2])

        canvas.pack()

        return canvas

    # 이미지를 메모리에 불러옵니다
    def load_images(self):
        rectangle = PhotoImage(
            Image.open("../img/rectangle.png").resize((65, 65)))
        triangle = PhotoImage(
            Image.open("../img/triangle.png").resize((65, 65)))
        circle = PhotoImage(
            Image.open("../img/circle.png").resize((65, 65)))

        return rectangle, triangle, circle

    # 그래픽에 출력될 텍스트와 좌표 설정
    def text_value(self, row, col, contents, action, font='Helvetica', size=10,
                   style='normal', anchor="nw"):
        if action == 0:
            origin_x, origin_y = 7, 42
        elif action == 1:
            origin_x, origin_y = 85, 42
        elif action == 2:
            origin_x, origin_y = 42, 5
        else:
            origin_x, origin_y = 42, 77

        x, y = origin_y + (UNIT * col), origin_x + (UNIT * row)
        font = (font, str(size), style)
        text = self.canvas.create_text(x, y, fill="black", text=contents,
                                       font=font, anchor=anchor)
        return self.texts.append(text)

    # 텍스트를 캔버스에 출력하기 위한 함수입니다.
    def print_value_all(self, q_table):
        for i in self.texts:
            self.canvas.delete(i)
        self.texts.clear()
        for x in range(HEIGHT):
            for y in range(WIDTH):
                for action in range(0, 4):
                    state = [x, y]
                    if str(state) in q_table.keys():
                        temp = q_table[str(state)][action]
                        self.text_value(y, x, round(temp, 3), action)

    # 좌표 계산을 위한 함수
    # 좌표를 비율로 계산하는 경우가 있는데
    # 디바이스의 크기나 화면의 크기가 변경되더라도 비율을 유지하기 위해서입니다
    def coords_to_state(self, coords):
        x = int((coords[0] - 50) / 100)
        y = int((coords[1] - 50) / 100)
        return [x, y]

    # 전부 클리어하는 함수
    def reset(self):
        self.update()
        time.sleep(0.5)
        x, y = self.canvas.coords(self.rectangle)
        self.canvas.move(self.rectangle, UNIT / 2 - x, UNIT / 2 - y)
        self.render()
        return self.coords_to_state(self.canvas.coords(self.rectangle))

    # 행동을 취할 때 호출되는 함수
    def step(self, action):
        state = self.canvas.coords(self.rectangle)
        base_action = np.array([0, 0])
        self.render()

        if action == 0:  # 상
            if state[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:  # 하
            if state[1] < (HEIGHT - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:  # 좌
            if state[0] > UNIT:
                base_action[0] -= UNIT
        elif action == 3:  # 우
            if state[0] < (WIDTH - 1) * UNIT:
                base_action[0] += UNIT

        # 에이전트 이동
        self.canvas.move(self.rectangle, base_action[0], base_action[1])
        # 에이전트(빨간 네모)를 가장 상위로 배치
        self.canvas.tag_raise(self.rectangle)
        next_state = self.canvas.coords(self.rectangle)

        # 보상 함수
        if next_state == self.canvas.coords(self.circle):
            reward = 100
            done = True
        elif next_state in [self.canvas.coords(self.triangle1),
                            self.canvas.coords(self.triangle2)]:
            reward = -100
            done = True
        else:
            reward = 0
            done = False

        next_state = self.coords_to_state(next_state)
        return next_state, reward, done

    # 화면을 그리는 (랜더링) 함수
    def render(self):
        time.sleep(0.03)
        self.update()

