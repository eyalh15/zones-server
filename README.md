# Zone Manager Server
This is a Python server-side application built with Django, designed to manage zones. It offers a RESTful API for creating, retrieving and deleting zones. Data is stored in a CSV file.

## Table of Contents
- Installation
- Usage
- API Endpoints


## Installation
1. **Clone the repository**:
   `git clone https://github.com/eyalh15/zones-server.git`

2. **Change directory**:
`cd zones-server`

3. **Set up a virtual environment** (optional but recommended):
   `python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate`

4. **Install dependencies**:
   `pip install -r requirements.txt`


5. **Start the development server**:
   `python manage.py runserver`
   This will start the server on `http://127.0.0.1:8000/`.

## Usage
The server provides an API for the client to interact with the zones data. You can use tools like Postman or Curl to test the endpoints directly.

## API Endpoints
The server exposes the following API endpoints:

1. **Fetch Zones** (GET):
   `GET /api/zones/`
   Retrieves a list of zones.

2. **Create Zone** (POST):
   `POST /api/zones/`
   Creates a new zone with the provided data.

3. **Delete Zone** (DELETE):
   `DELETE /api/zones/<zone_id>/`
   Deletes the specified zone by its ID.