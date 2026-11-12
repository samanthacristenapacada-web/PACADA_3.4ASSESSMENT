from binary_tree import root, display_tree, bfs as tree_bfs, dfs as tree_dfs
from graph import graph, display_graph, bfs as graph_bfs, dfs as graph_dfs


def main():
    while True:
        print("\n======================================")
        print("       NON-LINEAR DATA STRUCTURES")
        print("                 PACADA")
        print("======================================")
        print("[1] View Binary Tree")
        print("[2] Binary Tree with Traversal")
        print("[3] View Graph")
        print("[4] Graph with Traversal")
        print("[5] Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nBINARY TREE STRUCTURE")
            display_tree(root)

        elif choice == "2":
            print("\nBINARY TREE TRAVERSALS")

            print("BFS: ", end="")
            tree_bfs(root)

            print("\nDFS: ", end="")
            tree_dfs(root)
            print()

        elif choice == "3":
            print("\nGRAPH STRUCTURE")
            display_graph(graph)

        elif choice == "4":
            print("\nGRAPH TRAVERSALS")

            print("BFS: ", end="")
            graph_bfs(graph, "D")

            print("\nDFS: ", end="")
            graph_dfs(graph, "D")
            print()

        elif choice == "5":
            print("\nThank you! Program terminated.")
            break

        else:
            print("\nInvalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()
