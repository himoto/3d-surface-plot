import numpy as np
from scipy.integrate import ode

from model import *


def _solveode(diffeq, y0, tspan, args):
    sol = ode(diffeq)
    sol.set_integrator(
        'vode', method='bdf', with_jacobian=True,
        atol=1e-9, rtol=1e-9, min_step=1e-8
    )
    sol.set_initial_value(y0, tspan[0])
    sol.set_f_params(args)

    T = [tspan[0]]
    Y = [y0]

    while sol.successful() and sol.t < tspan[-1]:
        sol.integrate(sol.t + 1.)
        T.append(sol.t)
        Y.append(sol.y)

    return np.array(T), np.array(Y)


def compute_matrix():
    # setInitial
    y0 = initial_values()

    sim_n = 101
    sim_t = range(5401)

    # EGF-induced
    z_cFosmRNA_egf = np.empty((len(sim_t), sim_n))
    for i in range(sim_n):
        x = param_values()
        x[C.Ligand] = x[C.EGF]
        x[C.p11] = x[C.p11] * (1-0.01*i)
        (T, Y) = _solveode(diffeq, y0, sim_t, tuple(x))
        if i == 0:
            norm_max = np.max(Y[:,V.cfosmRNAc])
        z_cFosmRNA_egf[:,i] = Y[:,V.cfosmRNAc] / norm_max
    np.save('data/z_cFosmRNA_egf.npy', z_cFosmRNA_egf)

    # HRG-induced
    z_cFosmRNA_hrg = np.empty((len(sim_t), sim_n))
    for i in range(sim_n):
        x = param_values()
        x[C.Ligand] = x[C.HRG]
        x[C.p11] = x[C.p11] * (1-0.01*i)
        (T,Y) = _solveode(diffeq, y0, sim_t, tuple(x))
        if i==0:
            norm_max = np.max(Y[:,V.cfosmRNAc])
        z_cFosmRNA_hrg[:,i] = Y[:,V.cfosmRNAc] / norm_max
    np.save('data/z_cFosmRNA_hrg.npy', z_cFosmRNA_hrg)

if __name__ == "__main__":
    compute_matrix()