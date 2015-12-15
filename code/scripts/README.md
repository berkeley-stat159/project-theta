## Analysis with Scripts 

These are the scripts used to run our analyses and build our figures.
Run the following make commands for running the individual analysis. Note that 
`diagnostics` must come *before* `glm` and that `logistic`, `glm`, and 
`glmstandard` must come *before* `mixedeffect`, `heatmap`,and `bncorrelates`.

- `make histograms`: Generates preliminary histograms of all subjects, all runs
for all data in order to identify masking thresholds of smoothed non-standardize
BOLD data. May take around 15 minutes.
- `make diagnostics`: Generates diagnostics figures for checking the assumptions
of the linear model (for subject 2) and plots dvars and framewise displacements
of non-standardized ds005 BOLD data. 
- `make smoothing`: Generates smoothed graphs of BOLD slices for comparison.
- `make glm`: Performs smoothing, convolution and linear regression after of all
 subjects using the non-standardized ds005 data. Saves beta and t values. 
**Warning**: This may take up to 45 minutes.*Run after `make diagnostics`*
- `make glmstandard`: Performs the same procedure as `make glm`, but with the 
standardized ds005 data (with mni template). **Warning**: This may take several 
hours.
- `make logistic`: Performs logistic regression and generates diagnostic figures
of the behavorial data. 

- `make heatmap`: Generates figures of the heatmaps for the gain and loss beta 
values for each subject and for the corresponding t-values. *Run after 
`make glmstandard`, and `make glm`.*
- `make mixedmodel`: Calculates and saves calculates significant gain and loss
beta, anova values for the linear mixed effects model. **Warning**: This is most
time consuming analysis we have. Running on all subjects may take around 1 day.
Caution when running! *Run after `make glm` and `make logistic`.*
- `make bncorrelates` performs linear regression on standardized beta results 
and lambas of logistic regression, generates figures of neural/behavorial loss 
aversion and significant p-values by region/voxel. **Warning**: this may take 
over an hour. *Run after `make glmstandard` and `make logistic`.*

## Individual Script Documentation

- `find_mask_threshold.py` plots the histograms of mean BOLD data, filtered 
and raw, for every run for every subject in order to help find threshold value

- `find_outlier.py` is a script to find the outliers for each subject runs based
on dvars and framewise displacement

- `graph_lindiag_script.py` calculates and plots a qqplot and graph of residual
vs fitted for a chosen voxel

- `graphoutlier.py` takes the output created by findoutlier.py and plots the
outlier based on fd and dvars

- `lme_script.py` calculates the beta, anova values for the linear mixed 
effects model

- `logistic.py` calculates the lambdas and diagnostics such as ROC and AUC
for the logistic regression on each subjects behavioral data

- `make_smooth_graphs.py` creates smoothed graphs of selected slice with 
different FWHM for comparison

- `plot_heatmap.py` creates the heatmaps for the gain and loss beta values for
each subject and for the corresponding t-values

-`plot_heatmap_standard.py`: Same thing as `plot_heatmap.py`, but with the 
standard processed dataset. 

- `regression_script.py` calculates the beta and t values for the linear
regression on the raw BOLD data for each subject

- `regressions_script_standard.py` does the same as regression\_script.py for 
the filtered BOLD data

- `cross_subjects_linear_regression.py` performs linear regression of the 
neural loss and behavorial loss aversion of standard data. Run after 
`logistic.py` and `regression_scipt_standard.py`. Text output files used in 
`neural_behavial_plot.py`.

- `neural_behavial_plot.py` generates plot figures that correlates the 
behavioral loss aversion and neural loss aversion of specific slices of the 
brain. Run after `cross_subjects_linear_regression.py`. 
