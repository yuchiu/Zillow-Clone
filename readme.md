# Zillow Clone

## Tech Stack

- [React](https://github.com/facebook/react) ∙ [Redux](https://github.com/reduxjs/redux)
  - web client & client data management
- [Node.js](https://github.com/nodejs) ∙ [Expressjs](https://github.com/expressjs/express) ∙ [Jayson](https://github.com/tedeh/jayson)
  - web server & services in service oriented architecure
- [Python](https://github.com/python)
  - web scraper, backend server
- [RabbitMQ](https://github.com/rabbitmq)
  - message queue combo with scraper
- [MongoDB](https://github.com/mongodb/mongo)
  - persisted database
- [Tensorflow](https://github.com/tensorflow/tensorflow)
  - machine learning

---

## Objectives:

- Service Oriented Architecture
- Single Page Application
- Scrape raw real estate data from Zillow
- Provide real estate data with our own API
- Search real estate properties by location
- Display search result with properties details and map
- Property price prediction with machine learning

## Getting Started

### Tools & Versions

| Tools    | Versions  |
| -------- | --------- |
| npm      | 6.1.0     |
| pip      | 9.0.1     |
| nodejs   | 10.7.0    |
| python   | 3.6.5     |
| mongodb  | mlab      |
| rabbitmq | cloudamqp |

### Prerequisites

#### Environment Variables

**!important** .env file is required for setting up environment variables for this project  
 an example of default .env file is located at ./.env

- User Service

  - SERVICE_USER_DB_MONGO_URI is part of mLab service's variable, please change to your own

- Message Queues

  - MQ_REAL_ESTATE_FETCH_TASK_URI is part of cloudAMQP service's variable, please change to your own
  - MQ_REAL_ESTATE_FETCH_TASK_NAME is part of cloudAMQP service's variable, please change to your own

- Property Service

  - SERVICE_PROPERTY_DB_MONGO_URI is part of mLab service's variable, please change to your own
  - SERVICE_PROPERTY_DB_MONGO_HOST is part of mLab service's variable, please change to your own
  - SERVICE_PROPERTY_DB_MONGO_PORT is part of mLab service's variable, please change to your own
  - SERVICE_PROPERTY_DB_MONGO_NAME is part of mLab service's variable, please change to your own
  - SERVICE_PROPERTY_DB_MONGO_USER is part of mLab service's variable, please change to your own
  - SERVICE_PROPERTY_DB_MONGO_PASS is part of mLab service's variable, please change to your own

### Building Data Pipeline

#### Data Pipeline

- install dependencies

```terminal
pip install -r requirements.txt
```

- start scraper pipeline for fetching raw data from Zillow, process and store to MongoDB

```terminal
cd Zillow-Clone/data-pipeline
python3 fetcher.py
```

### Serving Application

#### User Service

- install dependencies & start User-Service

```terminal
cd Zillow-Clone/user-service
npm install
npm start
```

Application will be serving on http://localhost:3130

#### Web Server

- install dependencies & start Web-Server

```terminal
cd Zillow-Clone/web-server
npm install
npm start
```

Application will be serving on http://localhost:3030

#### Web Client

- install dependencies & start application

```terminal
cd Zillow-Clone/web-client
npm install
npm start
```

Application will be serving on http://localhost:3000

---

## Deployment

- Not set up yet

---

## Author

- Yu Chiu

---

## License

This project is licensed under the MIT License - see the LICENSE file for details

---

## Acknowledgments

- Not set up yet

---
