# Slides

See link below the learn how to use pandoc with beamer to produce
slides.

* http://pandoc.org/demo/example9/producing-slide-shows-with-pandoc.html

## Instructions

### Building the slides

`make` to clean and build both progress and final slides
`make final` to build the final slides
`make progress` to build the progress slides

**Note**: the slides include an old figure `lamba_boxplot.png`, we have 
included it here for completeness, all other figures are generated/updated
automatically with analyses. Navigate to `code` directory to perform analyses.

### Making the slides

- To edit progress slides, edit `progress.md` directly
- To edit final slides, edit each invidual portion beginning with `0X_`, where
`X` is the section number. To add a section, format each markdown file to begin
with `0X_`. For example, the 7th section can be `07_acknowledgment.md`.
