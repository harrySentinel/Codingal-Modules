print("=== Supervised vs Unsupervised ML Algorithms ===\n")

print("SUPERVISED LEARNING")
print("Definition: Model is trained on labeled data (input + correct output)\n")
supervised = {
    "Linear Regression":    "Predicting house prices based on area and location",
    "Logistic Regression":  "Classifying emails as spam or not spam",
    "KNN Classifier":       "Classifying flowers in the Iris dataset",
    "Decision Tree":        "Predicting whether a loan should be approved",
    "SVM":                  "Image classification and text categorization",
}
for algo, app in supervised.items():
    print(f"  {algo}")
    print(f"    Application: {app}\n")

print("=" * 50)
print("\nUNSUPERVISED LEARNING")
print("Definition: Model finds hidden patterns in unlabeled data\n")
unsupervised = {
    "K-Means Clustering":        "Customer segmentation based on spending behaviour",
    "DBSCAN":                    "Detecting outliers and noise in geographic data",
    "Hierarchical Clustering":   "Grouping documents by topic similarity",
    "Apriori (Association)":     "Market basket analysis — finding frequent item pairs",
    "PCA":                       "Dimensionality reduction for visualising high-dim data",
}
for algo, app in unsupervised.items():
    print(f"  {algo}")
    print(f"    Application: {app}\n")

print("=" * 50)
print("\nKey Difference:")
print("  Supervised   → needs labels → predicts outcomes")
print("  Unsupervised → no labels   → discovers structure")
