"""
Training script.

Entry point for running the training pipeline.
"""

from src.pipelines.training_pipeline import run_training_pipeline

def main():
    metrics = run_training_pipeline()

    print("\nEvaluation Metrics")
    print("-" * 25)

    for name, value in metrics.items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()