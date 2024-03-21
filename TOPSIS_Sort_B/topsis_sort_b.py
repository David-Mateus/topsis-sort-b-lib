import numpy as np

# Decision Matrix Normalization
def decision_matrix_normalization(decision_matrix, domain_matrix, weights):
    R = np.zeros_like(decision_matrix)
    for i in range(decision_matrix.shape[0]):
        for j in range(decision_matrix.shape[1]):
            # Avoiding division by zero
            R[i, j] = decision_matrix[i, j] / max(domain_matrix[0, j], np.finfo(float).eps)
    V = np.zeros_like(R)
    for i in range(V.shape[0]):
        for j in range(V.shape[1]):
            V[i, j] = weights[j] * R[i, j]
    return V
def approximation_coefficient(decision_matrix, domain_matrix, weights):
    V = decision_matrix_normalization(decision_matrix, domain_matrix, weights)
    # Ideal and Anti-Ideal Solutions Calculation
    V_ideal = np.max(V, axis=0)
    V_anti_ideal = np.min(V, axis=0)

    # Euclidean Distances Calculation
    d_plus = np.zeros(decision_matrix.shape[0])
    d_minus = np.zeros(decision_matrix.shape[0])

    for i in range(decision_matrix.shape[0]):
        d_plus[i] = np.sqrt(np.sum((V[i, :] - V_ideal)**2))
        d_minus[i] = np.sqrt(np.sum((V[i, :] - V_anti_ideal)**2))

    # Avoiding division by zero
    d_plus[d_plus == 0] = np.finfo(float).eps
    d_minus[d_minus == 0] = np.finfo(float).eps

    # Approximation Coefficient Calculation
    Cl = d_minus / (d_plus + d_minus)
    return Cl

def dominant_profiles_distances(decision_matrix, domain_matrix, dominant_profiles, weights):
    dominant_profiles_normalized = np.zeros_like(dominant_profiles)
    for i in range(dominant_profiles.shape[0]):
        for j in range(dominant_profiles.shape[1]):
            dominant_profiles_normalized[i, j] = dominant_profiles[i, j] / domain_matrix[0, j]

    V_profiles = np.zeros_like(dominant_profiles_normalized)
    for i in range(V_profiles.shape[0]):
        for j in range(V_profiles.shape[1]):
            V_profiles[i, j] = weights[j] * dominant_profiles_normalized[i, j]

    # Dominant Profiles Distances Calculation
    V_ideal_profiles = np.max(V_profiles, axis=0)
    V_anti_ideal_profiles = np.min(V_profiles, axis=0)

    d_plus_profiles = np.zeros(dominant_profiles.shape[0])
    d_minus_profiles = np.zeros(dominant_profiles.shape[0])
    for k in range(dominant_profiles.shape[0]):
        d_plus_profiles[k] = np.sqrt(np.sum((V_profiles[k, :] - V_ideal_profiles)**2))
        d_minus_profiles[k] = np.sqrt(np.sum((V_profiles[k, :] - V_anti_ideal_profiles)**2))

    # Avoiding division by zero
    d_plus_profiles[d_plus_profiles == 0] = np.finfo(float).eps
    d_minus_profiles[d_minus_profiles == 0] = np.finfo(float).eps

    # Dominant Profiles Approximation Coefficient Calculation
    Cl_profiles = d_minus_profiles / (d_plus_profiles + d_minus_profiles)
    return Cl_profiles

def topsis_b_sort_profile_classification(decision_matrix, domain_matrix, dominant_profiles, weights):
    Cl = approximation_coefficient(decision_matrix, domain_matrix, weights)
    Cl_profiles = dominant_profiles_distances(decision_matrix, domain_matrix, dominant_profiles, weights)
    
    C = np.zeros((decision_matrix.shape[0], 2))
    for i in range(decision_matrix.shape[0]):
        if Cl[i] >= Cl_profiles[0]:
            C[i, 0] = 1
        else:
            for k in range(1, dominant_profiles.shape[0]):
                if Cl_profiles[k-1] > Cl[i] >= Cl_profiles[k]:
                    C[i, 0] = k + 1
                    break
        C[i, 1] = Cl[i]

    best_solution_index = np.argmax(C[:, 1])  
    best_solution = decision_matrix[best_solution_index] 
    best_profile = int(C[best_solution_index, 0])  

    return C, best_solution, best_profile

# Leitura dos dados do arquivo
# data = np.loadtxt('./advertising.csv', delimiter=',', skiprows=1)
# # Matriz de decisão (excluindo a última coluna que representa as vendas)
# decision_matrix = data[:, :-1]

# decision_matrix = np.array([[10,30,40,40], [10,20,30,4], [100,20,30,40], [1,2,4,5]])
# dominant_profiles = np.array([[1, 11, 5,5]])
# domain_matrix = np.array([[1, 1, 1,1], [100, 100, 100,100]])
# weights = np.array([0.2, 0.2, 0.3, 0.3])
# classification_result, best_solution, best_profile = topsis_b_sort_profile_classification(decision_matrix, domain_matrix, dominant_profiles, weights)
#
# print("Classification Result:")
# print(classification_result)
# print("Best Solution:")
# print(best_solution)
# print("Dominant Profile of the Best Solution:", best_profile)