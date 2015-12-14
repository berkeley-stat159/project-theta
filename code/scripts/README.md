##Scripts

These are the scripts used to run our analyses and build our figures.

- `find_mask_threshold.py` plots the histograms of mean BOLD data, filtered 
and raw, for every run for every subject in order to help find threshold value

- `find_outlier.py` is a script to find the outliers for each subject runs based
on dvars and framewise displacement

- `graph_lindiag_script.py` calculates and plots a qqplot and graph of residual
vs fitted for a chosen voxel

- `graphoutlier.py` takes the output created by find\_outlier.py and plots the
outlier based on fd and dvars

- `lme_script.py` calculates the beta, anova values for the linear mixed 
effects model

- `logistic.py` calculates the lambdas and diagnostics such as ROC and AUC
for the logistic regression on each subjects behavioral data

- `make_smooth_graphs.py` creates smoothed graphs of selected slice with 
different FWHM for comparison

- `plot_heatmap.py` creates the heatmaps for the gain and loss beta values for
each subject and for the corresponding t-values

- `regression_script.py` calculates the beta and t values for the linear
regression on the raw BOLD data for each subject

- `regressions_script_standard.py` does the same as regression\_script.py for 
the filtered BOLD data

 
