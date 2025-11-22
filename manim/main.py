from manim import *


class FRVWeightsLoop(Scene):
    def construct(self):
        equations = [
            MathTex(r".9 \text{ OAA}"),
            MathTex(r"+ \text{ Fielder Throwing Runs}"),
            MathTex(r"+ .25 \text{ Blocks Saved}"),
            MathTex(r"+ .25 \text{ Blocks Saved}"),
            MathTex(r"+ .125 \text{ Strikes Saved}"),
            MathTex(r"+ .65 \text{ SB Prevented}"),
            MathTex(r"+ .4 \text{ Double Plays Added}")
        ]
        
        # Position equations
        for i, eq in enumerate(equations):
            eq.move_to(UP * (3 - i))
        
        # Animate sequentially
        for eq in equations:
            self.play(Write(eq), run_time = 1.44)
            #self.wait(0.1)
        
        self.wait(1)