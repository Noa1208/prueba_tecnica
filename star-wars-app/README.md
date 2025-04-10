# Star Wars App

This project is a simple application that lists characters from the Star Wars universe using the Star Wars API (SWAPI). Users can click on a character to view detailed information about them.

## Project Structure

```
star-wars-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── services
│   │   └── swapi_service.py   # Functions to interact with the SWAPI
│   ├── screens
│   │   ├── main_screen.py      # Main screen displaying the list of characters
│   │   └── detail_screen.py    # Detail screen showing character information
│   └── utils
│       └── prueba_request.py    # Utility functions for HTTP requests
├── requirements.txt            # Project dependencies
└── README.md                   # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd star-wars-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

- The application will display a list of Star Wars characters.
- Click on a character to view their details, including:
  - Name
  - Height
  - Weight
  - Gender
  - Films in which they appear

## License

This project is licensed under the MIT License.