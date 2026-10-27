# Subgroup calibration with rare-to-common and tail shift

Edit only `policy.py`, preserving `CalibrationMethod.fit(probs, labels,
groups)` and `predict_proba(probs, groups)`. Positive-class probabilities are
strictly between 0 and 1, labels are 0/1, and groups are integers 0–5.
Return one finite probability in [0,1] for each input score, in order.

Calibration and target populations differ: source subgroup counts are uneven,
and low-frequency source groups become common at evaluation. The distribution
of scores within each group also moves into less-observed tails. The true
probability map can differ in both intercept and score sensitivity by group.
Only calibration labels are available at fit time; target score lists contain
no labels or truth. Released development cases include target truth for
diagnostics. Evaluator-only hidden truth and reference code are not solver
workspace inputs.
