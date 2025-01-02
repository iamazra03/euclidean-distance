# Noktaları tanımlıyoruz
points = [(0, 0), (3, 4), (6, 8), (9, 12), (5, 1)]

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

# Mesafeleri hesaplayıp minimumu buluyoruz
distances = [euclideanDistance(p1, p2) for i, p1 in enumerate(points) for p2 in points[i+1:]]
min_distance = min(distances)

# Sonuçları yazdırıyoruz
print("Hesaplanan öklid mesafeleri:", distances)
print("Minimum mesafe:", min_distance)