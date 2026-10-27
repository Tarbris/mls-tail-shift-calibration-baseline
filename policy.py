"""Editable weak calibration method: identity mapping."""


class CalibrationMethod:
    def fit(self, probs, labels, groups):
        return self

    def predict_proba(self, probs, groups):
        return list(probs)
