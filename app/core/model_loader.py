import pickle

from app.core.config import MODEL_PATH


class ModelLoader:
    """
    Loads the trained ML model once when the application starts.
    """

    def __init__(self):
        self.model = self._load_model()

    def _load_model(self):
        """
        Load the trained model from disk.
        """
        with open(MODEL_PATH, "rb") as file:
            return pickle.load(file)

    def get_model(self):
        """
        Return the loaded model.
        """
        return self.model


model_loader = ModelLoader()