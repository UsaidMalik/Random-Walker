#!/usr/bin/env python3
from manimlib import *
import numpy as np
from utils.stastical_functions import * 

class MonteCarloPlotting(Scene):
    def construct(self):
        #vector_entries_text = Text("Plot Of x_1, x_2, x_3")
        # ill write this in the premiere project and AE
        T_text = Text("T = 30", font_size=40)
        d_text = Text("d = 4", font_size=40)

        T_text.next_to(ORIGIN, UR + np.array((8,4,0)), buff=0.5)
        d_text.next_to(T_text, DOWN, buff=0.2)

       # VGroup(T_text, d_text).arrange(UL)
        axes = Axes((0, 10), (0, 10))
        axes.add_coordinate_labels()
        
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        self.wait(1)
        self.play(Write(T_text))
        self.play(Write(d_text))


        d = 3
        dimension_distribution = {i: 1/d for i in range(d)}
        update_distribution = {-1: 1/2, 1: 1/2}
        values = monte_carlo_vector_entries(dimension_distribution, update_distribution)
        coords = create_histogram_coords(values, 30)
        print(coords)
        lbf_coords = create_line_of_best_fit(coords[0], coords[1])
        print(lbf_coords)


    