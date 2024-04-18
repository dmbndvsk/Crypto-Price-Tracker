# Crypto Price Tracker

## Overview

Crypto Price Tracker is an asynchronous web application built using Python and the aiohttp framework. It is designed to fetch and track the prices of various cryptocurrencies in real-time.

## Features

- **Real-time Crypto Pricing**: Fetches the latest bid prices of cryptocurrencies using the KuCoin API.
- **Price History**: Stores and retrieves the price history of each cryptocurrency.
- **Database Integration**: Uses PostgreSQL for storing currency data.
- **Asynchronous Architecture**: Built with async/await patterns for non-blocking operation.

## Technologies Used

- **Python 3.9+**: Main programming language.
- **aiohttp**: Asynchronous HTTP Client/Server for asyncio and Python.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) for Python.
- **PostgreSQL**: Open source relational database.
- **ccxt**: Library to connect and trade with cryptocurrency / exchange markets.

## Setup and Installation

### Requirements

- Python 3.9 or higher
- PostgreSQL server (local or remote)

### Environment Setup

1. Clone the repository:
   ```bash
   git clone https://repository-url
   cd crypto_price_tracker
   ```

# Set up a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

# Install dependencies:

```
pip install -r requirements.txt
```

## Database Configuration

Configure your database for the application:

```bash
# Create a PostgreSQL database.
# Set the following environment variables for your database connection:
export DB_USER="myuser"
export DB_PASSWORD="mypassword"
export DB_HOST="localhost"
export DB_NAME="mydbname"
```

## Running the Application

Start the application with the following command:

```bash
python3 main.py
```

### Using Gunicorn with aiohttp worker

To run the application using Gunicorn with a specialized aiohttp worker, use the following command:

```bash
gunicorn main:app --worker-class aiohttp.GunicornWebWorker --bind 127.0.0.1:8080
```

## API Endpoints

Explore the functionalities of the Crypto Price Tracker through these API endpoints:

- **GET /price/{currency}**: Fetches the current price of the specified currency.
- **GET /price/history**: Fetches the price history, supports pagination via the `?page=` query parameter.
- **DELETE /price/history**: Deletes all price history from the database.
