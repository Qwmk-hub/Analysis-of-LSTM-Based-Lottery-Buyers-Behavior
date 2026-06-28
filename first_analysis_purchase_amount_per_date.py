import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import pickle
import xgboost
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler




with open('./data/user_data_dict.pkl', 'rb') as f:
    user_data_dict = pickle.load(f)

X = []
Y = []

print(len(user_data_dict.keys()))

count = 0
for user in user_data_dict.keys():

    purchase_amount_per_day = user_data_dict[user][:, 0]
    purchase_time_per_day = user_data_dict[user][:, 1]

    plt.plot(purchase_amount_per_day)
    plt.show()
    # 1,2,3,4,5
    # 13,14,15,16,17

    for i in range(13):
        ##################### X part ###############################

        ##################### day-data ###############################
        temp = []
        for k in range(4):
            for j in range(7):
                temp.append(purchase_amount_per_day[7*(i+k)+j])

        for k in range(4):
            for j in range(7):
                temp.append(purchase_time_per_day[7*(i+k)+j])

        ##################### week-feature ###############################
        for k in range(4):
            F1 = 0
            F2 = 0
            F4 = 0
            for j in range(7):
                F1 = F1 + purchase_amount_per_day[7*(i+k)+j]
                F2 = F2 + purchase_time_per_day[7*(i+k)+j]

                if (purchase_amount_per_day[7*(i+k)+j]>0):
                    F4 = F4 + 1
            F6 = np.var(purchase_amount_per_day[7*(i+k):7*(i+k+1)])
            F3 = 0
            F5 = 7
            if F2>0:
                F3 = F1/F2
                F5 = 1/F2
            temp.append(F1)
            temp.append(F2)
            temp.append(F3)
            temp.append(F4)
            temp.append(F5)
            temp.append(F6)

        X.append(temp)

        ##################### Y part ###############################
        k=4
        F1 = 0
        for j in range(7):
            F1 = F1 + purchase_amount_per_day[7 * (i + k) + j]

        #F1 = np.log(F1)
        Y.append(F1)
    count = count + 1


#Y = np.log(Y+1.0)
X = np.array(X)
Y = np.array(Y)

#truncation_=0.5*max(Y)
#for i in range(len(Y)):
#    if Y[i]>truncation_:
#        Y[i]=truncation_

#truncation_=0.01*max(Y)
#for i in range(len(Y)):
#    if Y[i]<truncation_:
#        Y[i]=truncation_



print(X.shape)

plt.plot(Y)
plt.show()

X_train = X[0:31477,:]
Y_train = Y[0:31477]
X_test = X[31477:,:]
Y_test = Y[31477:]


# 사분위수에 따라 rank로 분류합니다.
quantiles = np.percentile(Y_train, [0, 25, 50, 75, 100])

Y_ranked_train = np.digitize(Y_train, bins=quantiles, right=True)
Y_ranked_test = np.digitize(Y_test, bins=quantiles, right=True)

# Rank는 1, 2, 3, 4로 매겨지며, 각각의 샘플에 해당하는 rank 값을 가집니다.
# 각 rank에 몇 개의 샘플이 들어갔는지 확인하고 싶다면:
unique, counts = np.unique(Y_ranked_train, return_counts=True)


#print(quantiles)
#print(unique)
#print(counts)

#XGBRegressor

#scaler = StandardScaler()
#X_train = scaler.fit_transform(X_train)
#X_test = scaler.transform(X_test)

param_grid = {
    'n_estimators': [500, 1000, 1500],
    'max_depth': [6, 8, 9],
    'learning_rate': [0.01, 0.02, 0.05],
#    'subsample': [0.7, 0.8, 0.9],
#    'colsample_bytree': [0.7, 0.8, 0.9],
    'reg_lambda': [0.5, 1.0, 1.5],
    'reg_alpha': [0.5, 1.0, 1.5]
}

# Best : 'learning_rate': 0.01, 'max_depth': 6, 'n_estimators': 1000, 'reg_alpha': 0.5, 'reg_lambda': 1.0}
xgb_model = xgboost.XGBRegressor(n_estimators=1000, learning_rate=0.01, gamma=2, subsample=0.75,
                                 colsample_bytree=1, max_depth=6, reg_lambda=1., reg_alpha=0.5)
xgb_model.fit(X_train, Y_train)

#grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid, cv=3, scoring='r2', verbose=2)
#grid_search.fit(X_train, Y_train)

#print("Best parameters found: ", grid_search.best_params_)


r_sq = xgb_model.score(X_train, Y_train)
#r_sq = r2_score(X_train, Y_train)
print(r_sq)

Y_predict = xgb_model.predict(X_test)

r_sq = xgb_model.score(X_test, Y_test)
#r_sq = r2_score(X_test, Y_test)
print(r_sq)

x = np.arange(0,  Y_train.max() + 0.1, 0.1)
y = x
Y_pred = xgb_model.predict(X_test)

Y_pred_train = xgb_model.predict(X_train)
Y_pred_test = xgb_model.predict(X_test)

plt.plot(x,y, linestyle='-', color='red', linewidth = 4)
plt.plot(Y_test, Y_pred, 'k.', linewidth = 0.5)
plt.show()

Y_test=np.array(Y_test)
Y_predict=np.array(Y_predict)
#print(Y_test)
np.savetxt('Y_pred.txt',Y_predict.squeeze())
np.savetxt('Y_test.txt',Y_test.squeeze())

np.savetxt('Y_pred_train.txt', Y_pred_train)
np.savetxt('Y_train.txt', Y_train)

#xgb_model = xgboost.XGBClassifier(n_estimators=1000, learning_rate=0.050, gamma=1, subsample=0.75, colsample_bytree=1, max_depth=7, reg_lambda=0.5, reg_alpha=0.5)
#xgb_model.fit(X_train, Y_train)
#r_sq = xgb_model.score(X_train, Y_ranked_train)
#print(r_sq)
#r_sq = xgb_model.score(X_test, Y_ranked_test)
#print(r_sq)
#x = np.arange(0,5 +0.1, 0.1)
#y = x
#Y_pred = xgb_model.predict(X_test)
#plt.plot(x,y, linestyle='-', color='red', linewidth = 4)
#plt.plot(Y_ranked_test, Y_pred, 'k.', linewidth = 0.5)
#plt.show()


feature_importances = xgb_model.feature_importances_

# feature_importances 배열에서 각 주차별 F1~F6 중요도 추출
# 리스트의 인덱스는 0부터 시작
week1_importances = feature_importances[56:56+6]
week2_importances = feature_importances[56+6:56+6*2]
week3_importances = feature_importances[56+6*2:56+6*3]
week4_importances = feature_importances[56+6*3:56+6*4]

F1_to_F6_all_weeks=week1_importances + week2_importances + week3_importances + week4_importances


features = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6']

#print(F1_to_F6_all_weeks)

'''
# 1주차 출력
print("Week 1: F1-F6 Importance")
for name, score in zip(features, week1_importances):
    print(f'{name}: {score:.6f}')
print()

# 2주차 출력
print("Week 2: F1-F6 Importance")
for name, score in zip(features, week2_importances):
    print(f'{name}: {score:.6f}')
print()

# 3주차 출력
print("Week 3: F1-F6 Importance")
for name, score in zip(features, week3_importances):
    print(f'{name}: {score:.6f}')
print()

# 4주차 출력
print("Week 4: F1-F6 Importance")
for name, score in zip(features, week4_importances):
    print(f'{name}: {score:.6f}')
print()
'''

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# 1주차
axs[0, 0].bar(features, week1_importances)
axs[0, 0].set_title('Week 1: F1-F6 Importance')
axs[0, 0].set_ylim([0, 0.7])



# 2주차
axs[0, 1].bar(features, week2_importances)
axs[0, 1].set_title('Week 2: F1-F6 Importance')
axs[0, 1].set_ylim([0, 0.7])


# 3주차
axs[1, 0].bar(features, week3_importances)
axs[1, 0].set_title('Week 3: F1-F6 Importance')
axs[1, 0].set_ylim([0, 0.7])


# 4주차
axs[1, 1].bar(features, week4_importances)
axs[1, 1].set_title('Week 4: F1-F6 Importance')
axs[1, 1].set_ylim([0, 0.7])


# 레이아웃 조정
plt.tight_layout()
plt.show()

plt.bar(features, F1_to_F6_all_weeks)
plt.show()

print(F1_to_F6_all_weeks)

#print(np.absolute(np.subtract(Y_train, Y_pred_train)).mean()/np.absolute(Y_train).mean())
#print(np.absolute(np.subtract(Y_test, Y_pred_test)).mean()/np.absolute(Y_test).mean())

print(np.corrcoef(Y_train,Y_pred_train))
print(np.corrcoef(Y_test,Y_pred_test))


#xgboost.plot_importance(xgb_model, importance_type='gain', show_values=True)
#plt.show()
#plt.bar(feature_importances)
#plt.show()

