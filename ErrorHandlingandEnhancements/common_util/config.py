#Contains all what is dynamic

path = r"C:\Users\sn27506\Learnings\FSDSession1Assignment1\ErrorHandlingandEnhancements"

datapath = path + "\\1.Development\\traindata\iris.csv"
modeloutput = path + "\\2.Deployment\\artifacts\model.pkl"
rawfields = ["Sepal_Length", "Sepal_Width", "Petal_Length","Petal_Width"]
target = "Class"
testsize = 0.3
randomstate = 50