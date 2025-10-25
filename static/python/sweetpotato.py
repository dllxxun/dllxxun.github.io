import turtle as t
import random
# 화면 설정
screen = t.Screen()
screen.title("파이썬 고구마 그리기")
screen.setup(width=600, height=400)
screen.bgcolor("skyblue")

# 기본 설정
t.speed(7)
t.pensize(3)

# 색상 설정
skin = "#A64CA6"     # 자색고구마 껍질색
flesh = "#CDA4DE"    # 속살색
leaf = "#2E8B57"
eye = "black"
mouth = "red"

# 고구마 몸통
t.penup()
t.goto(40,-80)
t.pendown()
t.color(skin)
t.begin_fill()
t.setheading(45)
t.circle(130, 90)
t.circle(70, 90)
t.circle(130, 90)
t.circle(70, 90)
t.end_fill()

# 잎사귀 1
t.penup()
t.goto(-30, 90)
t.pendown()
t.color(leaf)
t.begin_fill()
t.setheading(120)
t.circle(60, 80)
t.left(100)
t.circle(60, 80)
t.end_fill()

# 잎사귀 2
t.penup()
t.goto(-10, 80)
t.pendown()
t.begin_fill()
t.setheading(60)
t.circle(60, 80)
t.left(100)
t.circle(60, 80)
t.end_fill()

# --- 얼굴 부분 ---
# 왼쪽 눈
t.penup()
t.goto(-35, 30)
t.pendown()
t.color(eye)
t.begin_fill()
t.circle(5)
t.end_fill()

# 오른쪽 눈
t.penup()
t.goto(35, 30)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

# 입
t.penup()
t.goto(-25, -10)
t.setheading(-60)
t.pendown()
t.color(mouth)
t.width(4)
t.circle(30, 120)  # 웃는 입

# --- 팔 ---
t.color(skin)
t.width(8)

# 왼팔
t.penup()
t.goto(-80, 0)
t.pendown()
t.setheading(160)
t.forward(50)

# 오른팔
t.penup()
t.goto(80, 0)
t.pendown()
t.setheading(20)
t.forward(50)

# --- 다리 ---
# 왼다리
t.penup()
t.goto(-40, -80)
t.pendown()
t.setheading(-90)
t.forward(50)

# 오른다리
t.penup()
t.goto(40, -80)
t.pendown()
t.forward(50)

t.hideturtle()
t.done()
