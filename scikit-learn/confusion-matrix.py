# import

from sklearn.metrics import confusion_matrix

y_true=[1,0,1,1,0,1,0,0,1,0]

y_pred=[1,0,1,0,0,1,1,0,1,0]
cm=confusion_matrix(y_true,y_pred)

print("confusion matrix")
print(cm)

# Confusion Matrix (output)
# [[4 1]
#  [1 4]]
#
# TN (True Negative)  = 4
# FP (False Positive) = 1
# FN (False Negative) = 1
# TP (True Positive)  = 4
#
# meaning
# - 4 negative samples were correctly classified.
# - 4 positive samples were correctly classified.
# - 1 negative sample was incorrectly classified as positive.
# - 1 positive sample was incorrectly classified as negative.

