import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def tsp(self, src):
        visited = [False] * self.V
        visited[src] = True
        path = [src]
        min_dist = sys.maxsize
        min_path = []

        def tsp_util(curr_pos, visited, path, curr_dist):
            nonlocal min_dist, min_path

            if len(path) == self.V:
                if self.graph[curr_pos][src] != 0:
                    curr_dist += self.graph[curr_pos][src]
                    if curr_dist < min_dist:
                        min_dist = curr_dist
                        min_path = path.copy()
                return

            for v in range(self.V):
                if not visited[v] and self.graph[curr_pos][v] != 0:
                    visited[v] = True
                    path.append(v)
                    tsp_util(v, visited, path, curr_dist + self.graph[curr_pos][v])
                    visited[v] = False
                    path.pop()

        tsp_util(src, visited, path, 0)
        return min_dist, min_path

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            min_dist = sys.maxsize
            min_vertex = -1

            for v in range(self.V):
                if not visited[v] and dist[v] < min_dist:
                    min_dist = dist[v]
                    min_vertex = v

            visited[min_vertex] = True

            for v in range(self.V):
                if (
                    not visited[v]
                    and self.graph[min_vertex][v] != 0
                    and dist[min_vertex] != sys.maxsize
                    and dist[min_vertex] + self.graph[min_vertex][v] < dist[v]
                ):
                    dist[v] = dist[min_vertex] + self.graph[min_vertex][v]

        return dist

def print_path(path):
    print("Shortest Path:")
    for vertex in path:
        print(vertex, end=" -> ")
    print(path[0])

def print_execution_time(execution_time):
    print("Waktu Komputasi Perhitungan Path: %.6f detik\n" % execution_time)

def tsp_analysis():
    print("TSP Analysis:")
    print("1. Worst Case: O(n!)")
    print("   - Kompleksitas waktu dalam kasus ini adalah faktorial dari jumlah vertex.")
    print("   - Algoritma TSP akan mencoba semua kemungkinan permutasi vertex.")
    print("2. Best Case: O(n^2 * 2^n)")
    print("   - Kompleksitas waktu terbaik terjadi ketika jumlah vertex sangat sedikit.")
    print("   - Algoritma TSP akan mengunjungi setiap vertex satu kali.")
    print("3. Average Case: O(n^2 * 2^n)")
    print("   - Kompleksitas waktu rata-rata cenderung sama dengan best case karena algoritma TSP mencoba semua kemungkinan permutasi vertex.\n")

def dijkstra_analysis():
    print("Dijkstra Analysis:")
    print("1. Worst Case: O((V + E) log V)")
    print("   - Kompleksitas waktu terburuk terjadi ketika ada banyak edge dan bobot yang berbeda-beda di dalam graph.")
    print("2. Best Case: O(V^2)")
    print("   - Kompleksitas waktu terbaik terjadi ketika tidak ada edge negatif dan graph terhubung.")
    print("3. Average Case: O((V + E) log V)")
    print("   - Kompleksitas waktu rata-rata bergantung pada jumlah edge dan vertex di dalam graph.\n")

def main():
    graph = Graph(7)
    graph.graph = [
        [0, 12, 10, 0, 0, 0, 12],
        [12, 0, 8, 12, 0, 0, 0],
        [10, 8, 0, 11, 3, 0, 9],
        [0, 12, 11, 0, 0, 10, 0],
        [0, 0, 3, 0, 0, 7, 0],
        [0, 0, 0, 10, 7, 0, 9],
        [12, 0, 9, 0, 0, 9, 0],
    ]

    print("Graph:")
    for row in graph.graph:
        print(row)
    print("\n")

    choice = input("Pilih metode perhitungan shortest path (TSP/Dijkstra): ")

    if choice.lower() == "tsp":
        start_time = time.time()
        min_dist, min_path = graph.tsp(0)
        end_time = time.time()
        execution_time = end_time - start_time

        print("Jarak Terpendek (TSP):", min_dist)
        print_path(min_path)
        print_execution_time(execution_time)
        tsp_analysis()
    elif choice.lower() == "dijkstra":
        start_time = time.time()
        dist = graph.dijkstra(0)
        end_time = time.time()
        execution_time = end_time - start_time

        print("Jarak Terpendek (Dijkstra):")
        for i in range(graph.V):
            print("0 ->", i, ":", dist[i])
        print("\n")
        print_execution_time(execution_time)
        dijkstra_analysis()
    else:
        print("Pilihan tidak valid. Silakan pilih 'TSP' atau 'Dijkstra'.")


if __name__ == '__main__':
    main()
