# Reprocessing of Aeromagnetic and Gravity Data of the Mull Central Complex, Western Scotland
The following contains scripts that I used with my dissertation (Keele University, 2024-25) entitled "Reprocessing of aeromagnetic and gravity data of the Mull Central Complex, Western Scotland". I also look to add the final dissertation and LaTeX files which go with this once it has been completed. 

## More Content
Check out a short talk I gave at Keele University (January 2025; available [here](https://youtu.be/FvGF1hL2ERU) on the Geomagnetic field, where I briefly discuss the processed data used here, providing a wider context.

## Acknowledgements 
This project was completed with the help and support of my supervisor, [Dr. Ian Stimpson](https://www.keele.ac.uk/lifesci/ourpeople/ianstimpson/). Thank you, also, to the contributors of the [`harmonica`](https://www.fatiando.org/harmonica) and [`pyGIMLi`](https://www.pygimli.org) packages ([Prof. Leonardo Uieda](https://github.com/leouieda) and [Prof. Thomas Günther](https://github.com/halbmy)) for their help in answering questions I posed during the project. Tutorials on the package websites were also of great help in ensuring the code functioned. 

## Licence
Work here is licenced using the `LICENCE` file. However, please note that this work contains British Geological Survey data (for the aeromagnetic and gravity data) and Ordenance Survey data (for the map background of anomaly images). Licences and links to the sources are below:

- Contains British Geological Survey materials © UKRI [2025], licensed under the Open Government Licence v3.0. The Great Britain aeromagnetic survey is available from [here](https://www.bgs.ac.uk/datasets/gb-aeromagnetic-survey/), and Great Britain land gravity survey available from [here](https://www.bgs.ac.uk/datasets/gb-land-gravity-survey/).
- Contains OS data © Crown copyright and database right (2024), lienced under the Open Government Licence v3.0. The 1:250 000 Scale Colour Raster is used, available from [here](https://www.ordnancesurvey.co.uk/products/250k-raster).

## Files Contained
There are two folders, where `Report` contains the dissertation (LaTeX documents and PDF) and `Code` contains the Jupyter Notebooks, Python scripts and output files generated. Note, this is a working document, so changes will likely be made and the file structure may not be intuitive. 

The project consists of processing aeromagnetic and gravity data (in the `Aeromagnetic` and `Gravity` folders). Then models were generated in the `Modelling/Gravity` folder, before the half width of anomalies modelled and generated from processed data were calculated in `Calc_FWHM.ipynb`. 

Also, note that `AeromagCrossValScore.py` and `GravityCrossValScore.py` were run separately in a screen on a remote server, since this was quite computationally intensive. `Modelling.py` also contains a computationally intensive line when itterating through models (at the end), taking around 40 minutes to run.

Those files which are provided by the BGS and the Ordenance Survey have been redacted but are freely available online (by following the links provided above).

Finally, I have not been able to resolve a significant discrepency in the generated size of anomalies via modelling compared to those observed, hence why graphs contain two scales when showing modelled and observed anomalies.

## References
Throughout this work, the following have been extensively used:

Bott, M. H. P., & Tantrigoda, D. A. 1987. Interpretation of the gravity and magnetic anomalies over
the Mull Tertiary intrusive complex, NW Scotland. _Journal of the Geological Society_, **144**(1), 17–28.

Fatiando a Terra Project, Castro, Y. M., Esteban, F. D., Li, L., Oliveira J., Vanderlei C, Pesce, A., Shea, N., Soler, S. R., Souza-Junior, G. F., Tankersley, M., Uieda, L., & Uppal, I. 2024. _Harmonica v0.7.0: Forward modeling, inversion, and processing gravity and magnetic data._

Rücker, C., Günther, T., & Wagner, F. M. 2017. pyGIMLi: An open-source library for modelling and inversion in geophysics. _Computers and Geosciences_, **109**, 106–123.

Smalley, B. 2024. PHY-30027: _Data Analysis and Model Testing_. Lecture Notes (Keele University, UK).

Uieda, L. 2018. Verde: Processing and gridding spatial data using Green’s functions. _Journal of Open Source Software_, **3**(30), 957.

## Packages Used
I recommend creating two separate `Conda` environments with which to run code (one for modelling and one for processing gravity and aeromagnetic data), containing the following packages:
### Processing Data
- `numpy` 2.0.2
- `xarray` 2024.9.0
- `matplotlib` 3.9.2
- `pandas` 2.2.3
- `pygmt` 0.13.0
- `convertbng` 0.7.4 (pip)
- `xrft` 1.0.1
- `magnetic_field_calculator` 1.0.2 (pip)
- `harmonica` 0.7.0
- `verde` 1.8.1
- `jupyter` 1.1.1
- `pandas` 2.2.3
### Modelling
- `matplotlib` 3.10.0
- `numpy` 1.26.4
- `pygimli` 1.5.3
- `shapely` 2.0.6
- `mpl_axes_aligner` (download locally from the [repository(https://github.com/ryutok/mpl_axes_aligner))
- `jupyterlab` 4.3.4
