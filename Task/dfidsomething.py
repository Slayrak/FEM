import math


def dfid_alpha_edge(alpha, beta, gamma, local_vertex_coords):
    alpha_i = local_vertex_coords[0]
    beta_i = local_vertex_coords[1]
    gamma_i = local_vertex_coords[2]

    return 0.125 * (1 + beta * beta_i) * (1 + gamma * gamma_i) * (alpha_i
            * (2 * alpha * alpha_i + beta * beta_i + gamma * gamma_i - 1))


def dfid_beta_edge(alpha, beta, gamma, local_vertex_coords):
    alpha_i = local_vertex_coords[0]
    beta_i = local_vertex_coords[1]
    gamma_i = local_vertex_coords[2]

    return 0.125 * (1 + alpha * alpha_i) * (1 + gamma * gamma_i) * (beta_i
            * (alpha * alpha_i + 2 * beta * beta_i + gamma * gamma_i - 1))


def dfid_gamma_edge(alpha, beta, gamma, local_vertex_coords):
    alpha_i = local_vertex_coords[0]
    beta_i = local_vertex_coords[1]
    gamma_i = local_vertex_coords[2]

    return 0.125 * (1 + alpha * alpha_i) * (1 + beta * beta_i) * (gamma_i
            * (alpha * alpha_i + beta * beta_i + 2 * gamma * gamma_i - 1))


def dfid_alpha_rest(alpha, beta, gamma, local_vertex_coords):
    alpha_i = local_vertex_coords[0]
    beta_i = local_vertex_coords[1]
    gamma_i = local_vertex_coords[2]

    part1 = 0.25 * (1 + alpha * alpha_i) * (1 + beta * beta_i) * (1 + gamma * gamma_i)
    part2 = 1 - math.pow(alpha * beta_i * gamma_i, 2) - math.pow(beta * alpha_i * gamma_i, 2) - math.pow(gamma * alpha_i * beta_i, 2)

    return (0.25 * alpha_i * (1 + beta * beta_i) * (1 + gamma * gamma_i)) * part2 + (-2 * alpha * math.pow(beta_i, 2) * math.pow(gamma_i, 2)) * part1


def dfid_beta_rest(alpha, beta, gamma, local_vertex_coords):
    alpha_i = local_vertex_coords[0]
    beta_i = local_vertex_coords[1]
    gamma_i = local_vertex_coords[2]

    part1 = 0.25 * (1 + alpha * alpha_i) * (1 + beta * beta_i) * (1 + gamma * gamma_i)
    part2 = 1 - math.pow(alpha * beta_i * gamma_i, 2) - math.pow(beta * alpha_i * gamma_i, 2) - math.pow(
        gamma * alpha_i * beta_i, 2)

    return (0.25 * beta_i * (1 + alpha * alpha_i) * (1 + gamma * gamma_i)) * part2 + (-2 * beta * math.pow(alpha_i, 2) * math.pow(gamma_i, 2)) * part1


def dfid_gamma_rest(alpha, beta, gamma, local_vertex_coords):
    alpha_i = local_vertex_coords[0]
    beta_i = local_vertex_coords[1]
    gamma_i = local_vertex_coords[2]

    part1 = 0.25 * (1 + alpha * alpha_i) * (1 + beta * beta_i) * (1 + gamma * gamma_i)
    part2 = 1 - math.pow(alpha * beta_i * gamma_i, 2) - math.pow(beta * alpha_i * gamma_i, 2) - math.pow(
        gamma * alpha_i * beta_i, 2)

    return (0.25 * gamma_i * (1 + alpha * alpha_i) * (1 + beta * beta_i)) * part2 + (-2 * gamma * math.pow(alpha_i, 2) * math.pow(beta_i, 2)) * part1