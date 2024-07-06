from dance.py import Dance

class Lesson:
    def __init__(self, dance, steps):
        self.dance = dance
        self.steps = steps
    
    def __str__(self):
        return f"Lesson for {self.dance.name}:\nSteps: {', '.join(self.steps)}"

# 示例课程
def create_lessons():
    lesson1 = Lesson(Dance("Salsa", "Intermediate", "http://example.com/salsa.mp4"), ["Step 1", "Step 2", "Step 3"])
    lesson2 = Lesson(Dance("Tango", "Advanced", "http://example.com/tango.mp4"), ["Step A", "Step B", "Step C"])
    return [lesson1, lesson2]
