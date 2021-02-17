[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Timmyy3000/penguins-clf-heroku)

# Penguins web app deployed through Streamlit

## Penguin Prediction App
A web app that predicts the species of a Palmer penguin based on its features using Machine Learning
(Random Forest Classifier and K-Nearest Neighbours)

![alt text][image]

[image]: https://images.unsplash.com/photo-1462888210965-cdf193fb74de?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=967&q=80 "Photo by Jay Ruzesky on Unsplash"

*Data referenced from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.*

### Overview

Size measurements, clutch observations, and blood isotope ratios for 344 adult foraging Adélie, Chinstrap, and Gentoo penguins observed on islands in the Palmer Archipelago near Palmer Station, Antarctica. Data were collected and made available by [Dr. Kristen Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php) and the [Palmer Station, Antarctica Long Term Ecological Research (LTER)](https://pal.lternet.edu/)  Program.


The deployed web app is live at [here](https://share.streamlit.io/timmyy3000/penguins-clf-heroku/main/penguin-app.py)

The purpose of this ML Web App is to make a dynamic prediction of the species of a penguin based on its characteristics:

* Island
* Bill length
* Bill depth
* Flipper length
* Body mass
* Sex

## Tools

The web app was built in Python using the following libraries:
* streamlit
* pandas
* numpy
* scikit-learn
* pickle
