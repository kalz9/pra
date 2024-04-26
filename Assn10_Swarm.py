import numpy as np
import random

# Parameters
num_ants = 10
num_iterations = 100
evaporation_rate = 0.5
pheromone_deposit = 1.0
alpha = 1.0
beta = 2.0

# Function to calculate tour length
def tour_length(tour, distance_matrix):
    total_length = 0
    num_cities = len(tour)
    for i in range(num_cities - 1):
        total_length += distance_matrix[tour[i]][tour[i+1]]
    total_length += distance_matrix[tour[-1]][tour[0]]  # Return to the starting city
    return total_length

# Function to update pheromone
def update_pheromone(pheromone_matrix, ant_tours):
    pheromone_matrix *= evaporation_rate
    for tour in ant_tours:
        for i in range(len(tour) - 1):
            pheromone_matrix[tour[i]][tour[i+1]] += pheromone_deposit / tour_length(tour, distance_matrix)
        pheromone_matrix[tour[-1]][tour[0]] += pheromone_deposit / tour_length(tour, distance_matrix)

# Function to choose next city for an ant
def choose_next_city(pheromone_matrix, distance_matrix, current_city, visited_cities):
    unvisited_cities = [city for city in range(len(distance_matrix)) if city not in visited_cities]
    probabilities = [((pheromone_matrix[current_city][next_city]) ** alpha) * ((1.0 / distance_matrix[current_city][next_city]) ** beta) for next_city in unvisited_cities]
    probabilities /= np.sum(probabilities)
    chosen_city = np.random.choice(unvisited_cities, p=probabilities)
    return chosen_city

# Function to perform Ant Colony Optimization
def ant_colony_optimization(distance_matrix):
    num_cities = len(distance_matrix)
    pheromone_matrix = np.ones((num_cities, num_cities))
    best_tour = None
    best_tour_length = float('inf')

    for iteration in range(num_iterations):
        ant_tours = []
        for ant in range(num_ants):
            current_city = random.randint(0, num_cities - 1)
            visited_cities = [current_city]
            while len(visited_cities) < num_cities:
                next_city = choose_next_city(pheromone_matrix, distance_matrix, current_city, visited_cities)
                visited_cities.append(next_city)
                current_city = next_city
            ant_tours.append(visited_cities)

            tour_len = tour_length(visited_cities, distance_matrix)
            if tour_len < best_tour_length:
                best_tour_length = tour_len
                best_tour = visited_cities
        
        update_pheromone(pheromone_matrix, ant_tours)

    return best_tour, best_tour_length

# Example usage
# Define the distance matrix (replace this with your own)
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_tour, best_tour_length = ant_colony_optimization(distance_matrix)
print("Best tour:", best_tour)
print("Best tour length:", best_tour_length)