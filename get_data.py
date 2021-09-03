import os

import numpy as np
from biomass.dynamics.solver import *
from tqdm import tqdm

from model import *


def compute_matrix():
    os.makedirs("data", exist_ok=True)

    sim_n = 101
    sim_t = range(5401)
    sim_ligand = ["EGF", "HRG"]

    z_cFosmRNA = np.empty((len(sim_ligand), sim_n, len(sim_t)))
    norm_max = np.empty_like(sim_ligand, dtype=float)
    x = param_values()
    y0 = initial_values()
    y_ss = get_steady_state(diffeq, y0, tuple(x))
    for i in tqdm(range(sim_n)):
        x = param_values()
        x[C.p11] *= (1 - 0.01 * i)
        for j, ligand in enumerate(sim_ligand):
            x[C.Ligand] = x[C.NAMES.index(ligand)]
            sol = solve_ode(diffeq, y_ss, sim_t, tuple(x))
            if i == 0:
                norm_max[j] = np.max(sol.y[V.cfosmRNAc, :])
            z_cFosmRNA[j, i, :] = sol.y[V.cfosmRNAc, :] / norm_max[j]

    np.save(os.path.join("data", "z_cFosmRNA.npy"), z_cFosmRNA)
