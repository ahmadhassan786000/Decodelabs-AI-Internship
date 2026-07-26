from src.data_preprocessing import load_and_split_data
from src.evaluation import evaluate_model
from src.train import train_model


def main():
    X_train, X_test, y_train, y_test = load_and_split_data()
    model = train_model(X_train, y_train)
    results = evaluate_model(model, X_test, y_test)

    print("Model trained successfully.")
    print(f"Accuracy: {results['accuracy']:.4f}")
    print("Confusion Matrix:")
    print(results['confusion_matrix'])
    print(f"Precision: {results['precision']:.4f}")
    print(f"Recall: {results['recall']:.4f}")
    print(f"F1 Score: {results['f1_score']:.4f}")


if __name__ == "__main__":
    main()
