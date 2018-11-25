# Air quality (CO, PPM2.5, SO2) versus crime per capita 

All models use Random Forest regression with different numbers of estimators

## Univariate models - time series using day increments
CO arithmetic mean from 1991 to 2017
PPM 2.5 (size of particle) arithmetic mean from 1999 to 2017
SO2 arithmetic mean from 1999 to 2008 
Crime per-capita between 2003 to 2018

## Multivariate models 
Crime per-capita versus CO daily
Crime per-capita versus ppm 2.5 daily
Crime per-capita versus SO2 daily 
Petty crime versus CO daily
Non-criminal events versus CO daily

## Results using TimeSeriesSplit 10-fold cross validation
The columns for 'Crime versus respective pollutants' and 'Crime versus time' describe the relationship between crime and pollution in our best models. 

Crime refers to 'crime per capita' in SF during the years in the dataset.

|                   | Crime vs CO, time     | Crime vs time         |
|-------------------|-----------------------|-----------------------|
| MSE Overall       | 7.897421779846798e-09 | 9.276901009229072e-09 |
| MSE (10-fold) Avg | 8.866974704238635e-09 | 8.827877335005902e-09 |

|                   | Crime vs PPM 2.5, time| Crime vs time         |
|-------------------|-----------------------|-----------------------|
| MSE Overall       |1.0310219193387508e-08 | 9.276901009229072e-09 |
| MSE (10-fold) Avg |1.0766812210669124e-08 | 8.827877335005902e-09 |

|                   | Crime vs SO2, time    | Crime vs time         |
|-------------------|-----------------------|-----------------------|
| MSE Overall       | 1.020274991979367e-08 | 9.276901009229072e-09 |
| MSE (10-fold) Avg | 9.82317130708087e-09  | 8.827877335005902e-09 |

|                   | Crime vs total        | Crime vs time         |
|-------------------|-----------------------|-----------------------|
| MSE Overall       | 1.4768410446891544e-08| 9.276901009229072e-09 |
| MSE (10-fold) Avg | 1.5187209598765883e-08| 8.827877335005902e-09 |


This table describes how consistent the rates of pollution have been over the last 1-2 decades. 

|                   |  CO versus time       |
|-------------------| ----------------------|
| MSE Overall       |  0.059275811158194205 | 
| MSE (10-fold) Avg |  0.12678740006636074  | 

|                   |   PPM 2.5 versus time | 
|-------------------|  ---------------------|
| MSE Overall       |  37.44602731411004    | 
| MSE (10-fold) Avg |  85.61478985979657    | 

|                   |    SO2 versus time    | 
|-------------------| --------------------- |
| MSE Overall       |  1.530219822770318    |
| MSE (10-fold) Avg |  2.7354901197154247   | 

## Basic exploration 
Contains early exploration on using subset files under data/ 
