# Subgroup calibration with rare-to-common and tail shift

Edit only `policy.py`, preserving `CalibrationMethod.fit(probs, labels,
groups, record_probs)` and `predict_proba(probs, groups)`. Positive-class
probabilities are strictly between 0 and 1, labels are 0/1, and groups are
integers 0–5. Group `g` encodes `region = g // 2` (three ordered regions)
and `channel = g % 2` (two acquisition channels). Only a selected subset of
potential calibration labels is
recorded. `record_probs` provides each released row's known probability of
being recorded, conditional on that row's generated label and score.
Return one finite probability in [0,1] for each input score, in order.

Calibration and target populations differ: source subgroup counts are uneven,
and groups 4 and 5 have especially few recorded labels but become common at
evaluation. The distribution
of scores within each group also moves into less-observed tails. The true
probability map can differ in both intercept and score sensitivity by group,
while neighboring regions and shared channels carry transferable structure.
Label recording also depends on the realized label, so the released positive
fraction is not the population positive fraction. Only recorded calibration
labels are available at fit time; target score lists contain
no labels or truth. Released development cases include target truth for
diagnostics. Evaluator-only hidden truth and reference code are not solver
workspace inputs.
Each episode redraws its common and subgroup calibration coefficients; a
mapping copied from released development answers is not a hidden answer.
