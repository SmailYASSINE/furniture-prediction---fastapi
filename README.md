# Furniture Prediction with FastAPI and Jinja2

![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-brightgreen)
![Jinja2](https://img.shields.io/badge/Jinja2-3.0.3-blue)

A web application that uses FastAPI and Jinja2 to predict furniture attributes based on a machine learning model.

## Overview

This project demonstrates the integration of FastAPI, a modern Python web framework for building APIs, with Jinja2, a popular templating engine, to create a web application for predicting furniture attributes. It utilizes a machine learning model to make predictions based on user input.

## Features

- Predict furniture attributes such as category, sellability online, other colors, depth, height, and width.
- A user-friendly web interface for interacting with the machine learning model.
- Integration with Jinja2 for rendering HTML templates.
- Simple and clean code structure that can be extended for more complex machine learning models and features.

## Getting Started

Follow these steps to set up and run the project locally.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/SmailYASSINE/furniture-prediction---fastapi.git
   cd furniture-prediction---fastapi
2. **Usage**:
- On the main page, you can find information about the application.
- Use the "Predict" page to provide input for the prediction model and see the results.
3. **Project Structure**:
**app.py:** The FastAPI application.
**model.pkl:** The machine learning model (you can replace this with your own trained model).
**templates/:** Directory containing HTML templates used for rendering the web interface.

4. **Customization**:
You can customize this project by:

- Replacing the machine learning model in model.pkl with your own model.
- Extending the HTML templates in the templates directory to change the look and feel of the web interface.
