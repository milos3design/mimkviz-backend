# Mim Kviz API Documentation

This project is a Django-based API for a quiz application. It includes endpoints for retrieving quiz questions, managing the leaderboard, and recording game completions.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Models](#models)
- [Serializers](#serializers)
- [Views](#views)
- [Settings](#settings)
- [API Endpoints](#api-endpoints)
- [Security](#security)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Configuration

Create a `.env` file in the project root directory with the following variables:

```plaintext
SECRET_KEY=your_secret_key
AES_KEY=your_aes_key
IV_KEY=your_iv_key
DEBUG=True

# Database settings for production
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```

## Models

### Question

- **question**: `CharField` - The text of the question.
- **difficulty**: `CharField` - The difficulty level, choices are "Less Difficult" and "More Difficult".
- **possible_answers**: `JSONField` - A JSON array of possible answers.
- **correct_answer**: `CharField` - The correct answer to the question.
- **url**: `URLField` - Optional URL related to the question.

### Leaderboard

- **name**: `CharField` - The name of the player.
- **points**: `IntegerField` - The score of the player.
- **time**: `DecimalField` - The time taken by the player.
- **created_at**: `DateTimeField` - The timestamp when the entry was created.

### GameCompletionCounter

- **count**: `IntegerField` - A counter for the number of completed games.

## Serializers

### QuestionSerializer

- Custom `to_representation` method to encrypt the correct answer using AES encryption.

### LeaderboardSerializer

- Serializes `Leaderboard` model fields.

### GameCompletionCounterSerializer

- Serializes `GameCompletionCounter` model fields.

## Views

### QuestionsAPIView

- **GET**: Retrieves a list of 6 "less difficult" and 6 "more difficult" questions with shuffled possible answers.

### LeaderboardAPIView

- **GET**: Retrieves the top 10 leaderboard entries ordered by points, time, and creation date.
- **POST**: Creates a new leaderboard entry if it qualifies for the top 10.

### GameCompletionCounterAPIView

- **POST**: Increments the game completion counter.

## Settings

The settings for this project are found in `settings.py`. Key settings include:

- **DEBUG**: Toggle debug mode.
- **ALLOWED_HOSTS**: Define the allowed hosts.
- **CORS_ALLOWED_ORIGINS**: List of allowed origins for CORS.
- **CSRF_TRUSTED_ORIGINS**: List of trusted origins for CSRF.
- **DATABASES**: Configuration for the development and production databases.

## API Endpoints

### Retrieve Questions

- **Endpoint**: `/questions/`
- **Method**: `GET`
- **Response**: A list of questions with encrypted correct answers.

### Manage Leaderboard

- **Endpoint**: `/leaderboard/`
- **Method**: `GET`, `POST`
- **Response**:
  - `GET`: A list of top 10 leaderboard entries.
  - `POST`: The updated leaderboard if the new entry qualifies for the top 10.

### Record Game Completion

- **Endpoint**: `/record-completion/`
- **Method**: `POST`
- **Response**: The updated game completion count.

## Security

- **AES Encryption**: The correct answers for questions are encrypted using AES encryption with a fixed IV for security.
- **Environment Variables**: Sensitive information like secret keys and database credentials are stored in environment variables.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify this documentation as per your project requirements. If you have any questions or issues, please open an issue on the GitHub repository.
