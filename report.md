# Lock-In AI Meal Planner MVP Report (Team 10)
## Group Members: 
Ryan Craft (rcraft13@asu.edu), Stanley Drake De Castro (shdecas1@asu.edu), Devin Gallegos (dgalle14@asu.edu), Wells Marcus (wbmarcus@asu.edu), and Carter Roane (chroane@asu.edu)

## 1. Executive Summary:
Lock_In is an AI-assisted meal planning application that helps users generate personalized meal plans based on their goals, preferences, allergies, and budget. The main goal of the project is to make meal planning easier and more realistic by handling multiple constraints at the same time.
In phase 3, we expanded our Phase 2 prototype into a more complete MVP. The system now supports multi-day meal planning, grocery cost estimation, and user interaction for adjusting plans. While the current version is still mostly rules based, it does a much better job handling real constraints and sets up a strong foundation for future AI integration.

## 2. User & Use Case:
The main users are people who want to eat healthier but don’t want to spend a lot of time planning meals. Many people struggle to balance things like calories, protein, budget, allergies, and preferences all at once. 
A typical use case is a user entering their information into the web app, such as their dietary goals, preferences, and constraints. The system then generates a multi-day meal plan along with nutrition targets and an estimated grocery list. The user can also adjust the plan as needed. 

## 3. System Design:
The system is built with a modular structure that separates the frontend, backend, and planning logic.
The frontend is a simple browser-based interface **(static/index.html)** where users input their information and view results. The backend is a Python server **(app.py , server.py)** that handles API requests and sends responses. The core planning logic is implemented in **planner.py**, with additional modules supporting pricing, nutrition lookup, and user interaction. 
The system includes API endpoints such as **/api/plan** for generating meal plans, **/api/interact** for modifying plans, and **/api/cheaper-plan** for reducing cost.
Data flows from the frontend to the backend through API requests. The backend then calls the planner logic to generate a meal plan, and the results are sent back to the frontend to be displayed to the user. 

## 4. Data:
The system uses several structured data sources:
- **meals.json** for meal and ingredient information
- **prices.json** for estimating grocery costs
- **fdc_cache.json** for nutrition values
- **raw_data/** for original dataset files
The data is cleaned and organized so the planner can efficiently generate and evaluate meal combinations. Since the system is rules based and does not use a trained model, a train/test split is not required.

## 5. Technical Approach:
The current MVP uses a rules based approach instead of a trained machine learning model.
The planner selects meals based on user inputs and filters them using constraints based on how well they match calorie goals, variety, and other factors.
The system also:
- estimates grocery cost using pricing data
- attempts to generate cheaper versions of meal plans
- allows users to interact and refine plans
There is a placeholder for OpenAI integration **(openai_client.py)**, but it is not fully implemented yet. The system is designed so that AI can be added later to improve personalization and decision making. 



## 6. Evaluation:
The system was evaluated based on whether it works end to end and produces reasonable outputs.
The application successfully:
- takes user input through the frontend
- generates multi-day meal plans
- calculates nutrition targets
- estimates grocery costs
- allows users to modify and refine plans
For example, a user can input a calorie goal and budget, and the system generates a weekly meal plan along with a grocery estimate. This demonstrates a complete end to end workflow from user input to final output.
Unit tests in the **tests/** folder help verify that key components such as the planner, pricing logic, and nutrition lookup are working correctly.

## 7. Limitations & Risks: 
Limitations of the system include:
- Meal data is limited and may not cover all diets
- Cost estimates are based on static pricing
- There is no user account system or saved data
- Constraint handling is not perfect and may not always find the best plan
The largest risk would be the system making a mistake and recommending a recipe the user is allergic to. Users may also assume the results are fully accurate nutrition advice, even though the system is not designed for medical use. There may also be a risk of privacy since users input personal information.

## 8. Next Steps: 
With more time we would:
- integrate OpenAI or another LLM to improve meal generation and personalization
- improve constraint checking to ensure plans are always valid
- expand the meal dataset and improve ingredient tagging
- add user accounts and saved plans
- improve the frontend design
- improve cost and nutrition optimization

