class Dance:
    def __init__(self, name, difficulty, video_url):
        self.name = name
        self.difficulty = difficulty
        self.video_url = video_url
    
    def __str__(self):
        return f"{self.name} (Difficulty: {self.difficulty})"
