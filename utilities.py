def final_model (lst):
    diz =dict()
    diz['model'] = max(lst, key=lambda tup: tup[1])[0]
    diz['metric_value']=max(lst, key=lambda tup: tup[1])[1]
    diz['features'] =max(lst, key=lambda tup: tup[1])[2]
    return diz 

old_mcc_results_ce=[('Decision Tree', 0.09667982810086584, '25.0'),
 ('Logistic Regression', 0.10433690974901236, 'all'),
 ('Random Forest', 0.11974136293214326, 'all'),
 ('KNN', 0.07366884024137631, '50.0')]

mcc_results_ce=[('Logistic Regression', 0.1088963006795296, 10.0),
 ('Decision Tree', 0.0322217870005202, 67.0),
 ('KNN', 0.1061685389779593, 10.0),
 ('Random Forest', 0.1117330989074283, 10.0)]

old_mcc_results_pp=[('Logistic Regression ', 0.2965376261141505, '50.0'),
 ('KNN', 0.21897689807853166, 'all'),
 ('Random Forest', 0.3178326993953296, '50.0'),
 ('Decision Tree ', 0.33492038250592904, '50.0')]

mcc_results_pp=[('Logistic Regression ', 0.2900961417417739, '10.0'),
 ('KNN', 0.2463404281570071, '10.0'),
 ('Random Forest', 0.3430637966324857, 'all'),
 ('Decision Tree ', 0.318485976770124, '10.0')]

old_r2_results=[('Random Forest', 0.23679474191220976, 'all'),
 ('XGBoost Regression', 0.2250824085072309, 'all'),
 ('Linear SVR', 0.13956117089811007, '50.0'),
 ('Radial SVR', 0.20200460470018824, '50.0')]

r2_results=[('Linear SVR', 0.0367621382318914, 'all'),
 ('Radial SVR', 0.0061503942374037, 'all'),
 ('XGBoost Regression', 0.1255462525370943, '50.0'),
 ('Random Forest', 0.2048602777232935, '50.0')]

top50_score= [58,
 10,
 28,
 42,
 61,
 40,
 64,
 14,
 2,
 54,
 39,
 23,
 70,
 34,
 59,
 65,
 52,
 33,
 27,
 5,
 9,
 32,
 53,
 38,
 18,
 60,
 24,
 22,
 45,
 48,
 13,
 47,
 4,
 15,
 11,
 19,
 57,
 49,
 20,
 25,
 0,
 68,
 29,
 21,
 3,
 8,
 72,
 37,
 51,
 26]