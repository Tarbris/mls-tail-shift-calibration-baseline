"""Editable weak calibration method: identity mapping."""


class CalibrationMethod:
    def fit(self, probs, labels, groups, record_probs):
        return self

    def predict_proba(self, probs, groups):
        return list(probs)
