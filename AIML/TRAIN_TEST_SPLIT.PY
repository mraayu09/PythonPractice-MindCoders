from sklearn.model_selection import train_test_split,cross_val_score
import numpy as np

np.random.seed(42)
X = np.random.randn(500, 5)
y = np.random.randint(0,2,500)

#80/20 test split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state = 42, stratify=y)
print(f'Training samples: {len(X_train)} | Test samples: {len(X_test)}')

#5 fold cross validation
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=50, random_state=42)
cv_scores = cross_val_score(model,X,y, cv=5, scoring='accuracy')    #cv means number of folds
print(f'CV Scores each each fold: {cv_scores.round(3)}')
print(f'Mean: {cv_scores.mean(): .4f} ± {cv_scores.std(): .4f}')    # ± ye sign alt+ 0177 se aya 



