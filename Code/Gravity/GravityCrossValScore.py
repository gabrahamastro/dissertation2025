#import packages
import numpy as np
import pandas as pd # deal with datasets
import itertools

# fatiando libraries
import harmonica as hm 
import verde as vd

####
data = pd.read_csv('landgrav_csv.csv')
####

en = ([152207.0, 173499.0], [725285.0, 738732.0])

#adding 
extend = 30e3 #value to extend eastings and northings by, in metres

# Values to add to each number
additions = [[-extend, extend], [-extend, extend]] # what to add to each value

# Extending the region
updated_en = tuple(
    [en[i][j] + additions[i][j] for j in range(len(en[i]))] for i in range(len(en))
)

w_original = en[0][0]
e_original = en[0][1]
s_original = en[1][0]
n_original = en[1][1]
# storing the original easting northing limits (in metres)

eastings_d, northings_d = updated_en # storing updated easting northing limits, in metres

region_deg_ext = (eastings_d,northings_d)

region_deg = region_deg_ext[0] + region_deg_ext[1] # creating a new variable which is usable to define a region with Verde

inside = vd.inside((data.GRID_EAST,data.GRID_NORTH),
                   region_deg) # defining a filter with Verde

####
####
DataZoom = data[inside]

lat = DataZoom["GRID_NORTH"].astype('float')
long = DataZoom["GRID_EAST"].astype('float')
elev = DataZoom["STATION_ELEV"].astype('float')

Bouguer_Anomaly = DataZoom.BOUGUER_AN

region = vd.get_region((eastings_d, northings_d))

region_of_interest = vd.get_region(en)

# DataZoom = DataZoom.assign(easting=easting)
# DataZoom = DataZoom.assign(northing=northing)

coordinates = (long,lat,elev)

####
####

#define a set of parameters to explore
dampings = [0.01, 0.1, 1, 10]
depths = [5e2,1e3,2e3,5e3,10e3,50e3]
block_sizes = [200,400]

#create combinations to explore
parameter_sets = [
    dict(damping=combo[0], depth=combo[1], block_size=combo[2])
    for combo in itertools.product(dampings, depths, block_sizes)
]
print("Number of combinations:", len(parameter_sets))
print("Combinations:", parameter_sets)

#test these combinations
eql = hm.EquivalentSources()

scores = []
for params in parameter_sets:
    eql.set_params(**params)
    score = np.mean(
        vd.cross_val_score(
            eql,
            coordinates,
            Bouguer_Anomaly,
        )
    )
    scores.append(score)

#Calculate the best fit
best = np.argmax(scores)
print("Best score:", scores[best])
#print("Score with defaults:", score_first_guess)
print("Best parameters:", parameter_sets[best])

print('Gravity Done')