#!/usr/bin/env python3
from manimlib import *
import numpy as np
import sys
sys.path.insert(0, '.') # shows same level 

from utils.stastical_functions import * 
from utils.monte_carlo_functions import *
from scipy import stats
from scipy import optimize




class MonteCarloPlotting(Scene):
    def construct(self):
        #vector_entries_text = Text("Plot Of x_1, x_2, x_3")
        # ill write this in the premiere project and AE
        T = 30
        d = 4
        T_text = Text("T = 30", font_size=40)
        d_text = Text("d = ", font_size=40)

        T_text.next_to(ORIGIN, UR + np.array((8,4,0)), buff=0.5)
        d_text.next_to(T_text, DOWN, buff=0.2)

        axes = Axes((-15, 15), (0, 5))
        
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        self.wait(1)
        self.play(Write(T_text))
        self.play(Write(d_text))

        dimension_distribution = {i: 1/d for i in range(d)}
        update_distribution = {-1: 1/2, 1: 1/2}
        values = monte_carlo_vector_entries(dimension_distribution, update_distribution)
        coords = create_histogram_coords(values, 30)

        def min_max_normalize(v):
            return (v - v.min()) / (v.max() - v.min())
            
        normalized_coords = [30* min_max_normalize(coords[0]) - 15 , 5*min_max_normalize(coords[1])]

        for coord in zip(*normalized_coords):
            if coord[1] == 0:
                continue
            dot = Dot(color=RED)
            dot.move_to(axes.c2p(coord[0], coord[1]))
            self.play(FadeIn(dot, scale=0.5, run_time=0.07))
        # this one makes a dot fade in slowly but could make it faster

        lbf_graph = axes.get_graph(
            lambda x: 5*math.exp(-1*((x)**2)/(1.2*math.sqrt(T)**2)), #test_func(x, params[0], params[1]),
            color=BLUE,
        )

        self.play(
            ShowCreation(lbf_graph),
        )


