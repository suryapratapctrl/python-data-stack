from sklearn.metrics import accuracy_score,precision_score,recall_score, f1_score


#true answers (what actually happened)
y_true=[1,0,1,1,0,1,0]

#model's predictions (what is guessed)
y_pred=[1,0,1,0,0,1,1]

#evaluation 
print('Accuracy: ',accuracy_score(y_true,y_pred))
print('Precision: ',precision_score(y_true,y_pred))
print('Recall: ',recall_score(y_true,y_pred))
print('F1 score: ',f1_score(y_true,y_pred))



