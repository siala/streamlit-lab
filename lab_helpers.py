

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import streamlit as st


FEATURES = ["mean radius", "mean texture", "mean area", "mean concave points"]
CLASS_NAMES = {0: "Benign", 1: "Malignant"}
FEATURE_LABELS = {feature: feature.title() for feature in FEATURES}
FEATURE_DESCRIPTIONS = {
    "mean radius": (
        "Mean nucleus radius: distances from the centre to points on the boundary, "
        "averaged across the sampled nuclei. Values use the dataset's recorded scale."
    ),
    "mean texture": (
        "Mean nucleus texture: the standard deviation of grey-scale intensities, "
        "averaged across the sampled nuclei. Values use the dataset's recorded scale."
    ),
    "mean area": (
        "Mean area of the sampled cell nuclei in the image. "
        "Values use the dataset's recorded scale."
    ),
    "mean concave points": (
        "Mean concave-points measurement of the sampled nuclei: a descriptor of "
        "the number of concave portions of their boundaries. Values use the "
        "dataset's recorded scale."
    ),
}
THRESHOLD = 0.50
COLOURS = {"Benign": "#3176B5", "Malignant": "#C97932"}
STYLE = {
    "figure.dpi": 110,
    "font.size": 10,
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.labelcolor": "#262626",
    "text.color": "#262626",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
}


DATA_FILE = Path(__file__).resolve().parent / "data" / "wdbc.data"
MEASUREMENTS = [
    "radius", "texture", "perimeter", "area", "smoothness",
    "compactness", "concavity", "concave points", "symmetry", "fractal dimension",
]
COLUMNS = (
    [f"mean {m}" for m in MEASUREMENTS]
    + [f"{m} error" for m in MEASUREMENTS]
    + [f"worst {m}" for m in MEASUREMENTS]
)


@st.cache_data(show_spinner=False)
def load_data() -> dict:
    """Load the bundled data file and make the lecture's fixed, stratified 455/114 split.

    The data file records the diagnosis as M or B; this lab explicitly uses malignant = 1.
    The index identifies a dataset row, not a patient identifier.
    """
    raw = pd.read_csv(DATA_FILE, header=None, names=["id", "diagnosis"] + COLUMNS)
    X = raw[COLUMNS].astype(float)
    y = raw["diagnosis"].eq("M").astype(int).rename("malignant")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, stratify=y, random_state=42
    )
    exploration = X_train.copy()
    exploration["diagnosis"] = y_train.map(CLASS_NAMES)
    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "exploration": exploration,
        "full_count": len(X),
    }



