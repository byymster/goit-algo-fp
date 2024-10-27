import turtle
import math


# Функція для малювання гілок дерева Піфагора
def draw_branch(t, branch_length, level):
    if level == 0:
        return

    # Малюємо основну гілку
    t.forward(branch_length)

    # Зберігаємо початкову позицію і кут
    position = t.position()
    heading = t.heading()

    # Ліва гілка
    t.left(45)
    draw_branch(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Відновлюємо позицію і кут
    t.setposition(position)
    t.setheading(heading)

    # Права гілка
    t.right(45)
    draw_branch(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Повертаємося назад до основи
    t.setposition(position)
    t.setheading(heading)


# Основна функція для створення фрактала "дерево Піфагора"
def pythagoras_tree(level):
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Повертаємо черепашку вгору
    t.penup()
    t.setposition(0, -300)
    t.pendown()

    draw_branch(t, 200, level)

    screen.mainloop()


# Запит рівня рекурсії у користувача
if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
    pythagoras_tree(level)
