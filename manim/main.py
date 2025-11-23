from manim import *


from manim import *

class Clase(Scene):
    def construct(self):
        title = Text("Clase's Out of Zone Rate", font_size=48)
        equations = [
            MathTex(r"2022: \frac{117}{233} = 0.502145"),
            MathTex(r"2023: \frac{119}{260} = 0.457692"),
            MathTex(r"2024: \frac{100}{241} = 0.414937"),
        ]
        
        # Position title at top
        title.to_edge(UP, buff=0.5)
        
        # Arrange equations with custom spacing
        VGroup(*equations).arrange(DOWN, buff=0.8).next_to(title, DOWN, buff=1)
        
        # Animate title first
        self.play(Write(title), run_time=1)
        
        # Then animate equations sequentially
        for eq in equations:
            self.play(Write(eq), run_time=1)
        
        self.wait(1)