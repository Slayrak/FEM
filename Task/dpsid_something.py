import math


def psi_edge(eta, tau, local_vertex_coords):
    eta_i = local_vertex_coords[0]
    tau_i = local_vertex_coords[1]

    result = 0.25 * (1 + eta * eta_i) * (1 + tau * tau_i) * (eta * eta_i + tau * tau_i - 1)

    return result


def psi_5_7(eta, tau, local_vertex_coords):
    eta_i = local_vertex_coords[0]
    tau_i = local_vertex_coords[1]

    result = 0.5 * (1 - math.pow(eta, 2)) * (1 + tau * tau_i)

    return result


def psi_6_8(eta, tau, local_vertex_coords):
    eta_i = local_vertex_coords[0]
    tau_i = local_vertex_coords[1]

    result = 0.5 * (1 - math.pow(tau, 2)) * (1 + eta * eta_i)

    return result


def dpsi_d_eta_edge(eta, tau, local_vertex_coords):
    eta_i = local_vertex_coords[0]
    tau_i = local_vertex_coords[1]

    part1 = 0.25 * (1 + eta * eta_i) * (1 + tau * tau_i)
    part2 = (eta * eta_i + tau * tau_i - 1)

    result = 0.25 * eta_i * (1 + tau * tau_i) * part2 + part1 * eta_i
    return result


def dpsi_d_tau_edge(eta, tau, local_vertex_coords):
    eta_i = local_vertex_coords[0]
    tau_i = local_vertex_coords[1]

    part1 = 0.25 * (1 + eta * eta_i) * (1 + tau * tau_i)
    part2 = (eta * eta_i + tau * tau_i - 1)

    result = 0.25 * tau_i * (1 + eta * eta_i) * part2 + part1 * tau_i
    return result


def dpsi_d_eta_5_7(eta, tau, local_vertex_coords):
    eta_i = local_vertex_coords[0]
    tau_i = local_vertex_coords[1]

    result = 0.5 * (-2 * eta) * (1 + tau * tau_i)
    return result


def dpsi_d_tau_5_7(eta, tau, local_vertex_coords):
    eta_i = local_vertex_coords[0]
    tau_i = local_vertex_coords[1]

    result = 0.5 * (1 - math.pow(eta, 2)) * tau_i
    return result


def dpsi_d_eta_6_8(eta, tau, local_vertex_coords):
    eta_i = local_vertex_coords[0]
    tau_i = local_vertex_coords[1]

    result = 0.5 * (1 - math.pow(tau, 2)) * eta_i
    return result


def dpsi_d_tau_6_8(eta, tau, local_vertex_coords):
    eta_i = local_vertex_coords[0]
    tau_i = local_vertex_coords[1]

    result = 0.5 * (-2 * tau) * (1 + eta * eta_i)
    return result

