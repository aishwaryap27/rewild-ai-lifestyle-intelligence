import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
import matplotlib.pyplot as plt'
import seaborn as sns
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
df=pd.read_csv("data/sample_posts.csv")
def assign_strategy(score):
	if score>7:
		return "authentic"
	elif score>4 :
		return "educational"
	
	else:
		return "minimal"
df["strategy"]=df["engagement_score"].apply(assign_strategy)
X=df[["likes","comments","shares","engagement_score"]]
y=df["strategy"]

X_train,X_test,y_train,y_test=train_test_split(
	X,y,
	test_size=0.2
	random_state=42
)
model=DecisionTreeClassifier(
max_depth=4
random_state=42
)
model.fit(X_train,y_train)
