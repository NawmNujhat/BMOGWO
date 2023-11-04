import numpy as np

# Example data
obtained_set = np.array([[4.31827004, 2.74898285, 1.10449339],
                         [1.01137764, 2.07320038, 7.57305708],
                         [6.13401566, 3.79253743, 7.34972632],
                         [1.01137764, 2.07320038, 7.57305708],
                         [5.96085403, 4.43916562 ,8.46184180],
                         [1.01137764, 2.07320038, 7.57305708],
                         [3.68156417, 3.50546698, 9.60733386],
                         [1.01137764, 2.07320038, 7.57305708],
                         [6.28469921, 4.42943588, 3.99743467],
                         [1.32817385, 2.28029250, 7.51705951],
                         [4.31827004, 2.74898285, 1.10449339],
                         [1.32817385, 2.28029250, 7.51705951],
                         [6.13401566, 3.79253743, 7.34972632],
                         [1.32817385, 2.28029250 ,7.51705951]])  # Replace with your obtained set of solutions
true_pareto_front = np.array([[9.92036504, 1.34328355, 8.93697669],
                              [9.92036504, 1.34328355, 9.3697669],
                              [9.92036504, 1.34328355, 8.93697669],
                              [9.92036504, 1.34328355, 8.93697669],
                              [9.93275617, 1.70003581, 8.94641040],
                              [9.93275617, 1.70003581, 8.94641040],
                              [9.93275617, 1.70003581, 8.94641040],
                              [9.93275617, 1.70003581, 8.94641040],
                              [9.93275617, 1.70003581, 8.94641040],
                              [9.94096931, 2.28431104, 8.93460625],
                              [9.94096931, 2.28431104, 8.93460625],
                              [9.94096931, 2.28431104, 8.93460625],
                              [9.94096931, 2.28431104, 8.93460625],
                              [4.06176874, 1.99711363, 5.03831394]])  # Replace with the true Pareto front


# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))


# Calculate IGD
distances = []
print(obtained_set.shape)
print(true_pareto_front.shape)
for point in obtained_set:
    min_distance = min([euclidean_distance(point, true_point) for true_point in true_pareto_front])
    distances.append(min_distance)

igd_value = np.mean(distances)
print(f"The Inverted Generational Distance (IGD) is: {igd_value}")
