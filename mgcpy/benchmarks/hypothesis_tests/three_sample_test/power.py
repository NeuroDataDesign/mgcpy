import numpy as np
import math
from mgcpy.hypothesis_tests.transforms import k_sample_transform


def generate_three_two_d_gaussians(epsilon, num_samples, type=1):
    '''
    Three 2D Gaussians:
        - Type 1: all with same mean and covariance. mean = [0, 0] and cov = I
        - Type 2: two with same mean and covariance. mean = [0, 0] and cov = I; thrid: mean = [0, epsilon], cov = I
        - Type 3: mean1 = [0, 0], mean2 = [0, epsilon], mean3 = [(sqrt(3)*epsilon)/2, epsilon/2]
                  means 1, 2, and 3 should form an equvilateral triangle in 2d plane with cov = I.
    '''
    # default mean zeros
    mean_one, mean_two, mean_three = [0, epsilon], [0, epsilon], [0, epsilon]

    if type == 2:
        mean_one, mean_two, mean_three = [0, 0], [0, 0], [0, epsilon]
    elif type == 3:
        mean_one, mean_two, mean_three = [0, 0], [0, epsilon], [(np.sqrt(3)*epsilon)/2, epsilon/2]

    cov = [[1, 0], [0, 1]]  # identity matrix
    one = np.random.multivariate_normal(mean_one, cov, num_samples)
    two = np.random.multivariate_normal(mean_two, cov, num_samples)
    three = np.random.multivariate_normal(mean_three, cov, num_samples)

    return one, two, three


def power_given_epsilon(independence_test, simulation_type, epsilon, repeats=1000, alpha=.05, additional_params={}):
    # test statistics under the null, used to estimate the cutoff value under the null distribution
    test_stats_null = np.zeros(repeats)

    # test statistic under the alternative
    test_stats_alternative = np.zeros(repeats)

    for rep in range(repeats):
        matrix_X, matrix_Y, matrix_Z = generate_three_two_d_gaussians(epsilon, 100, simulation_type)

        data = np.concatenate([matrix_X, matrix_Y, matrix_Z], axis=0)
        labels = np.concatenate([np.repeat(1, matrix_X.shape[0]), np.repeat(2, matrix_Y.shape[0]), np.repeat(3, matrix_Z.shape[0])], axis=0).reshape(-1, 1)

        matrix_U, matrix_V = k_sample_transform(data, labels, is_y_categorical=True)

        # permutation test
        permuted_V = np.random.permutation(matrix_V)
        test_stats_null[rep], _ = independence_test.test_statistic(
            matrix_U, permuted_V, **additional_params)
        test_stats_alternative[rep], _ = independence_test.test_statistic(
            matrix_U, matrix_V, **additional_params)

    # the cutoff is determined so that 1-alpha of the test statistics under the null distribution
    # is less than the cutoff
    cutoff = np.sort(test_stats_null)[math.ceil(repeats*(1-alpha))]

    # the proportion of test statistics under the alternative which is no less than the cutoff (in which case
    # the null is rejected) is the empirical power
    empirical_power = np.where(test_stats_alternative >= cutoff)[0].shape[0] / repeats

    return empirical_power
