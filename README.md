## Introduction
A transimission model based on reported cases of 2019-nCoV within 1.12 and 1.26 to predict the possible course of the epidemic, as the potential impact of travel restrictions into and from Wuhan.

## SIR
The epidemic model is a way of simplifications of the reality, which helps refine our understanding about the logic of diffusion beneath social realities (disease transmission, information diffusion through networks, and adoption of new technologies or behaviors). 

Up to 27 January, since there are over 3000 confirmed 2019 n-CoV cases globally with growing cure rate, we choose the SIR (Susceptible - Infectious - Recovered) model to apply in the prediction model.

## Data & Visualization
- Source
  - API provided by CxZMoE: https://github.com/CxZMoE/nCoV (1.26 and before)
  - API provided by TankNee: https://github.com/TankNee/nCoV-2019-DataAPI (1.29 and before)

- Geographical distribution of 2019-nCoV in China for the data up to 29 January.

<p align="center">
  <img src="https://github.com/graveszhang/Beat-COVID-19-using-SIR-and-Graph-Neural-Networks/blob/master/img/geomap.png" alt="Geo Map"/>
</p>

<p align="center">
  <img src="https://github.com/graveszhang/Beat-COVID-19-using-SIR-and-Graph-Neural-Networks/blob/master/img/tracemap.png" alt="Trace Map"/>
</p>

## Results
We estimate that the basic reproduction number of the infection(R0) to be 1.273, with the infection parameter and recover parameter set to be 1 and 0.785 respectively. Our prediction of the epidemic in Wuhan is illustrated in below.

<p align="center">
  <img src="https://github.com/graveszhang/Beat-COVID-19-using-SIR-and-Graph-Neural-Networks/blob/master/img/SIRresult.png" alt="SIRresult"/>
</p>

<p align="center">
  <img src="https://github.com/graveszhang/Beat-COVID-19-using-SIR-and-Graph-Neural-Networks/blob/master/img/SIRplot.png" alt="SIRplot"/>
</p>

## Contribution
[Siyin Ma](https://github.com/siyinm)
