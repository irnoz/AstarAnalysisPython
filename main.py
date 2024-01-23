import Maze
import AstarArray
import AstarHeap
import AstarBinomialHeap
import AstarFibonacchiHeap
import time
import pandas as pd

def run_astar(algorithm, maze, start, end):
    start_time = time.time()
    path = algorithm.astar(maze, start, end)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return path, elapsed_time

def get_times_as_df(maze, start, end):
    results = []

    # A* with Array
    array_path, array_time = run_astar(AstarArray, maze, start, end)
    results.append(('Array', f'{len(maze)}x{len(maze)}', array_time))

    # A* with Heap
    heap_path, heap_time = run_astar(AstarHeap, maze, start, end)
    results.append(('Heap', f'{len(maze)}x{len(maze)}', heap_time))

    # A* with Binomial Heap
    binomial_heap_path, binomial_heap_time = run_astar(AstarBinomialHeap, maze, start, end)
    results.append(('Binomial Heap', f'{len(maze)}x{len(maze)}', binomial_heap_time))

    # A* with Fibonacci Heap
    fibonacci_heap_path, fibonacci_heap_time = run_astar(AstarFibonacchiHeap, maze, start, end)
    results.append(('Fibonacci Heap', f'{len(maze)}x{len(maze)}', fibonacci_heap_time))

    # Print results
    # for algorithm, size, time in results:
    #     print(f"A* with {algorithm} with size: {size} | Time: {time:.6f} seconds")

    # Create a DataFrame
    df = pd.DataFrame(results, columns=['Algorithm', 'Size', 'Time'])

    # Export to CSV
    # df.to_csv('results.csv', index=False)
    return df

def get_times(maze, start, end):
    array_path, array_time = run_astar(AstarArray, maze, start, end)
    print(f"A* with Array with size: {len(maze)}x{len(maze)} | Time: {array_time:.6f} seconds")
    # print(f"Path:\n {array_path}")

    heap_path, heap_time = run_astar(AstarHeap, maze, start, end)
    print(f"A* with Heap with size: {len(maze)}x{len(maze)} | Time: {heap_time:.6f} seconds")
    # print(f"Path:\n {heap_path}")

    binomial_heap_path, binomial_heap_time = run_astar(AstarBinomialHeap, maze, start, end)
    print(f"A* with Binomial Heap with size: {len(maze)}x{len(maze)} | Time: {binomial_heap_time:.6f} seconds")
    # print(f"Path:\n {binomial_heap_path}")

    fibonacci_heap_path, fibonacci_heap_time = run_astar(AstarFibonacchiHeap, maze, start, end)
    print(f"A* with Fibonacci Heap with size: {len(maze)}x{len(maze)} | Time: {fibonacci_heap_time:.6f} seconds")
    # print(f"Path:\n {fibonacci_heap_path}")

def main():
    # get_times(Maze.smallMaze, Maze.smallMazeStart, Maze.smallMazeEnd)
    # get_times(Maze.mediumMaze, Maze.mediumMazeStart, Maze.mediumMazeEnd)
    # get_times(Maze.largeMazeZeros, Maze.largeMazeStart, Maze.largeMazeend)

    small_df = get_times_as_df(Maze.smallMaze, Maze.smallMazeStart, Maze.smallMazeEnd)
    medium_df = get_times_as_df(Maze.mediumMaze, Maze.mediumMazeStart, Maze.mediumMazeEnd)
    large_df = get_times_as_df(Maze.largeMazeZeros, Maze.largeMazeStart, Maze.largeMazeend)
    super_large_df = get_times_as_df(Maze.superLargeMazeZeros, Maze.superLargeMazeStart, Maze.superLargelargeMazeend)

    combined_df = pd.concat([small_df, medium_df, large_df, super_large_df], ignore_index=True)

    # Print or display the combined DataFrame
    print(combined_df)
    combined_df.to_csv('results.csv', index=False)

if __name__ == '__main__':
    main()
