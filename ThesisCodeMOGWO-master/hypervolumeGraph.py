import numpy as np


# Assuming pf is the obtained Pareto front and ref_point is the reference point
# Example data
# Assuming 'pf' is the obtained Pareto front and 'ref_point' is the reference point
pf = np.array([[9.92036504 ,1.34328355 ,8.93697669],
[9.92036504,1.34328355 ,9.3697669],
[9.92036504 , 1.34328355 ,8.93697669],
[9.92036504 ,1.34328355 ,8.93697669],
[9.93275617 ,1.70003581 ,8.94641040],
[9.93275617 ,1.70003581 ,8.94641040],
[9.93275617, 1.70003581 ,8.94641040],
[9.93275617 ,1.70003581, 8.94641040],
[9.93275617, 1.70003581, 8.94641040],
[9.94096931 ,2.28431104 ,8.93460625],
[9.94096931 ,2.28431104, 8.93460625],
[9.94096931 ,2.28431104 ,8.93460625],
[9.94096931 ,2.28431104 ,8.93460625],
[9.94096931 ,2.28431104, 8.93460625],
[4.06176874 ,1.99711363, 5.03831394]])  # Replace with your obtained Pareto front
ref_point = [9.94096931, 2.28431104 ,8.94641040]  # Replace with your chosen reference point

# Calculate the hypervolume
hyp =Hypervolume(ref_point)
result=hyp.do(pf)
print(result)