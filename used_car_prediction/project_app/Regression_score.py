class Calculation():
    
    def __init__(self,model,x_tr,x_te,y_tr,y_te):
        self.model = model
        self.x_tr = x_tr
        self.x_te = x_te
        self.y_tr = y_tr
        self.y_te = y_te

    def testing(self):
        from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
        import numpy as np

        print("Testing data evalution")
        y_pred = self.model.predict(self.x_te)
        mse   = mean_squared_error(self.y_te,y_pred)
        rmse  = np.sqrt(mse)
        mae   = mean_absolute_error(self.y_te,y_pred)
        r2    = r2_score(self.y_te,y_pred)
        star = "*"*50
        return print(f"{star} \nmse:- {mse} \n{star} \nrmse:- {rmse} \n{star}  \nmae :- {mae} \n{star}  \nr2:- {r2} \n{star} ")
    
    def training(self):
        from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
        import numpy as np
        
        print("Training data evalution")
        y_pred_tr = self.model.predict(self.x_tr)
        mse_tr  = mean_squared_error(self.y_tr,y_pred_tr)
        rmse_tr = np.sqrt(mse_tr)
        mae_tr  = mean_absolute_error(self.y_tr,y_pred_tr)
        r2_tr   = r2_score(self.y_tr,y_pred_tr)
        star = "*"*50
        return print(f"{star} \nmse:- {mse_tr} \n{star} \nrmse:- {rmse_tr} \n{star} \nmae :- {mae_tr}  \n{star} \nr2:- {r2_tr} \n{star}")