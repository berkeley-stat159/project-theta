.PHONY: clean test verbose coverage all paperfig

clean:
	find .. -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" -o -name "testnib.nii.gz" -o -name "temp.txt" | xargs rm -f

test:
	nosetests code/utils/tests -w ..

verbose:
	nosetests -v code/utils/tests -w ..


coverage:
	nosetests code/utils/tests -w .. --with-coverage --cover-package=utils/functions

all: 
	cd scripts && make histograms
	cd scripts && make smoothing
	cd scripts && make diagnostics
	cd scripts && make glm
	cd scripts && make glmstandard
	cd scripts && make logistic
	cd scripts && make heatmap
	cd scripts && make bncorrelates
	cd scripts && make mixedmodel


paperfig:
# Goes to results/figures and updates files that already exist in figures, figures/Regression1/, and figures/Regression2/
	rsync -av --existing ../results/figures/ ../paper/figures/
	rsync -av --existing ../results/figures/ ../paper/figures/Regression1/
	rsync -av --existing ../results/figures/ ../paper/figures/Regression2/



# Old version [not working]
#	cd ../results && find -name 'anova_prop.png' -o -name 'processing.png' -o -name 'smoothed_images.png' -o -name 'dvars_sub2run2.png' -o -name 'qqplot.png'-o -name 'sub002_lme_beta_gain.png' -o -name 'fd_sub2run2.png' -o -name 'sub2diff_heatmap.png' -o -name 'mean_hists.png' -o -name 'sub2gain_heatmap.png' -o -name 'mean_sub2run2.png' -o -name 'sub2loss_heatmap.png' -exec cp {} ../paper/figures \;	
#	cd ../results && find -name 'logistic_summary.png' -o -name 'roc_curve.png' -exec cp {} ../paper/figures/Regression1 \;	
#	cd ../results && find -name 'beta_gain_cluster.png' -o -name  'diagnosis.png' -o -name 't_loss_standard_sub2.png' -o -name 'beta_loss_cluster.png' -o -name 't_gain_standard_sub2.png' -exec cp {} ../paper/figures/Regression2 \;	
#	cd ../results && find -name 'corr_neu_bah.png' -o -name 'sig_cor_y_neural_aversion.png' -o -name 'Orig_sig_cor_z_gain.png' -o -name 'sig_cor_z_gain.png' -o -name 'Orig_sig_cor_z_loss.png'-o -name 'sig_cor_z_loss.png' -o -name 'Orig_sig_cor_z_neural_aversion.png' -o -name 'sig_cor_z_neural_aversion.png' -exec cp {} ../paper/figures/Regression3 \;	

