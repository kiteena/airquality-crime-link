# Air quality (CO, PPM2.5, SO2) versus crime per capita 

All models use Random Forest regression with different numbers of estimators. 
All models use time series data in day increments. 

| Univariate models                                            |
|--------------------------------------------------------------|
| CO arithmetic mean from 1991 to 2017                         |
| PPM 2.5 (size of particle) arithmetic mean from 1999 to 2017 |
| SO2 arithmetic mean from 1999 to 2008                        |
| Crime per-capita between 2003 to 2018                        |

| Multivariate models 
|----------------------------------------------------------------|
| Crime per-capita versus total pollution (CO, ppm 2.5, SO2, NO2)|
| Crime per-capita versus CO daily                               |
| Crime per-capita versus ppm 2.5 daily                          |
| Crime per-capita versus SO2 daily                              |
| Petty crime versus CO daily                                    |
| Non-criminal events versus CO daily                            |

## Results using TimeSeriesSplit 10-fold cross validation
The columns for 'Crime versus respective pollutants' and 'Crime versus time' describe the relationship between crime and pollution in our best models. 

### MSE of crime versus pollution 
Crime refers to 'crime per capita' in SF during the years in the dataset.

|                   | Crime vs CO, time      | Crime vs time           |
|-------------------|------------------------|-------------------------|
| MSE Overall       | 2.5415165595869553e-09 | 2.4462734058830635e-09  |
| MSE (10-fold) Avg | 2.723012705770571e-09  | 2.7630746658902143e-09  |

|                   | Crime vs PPM 2.5, time| Crime vs time            |
|-------------------|-----------------------|--------------------------|
| MSE Overall       | 2.2334256374613945e-09| 2.4462734058830635e-09   |
| MSE (10-fold) Avg | 2.481363300527155e-09 | 2.7630746658902143e-09   |

|                   | Crime vs SO2, time    | Crime vs time            |
|-------------------|-----------------------|--------------------------|
| MSE Overall       | 1.769569613438401e-09 | 2.4462734058830635e-09   |
| MSE (10-fold) Avg | 1.9089008073627166e-09| 2.7630746658902143e-09   |

|                   | Crime vs total        | Crime vs time            |
|-------------------|-----------------------|--------------------------|
| MSE Overall       | 1.7580211083441344e-09| 2.4462734058830635e-09   |
| MSE (10-fold) Avg | 2.104379467336409e-09 | 2.7630746658902143e-09   |

### MSE of non-criminal events versus CO
Non-criminal events refer to traffic accidents, lost property, auto-impound, etc.

|                   | Non-criminal events versus CO | 
|-------------------| ------------------------------|
| MSE Overall       |  1.4940334427923478e-10       |
| MSE (10-fold) Avg |  1.422831725482845e-10        | 

|                   | Fire reports versus CO        | 
|-------------------| ------------------------------|
| MSE Overall       |  3.719187650277951e-13        |
| MSE (10-fold) Avg |  3.7593204106935054e-13       | 

### MSE of pollution over time 

|                   |  CO versus time       |
|-------------------| ----------------------|
| MSE Overall       |  0.04245489855557771  | 
| MSE (10-fold) Avg |  0.14481904370284474  | 

|                   |   PPM 2.5 versus time | 
|-------------------|  ---------------------|
| MSE Overall       |  45.64918194028494    | 
| MSE (10-fold) Avg |  85.31698434324686    | 

|                   |    SO2 versus time    | 
|-------------------| --------------------- |
| MSE Overall       |  1.4511614940381257   |
| MSE (10-fold) Avg |  9.230414518716842    | 


## Basic exploration 
Contains early exploration on using subset files under data/ 
