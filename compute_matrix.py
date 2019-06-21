import numpy as np
from scipy.integrate import ode


def solveode(diffeq,y0,tspan,args):
    sol = ode(diffeq)
    sol.set_integrator('vode',method='bdf',min_step=1e-8,with_jacobian=True)
    sol.set_initial_value(y0,tspan[0])
    sol.set_f_params(args)

    T = [tspan[0]]
    Y = [y0]

    while sol.successful() and sol.t < tspan[-1]:
        sol.integrate(sol.t+1.)
        T.append(sol.t)
        Y.append(sol.y)

    return np.array(T),np.array(Y)


def compute_matrix():
    # setInitial
    y0 = initial_values()

    sim_n = 101
    sim_t = range(5401)

    # EGF-induced
    z_cFosmRNA_egf = np.empty((len(sim_t),sim_n))
    for i in range(sim_n):
        x = f_params()
        x[Ligand] = x[EGF]
        x[p11] = x[p11]*(1-0.01*i)
        (T,Y) = solveode(diffeq,y0,sim_t,tuple(x))
        if i==0:
            norm_max = np.max(Y[:,cfosmRNAc])
        z_cFosmRNA_egf[:,i] = Y[:,cfosmRNAc]/norm_max
    np.save('data/z_cFosmRNA_egf.npy',z_cFosmRNA_egf)

    # HRG-induced
    z_cFosmRNA_hrg = np.empty((len(sim_t),sim_n))
    for i in range(sim_n):
        x = f_params()
        x[Ligand] = x[HRG]
        x[p11] = x[p11]*(1-0.01*i)
        (T,Y) = solveode(diffeq,y0,sim_t,tuple(x))
        if i==0:
            norm_max = np.max(Y[:,cfosmRNAc])
        z_cFosmRNA_hrg[:,i] = Y[:,cfosmRNAc]/norm_max
    np.save('data/z_cFosmRNA_hrg.npy',z_cFosmRNA_hrg)