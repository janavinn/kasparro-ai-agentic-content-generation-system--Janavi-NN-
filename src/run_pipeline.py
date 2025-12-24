from src.orchestrator import Orchestrator

def main():
    orch = Orchestrator(input_path="src/input/product.json", out_dir="outputs")
    orch.run()

if __name__ == "__main__":
    main()
