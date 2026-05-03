# Phase 2 Progress Report

## Objective and Current MVP Definition

The objective of Lock_In is to build an AI-assisted dieting application that helps users generate personalized meal plans based on profile information such as age, height, weight, activity level, dietary preferences, allergies, and fitness goals. The long-term vision is a nutrition-focused assistant that can eventually use a general-purpose AI model to provide more adaptive and personalized dietary recommendations.

The current minimum viable product (MVP) is a working local prototype that demonstrates the core end-to-end user flow. In its current form, the MVP allows a user to enter health and lifestyle information into a simple interface and receive a generated meal plan that includes a calorie target, macronutrient breakdown, hydration goal, and example meals. The MVP is intended to validate the project concept, user experience, and technical structure before introducing more advanced AI capabilities.

## What Has Been Built So Far

The project has moved beyond the documentation-only stage and now includes a functioning prototype. Earlier in development, the repository mainly contained a short project description and links to planning or presentation materials. It now contains working application code and a structured implementation foundation.

The following have been built so far:

- A Python-based web server that runs locally
- A browser-based user interface for entering dietary profile information
- Backend API endpoints for application health checks and plan generation
- Rules-based meal planning logic that calculates calories, macros, hydration, and daily meals
- Input and output data models for cleaner application structure
- A placeholder module for future OpenAI integration
- Unit tests for the planner logic
- Deployment preparation for Render
- Supporting repository files such as `.gitignore` and `requirements.txt`

At this point, the project is no longer only a concept. It is a working MVP that demonstrates the intended user flow and gives the team a concrete base for future development.

## Technical Approach

The technical approach for Phase 2 emphasized simplicity, modularity, and ease of local testing. The application is written in Python and uses a lightweight server design built with the standard library. This approach was chosen to keep the prototype easy to understand and easy to run while focusing attention on the product logic.

The application is divided into several core parts:

- `app.py` starts the local server
- `lock_in/server.py` handles incoming HTTP requests and API responses
- `lock_in/models.py` defines structured input and output objects
- `lock_in/planner.py` contains the meal-planning logic
- `lock_in/openai_client.py` is reserved for future AI integration
- `static/index.html` provides the frontend interface

From an agent-project perspective, the current system does not yet use a live large language model. Instead, the baseline behavior is a deterministic rules-based planner. This means the current prototype simulates the structure of an AI-assisted nutrition workflow without depending on real model calls yet. That choice was intentional because it allows the team to first validate the full workflow before adding a true AI generation layer.

The main interventions used so far are:

- Workflow design: collecting user data, validating it, generating a plan, and rendering it in the browser
- Context preparation: gathering the exact profile fields that a later AI prompt would need
- Modular design: separating server code, planner logic, data models, and future AI integration
- Deployment preparation: updating the server to support environment-based configuration for Render

At this phase, the project does not yet include retrieval, persistent user memory, multi-step model reasoning, or tool orchestration beyond the application’s internal logic.

## Evidence of Progress

There is clear before-and-after evidence of progress in Phase 2.

Before implementation:

- The repository mainly contained project planning artifacts and links
- There was no runnable interface
- There was no backend API or planner logic
- There was no deployment setup

After implementation:

- The application runs locally with `python3 app.py`
- The frontend allows users to enter dietary information
- The backend responds through `/api/health` and `/api/plan`
- The planner returns a structured diet plan with calories, macros, hydration, and meal suggestions
- Unit tests pass successfully
- Render deployment preparation has been completed

There is also direct technical evidence that the MVP works:

- The app starts successfully on a local machine
- The health endpoint returns a valid response
- The plan generation endpoint returns structured output
- The test suite passes for key planner behavior

A representative output from the MVP includes:

- A daily calorie target
- Protein, carbohydrate, and fat goals
- A hydration target
- A short rationale for the recommendation
- A set of example meals with notes tied to user preferences and restrictions

This demonstrates that the project has progressed from planning into a functioning prototype with an end-to-end user experience.

## Current Limitations and Open Risks

Although the MVP is functional, it still has important limitations.

First, the current planner is rules-based rather than AI-generated. The app is structured like an AI-assisted dieting system, but the core recommendation engine is still deterministic logic rather than live model inference.

Second, the nutritional recommendations are simplified. The calorie and macro estimates are based on general formulas and heuristic rules, and the meal suggestions are template-driven rather than deeply personalized. Because of this, the system is useful as a prototype but should not yet be treated as expert nutrition guidance.

Current missing capabilities include:

- No live OpenAI or LLM integration
- No retrieval from outside nutrition sources
- No persistent storage for user history or saved meal plans
- No conversational revision loop for refining recommendations
- No authentication or multi-user support
- No formal quality evaluation for generated plans beyond functional testing

There are also open risks:

- The application may appear more “intelligent” than it really is if users assume the current rules engine is already a full AI system
- Recommendations may be too generic for users with more specialized health or dietary conditions
- The current lightweight server design is acceptable for a prototype, but not ideal as a final production deployment architecture
- The project still needs stronger validation of plan usefulness and quality once true AI integration is added

From a generative-project perspective, the current system does not yet include a trained or fine-tuned model, dataset-backed generation, or formal evaluation metrics. At this stage, evaluation is mainly based on whether the workflow runs correctly and whether the outputs are structurally useful.

## Plan for Phase 3

Phase 3 should focus on turning the MVP into a more complete AI-assisted nutrition product.

The highest-priority goal is integrating a real general-purpose AI model through `lock_in/openai_client.py`. The structure for this already exists, which means the next phase can focus on improving recommendation quality rather than rebuilding the application architecture from scratch.

Planned goals for Phase 3 include:

1. Integrate OpenAI-powered meal-plan generation
2. Improve prompt and context design so outputs reflect user goals, allergies, dislikes, and diet style more naturally
3. Add plan refinement or regeneration features so users can iterate on recommendations
4. Improve frontend polish and overall usability
5. Add persistent storage for user profiles and previously generated plans
6. Deploy the application publicly on Render
7. Expand testing to include more API behavior and edge cases
8. Add stronger safety boundaries and clearer messaging around nutrition guidance

Phase 3 should also introduce stronger evaluation. A good approach would be comparing the current rules-based output against future AI-assisted output to determine whether personalization, flexibility, and overall usefulness improve. That would provide stronger evidence that the AI integration meaningfully advances the project rather than only changing how recommendations are generated internally.

## Conclusion

Phase 2 successfully transformed Lock_In from a planning-stage repository into a working MVP. The project now includes a frontend, backend, planner logic, tests, and deployment preparation. Most importantly, it demonstrates the complete user path from data entry to meal-plan generation.

At the same time, the project is still in an intermediate stage. The architecture now supports an AI-assisted vision, but the intelligence layer itself is still limited to rules-based planning. Phase 3 should therefore focus on live AI integration, stronger personalization, better evaluation, and deployment so that the final version more closely matches the original project objective.
