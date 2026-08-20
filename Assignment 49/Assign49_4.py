from sklearn.preprocessing import StandardScaler
import numpy as np
from scipy.spatial import distance

# Original points
P1 = np.array([25, 20000])
P2 = np.array([35, 80000])

# Distance before scaling
dist_before = distance.euclidean(P1, P2)

print('-'* 40)
print("Distance before scaling: ", dist_before)
print('-'* 40)

# Scale the dataset (including these points)
data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

P1_scaled = scaled_data[0]
P2_scaled = scaled_data[2]

# Distance after scaling
dist_after = distance.euclidean(P1_scaled, P2_scaled)

print('-'* 40)
print("Distance after scaling:", dist_after)
print('-'* 40)